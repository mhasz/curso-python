import sys, requests
from bs4 import BeautifulSoup
import threading, time
import re
import warnings

# Suprimir todos os warnings do modulo requests
warnings.filterwarnings("ignore", module="urllib3")

def getInfos(html):
	emailre = r"[a-z0-9_-]+@[a-z0-9_-]+\.[a-z\.]+"
	telelre = r"\+?\d{0,2}\s?\(\d{2}\)\s?\d{4,5}\s?-?\d{4}"

	emails = re.findall(emailre, html)
	telefones = re.findall(telelre, html)

	if len(emails) >= 1:
		for email in emails:
			if email not in temails:
				if email.split(".")[-1] not in ["png", "jpg", "jpeg", "mp4", "webm", "webp"]:
					temails.append(email)
					print(email)
	if len(telefones) >= 1:
		for telefone in telefones:
			if telefone not in ttelels:
				ttelels.append(telefone)
				print(telefone)

def checkLink(link, dominio, url):
	try:
		if "://" in link:
			dominiolink = link.split("://")[1].split("/")[0]
			if dominio in dominiolink:
				if link not in linksf:
					linksf.append(link)

		elif link[0] == "/":
			link = f"{semiurl}{link}"
			if link not in linksf:
				linksf.append(link)
		else:
			url = url.rpartition("/")[0]
			link = f"{url}/{link}"
			if link not in linksf:
				linksf.append(link)
	except IndexError:
		None

def findLinks(dominio, url):
	with semaforo:
		count = 0
		while True:
			try:
				re = requests.get(url, verify=False)
				break

			except requests.exceptions.ConnectionError:
				time.sleep(2)

			if count == 4:
				return 0

			count += 1

		html = re.text

		getInfos(html)
		soup = BeautifulSoup(html, "html.parser")

		for a in soup.find_all("a"):
			try:
				link = a["href"]
				checkLink(link, dominio, url)
			except KeyError:
				None

		for form in soup.find_all("form"):
			try:
				link = form["action"]
				checkLink(link, dominio, url)
			except KeyError:
				None

		for iframe in soup.find_all("iframe"):
			try:
				link = iframe["src"]
				checkLink(link, dominio, url)
			except KeyError: # Corrigido KetError -> KeyError
				None


url = sys.argv[1]
if url[:-1] != "/":
	url += "/"

protocolo = url.split("://")[0]
dominio = url.split("://")[1].split("/")[0]
semiurl = f"{protocolo}://{dominio}"

global linksf, semaforo, temails, ttelels

# Iniciando um sessão unica
# session = HTMLSession()

linksf = []
temails = []
ttelels = []

semaforo = threading.Semaphore(3)

findLinks(dominio, url)


if len(linksf) >= 1:
	for url in linksf:
		protocolo = url.split("://")[0]
		dominio = url.split("://")[1].split("/")[0]
		semiurl = f"{protocolo}://{dominio}"

		t = threading.Thread(target=findLinks, args=(dominio, url,))
		t.start()
