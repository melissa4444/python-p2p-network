from mels_p2p_application import NodeConnection

class mynodeConnetion (NodeConnection):
    #python class constructor 
    def __init__(self, main_node, sock, id, host, port):
        super(mynodeConnetion,self).__init__(main_node, sock, id, host, port) 

# Check yourself what you would like to change and override! See the 
 # documentation and code of the nodeconnection classfsdf