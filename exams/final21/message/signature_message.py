from message import Message

class SignatureMessage(Message):

    def __init__(self, sender, recipient, signature):
        super().__init__(sender, recipient)
        self.signature = signature

    def __str__(self):
        message_str = super().__str__()
        message_str += "\n{}".format(self.signature)
        return message_str