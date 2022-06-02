# basic starter code for a class that can be expanded to handle callbacks, attachents (buttons, etc) and more!
class Slash():

  def __init__(self, message):
    print("\nin Slash init\n")
    self.msg = message

  def getMessage(self):
    print("\nin slashCommand.getMessage\n")
    return self.msg
