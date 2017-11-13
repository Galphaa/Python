#!/bin/bash -x

while true
do
	allow_number=0
	value=`curl https://itops:123qweASD.@tbs01-mon01.cpanel.ge/cgi-bin/tac.cgi | grep  "class='hostHeader'" | awk '{print $5 ,$6}' | cut -d '>' --output-delimiter=$' ' -f 1- | awk '{print $2 }' | awk 'FNR == 1 {print}'`
	
	
	
	if [[ $value  != $allow_number ]]; then
		vlc /home/g/crowd-cheering.mp3
	fi
	sleep 120
done









