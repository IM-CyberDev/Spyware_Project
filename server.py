import socket
import sys
import cv2
import pickle
import numpy as np
import struct ## new
import random
import string

HOST='127.0.0.1'
PORT=49999

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

s.bind((HOST,PORT))
s.listen(10)


while True:
			try :
				conn,addr=s.accept()
			except:
				pass
			else:
				
				l = conn.recv(4096)
				if(l!= None):
					temp = "output".join(random.SystemRandom().choice(string.ascii_uppercase + string.digits) for _ in range(10))+".mp4"
					f= open(temp,'wb') 
					while (l):
						f.write(l)
						l = conn.recv(4096)
					f.close()
					l = None
					conn.close()
				
		
			