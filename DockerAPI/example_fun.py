from docker import Client

cli = Client(base_url='unix://var/run/docker.sock')

#print cli.containers()[0]


networks = cli.networks()[0]

#print networks

inspect_network = cli.inspect_network("faf69dd0b88d28d717af80b70b0d805ff78814c3f5661c83f9976e61bec8d157")

print inspect_network
