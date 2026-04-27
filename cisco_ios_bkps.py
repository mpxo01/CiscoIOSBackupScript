#Importando modulos necesarios
import netmiko 
from typing import List 
from netmiko import ConnectHandler 
from getpass import getpass 
from datetime import datetime, date
import yaml 
import os
os.mkdir("Network_Backups")
#------------------------------

fecha = date.today() #hacer que se tome la fecha actual del ordenador y se almacene en fecha.


#Abriendo archivo IPs.yml donde estan las direcciones y convirtiendo a lista
with open("IPs.yml") as file1:
	yml_doc = yaml.safe_load(file1)
	a2 = list(yml_doc)
#----------------------------------------------------------------------------

l2 = [] #Lista que guarde los diccionarios con las conexiones

username = input("Inserte nombre de usuario: ")
password = getpass("Inserte pass: ")


print("[+] accediendo al dispositivo...")

#almacenado todos los diccionarios con conexiones en l2
for i in a2:
	con = {
	"device_type": "cisco_ios_telnet",
	"host": i,
	"username": username,
	"password": password, 
	}
	
	l2.append(con)
#------------------------------------------------------

b = 0 #variable contador para recorrer lista de ips.
errip = [] #lista de ips erroneas.

for i in l2:	
	try:
		a = ConnectHandler(**i) #almacenado 1 por 1 cada conexion en a.
		out1 = a.find_prompt()
		hashtag = str(out1)
		out2 = a.send_command("show running-config")
		mitxt = open("Network_Backups\\" + str(fecha) + "_" + hashtag[:-1] + ".txt", "w")
		mitxt.write(out2)
		
		a.disconnect()
	except :
		errip.append("Connection error to " + str(a2[b]))
		print(errip)
		
	b += 1
#-----------------------------------------------------
#Guardando conexiones invalidas en archivo yml.
with open("errorips.yml", "w") as file2:
	yaml.dump(errip, file2)
