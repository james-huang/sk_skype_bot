sk_skype_bot
============

Shopkick's Skype Bot


  To run Shopkick's Skype Bot on OSX

  1. Download python 2.X from python.org. Make sure to grab a version with python-32 (the 32 bit version of python)
  2. arch -i386 pip install Skype4Py
  3. python-32 SKSkypeBotpy

  To add additional reponses to the skype bot:
   1. decide on the command you want to implement: e.g !sayhi
   2. Create a new file and class in the responses folder: sayhi.py
   3. Implement a reponse method.
   4. Update the commands dictionary below. The key is your regexp to match. Value is the filename.
   5. Go to response/help.py and put in instructions on how to use your command
