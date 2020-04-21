from flask import Flask, request, abort
from linebot.exceptions import InvalidSignatureError
from config.line_bot_api import handler
from api.router import api_module

app = Flask(__name__)

app.register_blueprint(api_module)


@app.route("/callback", methods=['POST'])
def callback():
    signature = request.headers['X-Line-Signature']
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)
    return 'OK'
