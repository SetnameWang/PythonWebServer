class loadFile:
    def __init__(self, path, block, debug, config, handShake):
        self.path = path
        self.block = block
        self.config = config
        self.handShake = handShake
        self.info = '[{type}][webBase][{time}]:{info}'
        self.debug = debug

    def loadFile(self):
        if self.block == True:
            if '/template' in self.path: return self.err404()
        message = {}
        import time
        if self.debug == True: print(self.info.format(time = time.asctime(time.localtime(time.time())), type = 'Debug', info = 'Try to open file ' + self.path))
        try:
            file = open(self.path, mode='rb').read()
        except:
            if self.debug == True: print(self.info.format(time = time.asctime(time.localtime(time.time())), type = 'Debug', info = 'Can\'t found file.'))
            return self.err404()
        
        if self.config['fileAllow'] == 'all':
            if self.debug == True: print(self.info.format(time = time.asctime(time.localtime(time.time())), type = 'Debug', info = 'Loading file allow list.'))
            import json
            fileList = open(self.path.split(self.config['webPath'])[0] + self.config['webPath'] + self.config['osSep'] + 'fileList.json', 'r',encoding='utf-8')
            list = fileList.read()
            fileList.close()
            list = json.loads(list)
            message = {}
            try:
                suffPath = self.path.split('.')[-1]
                patched = False
                suffix = ''
                for i in list['list']:
                    if i in self.path:
                        patched = True
                        suffix = list['reflection'][i]
                        break
            except:
                if self.debug == True: print(self.info.format(time = time.asctime(time.localtime(time.time())), type = 'Debug', info = 'Can\'t patch suffix.'))
                if self.config['allowUnknowFile'] == False: return self.err404()
                suffix = 'application/octet-stream'
                
            message['stateCode'] = '200'
            message['state'] = 'OK'
            import datetime
            message['date'] = datetime.datetime.utcnow().strftime('%a, %d %b %Y %H:%M:%S GMT')
            message['bodyMessage'] = file
            message['others'] = '\r\ncontent-type: {type}\r\naccept-ranges: bytes'.format(type = suffix)
            return message

        else:
            return self.err404()


    def err404(self):
        message = {}
        message['stateCode'] = '404'
        message['state'] = 'unExceptPath'
        import datetime
        message['date'] = datetime.datetime.utcnow().strftime('%a, %d %b %Y %H:%M:%S GMT')
        message['bodyMessage'] = b''
        message['others'] = ''
        return message