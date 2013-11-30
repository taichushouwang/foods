import readContent
import suggest


def test():
	foods = readContent.readContent()
	
	'''
	#print the contents to test
	for item in foods:
		tagString = ''
		for foodTag in foods[item]["tags"]:
			tagString = tagString + foodTag.decode("utf-8").encode("gbk") +"|"
		print item.decode("utf-8").encode("gbk") + " : " + tagString
		
		introString = ""
		try:
			foods[item]["intros"]
		except:
			print ''
		else:
			for introsItem in foods[item]["intros"]:
				introString = introString + introsItem + ":" + foods[item]["intros"][introsItem]
			print introString.decode("utf-8").encode("gbk") + "\n"
		
		relatedLinkString = ""
		#print type( foods[item]["relatedLink"] )
		for relatedLink in foods[item]["relatedLink"]:
			relatedLinkString = relatedLinkString + relatedLink.decode("utf-8").encode("gbk") +"|"
		print relatedLinkString
	'''
	
	
	food = {}
	count = 0
	for item in foods:
		if count == 0:
			count += 1
			food = foods[item]
			'''
			print item.decode("utf-8").encode("gbk")
			print food["number"]
			'''
	queue = suggest.suggest( food, foods, 5 )
	
	'''
	#print the suggestions to test
	try:
		while True:
			node = queue.get()
			name = node["name"]
			node = foods[name]
			
			#show tags string
			tagString = ''
			for foodTag in node["tags"]:
				tagString = tagString + foodTag +"|"
			
			tagString = name + " : " + tagString
			print tagString.decode("utf-8").encode("gbk")

			#show intro string
			introString = ""
			try:
				node["intros"]
			except:
				"""do nothing"""
			else:
				for introsItem in node["intros"]:
					introString = introString + introsItem + ":" + node["intros"][introsItem] + "&&"
				print introString.decode("utf-8").encode("gbk") + "\n"
	except:
		print "\nfinish"
	'''

if __name__ == "__main__":
	test()