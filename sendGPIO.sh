#!/bin/bash

# sudo ln -s /home/pi/Documents/SloganOmatic/pdtoGPIO.service /etc/systemd/system/
# run: sudo systemctl start pdtoGPIO.service

while true ; do
	 pdreceive 55444 udp | (while true ; do 
	 	read -a h
	 	#echo pin:${h[0]} val:${h[1]}
	 	gpio -g write ${h[0]} ${h[1]}
	 done)
done

	 
