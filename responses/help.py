
#
#
# Hi! So you want to add some documentation for your Skype Bot command?

# 1. Define your new tuple: e.g SAYHI_HELP = "!sayhi", "!sayhi", "this command makes the skype bot say hi"

# The help tuples are defined as:
#    1. what your command prefix is
#    2. usage
#    3. man pages
# 2. Add it to the HELP_MESSAGE_LIST
#
# Your help message will appear when people type !help sayhi or !help !sayhi


HELP_HELP = '!help', '!help [command]', \
"""!help
  Yo Dawg, I heard you like learning skype bot commands, so I put help in the help so you can learn skype bot commands while you learn skype bot commands
"""

POPCORN_HELP = '!popcorn', '!popcorn',\
"""!popcorn
  Called when there is a very interesting thread of conversation going on. A random gif of popcorn will be posted for you into the skype thread.
"""

SAD_HELP = '!sad', '!sad', \
"""!sad
  Sad? Upset? Angry? Don't like hearing bad news? A random gif of sadness will be posted for you into the skype thread.
"""

HAPPY_HELP = '!happy', '!happy', \
"""!happy
  Happy? Just heard good news? Want to gloat? Want to dance?  A random gif of happiness will be posted for you into the skype thread.
"""

WELLDONE_HELP = '!welldone', '!welldone [name]', \
"""!welldone
  Well Done! Use this when you want to approve of something. To congratulate someone for an exceptionaly well done job. A random gif of approval will be posted for you into the skype thread.
"""

HELP_MESSAGE_LIST = \
[
HELP_HELP,
POPCORN_HELP,
SAD_HELP,
HAPPY_HELP,
WELLDONE_HELP,
]

MAN_PAGES = {}
USAGE = []
for command,usage,mannual in HELP_MESSAGE_LIST:
  MAN_PAGES[command] = mannual
  USAGE.append(usage)

class Help(object):
  HELP_MESSAGE = \
  """ This is the SK Skype Bot 0.0.1. Commands:
    %s

    If you want to add some functionality, fork https://github.com/james-huang/sk_skype_bot and submit a pull request.
    If there is gif content that is offensive to you, please let James know and he will take it down.
  """ % '\n    '.join([k for k in sorted(USAGE)])

  def __init__(self):
    pass

  def response(self, *args):
    if args and len(args[0])>0:
      command_query = args[0] if args[0][0]=="!" else "!"+args[0]
      if command_query in MAN_PAGES:
        return MAN_PAGES[command_query]
    else:
      return self.HELP_MESSAGE

if __name__ == "__main__":
  #unit test here or something
  help = Help()
  print help.help()
  print help.response()
  print "all unit test passed!"