# -*- coding: utf-8 -*-  
import priorityQueue

#food : the food topic willing to get its related topics
#foods : all foods topics
#size : the number of food to feedback
#return a queue with most related topics
def suggest( food, foods, size ):
	queue = priorityQueue.PriorityQueue( size + 1 )
	
	#add the food topic which is more related with the current topic
	for foodName in foods:
		relPoint = 0
		for originItem in food["tags"]:
			for newItem in foods[foodName]["tags"]:
				if originItem == newItem:
					relPoint += 1
		
		for relatedLink in food["relatedLink"]:
			if relatedLink == foods[foodName]["number"]:
				relPoint += 2
		
		node = dict([('priorityNum', relPoint), ('name', foodName)])
		
		try:
			queue.put( node )
		except:
			popItem = queue.get()
			if popItem["priorityNum"] < node["priorityNum"]:
				queue.pop()
				queue.put( node )
				'''
				print ""
				print popItem["name"].decode("utf-8").encode("gbk")
				print popItem["priorityNum"]
				print node["name"].decode("utf-8").encode("gbk")
				print node["priorityNum"]
				'''				


				
	'''
	#print to test
	nodeList = []
	try:
		while True:
			node = queue.pop()
			nodeList.append( node )
	except:
		print "finish"
		
		
	nodeList.sort()
	
	for node in nodeList:
		print node['priorityNum']
		print node['name'].decode("utf-8").encode("gbk")
	'''
	return queue
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
