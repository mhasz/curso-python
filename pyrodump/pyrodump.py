import pyshark
import subprocess
import threading
import time
import signal
import os
import argparse

def extrair(camada, chave):
	valor = camada.split(chave)[1].split("\n")[0]
	valor = valor.replace("\x1b[0m\x1b[1m ", "").strip('"')

	return valor


def verificaBSSID(pacote, bssid):
	if "WLAN" in pacote:
		try:
			rede_bssid = pacote.wlan.bssid
		except AttributeError:
			return False

		if rede_bssid == bssid:
			return True

	return False

def ccanal(evento):
	if args.c != None:
		subprocess.run(["iwconfig", iface, "channel", str(args.c)])
	else:
		while not evento.is_set():
			for canal in [1,2,3,4,5,6,7,8,9,10,11,12,13,14]:
				subprocess.run(["iwconfig", iface, "channel", str(canal)])
				time.sleep(0.5)

def criptografia(pacote):
	if "RSN" in pacote:
		return "WPA2/RSN"
	elif "WPA" in pacote:
		return "WPA"
	elif "WEP" in pacote:
		return "WEB"
	else:
		return "Aberta"

def parsingPacket(pacote):
	if pacote.wlan.fc_type == "0":
		wlanmgt = str(pacote["WLAN.MGT"])
		bssid = pacote.wlan.bssid
		cifra = criptografia(wlanmgt)
		try:
			essid = extrair(wlanmgt, "SSID:")
			canal = extrair(wlanmgt, "Current Channel:")
		except IndexError:
			return 0

		if bssid not in redes and bssid != "ff:ff:ff:ff:ff:ff":
			redes[bssid] = essid
			print(f"{bssid}\t{canal}\t{cifra}\t{essid}")

	if "EAPOL" in pacote:
		bssid = pacote.wlan.bssid
		eapol = str(pacote["EAPOL"])
		n = extrair(eapol, "Message number:")
		handshake[n] = True
		if all(handshake.values()):
			print("Handshake capturado")
def capturar():
	evento = threading.Event()
	try:
		tcanal = threading.Thread(target=ccanal, args=(evento,))
		tcanal.start()

		print("BSSID                   CANAL   CIFRA           ESSID")

		if args.w:
			captura = pyshark.LiveCapture(interface=iface, output_file=args.w)
		else:
			captura = pyshark.LiveCapture(interface=iface)

		for pacote in captura.sniff_continuously():
			if not args.bssid or verificaBSSID(pacote, args.bssid):
				parsingPacket(pacote)

	except KeyboardInterrupt:
		evento.set()
		if args.w:
			subprocess.run(["editcap", "-F", "pcap", args.w, f"{args.w}.pcap"])

		os.killpg(os.getpid(), signal.SIGTERM)
		captura.close_async()
		captura.close()

parser = argparse.ArgumentParser()
parser.add_argument("-i", type=str, required=True, help="Interface de monitoramento")
parser.add_argument("--bssid", type=str, help="Filtra por BSSID da rede")
parser.add_argument("-c", type=str, help="Define um canal estatico")
parser.add_argument("-w", type=str, help="Salva captura em um arquivo PCAP")
args = parser.parse_args()

global redes
iface = args.i
redes = {}
handshake = {"1":False, "2":False, "3":False, "4":False}
capturar()

