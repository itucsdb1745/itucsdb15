class MessageStore:
    def __init__(self):
        self.messages = {}
        self.last_m_id = 0

    def add_message(self, message):
        self.last_m_id += 1
        self.messages[self.last_m_id] = message
        message._id = self.last_m_id

    def delete_message(self, messageId):
        del self.messages[messageId]

    def get_message(self, messageId):
        return self.messages[messageId]

    def get_messages(self):
        return self.messages
