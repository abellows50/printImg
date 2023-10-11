#!/bin/bash
function print(){
	if [ $1 == "--help" ]
	then
		echo "-------------print help--------------------"
		echo "This is a program to print images in the terminal"
		echo "The format of this cmd is: print img-path [resolution] [file?]"
		echo "The respolution specifies how large the image should be."
		echo "file? should be the word file if you want to print to a file"
		echo "-------------------------------------------"
		
	else
		python3 ~/printImg/print.py $1 $2 $3
	fi
	
}

