class webServer:
    def __init__(self, address, port, debug):
        self.address = address
        self.port = port
        print('Auther: Setname ©2019\r\nVersion: v0.01')
        self.info = '[{type}][webBase][{time}]:{info}'
        self.debug = debug
    
    #对请求列表进行切分储存
    def unpackHandshake(self,info):
        if self.debug == True: import time
        header = []
        header = info.split('\r\n')[1:]
        content = {}
        content['method'] = info.split('\r\n',1)[0].split(' ')[0]
        content['url'] = info.split('\r\n',1)[0].split(' ')[1]
        content['protocol'] = info.split('\r\n',1)[0].split(' ')[2]
        for i in range(0,len(header)-1):
            try:
                temp = ''
                temp = header[i].split(': ',1)
                content[temp[0]] = temp[1]
            except:
                pass
        if self.debug == True: print(self.info.format(time = time.asctime(time.localtime(time.time())), type = 'Debug', info = str(content)))
        return content

    def startServer(self):
        import socket
        import time
        import threading
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.bind((self.address, self.port))
        sock.listen(64)
        print(self.info.format(time = time.asctime(time.localtime(time.time())), type = 'info', info = 'Server listen on ' + self.address + ':' + str(self.port)))
        connPool = []
        while True:
            conn, addr = sock.accept()
            connPool.append(conn)
            thread = threading.Thread(target=self.messageFunc, args=(conn,connPool,))
            thread.setDaemon(True)
            thread.start()

    def messageFunc(self, conn, connPool):
        request = str(conn.recv(1024),'utf-8')
        import time
        if self.debug == True: print(self.info.format(time = time.asctime(time.localtime(time.time())), type = 'Debug', info = str(request)))
        try:
            handShake = self.unpackHandshake(request)
            message = self.message(handShake)
            content = 'HTTP/1.1 {stateCode} {state}\r\nDate: {date}{others}\r\n\r\n'.format(stateCode = message['stateCode'], state = message['state'], date = message['date'], others = message['others'])
            content = bytes(content, encoding='utf-8')
            content = content + message['bodyMessage']
        except: 
            if self.debug == True: print(self.info.format(time = time.asctime(time.localtime(time.time())), type = 'Debug', info = 'Bad request.'))
            content = b'HTTP/1.1 400 Bad request\r\n\r\n'
                
        conn.sendall(content)
        if self.debug == True: print(self.info.format(time = time.asctime(time.localtime(time.time())), type = 'Debug', info = 'Message sended.'))
        conn.close()
        connPool.remove(conn)
        return

    def message(self, handShake):
        import time
        message = {}
        if handShake['method'].upper() == 'GET':
            url = handShake['url'].split('?', 1)
            filePath = self.path + url[0].replace('\\',self.webConfig['osSep']).replace('/',self.webConfig['osSep'])
            if self.debug == True: print(self.info.format(time = time.asctime(time.localtime(time.time())), type = 'Debug', info = 'Looking for path: ' + filePath))
            if len(url) == 1:
                if filePath[-1] == self.webConfig['osSep']:
                    import imp
                    
                    try:
                        index = imp.load_source('index', filePath + 'index.py')
                    except:
                        if self.debug == True: print(self.info.format(time = time.asctime(time.localtime(time.time())), type = 'Debug', info = 'Can\'t load file.'))
                        message['stateCode'] = '404'
                        message['state'] = 'unExceptPath'
                        import datetime
                        message['date'] = datetime.datetime.utcnow().strftime('%a, %d %b %Y %H:%M:%S GMT')
                        message['bodyMessage'] = b''
                        message['others'] = ''
                        return message
                    return index.__init__(handShake,self.path)
                elif '.' not in filePath:
                    filePath = filePath + self.webConfig['osSep']
                    import imp
                    try:
                        index = imp.load_source('index', filePath + 'index.py')
                    except:
                        if self.debug == True: print(self.info.format(time = time.asctime(time.localtime(time.time())), type = 'Debug', info = 'Can\'t load file.'))
                        message['stateCode'] = '404'
                        message['state'] = 'unExceptPath'
                        import datetime
                        message['date'] = datetime.datetime.utcnow().strftime('%a, %d %b %Y %H:%M:%S GMT')
                        message['bodyMessage'] = b''
                        message['others'] = ''
                        return message
                    return index.__init__(handShake,self.path)
                else:
                    import webBase.loadStasticFile as loadStasticFile
                    if self.debug == True: print(self.info.format(time = time.asctime(time.localtime(time.time())), type = 'Debug', info = 'Try to load stastic file.'))
                    return loadStasticFile.loadFile(path = filePath.replace('root/','root/Stastic/').replace('root\\','root\\Stastic\\'), block = self.webConfig, debug = self.debug).loadFile()

            else:
                if self.debug == True: print(self.info.format(time = time.asctime(time.localtime(time.time())), type = 'Debug', info = 'With value:' + url[1]))
        elif handShake['method'].upper() == 'POST':
            pass
        else:
            pass


    webConfig = {
        'webPath' : '/webBase/root',
        'osSep' : '/',
        'blockTemplateName' : True,
        }
    path = ''
