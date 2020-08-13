# Guess Number Game
  This game create a random number between 0 and try_max_number(this value set by player),and the player must get this number in a prescribed number of times(<=log2(try_max_number)),console will indicate player's input is bigger or smaller than the right answer,before starting the game player can choose three options
##  Each option's introduction as follows
  1.  input username, and show this user's game records
  2.  game's main part,input username and set the max number here,then start the game
  3.  exit the game
##  Feature:
  1.  have user records
  2.  can set the max random number
  3.  easy to design,easy to modify 
##  Design Points:
  1.  the data structure,**dictionary nested list**.each user have many records,so we can use dictionary separate each user,the key is username,the value is a list of this user's game recoords
  2.  the user registration part design,to use list's append() methods adding each user's game record,we must init dictionary first,set new user an empty record list.so we need think about check the user is registed first
##  Improvement Points:
  1.  the check of illegal number input
  2.  the persistent storage of user game records
  3.  set the minimal random number
That's all
##  补充:
对这个猜数游戏的设计思想来源于《Python爬虫开发：从入门到实建》2.5节阶段案例-猜数游戏，作者：谢乾坤，十分感谢你的经验分享  
想对作者偷偷说一句，我看了你在微信读书下的评论，现在你多了一个粉丝:grin:
