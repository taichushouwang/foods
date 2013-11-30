# -*- coding: utf-8 -*-  
import os
import re

#return a dictionary represent all the food topics and their contents
def readContent():
	foods = {}
	
	#get content directory
	dirName = os.path.join( os.path.dirname( __file__ ), "static" )
	
	#get all exact content
	list = os.listdir( dirName )
	for item in list:
		food = {}
		contentPath = os.path.join( dirName, item )

		#get all tags for a topic
		tagsContentPath = os.path.join( contentPath, "tags.txt" )
		tagsFile = open( tagsContentPath, "r" )

		tagList = []
		for tag in tagsFile:
			tag = tag.strip("\n")
			tagList.append( tag )
		
		food["tags"] = tagList
		tagsFile.close()
		
		#get all introdutions for a topic if they exist
		introContentPath = os.path.join( contentPath, "introduction.txt" )
		if os.path.isfile( introContentPath ):
			introsFile = open( introContentPath, "r" )
			
			introDic = {}
			for introItem in introsFile:
				intro = introItem.split( "：" )
				introDic[intro[0].strip()] = intro[1].strip()
			
			food["intros"] = introDic
			introsFile.close()
		
		
		#get all the related link of the topic
		viewPath = os.path.join( contentPath, "view.txt" )
		viewFile = open( viewPath, "r" )
		pattern = re.compile( r"\d+" )
		relatedLinkList = []
		
		for relatedLine in viewFile:
			for relatedItem in pattern.findall( relatedLine ):
				relatedLinkList.append( relatedItem )
		
		food["relatedLink"] = relatedLinkList
		
		
		#get the link and name of the topic
		linkPath = os.path.join( contentPath, "link.txt" )
		linkFile = open( linkPath, "r" )
		
		name = linkFile.readline().strip("\n")
		link = linkFile.readline().strip("\n")
		food["link"] = link
		linkFile.close()
		
		#store the number of the topic in baidu baike
		food["number"] = item
		
		#store the topic as an element of the 'foods' dictionary
		foods[name] = food
	
	return foods
	
	
	