from random import choice

POPCORN_URLS = \
[
"http://i.imgur.com/qlRu3.gif",
"http://i.imgur.com/DDMBW.gif"
"http://i.imgur.com/SbyLU.gif"
"http://i.imgur.com/y8F8s.gif",
"http://i.imgur.com/lozGr.gif",
"http://i.imgur.com/YG6vv.gif",
"http://i.imgur.com/lae9h.gif",
"http://i.imgur.com/qvWDXtm.gif",
"http://i.imgur.com/enRL0.gif",
"http://i.imgur.com/kSkuJ.gif",
"http://i.imgur.com/GnrYm.gif",
"http://i.imgur.com/m19qf.gif",
"http://i.imgur.com/89rdf.gif",
"http://i.imgur.com/pMgoj.gif",
"http://i.imgur.com/taWbz.gif",
"http://i.imgur.com/SzSm0.gif",
"http://i.imgur.com/UgMlt.gif",
"http://i.imgur.com/sopAo.gif",
"http://i.imgur.com/UdT1E.gif",
"http://i.imgur.com/aatnM.gif",
"http://i.imgur.com/AMDLo.gif",
"http://i.imgur.com/T2vuc.gif",
"http://i.imgur.com/GdYtA.gif",
"http://i.imgur.com/BBidG.gif",
"http://tigzy.com/lj/popcorn.gif",
"http://stream1.gifsoup.com/webroot/animatedgifs/162138_o.gif",
]

class Popcorn(object):

  def __init__(self):
    pass


  def response(self):
    return choice(POPCORN_URLS)

if __name__ == "__main__":
  popcorn = Popcorn()
  print popcorn.response()
  print popcorn.response()
  print popcorn.response()
  print popcorn.response()
  #unit test here or something
  print "all unit test passed!"