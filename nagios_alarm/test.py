import time
from selenium import webdriver

usr = "itops"
passwd = "123qweASD."


#mon_url2  = "https://itops:123qweASD.@tbs01-mon01.cpanel.ge"
mon_url = ("https://{}:{}@tbs01-mon01.cpanel.ge".format(usr, passwd))
tac_mon_url = ("https://{}:{}@tbs01-mon01.cpanel.ge/cgi-bin/tac.cgi".format(usr, passwd))
test = "https://{}:{}@tbs01-mon01.cpanel.ge/cgi-bin/tac.cgi".format(usr, passwd)

print(test)
print(mon_url)

print(type(mon_url))
print(type(test))
# browser = webdriver.Firefox()
# 
# browser.get(mon_url)
# browser.get("https://itops:123qweASD%2E@tbs01-mon01.cpanel.ge/cgi-bin/tac.cgi")
