from flask import Blueprint
from config.line_bot_api import handler
from utils.line_util import TextMessageUtil


from linebot.models import MessageEvent, TextMessage
api_module = Blueprint('api_module', __name__, url_prefix='/api')


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    TextMessageUtil(event).distribution_message()
