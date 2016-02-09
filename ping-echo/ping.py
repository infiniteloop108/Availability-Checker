import sys
import signal
import time
import socket
from time import gmtime, strftime

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

if len(sys.argv) == 2 and sys.argv[1] == 'help':
	pcolor('This tool pings a machine which runs the complementary echo service to check whether that machine is available', "b")
	pcolor('Usage: python ping.py ip_of_machine period(sec)', "p")
	pcolor('Period is the time interval in seconds between pings', "")
	pcolor('It needs to be an integer. 0 means that it will ping only once', "")
	sys.exit(0)

if len(sys.argv) != 3:
	pcolor('Wrong Format', "r")
	print 'run: python ping.py help'
	sys.exit(0)

def quitting(signal, frame):
	sys.exit(0)

signal.signal(signal.SIGINT, quitting)


ip = sys.argv[1]
try:
	timer = int(sys.argv[2])
except:
	pcolor('Period should be an integer', "r")
	sys.exit(0)

pcolor('Starting Pinging', "b")

while 1:
	sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	try:
		sock.connect((ip, 32459))
	except:
		pcolor('Ping failed at ' + strftime("%H:%M:%S", time.localtime()) + '! Server is unavailable.', "r")
		sys.exit(0)
	sock.settimeout(0.2)
	try:
		sock.sendall('ping service. please reply')
		reply = sock.recv(1024)
	except:
		pcolor('Ping failed at ' + strftime("%H:%M:%S", time.localtime()) + '! Server is unavailable.', "r")
		sys.exit(0)

	if reply == 'i am alive':
		pcolor('Ping succeeded at ' + strftime("%H:%M:%S", time.localtime()), "g")
	else:
		pcolor('Ping failed at ' + strftime("%H:%M:%S", time.localtime()) + '! Server is unavailable.', "r")
		sys.exit(0)

	sock.close()

	if timer == 0:
		break
	time.sleep(timer)
