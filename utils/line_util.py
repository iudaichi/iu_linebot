from config.zoom_urls import config_url
from linebot.models import TextSendMessage, FlexSendMessage
from config.line_bot_api import line_bot_api
import json


class TextMessageUtil:
    def __init__(self, event):
        self.event = event

    def distribution_message(self):
        message = self.event.message.text
        if message == "テスト":
            text = config_url["home_room"]["E"]
            line_bot_api.reply_message(
                self.event.reply_token, TextSendMessage(text=text))
        elif message.startswith('/HR'):
            class_name = str.upper(message.split(" ")[1])
            text = config_url["home_room"][class_name]
            line_bot_api.push_message(
                self.event.source.user_id, TextSendMessage(text=text))
        elif message == 'test':
            line_bot_api.reply_message(
                self.event.reply_token, TextSendMessage(text=str(self.event)))
        elif message == 'ホームルーム':
            target_id = self.event.source.group_id if self.event.source.type == "group" else self.event.source.user_id
            with open("./config/flex.json") as f:
                flex_json = json.load(f)
            flex_message = FlexSendMessage(
                alt_text='home_room_flex', contents=flex_json["home_room"])
            line_bot_api.push_message(
                target_id, messages=flex_message)
