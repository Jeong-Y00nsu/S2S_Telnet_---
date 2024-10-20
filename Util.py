import server
import serverInfo

class Util:
    
    ''' 서버 목록을 입력으로 받고, 그 목록에서 중복되었는지 여부를 판단'''
    def isDuplicateServer(serverList, server):
        return server in serverList
    
    ''' 서버 정보에서 도착지 서버를 찾고 위치를 반환한다. '''
    def findDestinationServer(serverInfoList, server):
        i = 0
        for serverInfo in serverInfoList:
            j = 0
            for destinationServer in serverInfo.destinationServers:
                if server == destinationServer:
                    return i,j
                j += 1
            i += 1
        return i,j
    
    ''' 도착지 서버 위치의 서버를 가져온다. '''
    def getDestinationServerInfo(serverInfoList, i, j):
        return serverInfoList[i].destinationServers[j]
    
    ''' 도착지 서버 위치의 서버 정보를 변경한다. '''
    def setDestinationServerInfo(serverInfoList, i, j, server):
        serverInfoList[i].destinationServers[j] = server