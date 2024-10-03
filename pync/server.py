import socket

class Server:
	def udp(ip, port):
		s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
		s.bind((ip, port))
		print(f"Aguardando conexão UDP {ip} {port}")

		while True:
			dados, cliente = s.recvfrom(1024)
			print(f"{cliente} - {dados.decode()}")

			msg = input(">")
			s.sendto(msg.encode(), cliente)


	def tcp(ip, porta):
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		s.bind((ip, porta))
		s.listen(1)

		print(f"Aguardando conexão TCP {ip} {porta}")
		con, cliente = s.accept()

		con.send("Digite a senha: ".encode())
		senha = con.recv(1024)

		if senha.decode() == "senhafoda123":
			while True:
				msg = input("> ")

				if msg == "sair":
					s.close()
					break

				msg += "\n"

				con.send(msg.encode())

				dados = con.recv(1024)
				print(dados.decode())

		else:
			s.close()

