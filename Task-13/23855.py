from ipaddress import *

net = ip_network('172.95.116.174/255.255.192.0', False)
ip = min(net.hosts())
print(eval(str(ip).replace('.', '+')))

# 332


