import socket
import csv
import pandas as pd
import datetime
import random
 
HOST = "10.35.255.214"  
                        
PORT = 12345            

isHeader = False
mySocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
mySocket.settimeout(5.0)  
 
print("UDP Client started.")

def ping(msg, sock, host, port):
    sendPing=msg.encode()
    sock.sendto(sendPing, (host, port))
    print('Sent '+msg+' to HOST',host,port)
    try:
        sock.recvfrom(1024)
        print("Recieved first data")
    except socket.timeout:
        ping(msg,sock,host,port)

def generateTemps(list):
    listRandom = []
    for i in range(8):
        randomChoice = random.randrange(0,1)
        lowerBound = float(list[randomChoice])-random.random()
        upperBound = float(list[randomChoice])+random.random()
        element = str(round(random.uniform(lowerBound,upperBound),2))
        listRandom.append(element)
    return listRandom

def generateHum(list):
    listRandom = []
    for i in range(8):
        randomChoice = random.randrange(2,3)
        lowerBound = float(list[randomChoice])-random.random()
        upperBound = float(list[randomChoice])+random.random()
        element = str(round(random.uniform(lowerBound,upperBound),2))
        listRandom.append(element)
    return listRandom

def generateMoy(list):
    listMoy = []
    totalTemp = 0
    totalHum = 0
    for i in range(len(list)):
        if 12 > i > 3:
            totalTemp = totalTemp + float(list[i])
        elif i > 11:
            totalHum = totalHum + float(list[i])
    moyenneTemp = str(round((totalTemp + float(list[0]) + float(list[1]) )/ 10, 2))
    moyenneHum = str(round((totalHum + float(list[2]) + float(list[3]) )/ 10, 2))
    listMoy.append(moyenneTemp)
    listMoy.append(moyenneHum) 

    return listMoy

def writer(file, list, cond):
    with open(file, "a",newline='') as csv_file:
        writer = csv.writer(csv_file, delimiter=',')
        if cond == False:
            pass
        else:
            header = ["date"]
            secondHalf = []
            for i in range(len(list)):
                if i<2:
                    secondHalf.append(f"temp{i+1}")
                elif i<4:
                    secondHalf.append(f"hum{i-1}")
                elif i<12:
                    secondHalf.append(f"tempSim{i-3}")
                elif i<20:
                    secondHalf.append(f"humSim{i-11}")
            secondHalf.append(f"tempMoy")
            secondHalf.append(f"humMoy")
            header.extend(secondHalf) 
            print(header)   
            writer.writerow(header)

        elements = []
        date = [f"{datetime.datetime.now()}"]
        print(date)
        for i in range(len(list)):
            elements.append(list[i])
        date.extend(elements)
        writer.writerow(date)

while True:
    try:
        test = "ping"
        ping(test,mySocket,HOST,PORT)
        break
    except socket.timeout:
        print("No response received from ESP32 within 5 seconds")

try:
    with open("measurements.csv","a+") as csv_file: 
        pd.read_csv("measurements.csv")
    isHeader = False
except:
    isHeader = True


while True:
    try:
        response, server_address = mySocket.recvfrom(1024)
        variables = response.decode().split(",")
        print(variables)
        variables = variables + generateTemps(variables) + generateHum(variables)
        variables = variables + generateMoy(variables)
        writer("measurements.csv",variables,isHeader)
        isHeader = False
    except socket.timeout:
        print("No response received from ESP32 within 5 seconds")
        ping(test,mySocket,HOST,PORT)

mySocket.close()
print("Socket closed")