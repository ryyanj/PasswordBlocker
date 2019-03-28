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
class AveryExerciseScheduler():
	
	def avery_exercise_job(self):
		scheduler.start()
		scheduler.add_job(
		func=self.print_avery_exercise_job,
		#Use this one after Nov 17 when daylight savings time ends
		#trigger=CronTrigger(year='*', month='*', day='*', week='*', day_of_week='*', hour='16-23,0-3', minute='22', second='00',timezone=utc),
		#id='printing_job',
		#Use this one after March 10 when daylight savings time begins
		trigger=CronTrigger(year='*', month='*', day='*', week='*', day_of_week='*', hour='15-23,0-2', minute='22', second='00',timezone=utc),
		id='printing_job',
		name='Print exercise schedule message every day on the 22nd minute of each hour between 11am and 10pm Eastern Time',
		replace_existing=True)
		#UTC IS FIVE HOURS AHEAD BUT WHEN DAYLIGHT SAVINGS TIME KICKS IN AROUND MARCH IT IS ONLY 4 HOURS AHEAD!!!
		# Shut down the scheduler when exiting the app
		atexit.register(lambda: scheduler.shutdown())

	def print_avery_exercise_job(self):
		print('avery exercise func was called')
		#+14782513043 - ryyan's phone number
		#+14782922142 - twilio number
		#+12514228131 - avery's phone number
		try:
			message = client.api.account.messages.create(to="+12514228131",
                                             from_="+14782922142",
                                             body="Don't forget to do your exercises!")
		except error:
			print(error)
