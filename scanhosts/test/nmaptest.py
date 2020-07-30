import nmap
import pprint
nm = nmap.PortScanner()
result = nm.scan(hosts='172.25.254.20',arguments='-n -sP')
pprint.pprint(result)
print("nmap orderline:",nm.command_line())
print("host menu:",nm.all_hosts())
print("172.25.254.20 info:",nm['172.25.254.20'])