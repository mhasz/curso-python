import requests
import sys, time
import threading

def check(url):
	with semaforo:
		re = requests.head(url, allow_redirects=False)
		code = re.status_code
		if code in [301, 302]:
			if url+"/" == re.headers.get("Location"):
				dirprint = f"+ DIRETORIO {url}/"

				re = requests.get(url+"/")
				if re.status_code == 200:
					html = re.text
					if "<title>Index of " in html:
						print(dirprint,"\n\u2514 INDEX OF")
					else:
						print(dirprint)
						pastas.append(url)
				else:
					print(dirprint)
					pastas.append(url)

		elif code in [200, 403]:
			print(f"{url} - CODE:{code}")

def looping(wordlist, dominio):
	global semaforo
	semaforo = threading.Semaphore(3)

	threads = []
	for i in wordlist:
		item = i.replace("\n", "")
		url = f"{dominio}{item}"
		t = threading.Thread(target=check, args=(url,))
		threads.append(t)
		t.start()

	for tt in threads:
		tt.join()



dominio = sys.argv[1]
wlist = sys.argv[2]

if dominio[-1] != "/":
	dominio += "/"

with open(wlist) as f:
	wordlist = f.readlines()

pastas = []
looping(wordlist, dominio)

if len(pastas) >= 1:
	for pasta in pastas:
		dominio = pasta + "/"
		looping(wordlist, dominio)

