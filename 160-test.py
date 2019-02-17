class TextMessage(object):
    def __init__(self, to):
        self.to = to

    def send(self, message):
         print(f"Yo {self.to}, {message}")

thing = TextMessage("Larry")
thing.send("where you at?")
