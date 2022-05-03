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
        node = Node ("127.0.0.1", 10001, node_callback)

# start to spin off a new thread
        node.start()
        time.sleep(1)

#connect to another node, otherwise you do not have any network
        node.connect_with_node('127.0.0.1, 10002')
        time.sleep(2)

#send some message to the other nodes 
        node.send_to_nodes('{"message:": "hi from node 1"}')
        time.sleep(5)

#stop node 
        node.stop()