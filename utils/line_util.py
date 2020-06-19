from linebot.models import TextSendMessage, FlexSendMessage, ImageSendMessage
from config.line_bot_api import line_bot_api
import json
from config.main import JST
import datetime
import re


class TextMessageUtil:
    def __init__(self, event):
        self.event = event

    def send_zoom_url(self):
        with open("./config/flex.json") as f:
            flex_json = json.load(f)
        flex_message = FlexSendMessage(
            alt_text='home_room_flex', contents=flex_json["zoom_flex"])
        line_bot_api.reply_message(
            self.event.reply_token, messages=flex_message)

    def send_unit_image(self):
        image_message = ImageSendMessage(
            original_content_url='https://pacific-ocean-18208.herokuapp.com/static/graduation_unit.jpg',
            preview_image_url='https://pacific-ocean-18208.herokuapp.com/static/graduation_unit.jpg'
        )
        line_bot_api.reply_message(
            self.event.reply_token, messages=image_message)

    def send_schedule(self):
        message = self.event.message.text
        if message != "schedule":
            split_message = message.split(":")[1]
            if re.fullmatch(r"\d{4}", split_message):
                now_time = datetime.datetime.now(JST).strftime("%Y/") + \
                    f"{split_message[0:2]}/{split_message[2:4]}"
            else:
                return
        else:
            now_time = datetime.datetime.now(JST).strftime("%Y/%m/%d")
        now_time_split = now_time.split("/")
        now_time_text = f"{now_time_split[1]}月{now_time_split[2]}日"
        send_text = f"{now_time_text}の時間割"
        with open("./config/schedule.json") as f:
            schedule_json = json.load(f)
        for v in schedule_json.values():
            if v['day'] == now_time:
                send_text += f"\n\n{v['time_table']}時間目\n{v['class_name']}\nPASS : {v['class_room_password']}\nhttps://zoom.us/j/{v['class_room_number']}?"
        if send_text == f"{now_time_text}の時間割":
            line_bot_api.reply_message(
                self.event.reply_token, TextSendMessage(text=f"申し訳ありません。\n{now_time_text}の時間割が存在しません。"))
        else:
            line_bot_api.reply_message(
                self.event.reply_token, TextSendMessage(text=send_text))

    def send_test(self):
        now_time = datetime.datetime.now(JST).strftime("%Y/%m/%d")
        with open("./config/flex.json") as f:
            flex_json = json.load(f)
        template_json = flex_json["test"]
        with open("./config/schedule.json") as f:
            schedule_json = json.load(f)
        for v in schedule_json.values():
            if v['day'] == now_time:
                time_table_text = f"{v['time_table'].decode('unicode-escape')}時間目"
                class_name_text = f"{v['class_name'].decode('unicode-escape')}"
                class_room_password_text = f"pass : {v['class_room_password'].decode('unicode-escape')}"
                class_room_url_text = f"https://zoom.us/j/{v['class_room_number'].decode('unicode-escape')}?"
                template_json["contents"].append({
                    "type": "bubble",
                    "size": "micro",
                    "body": {
                        "type": "box",
                        "layout": "vertical",
                        "contents": [
                            {
                                "type": "text",
                                "text": time_table_text,
                                "weight": "bold",
                                "size": "sm",
                                "wrap": True
                            },
                            {
                                "type": "text",
                                "text": class_name_text,
                                "weight": "bold",
                                "size": "sm",
                                "wrap": False
                            },
                            {
                                "type": "text",
                                "text": class_room_password_text,
                                "weight": "bold",
                                "size": "sm",
                                "wrap": True
                            }
                        ],
                        "spacing": "sm",
                        "paddingAll": "13px"
                    },
                    "footer": {
                        "type": "box",
                        "layout": "vertical",
                        "contents": [
                            {
                                "type": "button",
                                "action": {
                                    "type": "uri",
                                    "label": "ここをタップ",
                                    "uri": class_room_url_text
                                }
                            }
                        ]
                    }
                })
        flex_message = FlexSendMessage(
            alt_text='home_room_flex', contents=template_json)
        line_bot_api.reply_message(
            self.event.reply_token, messages=flex_message)
