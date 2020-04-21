from flask import Blueprint
from config.line_bot_api import handler, line_bot_api
from utils.line_util import TextMessageUtil


from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
)
api_module = Blueprint('api_module', __name__, url_prefix='/api')


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    text = TextMessageUtil(event.message.text).distribution_message()
    line_bot_api.reply_message(event.reply_token, TextSendMessage(text=text))
