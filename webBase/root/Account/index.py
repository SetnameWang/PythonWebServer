def __init__(handShake):
    cookie = []
    try:
        cookie = handShake['Cookie'].split('; ')
    except:
        pass



    import datetime
    message = {}
    message['stateCode'] = '200'
    message['state'] = 'OK'
    message['date'] = datetime.datetime.utcnow().strftime('%a, %d %b %Y %H:%M:%S GMT')
    message['bodyMessage'] = b'Account mode is good'
    message['others'] = ''
    return message