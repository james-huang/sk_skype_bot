from random import choice
from gif_base import GifBase

URLS = \
[
"http://29.media.tumblr.com/tumblr_lxa76gNzdV1qfjjglo1_500.gif",
"http://i.imgur.com/tY4Xd.gif",
"http://i.imgur.com/3DPRf.gif",
"http://i.imgur.com/uM5NJ.gif",
"http://i.imgur.com/O2pBe.gif",
"http://i.imgur.com/8O8OU.gif",
"http://i.imgur.com/SfWLs.gif",
"https://www.youtube.com/watch?v=8X_Ot0k4XJc",
"http://i.imgur.com/VqPrv.gif",
"http://www.nastyhobbit.org/data/media/2/free-internet-coupon.jpg",
"http://i.imgur.com/srfOs.jpg",
"http://i.imgur.com/RmcvR.gif",
"http://i.imgur.com/rudNc.gif",
"http://i.imgur.com/mIDPq.gif",
"http://i.imgur.com/QHEeU.gif",
"http://i.imgur.com/ED4jh.gif",
"http://i.imgur.com/s24XH.gif",
"http://i.imgur.com/trwrzPg.gif",
"http://i.imgur.com/kY5hpdY.gif",
"http://i.imgur.com/ZLoHmpx.gif",
"http://i.imgur.com/2mqxnba.gif",
"http://i.imgur.com/aP80atj.gif",
"http://i.imgur.com/bjPcDtH.gif",
"http://i.imgur.com/tzbrjjE.gif",
"http://i.imgur.com/VanlIW5.gif",
"http://i.imgur.com/rDIQpV8.gif",
"http://i.imgur.com/c579xst.gif",
"http://i.imgur.com/3aRP0Tf.gif",
"http://i.imgur.com/FmhzPLX.gif",
"http://i.imgur.com/MxeLEF6.gif",
"http://i.imgur.com/18ghb1t.gif",
"http://i.imgur.com/cnW0Er7.gif",
"http://i.imgur.com/2Hz7Hm3.gif",
"http://i.imgur.com/qBt4AKy.gif",
"http://i.imgur.com/IT0cKwc.gif",
"http://i.imgur.com/rDHdwNU.gifhttp://i.imgur.com/Idg9aXR.gif",
"http://i.imgur.com/B6LQSsU.gif",
"http://i.imgur.com/yltZDgp.gif",
"http://i.imgur.com/zcer5Rj.gif",
"http://i.imgur.com/4kaUk0z.gif",
"http://i.imgur.com/3YlO9Ud.gif",
"http://i.imgur.com/eQ8ECXX.gif",
"http://i.imgur.com/9Dsd7cZ.gif",
"http://i.imgur.com/A3Sc6Jf.gif",
"http://i.imgur.com/ezpVYup.gif",
"http://i.imgur.com/QVLPeGi.gif",
"http://i.imgur.com/uBODpmy.gif",
"http://i.imgur.com/2sREC.gif",
"http://i.imgur.com/3w1ej.gif",
"http://i.imgur.com/MIj6o.gif",
"http://i.imgur.com/EqRJH.gif",
"http://i.imgur.com/JSBTl.gif",
"http://i.imgur.com/s3AoP.gif",
"http://i.imgur.com/ZYKBr.gif",
"http://i.imgur.com/yGBuI.gif",
"http://i.imgur.com/kQWV2.gif",
"http://i.imgur.com/sWiS2.gif",
"http://i.imgur.com/Ichev.gif",
"http://i.imgur.com/bhKp2.gif",
"http://i.imgur.com/Jdvdr.gif",
"http://i.imgur.com/SBt3o.gif",
"http://i.imgur.com/u8awa.gif",
"http://i.imgur.com/NAk6C.gif",
"http://i.imgur.com/iFdT0.gif",
"http://i.imgur.com/wZuxj.gif",
"http://i.imgur.com/lNEg8.gif",
"http://i.imgur.com/8NAub.gif",
"http://i.imgur.com/1RPcr.gif",
"http://i.imgur.com/NnBHS.gif",
"http://i.imgur.com/Ft1Bt.gif",
"http://i.imgur.com/8UuPv.gif",
"http://i.imgur.com/AtuzC.gif",
"http://i.imgur.com/vV9zj.gif",
"http://i.imgur.com/UcCIa.gif",
"http://i.imgur.com/SjXn4.gif",
"http://i.imgur.com/oib2k.gif",
"http://i.imgur.com/wGDi8.gif",
"http://i.imgur.com/BDQwE.gif",
"http://i.imgur.com/JvkIs.gif",
]

class Welldone(GifBase):

  def __init__(self):
    self.URLS = URLS

if __name__ == "__main__":
  wd = Welldone()
  print wd.response()
  print wd.response()
  print wd.response()
  print wd.response()
  #unit test here or something
  print "all unit test passed!"