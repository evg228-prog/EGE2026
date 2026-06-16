from ipaddress import *

def f(ip):
    ip = f'{int(ip):032b}'
    return ip.count('1') % 2 == 0

net = ip_network('172.16.128.0/255.255.192.0', False)
print(sum(f(i) for i in net))

# 8192
