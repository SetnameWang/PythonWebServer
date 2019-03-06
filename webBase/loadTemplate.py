class loadTemp:
    def __init__(self, tempPath):
        self.tempPath = tempPath

    def loadedTemp(self):
        import os
        return open(self.tempPath.replace('/',os.sep).replace('\\',os.sep), encoding='utf-8').read()