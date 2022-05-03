from platform import Node
import sys 
import time

from myp2pnode import myp2pnode

node = myp2pnode("127.0.0.1", 10001)


time.sleep(1)
node_1 = myp2pnode("127.0.0.1", 8001, 1)
node_2 = myp2pnode("127.0.0.1", 8002, 2)
node_3 = myp2pnode("127.0.0.1", 8003, 3)


node_1.start()
node_2.start()
node_3.start()


#start node 
node.start()
time.sleep(1)
#debug

node_1.connect_with_node('127.0.0.1', 8002)
node_2.connect_with_node('127.0.0.1', 8003)
node_3.connect_with_node('127.0.0.1', 8001)
time.sleep(2)

node_1.send_to_nodes("msg: hello friends!")
time.sleep(2)

print("node 1 is stoping...")
node_1.stop()

time.sleep(10)
#connect with another node, otherwise no network creation
#node.send_to_nodes({"message:" "hello friend..."})

node_2.send_to_nodes("msg: hi node 2")
node_2.send_to_nodes("msg: hi node 2")
node_2.send_to_nodes("msg: hi node 2")
node_3.send_to_nodes("msg: hi node 2")
node_3.send_to_nodes("msg: hi node 2")
node_3.send_to_nodes("msg: hi node 2")

#main lopp creation of application
time.sleep(5) 
#node.stop()
node_1.stop()
node_2.stop()
node_3.stop()
print('end...')