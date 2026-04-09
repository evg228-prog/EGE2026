from ipaddress import *

ip_host = ip_address('143.172.12.114')
ip_net = ip_address('143.172.8.0')

for mask in range(16, 25):
    net = ip_network(f'{ip_net}/{mask}', False)
    if ip_host in net.hosts() and ip_net == net.network_address:
        print(net.netmask)
        break

# 248