import sys
import os
import time
import datetime


ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, ROOT_DIR + '/Controllers')
sys.path.insert(0, ROOT_DIR + '/Models')
sys.path.insert(0, ROOT_DIR + '/Utilities')
sys.path.insert(0, ROOT_DIR + '/Schedulers')

from TimeController import Time
from XboxTimeController import XboxTime
from flask import Flask, jsonify, request, Response, render_template 
from pill_scheduler import PillScheduler
from avery_exercise_scheduler import AveryExerciseScheduler
from avery_meditation_scheduler import AveryMeditationScheduler


app = Flask(__name__)
time = Time()
xboxtime = XboxTime()

pillSched = PillScheduler()
averyExerciseSched = AveryExerciseScheduler()
averyMeditationSched = AveryMeditationScheduler()

#start scheduled jobs
pillSched.pill_job()
averyExerciseSched.avery_exercise_job()
averyMeditationSched.avery_meditation_job()


@app.route('/',methods=['GET'])
def defaultFunction():
	return render_template('index.html')


@app.route('/setTime',methods=['GET'])
def setTime():
	response = Response('</!DOCTYPE html><html><head><meta name="viewport" content="width=device-width, initial-scale=1"><title>Ryyan Password Blocker</title></head><h2><a href="/">Home</a><br><body style="background-color:blue;"><form action="/showNewTime" width="2000px" method="POST"><input name="t"><input type="submit" value="Enter Time"></form></body></html>')
	response.headers['Cache-Control'] = 'no-cache, no-store, must-revalidate'
	return response

@app.route('/showNewTime',methods=['POST'])
def showNewTime():
	blockTime = request.form['t'] 
	response = Response(time.setBlockTime(blockTime))
	response.headers['Cache-Control'] = 'no-cache, no-store, must-revalidate'
	return response

@app.route('/setExtendTime',methods=['GET'])
def setExtendTime():
	response = Response('</!DOCTYPE html><html><head><meta name="viewport" content="width=device-width, initial-scale=1"><title>Ryyan Password Blocker</title></head><h2><a href="/">Home</a><br><body style="background-color:blue;"><form action="/showExtendTime" width="2000px" method="POST"><input name="et"><input type="submit" value="Enter Additional Time"></form></body></html>')
	response.headers['Cache-Control'] = 'no-cache, no-store, must-revalidate'
	return response

@app.route('/showExtendTime',methods=['POST'])
def showExtendTime():
	extendTime = request.form['et']
	response = Response(time.extendBlockTime(extendTime))
	response.headers['Cache-Control'] = 'no-cache, no-store, must-revalidate'
	return response

@app.route('/time',methods=['GET'])
def getTime():
	response = Response(time.getTime())
	response.headers['Cache-Control'] = 'no-cache, no-store, must-revalidate'
	return response

@app.route('/password',methods=['GET'])
def getPassword():
	response = Response(time.getPassword())
	response.headers['Cache-Control'] = 'no-cache, no-store, must-revalidate'
	return response

@app.route('/setPassword',methods=['GET'])
def setPassword():
	response = Response('</!DOCTYPE html><html><head><meta name="viewport" content="width=device-width, initial-scale=1"><title>Ryyan Password Blocker</title></head><body style="background-color:blue;"><form action="/showNewPassWord" width="2000px" method="POST"><input name="p"><input type="submit" value="Enter Password"></form></body></html>')
	response.headers['Cache-Control'] = 'no-cache, no-store, must-revalidate'
	return response

@app.route('/showNewPassWord',methods=['POST'])
def showNewPassword():
	password = request.form['p'] 
	response = Response(time.setPassword(password))
	response.headers['Cache-Control'] = 'no-cache, no-store, must-revalidate'
	return response





@app.route('/xboxsetTime',methods=['GET'])
def xboxsetTime():
	response = Response('</!DOCTYPE html><html><head><meta name="viewport" content="width=device-width, initial-scale=1"><title>Ryyan Password Blocker</title></head><h2><a href="/">Home</a><br><body style="background-color:blue;"><form action="/xboxshowNewTime" width="2000px" method="POST"><input name="t"><input type="submit" value="Enter Time"></form></body></html>')
	response.headers['Cache-Control'] = 'no-cache, no-store, must-revalidate'
	return response

@app.route('/xboxshowNewTime',methods=['POST'])
def xboxshowNewTime():
	blockTime = request.form['t'] 
	response = Response(xboxtime.setBlockTime(blockTime))
	response.headers['Cache-Control'] = 'no-cache, no-store, must-revalidate'
	return response

@app.route('/xboxsetExtendTime',methods=['GET'])
def xboxsetExtendTime():
	response = Response('</!DOCTYPE html><html><head><meta name="viewport" content="width=device-width, initial-scale=1"><title>Ryyan Password Blocker</title></head><h2><a href="/">Home</a><br><body style="background-color:blue;"><form action="/xboxshowExtendTime" width="2000px" method="POST"><input name="et"><input type="submit" value="Enter Additional Time"></form></body></html>')
	response.headers['Cache-Control'] = 'no-cache, no-store, must-revalidate'
	return response

@app.route('/xboxshowExtendTime',methods=['POST'])
def xboxshowExtendTime():
	extendTime = request.form['et']
	response = Response(xboxtime.extendBlockTime(extendTime))
	response.headers['Cache-Control'] = 'no-cache, no-store, must-revalidate'
	return response

@app.route('/xboxtime',methods=['GET'])
def xboxgetTime():
	response = Response(xboxtime.getTime())
	response.headers['Cache-Control'] = 'no-cache, no-store, must-revalidate'
	return response

@app.route('/xboxpassword',methods=['GET'])
def xboxgetPassword():
	response = Response(xboxtime.getPassword())
	response.headers['Cache-Control'] = 'no-cache, no-store, must-revalidate'
	return response

@app.route('/xboxsetPassword',methods=['GET'])
def xboxsetPassword():
	response = Response('</!DOCTYPE html><html><head><meta name="viewport" content="width=device-width, initial-scale=1"><title>Ryyan Password Blocker</title></head><body style="background-color:blue;"><form action="/xboxshowNewPassWord" width="2000px" method="POST"><input name="p"><input type="submit" value="Enter Password"></form></body><html>')
	response.headers['Cache-Control'] = 'no-cache, no-store, must-revalidate'
	return response

@app.route('/xboxshowNewPassWord',methods=['POST'])
def xboxshowNewPassword():
	password = request.form['p'] 
	response = Response(xboxtime.setPassword(password))
	response.headers['Cache-Control'] = 'no-cache, no-store, must-revalidate'
	return response

if __name__=='__main__':
	app.run(debug=True, port=8081)
