import os
import io
import os.path

def writePasswordToFile(password):
	with io.open(os.path.abspath(os.pardir) + '/passwords.txt', 'a', encoding='utf-8') as file:
    		file.write(password + '\n\n')
