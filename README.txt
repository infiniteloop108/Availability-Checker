CS654 Assignment 4
Akshay Aggarwal, 12068

Installation:

Install python and pip.
Do pip install psutil




1. ping-echo

This tool checks the availability of a machine by pinging it through another machine and expecting a response.
Machine B checks the availability of Machine A. Machine A runs the echo server and Machine B pings it.

First run the echo server on the machine you want to monitor (Machine A) using:

	python echo.py ip

where ip is the machine of the current machine (which is visible to the machine that will ping)

Now you can ping this machine from anywhere. run:

	python ping.py ip timer

where ip is the IP address of the machine to be checked and timer is the period in seconds between the pings. A timer of 0 pings only once.


You can also use ping_icmp which uses the ping utility provided by OS. run:

	python ping_icmp.py ip timer




2. heartbeat

This tool sends a heartbeat from Machine A for a particular process to Machine B which monitors it and reports error in case Machine A becomes unavailable.

First run beat.py on Machine A as:

	python beat.py ip timer pid

where ip is the IP of machine B (the machine you want to send the heartbeat to). Timer is your heart rate. and pid is the process you want to send the heartbeat for. A pid of -1 sends the heartbeat on behalf of the whole machine.

Now you can run monitor.py on Machine B as:

	python monitor.py ip period

where ip is the machine of the current machine (which is visible to the machine that will send the heartbeat)
