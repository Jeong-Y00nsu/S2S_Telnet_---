import serverInfo
import pickle

class FileIO:
    def __init__(self):
        self.result = 0

    def writeServersInFile(servers):
        with open('s2s_telnet_autoGUI_servers.pkl', 'wb') as outp:
            for server in servers:
                pickle.dump(server)

    def readServersInFile(filename):
        servers = []
        with open(filename, "rb") as inp:
            while True:
                try:
                    servers.append(pickle.load(inp))
                    yield pickle.load(inp)
                except EOFError:
                    break
        return servers
    
    def writeCryptKey(key):
        with open('s2s_telnet_autoGUI_servers.pkl','wb') as outp:
            pickle.dump(key)

    def readCryptKey(fileName):
        key : str
        with open(fileName, 'rb') as inp:
            while True:
                try: 
                    key = pickle.load(inp)
                except EOFError:
                    break
        return key