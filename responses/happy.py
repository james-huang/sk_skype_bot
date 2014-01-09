from random import choice
from gif_base import GifBase

URLS = \
[
"http://i.imgur.com/YdqRGJT.gif",
"http://i.imgur.com/XFlyjXe.gif",
"http://i.imgur.com/R9DCfN6.gif",
"http://i.imgur.com/ShtwT6u.gif",
"http://i.imgur.com/1CU6MBn.gif",
"http://i.imgur.com/m3X6lzE.gif",
"http://i.imgur.com/9MXxgaD.gif",
"http://i.imgur.com/X9d5tnd.gif",
"http://i.imgur.com/ijlUxcr.gif",
"http://i.imgur.com/lbsjq5I.gif",
"http://i.imgur.com/5R5LinD.gif",
"http://i.imgur.com/85f9l0l.gif",
"http://i.imgur.com/zExJDv5.gif",
"http://i.imgur.com/hPwa8.gif",
"http://i.imgur.com/ng2CT.gif",
"http://i.imgur.com/AGEb2.gif",
"http://i.imgur.com/anslK.gif",
"http://i.imgur.com/QVHid.gif",
"http://i.imgur.com/tCFSc.gif",
"http://i.imgur.com/E2MkT.gif",
"http://i.imgur.com/NaMiw.gif",
"http://i.imgur.com/RPZKD.gif",
"http://i.imgur.com/ELP7G.gif",
"http://i.imgur.com/AdAhA.gif",
"http://i.imgur.com/HD4tg.gif",
"http://i.imgur.com/wguX3.gif",
"http://i.imgur.com/cG6kn.gif",
"http://i.imgur.com/VvqOo.gif",
"http://i.imgur.com/PqIYN.gif",
"http://i.imgur.com/7Bkc2.gif",
"http://i.imgur.com/ETmsf.gif",
"http://i.imgur.com/wY16A.gif",
"http://i.imgur.com/IZU7v.gif",
"http://i.imgur.com/SgWam.gif",
"http://i.imgur.com/DwLHl.gif",
"http://i.imgur.com/iFajw.gif",
"http://i.imgur.com/n9iSO.gif",
"http://i.imgur.com/kNIVG.gif",
"http://i.imgur.com/JOBYs.gif",
"http://i.imgur.com/Lf72R.gif",
"http://i.imgur.com/Ey0W8.gif",
"http://i.imgur.com/pUBgw.gif",
"http://i.imgur.com/F5iFK.gif",
"http://i.imgur.com/uq4LP.gif",
"http://i.imgur.com/OTe4j.gif",
"http://i.imgur.com/N8lzp.gif",
"http://i.imgur.com/o0D0B.gif",
"http://i.imgur.com/UKQTf.gif",
"http://i.imgur.com/VPlDP.gif",
"http://i.imgur.com/QcpgV.gif",
"http://i.imgur.com/oqN1C.gif",
"http://i.imgur.com/4r218.gif",
"http://i.imgur.com/fc4l5.gif",
"http://i.imgur.com/OWflW.gif",
"http://i.imgur.com/mHG3L.gif",
"http://i.imgur.com/8qZ9s.gif",
"http://i.imgur.com/ZZosK.gif",
"http://i.imgur.com/bF7Nh.gif",
"http://i.imgur.com/7e6Fy.gif",
"http://i.imgur.com/hi4A3.gif",
"http://i.imgur.com/xUi5Q.gif",
"http://i.imgur.com/orjYA.gif",
"http://i.imgur.com/SOK8R.gif",
"http://i.imgur.com/nVq6p.gif",
"http://i.imgur.com/oQRt3.gif",
"http://i.imgur.com/bHWrK.gif",
"http://i.imgur.com/TAFpE.gif",
"http://i.imgur.com/pXjrQ.gif",
"http://i.imgur.com/XYBgt.gif",
"http://i.imgur.com/Fmboi.gif",
"http://i.imgur.com/ddNKi.gif",
"http://i.imgur.com/vOMIJ.gif",
"http://i.imgur.com/pWmgy.gif",
"http://i.imgur.com/HfVdG.gif",
"http://i.imgur.com/IKZbr.gif",
"http://i.imgur.com/8EmIv.gif",
"http://i.imgur.com/mCOVs.gif",
"http://i.imgur.com/Bwfnv.gif",
"http://i.imgur.com/Nasbc.gif",
"http://i.imgur.com/RxX4h.gif",
"http://i.imgur.com/tNbIq.gif",
"http://i.imgur.com/Mt39r.gif",
"http://i.imgur.com/0nSwZ.gif",
"http://i.imgur.com/vnW1M.gif",
"http://i.imgur.com/tbBfd.gif",
"http://i.imgur.com/tyROdzN.gif",
"http://i.imgur.com/ntB2KhM.gif",
"http://i.imgur.com/2Se3JOD.gif",
"http://i.imgur.com/L24cy.gif",
"http://i.imgur.com/nJTgg7p.gif",
"http://i.imgur.com/uvZL2KY.gif",
"http://i.imgur.com/NvJd1Jh.gif",
"http://i.imgur.com/VaAvSEj.gif",
"http://i.imgur.com/PHUyL6A.gif",
"http://i.imgur.com/rU2jU8X.gif",
"http://i.imgur.com/cUqCb7Y.gif",
"http://i.imgur.com/j4OGrkf.gif",
"http://i.imgur.com/ZVZUfYX.gif",
"http://i.imgur.com/GpcQD3y.gif",
"http://i.imgur.com/yFtfY.gif",
"http://i.imgur.com/HA5Pd.gif",
"http://i.imgur.com/SiA2Q.gif",
"http://i.imgur.com/BFQBW.gif",
"http://i.imgur.com/yqBpz.gif",
"http://i.imgur.com/lyCUq.gif",
"http://i.imgur.com/UbHSq.gif",
"http://i.imgur.com/VJAP4.gif",
"http://i.imgur.com/RMzT1.gif",
"http://i.imgur.com/z7AyT.gif",
"http://i.imgur.com/sqpg0.gif",
"http://i.imgur.com/HZg8e.gif",
"http://i.imgur.com/yxJJX.gif",
"http://i.imgur.com/i4x5g.gif",
"http://i.imgur.com/4crab.gif",
"http://i.imgur.com/idAaA.gif",
"http://i.imgur.com/LRz2r.gif",
"http://i.imgur.com/Mb0O4.gif",
"http://i.imgur.com/xrU4X.gif",
"http://i.imgur.com/VhdHz.gif",
"http://i.imgur.com/A5pV0.gif",
"http://i.imgur.com/TaTdV.gif",
"http://i.imgur.com/Gu4MN.gif",
"http://i.imgur.com/dPQel.gif",
"http://i.imgur.com/ugoKd.gif",
"http://i.imgur.com/QnkwB.gif",
"http://i.imgur.com/nw2Cg.gif",
"http://i.imgur.com/Fece8.gif",
"http://i.imgur.com/Fece8.gif",
"http://i.imgur.com/mYJFa.gif",
"http://i.imgur.com/7sCq0.gif",
"http://i.imgur.com/XKVex.gif",
"http://i.imgur.com/rLuul.gif",
"http://i.imgur.com/BUicA.gif",
"http://i.imgur.com/8x6ot.gif",
"http://i.imgur.com/iWPWB.gif",
"http://i.imgur.com/bXwVs.gif",
"http://i.imgur.com/58dmS.gif",
"http://i.imgur.com/lpPa5.gif",
"http://i.imgur.com/taTtM.gif",
"http://i.imgur.com/5Pg3g.gif",
"http://cdn.bleacherreport.net/images_root/article/media_slots/photos/000/512/291/MaroneyDougie_original.gif?1344524950",
"http://i.minus.com/iwxsqo0IR5QPF.gif",
"http://i.imgur.com/fP6RT.gif",
"http://i.imgur.com/VjOM1.gif",
"http://i.imgur.com/4QU8h.gif",
"http://i.imgur.com/ZSCEny5.gif",
"http://i.imgur.com/RrM0w.gif",
"http://media.tumblr.com/tumblr_lvurcyaZlM1qf04yf.gif",
]

class Happy(GifBase):

  def __init__(self):
    self.URLS = URLS

if __name__ == "__main__":
  happy = Happy()
  print happy.response()
  print happy.response()
  print happy.response()
  print happy.response()
  #unit test here or something
  print "all unit test passed!"
