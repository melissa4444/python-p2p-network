import sys
import time 

from p2pnetwork.securenode import SecureNode

node = SecureNode("127.0.0.1", 10001)
time.sleep(1)

node.start()