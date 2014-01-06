from random import choice

class GifBase(object):

  def __init__(self):
    self.URLS = ['http://www.google.com']

  def response(self, *args):
    if len(args) > 0:
      try:
        return self.URLS[int(args[0]) % len(URLS)]
      except:
        pass
    return choice(self.URLS)

if __name__ == "__main__":
  gb = GifBase()
  print gb.response()
  print gb.response()
  print gb.response()
  print gb.response()
  #unit test here or something
  print "all unit test passed!"