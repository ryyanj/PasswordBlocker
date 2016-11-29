import time
from TimeModelInMemory import TimeRAM
from WriteToFile import writePasswordToFile

timeram = TimeRAM()
MAX_BLOCK_LIMIT = 1200 

class Time():
	def blockerNotSet(self):
		print('the current time is ' + str(timeram.getCurrentTime()) + ' the stop time is ' + str(timeram.getStopTime()) )
		return timeram.getCurrentTime() > timeram.getStopTime()
	def getTimeLeftInMinutes(self):
		timeLeftInSeconds = timeram.getStopTime() - timeram.getCurrentTime()
		return time.strftime('%H:%M:%S', time.gmtime(timeLeftInSeconds))
	def setBlockTime(self,time):
		if not time.isdigit():
			return "This is not a valid entry."
		if float(time) > MAX_BLOCK_LIMIT:
			return "are you sure you want to block your password the long?"
		if self.blockerNotSet():
			newTime = timeram.getCurrentTime() + ( int(time) * 60 )
			timeram.updateStopTime(newTime)
			return "Temporary block time has begun." 
		else:
			return "Blocker is currently set. Time left is " + self.getTimeLeftInMinutes() + "."
	def getPassword(self):
		if self.blockerNotSet():
			return timeram.getPassword()
		else:
			return "Blocker is currently set."
	def getTime(self):
		if not self.blockerNotSet():
			return "Blocker is currently set. Time left is " + self.getTimeLeftInMinutes() + "."
		else:
			return "Blocker is not yet set."
	def setPassword(self,password):
		if self.blockerNotSet() and password.isdigit()==False:
			timeram.updatePassword(password)
			writePasswordToFile(password)
			return "Your password has been updated to " + password + "."
		elif password.isdigit()==True:
			return "Your password is invalid because it is a digit"
		else:
			return "Password can't be updated while blocker is set."
	def extendBlockTime(self,time):
		if not self.blockerNotSet():
			newStopTime = ( timeram.getStopTime() + ( float(time) * 60 ) )
			diffInSeconds = newStopTime - timeram.getCurrentTime();
			diffInMInutes = float(diffInSeconds)/60
			if diffInMInutes < 300:
				timeram.updateStopTime(newStopTime)
				return "Block time has been updated. Time left is " + self.getTimeLeftInMinutes() + "."
			else:
				return "You have blocked your password for the maximum block limit of " + str(MAX_BLOCK_LIMIT) + " already."
		else:
			return  "Blocker is not yet set."

