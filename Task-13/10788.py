from ipaddress import *

def f(ip):
    ip = f'{int(ip):032b}'
    return ip.count('1') >= 5

ip1 = ip_address('201.44.240.33')
ip2 = ip_address('201.44.240.107')

cnt = 0
for mask in range(10, 31):
    net = ip_network(f'{ip1}/{mask}', False)
    if f(net.network_address) and ip1 in net.hosts() and ip2 in net.hosts():
        cnt += 1
print(cnt)