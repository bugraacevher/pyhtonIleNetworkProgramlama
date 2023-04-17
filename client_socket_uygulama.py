# -*- coding: utf-8 -*-
"""
Created on Mon Apr 17 09:14:19 2023

@author: Buğra
"""

"""
        CLİENT SOCKET
"""

import socket

#soketi oluşturuyoruz.
client_socket = socket.socket() 

#server sokete bağlantı sağlıyoruz
client_socket.connect("localhost",50000)

mesaj = "client sistemden selamlar..."
cikis_mesaj = "exit"

#server sisteme mesaj gönderiyoruz..
client_socket.send(bytes(cikis_mesaj,'utf-8'))















