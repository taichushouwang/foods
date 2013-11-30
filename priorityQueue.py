#priorityQueue

class PriorityQueue:
	def __init__( self, maxsize ):
		self.queue = []
		self.maxSize = maxsize
		
	def qsize( self ):
		return len( self.queue )
		
	def pop( self ):
		if len( self.queue ) > 0:
			return self.queue.pop()
		else:
			raise

	def get( self ):
		if len( self.queue ) > 0:
			return self.queue[len( self.queue ) - 1]
		else:
			raise
	
	def put(self, item):
		if len( self.queue ) < self.maxSize:
			self.queue.insert(0, item)
			self.queue.sort(key=lambda it: it['priorityNum'], reverse=True)
		else:
			raise