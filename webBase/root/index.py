def __init__(handShake, path):
    cookie = []
    try:
        cookie = handShake['Cookie'].split('; ')
    except:
        pass
    if cookie == []:
        return unloged(path)
    else:
        return unloged(path)

def unloged(path):
    import webBase.loadTemplate as loadTemplate
    template = loadTemplate.loadTemp(path + '/template/index.html').loadedTemp()
    import datetime
    message = {}
    message['stateCode'] = '200'
    message['state'] = 'OK'
    message['date'] = datetime.datetime.utcnow().strftime('%a, %d %b %Y %H:%M:%S GMT')
    message['bodyMessage'] = bytes(template, encoding='utf-8')
    message['others'] = ''
    return message