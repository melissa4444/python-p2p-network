import sys
from FileSharingNode import FileSharingNode
## the port to listen to incoming node connections 
port = 9876

#synta for file_sharing_node.py port ls
if len(sys.argv)> 1:
    port = int(sys.argv[1])

# instantiate the node FileSharingNode - it creates a thread to handle all functionality 
node = FileSharingNode("127.0.0.1", port)
#start the node if not started it will not handle any requests
node.start()

#the method prints the help commands text to the console 
def print_help():
    print("stop")
    print("help")

#implement a console application 
command = input("?")
while (command != "stop "):
    if(command == "help"):
        print_help()
        
    command = input("?")

node.stop()
''' 
From this moment already have the bare minimum application that implements the framework p2pnetwork.
No application specifics have been coded yet. The node is already listening to incoming connections
and able to connect to other nodes at your command. From this point add the required functionality 
to the application. In order to test this application run the application twice on different ports.
In this case you could open two terminals and run the following commands:
1. ````python file_sharing_node.py 9876````
2. ````python file_sharing_node.py 9877```` '''