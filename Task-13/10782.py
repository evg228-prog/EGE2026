from ipaddress import *

ip_1 = ip_address('118.187.59.255')
ip_2 = ip_address('118.187.65.115')

for mask in range(16, 31)[::-1]:
    net = ip_network(f'{ip_1}/{mask}', False)
    if ip_1 in net.hosts() and ip_2 not in net.hosts():
        print(mask)
        break

# 21