class Server:
    serverName: str
    ip : str
    port : str

    def __init__(self, serverName, ip, port):
        self.serverName = serverName
        self.ip = ip
        self.port = port

    def setServerName(self, serverName):
        self.serverName = serverName

    def setIp(self, ip):
        self.ip = ip

    def setPort(self, port):
        self.port = port

    def getServerName(self):
        return self.serverName
    
    def getIp(self):
        return self.ip
    
    def getPort(self):
        return self.port