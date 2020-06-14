from linebot.models import TextSendMessage, FlexSendMessage, ImageSendMessage
from config.line_bot_api import line_bot_api
import json
import datetime
import re


class TextMessageUtil:
    def __init__(self, event):
        self.event = event

    def distribution_message(self):
        message = self.event.message.text
        if message == 'test':
            line_bot_api.reply_message(
                self.event.reply_token, TextSendMessage(text=str(datetime.datetime.now().strftime("%Y/%m/%d"))))
        elif message.startswith('zoom'):
            #             target_id = self.event.source.group_id if self.event.source.type == "group" else self.event.source.user_id
            with open("./config/flex.json") as f:
                flex_json = json.load(f)
            flex_message = FlexSendMessage(
                alt_text='home_room_flex', contents=flex_json["zoom_flex"])
            line_bot_api.reply_message(
                self.event.reply_token, messages=flex_message)
        elif message.startswith('卒業単位'):
            image_message = ImageSendMessage(
                original_content_url='https://pacific-ocean-18208.herokuapp.com/static/graduation_unit.jpg',
                preview_image_url='https://pacific-ocean-18208.herokuapp.com/static/graduation_unit.jpg'
            )
            line_bot_api.reply_message(
                self.event.reply_token, messages=image_message)
        elif message.startswith('schedule'):
            if message != "schedule":
                split_message = message.split(":")[1]
                if re.fullmatch(r"\d{4}", split_message):
                    now_time = datetime.datetime.now().strftime("%Y/") + \
                        f"{split_message[0:2]}/{split_message[2:4]}"
                else:
                    return
            else:
                now_time = datetime.datetime.now().strftime("%Y/%m/%d")
            now_time_split = now_time.split("/")
            now_time_text = f"{now_time_split[1]}月{now_time_split[2]}日"
            send_text = f"{now_time_text}の時間割"
            with open("./excel/schedule.json") as f:
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
