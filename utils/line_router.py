from utils.line_util import TextMessageUtil


class TextMessageRouter:
    def __init__(self, event):
        self.event = event

    def distribution_message(self):
        message = self.event.message.text
        if message.startswith('test'):
            TextMessageUtil(self.event).send_test()
        elif message.startswith('zoom'):
            TextMessageUtil(self.event).send_zoom_url()
        elif message.startswith('卒業単位'):
            TextMessageUtil(self.event).send_unit_image()
        elif message.startswith('スケジュール'):
            TextMessageUtil(self.event).send_schedule()
