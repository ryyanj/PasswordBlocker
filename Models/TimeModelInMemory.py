import time


class TimeRAM():
	def __init__(self):
		self.stop_time=0
		self.password='default password'
	def getCurrentTime(self):
		return time.time()
	def getStopTime(self):
		return self.stop_time
	def getPassword(self):
		return self.password
	def updateStopTime(self,newStopTime):
		self.stop_time=newStopTime
		print(self.stop_time)
	def updatePassword(self,password):
		self.password = password
