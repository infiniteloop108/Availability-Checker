import sys
import signal
import time
import socket
from time import gmtime, strftime
from thread import *

def pcolor(arr, col):
	if col == "p":
		print '\033[95m' + arr + '\033[0m'
	elif col == "g":
		print '\033[95m' + arr + '\033[0m'
	elif col == "r":
		print '\033[91m' + arr + '\033[0m'
	elif col == "b":
		print '\033[94m' + arr + '\033[0m'
	elif col == "y":
		print '\033[93m' + arr + '\033[0m'
	else:
		print arr;

if len(sys.argv) == 2 and sys.argv[1] == '--help':
	pcolor('This tool echoes to a machine which runs the complementary ping service to check whether this machine is available', "b")
	pcolor('Usage: python echo.py my_ip', "p")
	sys.exit(0)

if len(sys.argv) != 2:
	pcolor('Wrong Format', "r")
	print 'run: python echo.py --help'
	sys.exit(0)

ip = sys.argv[1]

pcolor('Starting Echo Service', "b")
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
	sock.bind((ip, 32459))
except:
	pcolor('Unable to bind to port 32459! Please free it.', "r")
	sys.exit(0)

sock.listen(10)

def handle_client(conn, addr):
	data = conn.recv(1024)
	if data == 'ping service. please reply':
		print 'Ping received from ' + addr[0]
		conn.sendall('i am alive')
	conn.close()

def quitting(signal, frame):
	print 'Closing echo'
	sock.close()
	sys.exit(0)

signal.signal(signal.SIGINT, quitting)


while 1:
	conn, addr = sock.accept()
	start_new_thread(handle_client ,(conn,addr))
