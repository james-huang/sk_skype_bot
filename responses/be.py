from random import choice

"""
Use this to impersonate people
~/Library/Application\ Support/Skype/<username>/main.db has message history
sqlite3 main.db "SELECT author,timestamp, body_xml, dialog_partner  FROM messages where author = '<SOMEONE>';" to impersonate
"""

MARK = \
[
"YO!",
"whoa, Juice!",
"why am I NOT surprised...",
"y'all saw that",
"you're full of CRAP, Ryu!",
"one of yooz will be bringin' the Whisky, correct?",
"already kicked it off...",
"kewl...thanks, Karthick!",
"will the REAL Ryan...please stand up",
"that's messed up...",
"so that's NOT a good idea...",
"dang, Ryan\n next thing you know you've got the LLAMA NECK goin'...",
"Manisha does a pretty MEAN LLAMA NECK",
"shoot.",
"don't be tootin' your own horn, there Ginger-Spice!",
"so far... as the record stands you're all talk",
"Hey, Team!",
"Anyone holding on to the Galaxy Nexus Android device? trying to repro an issue, but I need that specifc Android device...",
"it's alright, Ryu...",
"Thanks!",
"Hey there, Android DEV Team...\njust checking to make sure that there are no more commits going into the Android branch...",
"kewl...",
"that means we've got our official Android build, then..",
"we don't walk in there no mo'...",
"YO!",
"Team Delirium!",
"(high five)",
"great job, Guys!",
"you're still delirious Nandan...LOL",
"hmmm, apparently we might have an issue with this on Android. ok, thanks, Nandan!",
"you to slow, Spoonz!",
"nope...I kicked it off!",
"no problemo, meng! anything for a fellow shopkicker...RESPEK!",
"ah, crap!",
"I'm gonna kill you",
"don't mess with me right now. especially since I've been up all night",
"not kewl, dude!",
"props to whoever put up Biggie Smallz",
"After that poor GONG experience from Gretchen... her nickname is henceforth 'Olive Oyl'...",
"yep, it is back, indeed!",
"SMH",
"does the cake have curry frosting?",
"already building...",
"Rebuilding QA...",
"yeah...\nhose foreign folk...\nyou NEVER know...",
"LOL",
"I'll get you a (beer)\nonly cuz you're da BEST!\nI'd get Kiyoshi something meat related, but there are no meat emoticons...",
"Hey, Team! iOS trunk build's broken...",
"you started drinkin' already, HomeSlice?",
"rebuilding QA",
"I'm afraid to ask...",
"ok...",
"SMH",
"shuddap, Fool!",
"don't listen to this nonsense",
"Yeah, TinkerBell!",
"in otherwords...\nRyu said\nProtek Yo Neck!",
"Hey!",
"Mortal Fool...",
"mortal fool",
"I hear that section that MACS speaks of has a bag of Big League Chew for you fools over there",
"kewl, thanks!",
"whatchu need, fool?",
"you sure it's fixed?",
"better be fixed, fool!",
"PUNK!",
"shuddap Kiyoshi!",
"whoa!",
"no need for profanity, Son!",
"we all about RESPEK here, Brah!",
"SMH",
"is there Bourbon in it?",
"as a fellow Cold-Blooded Brutha, you should already know the answer, Mortal Fool!",
"who wrote that nonsense?",
"Hey there!",
"it's da BOMB-Diggity",
"Hey, Juice!",
"you Mizzou folks...",
"the nerve of you two...",
"now you wonder why you two get DISSED!",
"whatever...",
"the both of you are DIZZY!",
"protek yo neck, Juice!",
"that some foolishness you be speakin' Mortal Fool",
"already rebuilding",
"you too slow",
"yeah, try again, son!",
"Mark, 1\nAmanda...\nNONE!",
"so don't touch QA, then, fool!",
"stop drinkin' dem dang Jello Shots",
"mmmhmmmmn",
"QA rebuilding now...",
"hence the word, now...\n FOOL!",
"all the more reason...to re-enforce the fact that you need to fix yo tihs...",
"QA rebuilding",
"shuddap, Bo!",
"stop complainin' Y'ALL!",
"I just rebuilt it...",
"we support multiple logins now, Mr. Young!",
"I can show you, AirBNB...",
"Yo!",
"ok to bounce QA?",
"you're alright, Ryan\ndespite what everyone in the office says about you!",
"(evil)",
"(devil)",
"I kid, of course!",
"awww, come on, now!",
"that sounds like something Lauren would say...",
"Hey, Bo!",
"you need to stay out of this convo",
"you're sleep deprived, Bo!",
"Rule #2...\ndon't listen to Ryan",
"puh shaw, Mortal Fool!",
"you laughed, heck, BELLOWED in agreement",
"Hey, Team!",
"QA is still holding on to the build for iOS",
"I'm givin' him da BEAT DOWN!!!",
"yo, Juice! Lay off the Beer already!",
"whatever...you're just highfallutin, Son!",
"YO!",
"Any of you folks getting Sashimi for lunch?",
"Suisha House, perhaps...",
"shut the PHO up, Ananda!",
"no, don't see Mr. Wizard yet",
"whashopwobwem?!?!?",
"YOURmypwobwem!",
"yeah, Bo...\nZo...\nwhashyopwobwem?!?!?",
"I told you before...\nthat's YOUR\nperception\nsee?",
"even the rookies have caught, Bo...\nwhy can't you?\nLOL",
"AirBnB...\ncan you try again?",
"Ryan\nyou're in DELIRIOUS mode now",
"kewl...",
"glad to know it's back up...",
"RESPEK!",
"already rebuilding, Spoonz!",
"it's just YOUR perception, Mr. Rueth!",
"I feel the vibes when someone wants to touch QA",
"Ryan...\nyou're\nDELIRIOUS",
"Au Contraire",
"Mortal Fool!",
"thanks, Karthick!",
"Juice!\ngo home",
"stop being a JERK!",
"shuddap!",
"I restarted moments ago, Karnivarian",
"yo, Juice!",
"no, Juyoshi\n I mean, Kunichi",
"LOL",
"LOL",
"RESPEK!",
"BRO!",
"cut dat shit out, Bo\n ZO!",
"Granola Grizzly",
"Sorry, TinkerBell...",
"ding Ding DING!!!",
"yo, Ryan!\ngo\ntake\na\nnap",
"Yo, Team!",
"the last octet of the build machine is now 157",
"ZACKLY",
"nicely done, Smokin' Joe!",
"BOOM!",
"Hey, Team!",
"Who's got the Black Verizon iPhone 5 with them?",
"Bo\nget the heck out of this chat\ncuz it's about Transformers and Voltron and G.I. Joe\nNOT this my little pony crap",
"His name is\nKiyoshi\nplaying with his my little ponies in the bathroom",
"it's done rebuilding...",
"LOL...",
"yep, saw your commit...and did the rebuild myself",
"yeah, yeah...I'm out tomorrow, so you won't have to deal with me giving your crap, Juice! :-D",
"dude, don't be a scabbard!",
"aight, that's enough...I'll stop before HR takes over...",
"Ryan, I have faith that you can figure it out...",
"That's why Brooke's called the 'Halfway Crook'...",
"Whaddup, Y'all!!!",
"Ciao, Bella Lindsey!",
"People skills, King Boo! ;-)",
"And you're qualified?!?!? Lord, help you...",
"Word, Nerd!",
"LOL",
"YO!",
"Who's got the Black iPhone 5 on the Sprint network?",
"rebuilding QA in a moment...",
"Hey, Team!",
"Please don't touch the QA Environment from 2pm to 3:30pm...\nthanks!",
"I'll be Da Po Po",
"shuddap, Junichi!",
"thanks, Juice!",
"but I wanna upload these builds for QA",
"I KILL YOU!",
"We have yet another release candidate that's been uploaded to Dropbox now",
"whatchu know about that word, 'thang'?!?!?",
"you're CRAY",
"Sorry, Guys!\nMy\nBad!\nI'll be better about letting y'all know when I rebuild QA...\npromise!",
"rebuilding QA now...",
"I believe Juice needs to run the indexer...",
"shuddap, Juice!",
"dude!",
"stay in the loop, BRO!",
"thanks, Karthick!",
"YO!",
"Hey, Team!",
"Please DO NOT touch the QA Environment between 11am and 1pm...",
"Hey, Team!\nWho has the iPhone 4S?",
"does anyone have the other WHITE iPhone 4s running iOS 6?",
"gotta keep da PIMP HAND strong...y'know?!?!?",
"Yo, Karthick!",
"RESPEK, Duchess!",
"This is the best!",
"LOVE seeing JK do this every year!",
"Puh-LEEZ!",
"Come on, SPOONZ!",
"You're LAME!",
"Yep!",
"YO, STEVE!",
"Hey, Team!",
"Please leave the QA Environment alone for the next few hours...thanks!",
"Hey, Dev!",
"Can someone please look at Production?",
"The current app gives an error when tapping on STORE!",
"Thanks, Guys!",
"YEP! +1",
"don't touch it, please!",
"come on, AirBnB...\nyou should know better by now!",
"Who's signed up at Crunch?\nyou joining Zumba, MACS?!?!",
"yeah, Bo...\nyou require filtering",
"La Vics...NOYCE!",
"SMH...",
"slow down, meng...",
"good one, J-Mo!",
"yes, Spoonz",
"I'm rebuilding QA now",
"Hey, AirBnB?",
"Where's the iPhone 5 you've been using?",
"No, don't Skype it out...\nJust go Ol' Skool and go vocal.\nKarthick can hear you! ;-D",
"TRUST!",
"I'm at Burger Bar in Macy's SF, and I've got my Cookies & Cream shake, SUCKAS!!!(highfive)",
"Lgtm: marky mark\nSike!",
"So you should, Bo! High-Tower told me to never trust a Bo\nOr a Boo, or even a King Boo!",
"Bo...\nlay off the HOOKAH!",
"Hey, Team...\nspecifically, Kiyoshi and Ryan...\nI don't think the build version got updated to for iOS...",
"Hey, Juice!\ndo you really need the 3GS?",
"Head shot!",
"You're dead!",
"Address the DEV team with RESPEK, Fool!",
"thanks for posting this on Dev Chat, Joe!",
"don't ask silly questions about v4.0.2",
"it's called\nSACKIN' UP!",
"no coddling on this side of the office",
"IN!",
"YO, AirBNB",
"Stay on point, man!",
"Yo, Stop Fighting, Y'all!",
"oh puh leez",
"you know you LOVED IT!!!",
"Hey, Bo!\n Get your Dang Cherrypick in already!",
"Hey, Android Team!\nCan one of you guys bump the buildVersion?",
"grassy-ass, Cyclops!",
"whatchu need, Karnivore?",
"Hey, Team!\nMost specifically, the Core Team!\nWho's working on the force upgrade tasks on Android and iOS?",
"Hey there, Y'all!!!",
"Man, what's wrong with you...",
"James...\nyou're OUT!!!",
"YO, MACS!!!",
"MACS!",
"you're KILLING the mood here",
"shuddap, Bo!",
"you too, JUICE!!!",
"Spoonz!",
"Do you NOT read DomDiggity's weekly emails?",
"What's DA MATTER with all you folks on GROWTH?",
"It's aight, AirBnB...",
"I'm just in a 'messin' with Spoonz' kinda mood today...",
"Hey, DEV!!!",
"Can anyone of you iOS guys fix the branch build?",
"QA needs to get started on testing and the branch build is still broken...",
"kicking off a build...\nwill update y'all in a few minutes...",
"Thanks for the help, High-Tower! Nicely done!",
"next time you ladies go out shopping...\nbring Adam Bossy with you, instead of your significant dude...\ny'all know Spoonz likes to shop...",
"y u gotta be so negatory all da time?",
"Spanx, Ms. Gonsalves!",
"RESPEK!",
"SHHHH!!!",
"VERY\nNICE!",
"Y'all are such HAMS!!!",
"Have a coke and a smile, Karnivore!",
"QA's broken, Y'all!",
"Grassy-Ass, Juice!",
"Yo, Juice!",
"don't be such a partypooper, TinkerBell!",
"PEACE!!!!",
"Yeah, agreed!",
"Way to mess things up, Sir Charles! SMH",
"yep, QA just got rebuilt",
"Heads up, y'all!",
"dang\nit",
"QA is already rebuilding",
"LOL",
"Hey, Karthick!\nwhy dontchu go play some hockey, huh?",
"LOL",
"LOL",
"MAD RESPEK!",
"LOL...",
"I'ma call you 'JerryCurl James' now...",
"Ima just start calling you\n'Rick'...\nJames!",
"I gotchu, Ms. Gonsalves ;-D",
"YO, Fife!",
"Why you holdin' back?!?!?",
"Juice, stop bein' a know it all, fool!",
"QA env ok?",
"Spanx!",
"Grassy-ass, Jugo! (Y)",
"RESPEK!",
"Hey, Spoonz!\nYou around?\nFYI...\nyour commit(s) broke the iOS build...",
"grassy-ass, Cucharas!!!",
"Yo, Spoonz!\nIt's still broken...",
"care to put a wager on it?\nAmerican Dollars?",
"alright, looks like the build is fixed, indeed! Spanx, Spoonz!",
"yeah...I DIG IT!",
]

class Be(object):

  def __init__(self):
    self.MARK = MARK

  def response(self, *args):
    if len(args) == 1:
      if args[0].lower().strip() in ["mark", "markymark", "marky mark", "markaguirre", "mark aguirre", "markbot"]:
        return "mark_bot: " + choice(self.MARK).replace("\n","\nmark_bot: ")

if __name__ == "__main__":
  be = Be()
  print be.response("mark")
  print "======="*20
  print be.response("Mark")
  print "======="*20
  print be.response("Marky Mark")
  print "======="*20
  print be.response("Marky Mark")
  print "======="*20
  #unit test here or something
  print "all unit test passed!"