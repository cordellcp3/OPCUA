#Author: Benjamin Isak - last update 03/18/2019

from opcua import Server
from random import randint
import datetime
import time

#---SERVER INIT---#
server = Server()
url = "opc.tcp://localhost:4841"
server.set_endpoint(url)

name = "OPCUA_MACHINE_SIMULATION_SERVER"
addspace = server.register_namespace(name) #Addressraum

machine_node = server.get_objects_node()
#-----------------#

#---MASCHINEN PARAMETER / SENSOREN---#
Params = machine_node.add_object(addspace, "Parameters")

temperature = Params.add_variable(addspace, "Temperatur", 0)
pressure = Params.add_variable(addspace, "Druck", 0)
systemTime = Params.add_variable(addspace, "Zeitstempel", 0)

temperature.set_writable()
pressure.set_writable()
systemTime.set_writable()

server.start()
print("OPC UA - Server started at {}".format(url))

#---SIMULATION---#
while True:
    Temp = randint(10, 50)
    Press = randint(100, 999)
    Time = datetime.datetime.now()

    print("Temp °C: {} - ".format(Temp), "Druck (bar): {} - ".format(Press), Time)

    temperature.set_value(Temp)
    pressure.set_value(Press)
    systemTime.set_value(Time)

    time.sleep(1.5)
    
#----------------#


