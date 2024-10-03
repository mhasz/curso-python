import sys
import base64
import math
import random, string, os, shutil
import PyInstaller.__main__

def randomName(n):
    name = random.choice(string.ascii_uppercase)
    
    for i in range(n - 1):
        ch = random.choice(string.ascii_uppercase + "1234567890")
        name += ch

    return name
    

with open(sys.argv[1], "rb") as f:
    enc_code = base64.b64encode(f.read()).decode()
    metade = math.floor(len(enc_code) / 2)
    
    p1 = enc_code[:metade]
    p2 = enc_code[metade:]

with open("raw_code.py") as raw:
    raw_code = raw.read()
    raw_code = raw_code.replace('{p2}', p2)
    raw_code = raw_code.replace('{p1}', p1)
    randomize = ['<nomescript>', '<mem>', '<memtotal>', '<cpu>', '<lcpu>', '<fcpu>', '<base64>', '<junto>', '<p1>', '<p2>', '<process>', '<psutil>', '<rr>', '<rr2>', '<filed>', '<savef>']
    for i in randomize:
        raw_code = raw_code.replace(i, randomName(10))


with open("codigo.py", "w") as f:
    f.write(raw_code)

PyInstaller.__main__.run(["codigo.py", '--onefile', '--windowed', '--distpath', './', '--name', 'codigo.exe', '--clean',])

shutil.rmtree('build')
os.remove('codigo.exe.spec')
