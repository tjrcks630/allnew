#!/bin/bash

opt=$1
opt2=$2

if [ $# -eq 2 ];then
	if [ $opt == 'test' -a $opt2 == 'aaa' ]; then
		echo good

	elif [ $opt == 'aaa' -a $opt2 == 'test' ]; then
		echo good
	
	else
		echo bad
	fi
else
	echo "Input two parameters..!!"
fi

