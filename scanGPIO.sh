#!/bin/bash

# sudo ln -s /home/pi/Documents/SloganOmatic/pdGPIO.service /etc/systemd/system/
# run: sudo systemctl start pdGPIO.service

pin[1]=4
pin[2]=17
pin[3]=27
pin[4]=22

b[1]=0
b[2]=0
b[3]=0
b[4]=0

for n in 1 2 3 4; do gpio -g mode ${pin[$n]} up ; done

while true ; do
	for n in 1 2 3 4; do 
	 	button=`gpio -g read ${pin[$n]}`
		if [ $button != ${b[$n]} ] ; then
			b[$n]=$button
			echo $n ${b[n]}";" | pdsend 55443 localhost udp
		fi
	done
	sleep 0.05;
done

	 
