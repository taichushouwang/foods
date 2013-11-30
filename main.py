# -*- coding: utf-8 -*-  

import tornado.httpserver
import tornado.ioloop
import tornado.web
import tornado.escape
import os
import time
#module to get contents
import readContent
import suggest
		
class MainHandler( tornado.web.RequestHandler ):
	def get( self ):
		self.render( "search.html" )

class ListResultHandler( tornado.web.RequestHandler ):
	def get( self ):
		searchName = self.get_argument( "searchName" ).encode("utf-8")
		
		try:
			foods[searchName]
		except:
			self.render( "listResult.html", tips = "Oops!", feedback = "Sorry, there is no such kind of food." )
		else:
			self.redirect( "/topic?foodName=" + searchName )
		
class TopicHandler( tornado.web.RequestHandler ):
	def get( self ):
		#get the food name
		foodName = self.get_argument( "foodName" ).encode("utf-8")

		#get the tags
		tagString = ''
		for foodTag in foods[foodName]["tags"]:
			tagString = tagString + foodTag +"|"
			
		tagString = foodName + " : " + tagString
		
		#get the introdutions
		introString = ""
		try:
			foods[foodName]["intros"]
		except:
			'do nothing'
		else:
			for introsItem in foods[foodName]["intros"]:
				introString = introString + introsItem + ":" + foods[foodName]["intros"][introsItem]
		
		#get the image path
		picPath = os.path.join( foods[foodName]["number"], "pic.jpg" )
		
		#get the suggestion
		queue = suggest.suggest( foods[foodName], foods, 5 )
		sugguestion = ''
		try:
			while True:
				node = queue.pop()
				sugguestion += node["name"] + "\n"
		except:
			'do nothing'
		
		#get the link of the topic
		link = foods[foodName]["link"]
		
		self.render( "topic.html", foodName = foodName, tags = tagString, intros = introString, sugguestion = sugguestion,
					topicLink = link, picPath = picPath )
		
		
		
foods = readContent.readContent()
	
app = tornado.web.Application (
	[( r"/", MainHandler ),
	( r"/listResult", ListResultHandler ),
	( r"/topic", TopicHandler )],
	debug = True,
	static_path = os.path.join( os.path.dirname( __file__ ), "static" ),
	template_path = os.path.join( os.path.dirname( __file__ ), "template" ),
	autoscape = None
)

if __name__ == "__main__":
	http_server = tornado.httpserver.HTTPServer(app)
	http_server.listen(8888, '172.18.156.93')
	tornado.ioloop.IOLoop.instance().start()