allow_number=0

while Ture:
	if [[ $(curl https://itops:123qweASD.@tbs01-mon01.cpanel.ge/cgi-bin/tac.cgi | grep  "class='hostHeader'" | awk '{print $5 ,$6}' | cut -d '>' --output-delimiter=$' ' -f 1- | awk '{print $2 }' | awk 'FNR == 1 {print}') != $allow_number]]; then
        	echo "good"
	else
		
	fi










