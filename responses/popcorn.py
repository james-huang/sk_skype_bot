from random import choice
from gif_base import GifBase

URLS = \
[
"http://i.imgur.com/o3Exb.gif",
"http://i.imgur.com/8adTE.gif",
"http://i.imgur.com/qYNFUyF.gif",
"http://i.imgur.com/fYlRLP9.gif",
"http://i.imgur.com/JkOzKst.gif",
"http://i.imgur.com/aq5UZga.gif",
"http://i.imgur.com/B0lpdkU.gif",
"http://i.imgur.com/xT2sH29.gif",
"http://i.imgur.com/aIj2TkL.gif",
"http://i.imgur.com/76tVwoI.gif",
"http://i.imgur.com/Je3OP.gif",
"http://i.imgur.com/hinAw.gif",
"http://i.imgur.com/Awp0c.gif",
"http://i.imgur.com/YCzMI.gif",
"http://i.imgur.com/I8Oum.gif",
"http://i.imgur.com/UGOBF.gif",
"http://i.imgur.com/yGWbw.gif",
"http://i.imgur.com/D1cEM.gif",
"http://i.imgur.com/WJGZ5.gif",
"http://i.imgur.com/7naA9.gif",
"http://i.imgur.com/2fPdH.gif",
"http://i.imgur.com/79Yeo.gif",
"http://i.imgur.com/KaoXj.gif",
"http://i.imgur.com/cXyob.gif",
"http://i.imgur.com/62iwz.gif",
"http://i.imgur.com/G97HU.gif",
"http://i.imgur.com/GkmRr.gif",
"http://i.imgur.com/PYPUJ.gif",
"http://i.imgur.com/BawxZ.gif",
"http://i.imgur.com/Fz6am.gif",
"http://i.imgur.com/czRZI.gif",
"http://i.imgur.com/uh5A6.gif",
"http://i.imgur.com/9jRYJ.gif",
"http://i.imgur.com/GpqVJ.gif",
"http://i.imgur.com/Cvaif.gif",
"http://i.imgur.com/pibPJ.gif",
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

class Popcorn(GifBase):

  def __init__(self):
    self.URLS = URLS

if __name__ == "__main__":
  popcorn = Popcorn()
  print popcorn.response()
  print popcorn.response()
  print popcorn.response()
  print popcorn.response()
  #unit test here or something
  print "all unit test passed!"