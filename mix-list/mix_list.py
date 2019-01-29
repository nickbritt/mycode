#!/usr/bin/env python3

mylist = ['192.168.0.5', 5060, 'UP']
#print("The first item in the list (IP): " + mylist[0])
#print("The second item in the list (port): " + str(mylist[1]))
#print("The last item in the list (state): " + mylist[2])

newlist = [5060, '80', 55, '10.0.0.1', '10.20.30.1', 'ssh']
print("When I " + newlist[5] + " into IP addresses " + newlist[3] + " or " + newlist[4] + " I am unable to ping ports " + str(newlist[0]) + ", " + str(newlist[1]) + ", " + str(newlist[2]))


