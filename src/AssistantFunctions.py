from datetime import datetime

def GetTime():
    return datetime.now().strftime('%H часов %M минут %S секунд')

def GetData():
    return datetime.now().strftime('%d день %m месяц %Y года')