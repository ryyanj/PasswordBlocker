import atexit
import logging
from pytz import timezone
import pytz
from twilio.rest import Client
from datetime import datetime

from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.triggers.cron import CronTrigger

logging.basicConfig()
# Find these values at https://twilio.com/user/account
account_sid = "ACdc0bae8c0927f2fc28fb18d90d742832"
auth_token = "07b890944fba14516cdae417f4b9e4fb"
client = Client(account_sid, auth_token)
scheduler = BackgroundScheduler()
class PillScheduler():
	
	def pill_job(self):
		scheduler.start()
		scheduler.add_job(
		func=self.print_pill_message,
		trigger=CronTrigger(year='*', month='*', day='*', week='*', day_of_week='*', hour='22', minute='22', second='00'),
		id='printing_job',
		name='Print pill message every day at 11:30 AM Eastern Time',
		replace_existing=True)
		# Shut down the scheduler when exiting the app
		atexit.register(lambda: scheduler.shutdown())

	def print_pill_message(self):
		print('pill func was called')
		#+14782513043 - ryyan's phone number
		#+14782922142 - twilio number
		#+12514228131 - avery's phone number
		try:
			message = client.api.account.messages.create(to="+14782513043",
                                             from_="+14782922142",
                                             body="Don't forget to take your pill babe! I love you! ")
		except error:
			print(error)
