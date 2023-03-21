#!/bin/bash

if [ -f /home/$1/.plan ]; then
	cat /home/$1/.plan
else
	echo "Uer $1 is not make .plan file."
fi
