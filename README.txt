CS654 Assignment 4
Akshay Aggarwal, 12068

1. ping-echo

This tool checks the availability of a machine by pinging it through another machine and expecting a response.

First run the echo server on the machine you want to monitor using:
	python echo.py ip
where ip is the machine of the current machine (which is visible to the machine what will ping)

Now you can ping this machine from anywhere. run:
	python ping.py ip timer
where ip is the IP address of the machine to be checked and timer is the period in seconds between the pings. A timer of 0 pings only once. 
