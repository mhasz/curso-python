import portClass
import sys


help = f""" PYPORT USAGE
python3 {sys.argv[0]} [hostname] [scantype=s/n] [-p- (OPCIONAL)]

s\tSYNSCAN / n = NORMAL SCAN
-p-\tTESTA 65535 PORTAS

"""
if len(sys.argv) < 3:
	print(help)
	exit(0)

host = sys.argv[1]
type = sys.argv[2]

try:
	ports = sys.argv[3]
except:
	ports = 0

if ports != "-p-" and ports != 0:
	print("Parametro invalido")
	exit(0)

if type != "s" and type != "n":
	print("Tipo de scan invalido")
	exit(0)

p = portClass.PortScan()

addr = p.getIP(host)
p.scanning(addr, type, ports)
