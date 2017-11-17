import atexit
import logging
from pytz import timezone
import pytz
from twilio.rest import Client
from datetime import datetime

from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.triggers.cron import CronTrigger

logging.basicConfig()
utc = pytz.utc
# Find these values at https://twilio.com/user/account
account_sid = "ACdc0bae8c0927f2fc28fb18d90d742832"
auth_token = "07b890944fba14516cdae417f4b9e4fb"
client = Client(account_sid, auth_token)
scheduler = BackgroundScheduler()
class AveryExerciseScheduler():
	
	def avery_exercise_job(self):
		scheduler.start()
		scheduler.add_job(
		func=self.print_avery_exercise_job,
		trigger=CronTrigger(year='*', month='*', day='*', week='*', day_of_week='*', hour='12-23', minute='22', second='00',timezone=utc),
		id='printing_job',
		name='Print exercise schedule message every day on the 22nd minute of each hour between 11am and 10pm Eastern Time',
		replace_existing=True)
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