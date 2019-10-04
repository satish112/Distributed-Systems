import socket
import os
import time

def main():
    host = '127.0.0.1'
    port=input("Enter port no->")
    type(port)
    
    global s
    s = socket.socket()
    s.connect((host, port))
    mesage=raw_input("Connection established succesfully! Press enter to continue..")
    print("1. DOWNLOAD 2.UPLOAD 3.RENAME 4.DELETE");
    choice=input("Enter your choice ->")
    type(choice)
	
	
    if choice==1:
	download()
    elif choice==2:
	upload()
    elif choice==3:
	rename()
    elif choice==4:
	delete()
	
    


		
		

def download():
    s.send("DL")
    filename = raw_input("Filename to Download? -> ")
    name=str(time.time())
    if filename != 'q':
        s.send(filename)
        data = s.recv(1024)
        if data[:6] == 'EXISTS':
            filesize = long(data[6:])
            message = raw_input("File exists, " + str(filesize) +"Bytes, download? (Y/N)? -> ")
            if message == 'Y':
                s.send("OK")
                f = open('download_new'+name, 'wb')
                data = s.recv(1024)
                totalRecv = len(data)
                f.write(data)
                while totalRecv < filesize:
                    data = s.recv(1024)
                    totalRecv += len(data)
                    f.write(data)
                    print "{0:.2f}".format((totalRecv/float(filesize))*100)+ "% Done"
                print "Download Complete!"
                f.close()
        else:
            print "File Does Not Exist!"

    s.close()

def upload():
	s.send("UL")
	filename = raw_input("Filename to Upload? -> ")
	if os.path.isfile(filename):
		s.send("EXISTS" + str(os.path.getsize(filename)))
		userResponse2=s.recv(1024)
        	if userResponse2[:2] == 'OK':
			with open(filename, 'rb') as f:
            				bytesToSend = f.read(1024)
            				s.send(bytesToSend)
            				while bytesToSend != "":
            					bytesToSend = f.read(1024)
                				s.send(bytesToSend)
			print("File uploaded successfully")
	else:
		print("Error,File not found")


def delete():
	s.send("DE")
	filename = raw_input("Filename to Delete? -> ")
    	if filename != 'q':
        	s.send(filename)
        	
	s.close()	
		
def rename():
	s.send("RE")
	filename=raw_input("Filename to Rename? ->")
	if filename != 'q':
		s.send(filename)
		serverresponse=s.recv(1024)
		if serverresponse[:2]=='OK':
			newfile=raw_input("File found! Enter the new filename ->")
			s.send(newfile)
		else:
			print("File not found on server")

	else:
		print("Invalid file name")
	
	

    

if __name__ == '__main__':
    main()
    


