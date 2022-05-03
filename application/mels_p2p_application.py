import sys 
import time

from myp2pnode import myp2pnode

node = myp2pnode("127.0.0.1", 10001)
time.sleep(1)

#start node 
node.start()
time.sleep(1)

#connect with another node, otherwise no network creation
node.send_to_nodes({"message:" "hello friend..."})

#main lopp creation of application
time.sleep(5) 
node.stop()