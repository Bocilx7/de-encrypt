import os
import sys
import fileinput
import time
#warna
hitam   = "\033[0;30m"
biru    = "\033[0;34m"
ijo     = "\033[0;32m"
bm      = "\033[0;36m"
red     = "\033[0;31m"
purple  = "\033[0;35m"
brown   = "\033[0;33m"
abu     = "\033[0;37m"
hijo    = "\033[1;32m"
yellow  = "\033[1;33m"
putih   = "\033[1;37m"

N = '\x1b[0m'
D = '\x1b[90m'
W = '\x1b[0;37m'
B = '\x1b[1;34m'
R = '\x1b[1;31m'
G = '\x1b[1;32m'
Y = '\x1b[1;33m'
C = '\x1b[1;36m'
ask = G + '[' + W + '?' + G + '] '
sukses = G + '[' + W + '\xe2\x88\x9a' + G + '] '
eror = R + '[' + W + '!' + R + ']'
print("\033[0;34m         ___  ____ ____ ____ _   _ ___  ___")
print("\033[0;34m         |  \ |___ |    |__/  \_/  |__]  |")
print("\033[0;34m         |__/ |___ |___ |  \   |   |     |")
print("\033[0;36m======================================================\033[0m")
print u"\u001b[45mTools Decrypt File Bash Shell | Coded by Zen | Cr 2k19\u001b[0m"
print("\033[0;36m======================================================\033[0m")
print("\033[0;36m["+abu+"+"+bm+"]"+abu+"Author = Zen")
print("\033[0;36m["+abu+"+"+bm+"]"+abu+"Ask Me On Ig= https://instagram.com/aditiastrom")
print("\033[0;36m======================================================\033[0m")
print("\033[0;36m["+abu+"01"+bm+"]"+abu+"Decrypt File")
print("\033[0;36m["+abu+"00"+bm+"]"+abu+"Out Tools")
def dekrip():
   try:
       sc = raw_input(ask + W + "Input Your File " + G + "|> " + W)
       f = open(sc,'r')
       filedata = f.read()
       f.close()

       newdata = filedata.replace("eval","echo")

       out = raw_input(ask + W + "Output Your File" + G + " |> " + W)
       f = open(out,'w')
       f.write(newdata)
       f.close()

       os.system("touch tes.sh")
       os.system("bash " + out + " > tes.sh")
       os.remove(out)
       os.rename("tes.sh", out)
       print (sukses + "File Berhasil di Decrypt..")

   except KeyboardInterrupt:
       print (eror + " Berhenti!")
   except IOError:
       print (eror + " File Not Found!")

def enkrip():
   try:
       script = raw_input(ask + W + "Input Alamat File " + G + "> " + W)
       output = raw_input(ask + W + "Alamat Output File " + G + "> " + W)
       os.system("bash-obfuscate " + script + " -o " + output )
       print (sukses + "File Berhasil Di Encript.")
   except KeyboardInterrupt:
       print (eror + " Berhenti!")
   except IOError:
       print (eror + " File Not Found!")


takok = raw_input(W + "Input Number" + G + " |> ")

if takok == "2" or takok == "02":
   enkrip()
elif takok == "1" or takok == "01":
   dekrip()
else:
   print (eror + " Wrong input")
