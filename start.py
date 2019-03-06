import webBase
import config
import os

server = webBase.webServer('127.0.0.1',1000, debug = True)
config.webConfig['osSep'] = os.sep
server.webConfig = config.webConfig
server.path = str(os.path.dirname(os.path.realpath(__file__))) + str(server.webConfig['webPath'].replace('\\',os.sep).replace('/',os.sep))
server.startServer()