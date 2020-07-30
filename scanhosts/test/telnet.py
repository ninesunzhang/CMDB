import telnetlib
import re

tn = telnetlib.Telnet(host='172.25.254.20',port=22,timeout=5)
tn_result=tn.read_until(b"\n",timeout=5).decode('utf-8')
ssh_result=re.search(pattern=r'ssh',string=tn_result,flags=re.I)
if ssh_result:
    print("linux yes")
else:
    print("no")