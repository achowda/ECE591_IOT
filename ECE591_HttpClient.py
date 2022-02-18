import requests
import time
import statistics
import sys

NUM_TRANSFERS = 10
HOST = 'http://192.168.1.20:8081/Server/10MB'

timeList = []

def transferTimeMeas():
    for i in range(0,NUM_TRANSFERS):
        start = time.time()
        req = requests.get(HOST,timeout = 10)
        #print("Num Bytes = " + str(len(req.content)))
        end = time.time()
        timeList.append((end-start))


    print("Average Time Elapsed = " + str(statistics.mean(timeList)) + " seconds")
    print("Standard Deviation = " + str(statistics.stdev(timeList)) + " seconds")
    timeList.clear()

def headerSizeMeas():
    req = requests.head('http://192.168.1.20:8081/Server/10MB',timeout = 10)
    print("Header Size (10MB) = " + str(sys.getsizeof(req.headers)))
    req = requests.head('http://192.168.1.20:8081/Server/1MB',timeout = 10)
    print("Header Size (1MB) = " + str(sys.getsizeof(req.headers)))
    req = requests.head('http://192.168.1.20:8081/Server/10KB',timeout = 10)
    print("Header Size (10KB) = " + str(sys.getsizeof(req.headers)))
    req = requests.head('http://192.168.1.20:8081/Server/100B',timeout = 10)
    print("Header Size (100B) = " + str(sys.getsizeof(req.headers)))

def main():
    transferTimeMeas() #Function to measure transfer time 
    headerSizeMeas()   #Function to measure header size
    
if __name__ == "__main__":
    main()
