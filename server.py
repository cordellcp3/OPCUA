#Author: Benjamin Isak - last update 04/02/2019

from opcua import ua, Server, uamethod
from random import randint
from colorama import init, Fore, Style
import datetime
import time
import logging
import os
import pyfiglet

#---SERVER INIT---#
logger = logging.getLogger("opcua.address_space")
logger.setLevel(logging.DEBUG)

#---colorama init---#
init(autoreset=True)
#-------------------#

server = Server()

url = "opc.tcp://192.168.178.23:4840"
server.set_endpoint(url)

name = "OPCUA_MACHINE_SIMULATION_SERVER"
addspace = server.register_namespace(name) #Addressraum

# alle Node-Objekte kommen hier rein
machine_node = server.get_objects_node()
#-----------------#

def getSensors():
    print(Fore.GREEN + "\nAktuelle Sensoren: \n","-Temperatur (°C) \n", "-Druck (bar) \n")

#---MASCHINEN PARAMETER / SENSOREN---#

# unseren Adressraum füllen
Params = machine_node.add_object(addspace, "Parameters")

temperature = Params.add_variable(addspace, "Temperatur", 0)
pressure = Params.add_variable(addspace, "Druck", 1.5)
systemTime = Params.add_variable(addspace, "Zeitstempel", 0)

for p in Params.get_children():
    p.set_writable()

try:
    server.start()
    os.system("cls")

    ascii_banner = pyfiglet.figlet_format("OPC UA Server")
    print(ascii_banner)
    print("...by Benjamin Isak ...2019\n")
    print(Fore.LIGHTBLUE_EX + "Server started at {}".format(url))
    time.sleep(0.5)

    getSensors()

    for x in range(0,8):
        print(".")
        time.sleep(0.2)

#---SIMULATION---#

    Press = 1.50

    while True:
        Temp = randint(10, 50)
        Press += 0.10 
        Time = datetime.datetime.now()

        print("Temp °C: {}".format(Temp))
        if (Press >= 2.5): 
            print(Fore.RED + "Druck (bar): {}".format(round(Press,2)))
        else:
             print("Druck (bar): {}".format(round(Press,2)))

        print(Time, "\n")

        temperature.set_value(Temp)
        pressure.set_value(Press)
        systemTime.set_value(Time)

        time.sleep(1)
#----------------#

finally:
    server.stop()

