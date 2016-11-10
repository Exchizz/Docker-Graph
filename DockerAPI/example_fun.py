from __future__ import print_function
from docker import Client
from pprint import pprint
cli = Client(base_url='unix://var/run/docker.sock')

#print cli.containers()[0]


networks = cli.networks()
for network in networks:
	id = network['Id']
	network_ = network['IPAM']['Config']
	print(network['Driver'], " ", end="")
	try:
		print(network_[0]['Subnet'])
	except:
		print("No dhcp")
	inspect_network = cli.inspect_network(id)
	for host in inspect_network['Containers']:
		docker = inspect_network["Containers"][host]
		print("\tFound docker: ", docker["Name"], " ip: ", docker["IPv4Address"])
		
