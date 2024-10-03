import server
import client
import sys


help = """ ncpy USAGE

python3 ncpy.py -s [tcp/udp] port
python3 ncpy.py -c [tcp/udp] ip port

"""
try:
	tipo = sys.argv[1]
except:
	print (help)
	exit(0)


if tipo == "-s":
	ip = "0.0.0.0"
	protocol = sys.argv[2]
	port = int(sys.argv[3])

	s = server.Server

	if protocol == "tcp":
		try:
			s.tcp(ip, port)
		except KeyboardInterrupt:
			exit(0)

	elif protocol == "udp":
		try:
			s.udp(ip, port)
		except KeyboardInterrupt:
			exit(0)
	else:
		print (help)

elif tipo == "-c":
	protocol = sys.argv[2]
	ip = sys.argv[3]
	port = int(sys.argv[4])

	c = client.Client

	if protocol == "tcp":
		try:
			c.tcp(ip, port)
		except KeyboardInterrupt:
			exit(0)

	elif protocol == "udp":
		try:
			c.udp(ip, port)
		except KeyboardInterrupt:
			exit(0)
	else:
		print (help)

elif tipo == "-h" or tipo == "--help":
	print(help)
else:
	print(help)
