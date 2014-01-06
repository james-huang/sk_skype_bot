from random import choice
from gif_base import GifBase

URLS = \
[
"http://i.imgur.com/PnDrd3O.gif",
"http://i.imgur.com/Kn0V3D8.gif",
"http://i.imgur.com/6D8DqTG.gif",
"http://i.imgur.com/v6JHwtK.gif",
"http://i.imgur.com/RMsnqCF.gif",
"http://i.imgur.com/PFRaVV6.gif",
"http://i.imgur.com/ZQ4RyHo.gif",
"http://i.imgur.com/biHam6L.gif",
"http://i.imgur.com/0U2cnck.gif",
"http://i.imgur.com/t6jxZYx.gif",
"http://i.imgur.com/AT5je46.gif",
"http://i.imgur.com/G4QbkbX.gif",
"http://i.imgur.com/vFhh4JW.gif",
"http://i.imgur.com/E3jqOHP.gif",
"http://i.imgur.com/PeOkjoB.gif",
"http://i.imgur.com/qGr2jmT.gif",
"http://i.imgur.com/YsEvEu3.gif",
"http://i.imgur.com/SqUnkNY.gif",
"http://i.imgur.com/0fY0s03.gif",
"http://i.imgur.com/GqUfvsA.gif",
"http://i.imgur.com/tXysky4.gif",
"http://i.imgur.com/woZL9TO.gif",
"http://i.imgur.com/fFUjGje.gif",
"http://i.imgur.com/dEFHI.gif",
"http://i.imgur.com/GPqtwr7.gif",
"http://i.imgur.com/NpAbl.gif",
"http://i.imgur.com/megqR.gif",
"http://i.imgur.com/8waIx0Y.gif",
"http://i.imgur.com/RVBi3T1.gif",
"http://i.imgur.com/RuYH0.gif",
"http://i.imgur.com/TghktaI.gif",
"http://i.imgur.com/5Xq1Tyi.gif",
"http://i.imgur.com/zS5rRxa.gif",
"http://i.imgur.com/1tWt2Nt.gif",
"http://i.imgur.com/P09txRD.gif",
"http://i.imgur.com/2oBmP5E.gif",
"http://i.imgur.com/0oqVSeT.gif",
"http://i.imgur.com/AVbZZwP.gif",
"http://i.imgur.com/00uDyDJ.gif",
"http://i.imgur.com/X7PnFIl.gif",
"http://i.imgur.com/1ksAqJu.gif",
"http://i.imgur.com/HSYVsRp.gif",
"http://i.imgur.com/xAtktd5.gif",
"http://i.imgur.com/Sp5b3RC.gif",
"http://i.imgur.com/oqC5USk.gif",
"http://i.imgur.com/rrxcK1q.gif",
"http://i.imgur.com/WSmpayC.gif",
"http://i.imgur.com/tPzTdA4.gif",
"http://i.imgur.com/NIIDeQk.gif",
"http://i.imgur.com/ldtpOON.gif",
"http://i.imgur.com/pwg9kid.gif",
"http://i.imgur.com/fkLF9.gif",
"http://i.imgur.com/odydm.gif",
"http://i.imgur.com/Rav8F.gif",
"http://i.imgur.com/JKHTl.gif",
"http://i.imgur.com/S3VpN.gif",
"http://i.imgur.com/rkZq7.gif",
"http://i.imgur.com/Opv98.gif",
"http://i.imgur.com/U2v0g.gif",
"http://i.imgur.com/dAgeI.gif",
"http://i.imgur.com/LbEbK.gif",
"http://i.imgur.com/fQXqO.gif",
"http://i.imgur.com/WeXPc.gif",
"http://i.imgur.com/HYkqC.gif",
"http://i.imgur.com/E7J3W.gif",
"http://i.imgur.com/kVBDO.gif",
"http://i.imgur.com/t5BwT.gif",
"http://i.imgur.com/mtMol.gif",
"http://i.imgur.com/xcmP1.gif",
"http://i.imgur.com/1u2L0.gif",
"http://i.imgur.com/CMRx3.gif",
"http://i.imgur.com/KxvRn.gif",
"http://i.imgur.com/683ID.gif",
"http://i.imgur.com/oov56.gif",
"http://i.imgur.com/FxB3m.gif",
"http://i.imgur.com/Dg5J7.gif",
"http://i.imgur.com/vmcCc.gif",
"http://i.imgur.com/q3O8A.gif",
"http://i.imgur.com/8ByaI.gif",
"http://i.imgur.com/8DE8J.gif",
"http://i.imgur.com/1Kq6I.gif",
"http://i.imgur.com/TkLVk.gif",
"http://i.imgur.com/62qgY.gif",
"http://i.imgur.com/MbiXv.gif",
"http://i.imgur.com/1vxHz.gif",
"http://i.imgur.com/z7uwD.gif",
"http://i.imgur.com/yCbCV.gif",
"http://i.imgur.com/MsUI5.gif",
"http://i.imgur.com/jCQJt.gif",
"http://i.imgur.com/MzTDX.gif",
"http://i.imgur.com/CLcKV.gif",
"http://i.imgur.com/ebdJb.gif",
"http://i.imgur.com/ACPOb.gif",
"http://i.imgur.com/yshiM.gif",
"http://i.imgur.com/FPkYs.gif",
"http://i.imgur.com/D9dQr.gif",
"http://i.imgur.com/rxE7M.gif",
"http://i.imgur.com/NChLj.gif",
"http://i.imgur.com/6UA6P.gif",
"http://i.imgur.com/sez4T.gif",
"http://i.imgur.com/4ntUJ.gif",
"http://i.imgur.com/9ty88.gif",
"http://i.imgur.com/NlOFY.gif",
"http://i.imgur.com/p2KGT.gif",
"http://i.imgur.com/07Sho.gif",
"http://i.imgur.com/kThan.gif",
"http://i.imgur.com/8bwXv.gif",
"http://i.imgur.com/4wcyX.gif",
"http://i.imgur.com/Tcwwz.gif",
"http://i.imgur.com/qkfZa.gif",
"http://i.imgur.com/1jZuq.gif",
"http://i.imgur.com/w7N8P.gif",
"http://i.imgur.com/ivxph.gif",
"http://i.imgur.com/mObXY.gif",
"http://i.imgur.com/SdbdK.gif",
"http://i.imgur.com/RcHLX.gif",
"http://i.imgur.com/hdW2w.gif",
"http://i.imgur.com/01Ztj.gif",
"http://i.imgur.com/pT4Ia.gif",
"http://i.imgur.com/0GEgv.gif",
"http://i.imgur.com/yJ7SC.gif",
"http://i.imgur.com/Y8mw8.gif",
"https://s3.amazonaws.com/uploads.hipchat.com/30/23973/m4hq9f73j98teqh/phanatic-pervert-o.gif",
"http://i.imgur.com/6I4eT.gif",
"http://blog.wtfconcept.com/wp-content/uploads/2011/10/cat-attack-gif.gif",
"http://media.tumblr.com/tumblr_lsdhbmlL611qhjgo1.gif",
"http://i.imgur.com/cCGJ8.gif",
"http://26.media.tumblr.com/tumblr_liwjqazNtx1qixleeo1_500.gif",
"http://i.imgur.com/cG9j1.gif",
"http://awesomegifs.com/wp-content/uploads/panda-smackdown.gif",
"http://i.imgur.com/jBXuE.gif",
"http://oi43.tinypic.com/148p3wn.jpg",
"http://i.imgur.com/8kRUE.gif",
"http://i.imgur.com/QfVAU.gif",
"http://i.imgur.com/TX4ZJ.gif",
"http://i.imgur.com/xCnGj.gif",
"http://i.imgur.com/p2xgX.gif",
"http://i.imgur.com/sURma.gif",
"http://media.tumblr.com/tumblr_lo02g5Aa6K1qzcbom.gif",
"http://i.imgur.com/OelVq.gif",
"http://i.imgur.com/60cq5.gif",
"http://25.media.tumblr.com/30c0ae5e4a4145029e6baa72e1be8098/tumblr_moro1xsGkN1r7g304o1_250.gif",
]

class Sad(GifBase):

  def __init__(self):
    self.URLS = URLS

if __name__ == "__main__":
  sad = Sad()
  print sad.response()
  print sad.response()
  print sad.response()
  print sad.response()
  #unit test here or something
  print "all unit test passed!"