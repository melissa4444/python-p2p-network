from typing import Callable
from mynodeConnection import mynodeConnetion
from p2pnetwork.node import Node 

class myp2pnode (Node) :
    #python class constructor 
    def __init__(self, host: str, port: int, id: str = None, callback: Callable = None, max_connections: int = 0):
        super(myp2pnode.node, self).__init__(host, port, id, callback, max_connections)
        print("Mels Peer2PeerNode: Started...")

    def outbound_node_connected(self, connected_node):
        print("outbound_node_connected: (" + self.id + "):"+ connected_node.id)
   
    def inbound_node_connected(self, connected_node):
        print("inbound_node_connected: (" + self.id + "):" + connected_node.id)
    
    def inbound_node_disconnected(self, connected_node):
        print("inbound_node_disconnected: (" + self.id + "):" + connected_node.id)

    def outbound_node_disconnected(self, connected_node):
        print("outbound_node_disconnected: (" + self.id + "):"+ connected_node.id)

    def node_message(self, connected_node, data):
        print("node_message from:(" + self.id + "): "+ connected_node.id + ":" + str(data))
    
    def node_disconnect_with_outbound_node(self, connected_node):
        print("node wants to disconnect with other outbound node: " + connected_node.id)
    
    def node_request_to_stop(self):
        print("node is requesting to stop!")

    # to override node connection - to initiate NodeConnection Class
    def create_new_connection(self, connection, id, host, port):
       return mynodeConnetion(self, connection, id, host, port)

      