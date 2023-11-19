from flask import Flask, request, abort
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import *
import os

app = Flask(__name__)
CHANNEL_ACCESS_TOKEN = os.environ.get("CHANNEL_ACCESS_TOKEN","IPfGFd0aLtai0SL6qgZOXHFAAKRdDMdsbtZIV8mCkeH7UiPfSydY0Dw2J/GSHLbCZasIFJy07yFOMpdYyIc5EJxrAvqEOu0mhSbTiEKAaRTsDjbUEWLz+yDfJt+eSqADDSkK/gAAguNTWcWIJwBLUAdB04t89/1O/w1cDnyilFU=")
CHANNEL_SECRET = os.environ.get("CHANNEL_SECRET", "66f9192c153f1a643df44c69d7d39de3")
print(CHANNEL_ACCESS_TOKEN)
print(CHANNEL_SECRET)
line_bot_api = LineBotApi(str(CHANNEL_ACCESS_TOKEN))
handler = WebhookHandler(str(CHANNEL_SECRET))


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

@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    message = TextSendMessage(text=event.message.text)
    line_bot_api.reply_message(event.reply_token, message)

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 8080))
    app.run(host='0.0.0.0', port=port)
