import sys
from FileSharingNode import FileSharingNode
## the port to listen to incoming node connections 
port = 9876

#synta for file_sharing_node.py port 
if len(sys.argv[1])> 1:
    port = int(sys.argv[1])

# instantiate the node FileSharingNode - it creates a thread to handle all functionality 
node = FileSharingNode("127.0.0.1", port)
#start the node if not started it will not handle any requests
node.start()

#the method prints the help commands text to the console 
def print_help():
    print("stop - Stops the application.")
    print("help - Prints this help text. ")

#implement a console application 
command = input("?")
while (command != "stop "):
    if(command == "help"):
        print_help()
        
    command = input("?")
node.stop()