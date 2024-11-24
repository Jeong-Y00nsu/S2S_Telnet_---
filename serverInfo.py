import server

class ServerInfo:
    sourceServer : server.Server
    destinationServers : list
    telnetResults : list
    sleepTime : int

    def __init__(self):
        return

    def setSourceServer(self, sourceServer):
        self.sourceServer = sourceServer
    
    def setDestinationServers(self, destinationServers):
        self.sourceServer = destinationServers

    def getSourceServer(self):
        return self.sourceServer
    
    def getDestinationServers(self):
        return self.destinationServers
    
    def setSleepTime(self, sleepTime):
        self.sleepTime = sleepTime

    def getSleepTime(self):
        return self.sleepTime