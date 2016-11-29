import os
import io
import os.path
def writePasswordToFile(password):
	FilePath = os.path.abspath(os.path.join(os.pardir,os.pardir)) + '/passwords.txt'
	with io.open(FilePath, 'a', encoding='utf-8') as file:
    		file.write(password + '\n\n')
