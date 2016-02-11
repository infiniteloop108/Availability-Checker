import sys
import psutil
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

if len(sys.argv) == 2 and sys.argv[1] == '--help':
	pcolor('This tool sends a heartbeat to a machine which can monitor it to check whether this machine/process is available', "b")
	pcolor('Usage: python beat.py ip_of_machine period(sec) process_id', "p")
	pcolor('Period is the time interval in seconds between pings', "")
	pcolor('It needs to be an integer > 0', "")
	pcolor('process_id is the pid of the process you want to monitor (send heartbeat for)', "")
	pcolor('If it is given as -1, then no single process is monitored. The whole machine sends the heartbeat', "")
	sys.exit(0)

if len(sys.argv) != 4:
	pcolor('Wrong Format', "r")
	print 'run: python beat.py --help'
	sys.exit(0)

def quitting(signal, frame):
	sys.exit(0)

signal.signal(signal.SIGINT, quitting)


ip = sys.argv[1]
try:
	timer = int(sys.argv[2])
	pid = int(sys.argv[3])
except:
	pcolor('Period should be an integer', "r")
	pcolor('pid should be an integer', "r")
	sys.exit(0)

if timer <= 0 :
	pcolor('Period should be positive', "r")
	sys.exit(0)

pcolor('Starting Heartbeat', "b")

while 1:
	if pid >=0 and not psutil.pid_exists(pid):
		pcolor('Heartbeat sending failed at ' + strftime("%H:%M:%S", time.localtime()) + '! Given process is not alive!', "r")
		sys.exit(0)
	else:
		sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		try:
			sock.connect((ip, 32460))
			sock.sendall('i am alive')
			pcolor('Heartbeat sent at ' + strftime("%H:%M:%S", time.localtime()), "g")
		except:
			pcolor('Heartbeat sending failed at ' + strftime("%H:%M:%S", time.localtime()) + '! No one is listening to it!', "r")
		sock.close()
	time.sleep(timer)
