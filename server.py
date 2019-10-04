import socket
import threading
import os
import random
import time

def send(name, sock):
    userResponse = sock.recv(1024)
    if userResponse[:2] == 'DL':
	filename = sock.recv(1024)
    	if os.path.isfile(filename):
        	sock.send("EXISTS " + str(os.path.getsize(filename)))
		userResponse2=sock.recv(1024)
        	if userResponse2[:2] == 'OK':
            		with open(filename, 'rb') as f:
            			bytesToSend = f.read(1024)
            			sock.send(bytesToSend)
            			while bytesToSend != "":
            				bytesToSend = f.read(1024)
                			sock.send(bytesToSend)
    elif userResponse[:2] == 'UL':
	filename=str(time.time())
	data=sock.recv(1024)
	if data[:6] == 'EXISTS':
            filesize = long(data[6:])
	    
            sock.send("OK")
            f = open('new_upload_'+filename, 'wb')
            totalRecv = len(data)
            f.write(data)
            while totalRecv < filesize:
            	data = sock.recv(1024)
            	totalRecv += len(data)
            	f.write(data)
            print "Upload Complete!"
            f.close()
	    sock.close()
   	
    	else:
		print("Error in connection")        	
		sock.send("ERR ")
    elif userResponse[:2] == 'DE':

		filename = sock.recv(1024)
	    	if os.path.isfile(filename):
			os.remove(filename)
		    	print("File deleted")
		else:
			print("File not found on server")
    elif userResponse[:2] == 'RE':
		filename = sock.recv(1024)
	    	if os.path.isfile(filename):
			sock.send("OK")
			newfile=sock.recv(1024)
			os.rename(filename,newfile)
		    	print("File "+str(filename)+" renamed to "+str(newfile))
		else:
			print("File not found on server")


def Main():
    host = '127.0.0.1'
    port=random.randint(5000,8000)
    


    s = socket.socket()
    s.bind((host,port))

    s.listen(5)

    print("Server Started at Port:")
    print(port)
    while True:
        c, addr = s.accept()
        print "client connected ip:<" + str(addr) + ">"
        t = threading.Thread(target=send, args=("RetrThread", c))
        t.start()
         
    s.close()

if __name__ == '__main__':
    Main()
