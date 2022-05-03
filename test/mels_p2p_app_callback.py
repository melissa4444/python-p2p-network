

import sys
import time 

from p2pnetwork.node import Node

#node_callback 
# event : event name 
# node : the node (Node) that holds the node connections
# connected_node : node (NodeConnection) that is involved 
# data : data that is send by the node (couble be empty)
def node_callback(event, node, connected_node, data):
    try: 
        # node_request_to_stop does not have any connected_node
        # while it is the main_node that is stoped!
        if event != 'node_request_to_stop':
            print('Event: {} from main node {}: connected node {}: {}'.format(event, node.id, connected_node.id, data))

    except Exception as e:
        print(e)

# the main node that is able to make connection to other nodes 
# and accept connection from other nodes on port 8001.
      #  node = Node ("127.0.0.1", 10001, node_callback)
        # test nodes 
        node_1 = Node("127.0.0.1", 8001, callback=node_callback)
        node_2 = Node("127.0.0.1", 8002, callback=node_callback)
        node_3 = Node("127.0.0.1", 8003, callback=node_callback)
# start to spin off a new thread
        time.sleep(1)
       # node.start()
        node_1.start()
        node_2.start()
        node_3.start()
        
        time.sleep(1)

#connect to another node, otherwise you do not have any network
       # node.connect_with_node('127.0.0.1, 10002')

        node_1.connect_with_node('127.0.0.1', 8001)
        node_2.connect_with_node('127.0.01', 8002)
        node_3.connect_with_node('127.0.0.1',8003 )
        time.sleep(2)
        

#send some message to the other nodes 
        node_1.send_to_nodes('{"message:": "hi from node 1"}')
        time.sleep(5)


#stop node 
        #node.stop() 
        node_1.stop()
        node_2.stop()
        node_3.stop()

print('goodbye...')