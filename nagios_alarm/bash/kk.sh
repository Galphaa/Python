## Geting monitoring tactical page source
mon_tac_url="curl https://itops:123qweASD.@tbs01-mon01.cpanel.ge/cgi-bin/tac.cgi"

## Parsing source code for hostheader tag
tac_source="grep  "class='hostHeader'" " 

## Parising for values(Down unreachable, up adn pending)
pars_value="awk '{print $4 ,$6}'" 

## Parsing output of pars_value for numbers only
par_val_out="cut -d '>' --output-delimiter=$' ' -f 1-" 

## Getting firt number (in this case is Down value)
Dowb_val="awk '{print $2 }' | awk 'FNR == 1 {print}'"

`$mon_tac_url | $tac_source | $pars_value | $par_val_out | $Dowb_val`
