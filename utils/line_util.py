from config.zoom_urls import config_url


class TextMessageUtil:
    def __init__(self, message: str):
        self.message = message

    def distribution_message(self):
        message = self.message
        if message == "テスト":
            return_data = config_url["home_room"]["E"]
        elif message.startswith(('HR', 'hr', 'ホームルーム')):
            class_name = str.upper(message.split(" ")[1])
            return_data = config_url["home_room"][class_name]
        return return_data
