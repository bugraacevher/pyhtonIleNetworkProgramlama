# -*- coding: utf-8 -*-
"""
Created on Fri Apr 14 15:27:42 2023

@author: Buğra
"""

import socket

# Socket oluşturma
server_socket = socket.socket()

"""
Ports 0-1024 are forbidden for programs..
Ports 1024-49151- Registered Port -These can be registered for services wİth the IANA and should be
treated as semi- reserved. User written programs should not üşe these ports.
Ports 49152-65535— These are üşed by client programs and you are free to üşe these İn client programs .
"""

server_socket.bind("localhost",50000)

#soketimiz dinlemeye başlıyor.
server_socket.listen(5)
print("Soket bağlantısı oluşturuldu...")

while True:
    client_socket ,adres = server_socket.accept() 
    print(adres," isimli bilgisayar ile bağlantı kuruldu...")
    
    #client sistemden gelen mesajı ekrana yazıyoruz..
    gelen_mesaj = client_socket.recv(1024).decode()
    print(gelen_mesaj)
    
    client_socket.close()       
    
    # While döngüsünde programımızın takı Zıp kalmaması için client'den 'exit' ıpesajı geldiğinde
    # while döngüsünden çıkıyoruz ve server artık 59999. porttan dinlemeyi bitiyiryor, program sonlanıyor.
    # Burası önemli çünkü bu kısmı yapmazsak 59999. port bind edi Imiş bir şekilde kalır ve hata alırız. .
    
    if(gelen_mesaj == "exit"):
        break

print("Hoşçakalın..")
