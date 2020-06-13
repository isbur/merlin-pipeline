# https://stackoverflow.com/a/48100440/10216512
class Data:

    def __init__(self):
        self.contents = None

    def get(self):
        print("I'm going to get data somehow...")
        self.contents = open("input.json", "r")


data = Data()