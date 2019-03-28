import atexit
import logging
from pytz import timezone
import pytz
from twilio.rest import Client
from datetime import datetime

from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.triggers.cron import CronTrigger

#######REMEMBER WHEN DEBUGGING THE SCHEDULER MESSAGES WITH TWILIO IT TAKES UP TO TWO MINUTES FOR THE CODE TO BE FULLY DEPLOYED#######

logging.basicConfig()
utc = pytz.utc	
# Find these values at https://twilio.com/user/account
account_sid = os.environ['ACCOUNT_SID']
auth_token = os.environ['AUTH_TOKEN']
client = Client(account_sid, auth_token)
scheduler = BackgroundScheduler()
class AveryMeditationScheduler():
	
	def avery_meditation_job(self):
		scheduler.start()
		scheduler.add_job(
		func=self.print_avery_meditation_job,
		#use this timer after daylight savings time end on November 17
		#trigger=CronTrigger(year='*', month='*', day='*', week='*', day_of_week='*', hour='3', minute='30', second='00',timezone=utc),
		#id='printing_job',
		#use this timer after daylight savings time begins on March 10
		trigger=CronTrigger(year='*', month='*', day='*', week='*', day_of_week='*', hour='2', minute='30', second='00',timezone=utc),
		id='printing_job',
		name='Print meditation schedule message every day at 10:30 pm Eastern Time',
		replace_existing=True)
		#UTC IS FIVE HOURS AHEAD BUT WHEN DAYLIGHT SAVINGS TIME KICKS IN AROUND MARCH IT IS ONLY 4 HOURS AHEAD!!!
		# Shut down the scheduler when exiting the app
		atexit.register(lambda: scheduler.shutdown())

	def print_avery_meditation_job(self):
		print('avery meditation func was called')
		#+14782513043 - ryyan's phone number
		#+14782922142 - twilio number
		#+12514228131 - avery's phone number
		try:
			message = client.api.account.messages.create(to="+12514228131",
                                             from_="+14782922142",
                                             body="It's time to meditate! Take some time to chill! ")
		except error:
			print(error)
