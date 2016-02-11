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
		print '\033[92m' + arr + '\033[0m'
	elif col == "r":
		print '\033[91m' + arr + '\033[0m'
	elif col == "b":
		print '\033[94m' + arr + '\033[0m'
	elif col == "y":
		print '\033[93m' + arr + '\033[0m'
	else:
		print arr;

if len(sys.argv) == 2 and sys.argv[1] == '--help':
	pcolor('This tool monitors a machine which sends it a heartbeat', "b")
	pcolor('Usage: python monitor.py my_ip period(sec)', "p")
	sys.exit(0)

if len(sys.argv) != 3:
	pcolor('Wrong Format', "r")
	print 'run: python monitor.py --help'
	sys.exit(0)

ip = sys.argv[1]
try:
	timer = int(sys.argv[2])
except:
	pcolor('Period should be an integer', "r")
	sys.exit(0)

if timer <= 0 :
	pcolor('Period should be positive', "r")
	sys.exit(0)


pcolor('Starting Monitoring Service at ' + strftime("%H:%M:%S", time.localtime()), "b")
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
	sock.bind((ip, 32460))
except:
	pcolor('Unable to bind to port 32460! Please free it.', "r")
	sys.exit(0)

sock.listen(10)

def quitting(signal, frame):
	print 'Closing Monitor'
	sock.close()
	sys.exit(0)

signal.signal(signal.SIGINT, quitting)

last_time = time.time()
def check_heartbeat():
	while 1:
		curr_time = time.time()
		if curr_time - last_time > timer:
			pcolor(strftime("%H:%M:%S", time.localtime()) + ': Heartbeat is not coming on time. Process may be unavailable', "r")
		time.sleep(1)

start_new_thread(check_heartbeat, ())

def handle_client(conn, addr):
	data = conn.recv(1024)
	if data == 'i am alive':
		pcolor(strftime("%H:%M:%S", time.localtime())  + ': Heartbeat received from ' + addr[0], "g")
		global last_time
		last_time = time.time()
	conn.close()

while 1:
	conn, addr = sock.accept()
	start_new_thread(handle_client ,(conn,addr))
