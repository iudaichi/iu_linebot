from linebot.models import TextSendMessage, FlexSendMessage, ImageSendMessage
from config.line_bot_api import line_bot_api
import json


class TextMessageUtil:
    def __init__(self, event):
        self.event = event

    def distribution_message(self):
        message = self.event.message.text
        if message == 'test':
            line_bot_api.reply_message(
                self.event.reply_token, TextSendMessage(text=str(self.event)))
        elif message == 'zoom':
            #             target_id = self.event.source.group_id if self.event.source.type == "group" else self.event.source.user_id
            with open("./config/flex.json") as f:
                flex_json = json.load(f)
            flex_message = FlexSendMessage(
                alt_text='home_room_flex', contents=flex_json["zoom_flex"])
            line_bot_api.reply_message(
                self.event.reply_token, messages=flex_message)
        elif message == 'test21':
            #            target_id = self.event.source.group_id if self.event.source.type == "group" else self.event.source.user_id
            with open("./config/flex.json") as f:
                flex_json = json.load(f)
            flex_message = FlexSendMessage(
                alt_text='home_room_flex', contents=flex_json["zoom_flex"])
            line_bot_api.reply_message(
                self.event.reply_token, messages=flex_message)
        elif message == '卒業単位':
            image_message = ImageSendMessage(
                original_content_url='https://example.com/original.jpg',
                preview_image_url='https://example.com/preview.jpg'
            )
            line_bot_api.reply_message(
                self.event.reply_token, messages=image_message)
