programfile = open('/home/srishti/myws/mlopsproject1/main_code.py','r')	#connecting to the code file
code = programfile.read()				

if 'keras' or 'tensorflow' in code:			
	if 'Conv2D' in code:				 
		print('CNN')
	else:
		print('not CNN')
else:
	print('not deep learning')