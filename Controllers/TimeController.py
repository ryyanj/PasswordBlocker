import time
import datetime
from TimeModelInMemory import TimeRAM
from WriteToFile import writePasswordToFile

timeram = TimeRAM()
MAX_BLOCK_LIMIT = 30000

class Time():
	def blockerNotSet(self):
		print('the current time is ' + str(timeram.getCurrentTime()) + ' the stop time is ' + str(timeram.getStopTime()) )
		return timeram.getCurrentTime() > timeram.getStopTime()
	def getTimeLeftInMinutes(self):

		seconds = timeLeftInSeconds = timeram.getStopTime() - timeram.getCurrentTime()
		hours = seconds // 3600
		minutes = (seconds % 3600) // 60
		seconds = seconds % 60
		td = datetime.timedelta(hours=hours, minutes=minutes, seconds=seconds)
		
		return '{}:{}:{}'.format(int(hours), int(minutes), int(seconds))
	def setBlockTime(self,time):
		if not time.isdigit() or float(time) < 0:
			return "This is not a valid entry."
		if float(time) > MAX_BLOCK_LIMIT:
			return "are you sure you want to block your password the long?"
		if self.blockerNotSet():
			newTime = timeram.getCurrentTime() + ( int(time) * 60 )
			timeram.updateStopTime(newTime)
			return "Temporary block time has begun." 
		else:
			return "Block Time: " + self.getTimeLeftInMinutes() + "."
	def getPassword(self):
		if self.blockerNotSet():
			return timeram.getPassword()
		else:
			return "Blocker is currently set."
	def getTime(self):
		if not self.blockerNotSet():
			return "Time Left: " + self.getTimeLeftInMinutes() + "."
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
		if not self.blockerNotSet() and float(time) > 0:
			newStopTime = ( timeram.getStopTime() + ( float(time) * 60 ) )
			diffInSeconds = newStopTime - timeram.getCurrentTime();
			diffInMInutes = float(diffInSeconds)/60
			if diffInMInutes < MAX_BLOCK_LIMIT:
				timeram.updateStopTime(newStopTime)
				return "Updated Time: " + self.getTimeLeftInMinutes() + "."
			else:
				return "You have blocked your password for the maximum block limit of " + str(MAX_BLOCK_LIMIT) + " already."
		elif float(time) < 0:
			return "This is not a valid entry"
		else:
			return  "Blocker is not yet set."

