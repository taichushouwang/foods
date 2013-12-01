#coding=utf-8
import pymongo
class Datebase(object):
	"""docstring for Datebase"""
#初始化数据库
	def __init__(self):
		self.Con=pymongo.Connection();
		self.db=self.Con.AI;#数据库
		self.users=self.db.user
		self.foods=self.db.food
#插入用户名和密码
	def _insert(self,username,pw):
		u={"username":username,"password":pw}
		self.db.user.insert(u)
#输出数据库中所有的用户名和密码
	def _print(self):
		for i in self.db.user.find({},{"_id":0}):
			print i
#查找用户，匹对密码
	def _login(self,username,pw):
		u=self.db.user.find_one({"username":username,"password":pw}
					,{"_id":0})
		if(u==None):
			print "Username or password is wrong!!"
		else:
			print "Username is : "
			print u
#注册用户
	def _register(self,username,pw):
		u=self.db.user.find_one({"username":username})
		if(u==None):
			self._insert(username,pw)
		else:
			print "The username is existed!!"
#删除用户
	def _remove(self,username,pw):
		u=self.db.user.find_one({"username":username,"password":pw})
		if(u==None):
			print "Username or password is wrong!!"
		else:
			self.db.user.remove(u)
			print "Remove successfully!"
