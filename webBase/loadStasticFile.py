class loadFile:
    def __init__(self, path, block, debug):
        self.path = path
        self.block = block
        self.info = '[{type}][webBase][{time}]:{info}'
        self.debug = debug

    def loadFile(self):
        if self.block == True:
            if '/template' in self.path: return self.err404()
        message = {}
        import time
        if self.debug == True: print(self.info.format(time = time.asctime(time.localtime(time.time())), type = 'Debug', info = 'Try to open file ' + self.path))
        if '.jpg' in self.path:
            try:
                file = open(self.path, mode='rb').read()
            except:
                if self.debug == True: print(self.info.format(time = time.asctime(time.localtime(time.time())), type = 'Debug', info = 'Can\'t uncode jpg file.'))
                return self.err404()
            if self.debug == True: print(self.info.format(time = time.asctime(time.localtime(time.time())), type = 'Debug', info = 'Success uncode jpg file.'))
            message['stateCode'] = '200'
            message['state'] = 'OK'
            import datetime
            message['date'] = datetime.datetime.utcnow().strftime('%a, %d %b %Y %H:%M:%S GMT')
            message['bodyMessage'] = file
            message['others'] = '\r\ncontent-type: image/jpg\r\naccept-ranges: bytes'
            return message
        elif '.png' in self.path:
            try:
                file = open(self.path, mode='rb').read()
            except:
                if self.debug == True: print(self.info.format(time = time.asctime(time.localtime(time.time())), type = 'Debug', info = 'Can\'t uncode png file.'))
                return self.err404()
            if self.debug == True: print(self.info.format(time = time.asctime(time.localtime(time.time())), type = 'Debug', info = 'Success uncode png file.'))
            message['stateCode'] = '200'
            message['state'] = 'OK'
            import datetime
            message['date'] = datetime.datetime.utcnow().strftime('%a, %d %b %Y %H:%M:%S GMT')
            message['bodyMessage'] = file
            message['others'] = '\r\ncontent-type: image/png\r\naccept-ranges: bytes'
            return message
        elif '.gif' in self.path:
            try:
                file = open(self.path, mode='rb').read()
            except:
                if self.debug == True: print(self.info.format(time = time.asctime(time.localtime(time.time())), type = 'Debug', info = 'Can\'t uncode gif file.'))
                return self.err404()
            if self.debug == True: print(self.info.format(time = time.asctime(time.localtime(time.time())), type = 'Debug', info = 'Success uncode gif file.'))
            message['stateCode'] = '200'
            message['state'] = 'OK'
            import datetime
            message['date'] = datetime.datetime.utcnow().strftime('%a, %d %b %Y %H:%M:%S GMT')
            message['bodyMessage'] = file
            message['others'] = '\r\ncontent-type: image/gif\r\naccept-ranges: bytes'
            return message
        elif '.ico' in self.path:
            try:
                file = open(self.path, mode='rb').read()
            except:
                print(self.path)
                if self.debug == True: print(self.info.format(time = time.asctime(time.localtime(time.time())), type = 'Debug', info = 'Can\'t uncode ICO file.'))
                return self.err404()
            if self.debug == True: print(self.info.format(time = time.asctime(time.localtime(time.time())), type = 'Debug', info = 'Success uncode ICO file.'))
            message['stateCode'] = '200'
            message['state'] = 'OK'
            import datetime
            message['date'] = datetime.datetime.utcnow().strftime('%a, %d %b %Y %H:%M:%S GMT')
            message['bodyMessage'] = file
            message['others'] = '\r\ncontent-type: image/x-icon\r\naccept-ranges: bytes'
            return message

        elif '.js' in self.path:
            try:
                file = open(self.path, mode='r',encoding='utf-8').read()
            except:
                if self.debug == True: print(self.info.format(time = time.asctime(time.localtime(time.time())), type = 'Debug', info = 'Can\'t uncode js file.'))
                return self.err404()
            if self.debug == True: print(self.info.format(time = time.asctime(time.localtime(time.time())), type = 'Debug', info = 'Success uncode js file.'))
            message['stateCode'] = '200'
            message['state'] = 'OK'
            import datetime
            message['date'] = datetime.datetime.utcnow().strftime('%a, %d %b %Y %H:%M:%S GMT')
            message['bodyMessage'] = bytes(file,encoding='utf-8')
            message['others'] = '\r\ncontent-type: text/javascript'
            return message
        elif '.css' in self.path:
            try:
                file = open(self.path, mode='r',encoding='utf-8').read()
            except:
                if self.debug == True: print(self.info.format(time = time.asctime(time.localtime(time.time())), type = 'Debug', info = 'Can\'t uncode css file.'))
                return self.err404()
            if self.debug == True: print(self.info.format(time = time.asctime(time.localtime(time.time())), type = 'Debug', info = 'Success uncode css file.'))
            message['stateCode'] = '200'
            message['state'] = 'OK'
            import datetime
            message['date'] = datetime.datetime.utcnow().strftime('%a, %d %b %Y %H:%M:%S GMT')
            message['bodyMessage'] = bytes(file,encoding='utf-8')
            message['others'] = '\r\ncontent-type: text/css'
            return message
        elif '.html' in self.path:
            try:
                file = open(self.path, mode='r',encoding='utf-8').read()
            except:
                if self.debug == True: print(self.info.format(time = time.asctime(time.localtime(time.time())), type = 'Debug', info = 'Can\'t uncode html file.'))
                return self.err404()
            if self.debug == True: print(self.info.format(time = time.asctime(time.localtime(time.time())), type = 'Debug', info = 'Success uncode html file.'))
            message['stateCode'] = '200'
            message['state'] = 'OK'
            import datetime
            message['date'] = datetime.datetime.utcnow().strftime('%a, %d %b %Y %H:%M:%S GMT')
            message['bodyMessage'] = bytes(file,encoding='utf-8')
            message['others'] = '\r\ncontent-type: text/html'
            return message
        else:
            if self.debug == True: print(self.info.format(time = time.asctime(time.localtime(time.time())), type = 'Debug', info = 'Can\'t unexcept path.'))
            message['stateCode'] = '400'
            message['state'] = 'unExceptPath'
            import datetime
            message['date'] = datetime.datetime.utcnow().strftime('%a, %d %b %Y %H:%M:%S GMT')
            message['bodyMessage'] = b''
            message['others'] = ''
            return message

    def err404(self):
        message = {}
        message['stateCode'] = '404'
        message['state'] = 'unExceptPath'
        import datetime
        message['date'] = datetime.datetime.utcnow().strftime('%a, %d %b %Y %H:%M:%S GMT')
        message['bodyMessage'] = b''
        message['others'] = ''
        return message