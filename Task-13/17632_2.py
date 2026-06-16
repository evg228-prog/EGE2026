from ipaddress import *

def f(ip):
    ip = f'{int(ip):032b}'
    return ip.count('1') % 5 == 0

net = ip_network('112.160.0.0/12', False)
print(sum(f(i) for i in net))

# 215766