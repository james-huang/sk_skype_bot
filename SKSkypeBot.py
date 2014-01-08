#arch -i386 python

import Skype4Py
import time
import re

import os
import glob
import sys


# import all the reponse classes from the reponses folder
os.chdir("responses")
sys.path.append(os.getcwd())
response_modules = [n[:-3] for n in glob.glob("*.py") if n[0] != '_']
#print response_modules
module_dict = {}
for module_name in response_modules:
  module = __import__(module_name)
  for item_name in dir(module):
    try:
      new_action = getattr(module, item_name)()
      module_dict[module_name] = new_action
    except:
      pass
#print module_dict


class SkypeBot(object):
  """
  To add additional reponses to the skype bot:
   1. decide on the command you want to implement: e.g !sayhi
   2. Create a new file and class in the responses folder: sayhi.py
   3. Implement a reponse method.
   4. Update the commands dictionary below. The key is your regexp to match. Value is the filename.
   5. Go to response/help.py and put in instructions on how to use your command
  """
  commands = {
    #"!help *(.*)": "help",
    "^!help *(.*)": "help",
    "^!popcorn *(.*)": "popcorn",
    "^!happy *(.*)": "happy",
    "^!sad *(.*)": "sad",
    "^!welldone *(.*)": "well_done",
    "^!be *(.*)":"be",
  }

  def __init__(self):
    self.skype = Skype4Py.Skype(Events=self)
    self.skype.FriendlyName = "SK Skype Bot"
    self.skype.Attach()

  def __del__(self):
    # may want to to save state across sessions
    pass

  def AttachmentStatus(self, status):
    if status == Skype4Py.apiAttachAvailable:
      self.skype.Attach()

  def MessageStatus(self, msg, status):
    if status == Skype4Py.cmsReceived:
      #if "Dev Chat" in msg.Chat.Topic:
      #if msg.Chat.Type in (Skype4Py.chatTypeDialog, Skype4Py.chatTypeLegacyDialog):
      for regexp, target in self.commands.items():
        match = re.match(regexp, msg.Body, re.IGNORECASE)
        if match:
          msg.MarkAsSeen()
          reply = module_dict[target].response(*match.groups())
          if reply:
            msg.Chat.SendMessage(reply)
          if target == "be": # say 2 things
            reply2 = module_dict[target].response(*match.groups())
            msg.Chat.SendMessage(reply2)
          break


if __name__ == "__main__":
  bot = SkypeBot()

  while True:
    time.sleep(1.0)
