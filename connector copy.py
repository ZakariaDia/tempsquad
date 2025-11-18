import socket
import csv
import pandas as pd
import datetime
import random
 
# Arduino’s IP address (from Arduino Serial Monitor)
HOST = "192.168.229.214"  # Use Your Arduino's IP. It will print when
                        #You Run the Arduino Server Program
PORT = 12345            # Must match Arduino’s UDP port

isHeader = False
# Create a UDP socket
mySocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
mySocket.settimeout(5.0)  # 5 seconds timeout for responses
 
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

def generator(list):
    listRandom = []
    for i in range(10):
        randomChoice = random.randrange(0,1)
        listRandom.append(random.uniform(list[randomChoice]-random.random(),list[randomChoice]+random.random()))
    return list

def writer(file, list, cond):
        writer = csv.writer(csv_file, delimiter=',')
        if cond == False:
            pass
        else:
            writer.writerow(["date","id","value"])
        for i in range(len(list)):
            if i<2:
                writer.writerow([datetime.datetime.now(),f"temp{i+1}",list[i]])
            else:
                writer.writerow([datetime.datetime.now(),f"hum{i-1}",list[i]])
            

while True:
    # Try to get a response, skip on timeout
    try:
        test = "ping"
        ping(test,mySocket,HOST,PORT)
        break
    except socket.timeout:
        # Send the ping to the server
        print("No response received from ESP32 within 5 seconds")

try:
    with open("measurements.csv","a+") as csv_file: 
        pd.read_csv("measurements.csv")
    isHeader = False
except:
    isHeader = True

csv_file = open("measurements.csv", "a",newline='')
while True:
    try:
        response, server_address = mySocket.recvfrom(1024)
        variables = response.decode().split(",")
        print(variables)
        variables = variables + generator(variables)
        
        writer(csv_file, variables,isHeader)
        isHeader = False
    except socket.timeout:
        print("No response received from ESP32 within 5 seconds")
        ping(test,mySocket,HOST,PORT)

close(csv_file)
# Close the socket
mySocket.close()
print("Socket closed")