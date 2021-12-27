from datetime import datetime
import time
from utils import localtime_support_func

def GetTime():
    localtime = time.asctime( time.localtime(time.time()) )
    correct_time = localtime.split()
    correct_time = correct_time[3].split(':')

    if (int(correct_time[0]) >= 4 and int(correct_time[0]) < 13):

        if (int(correct_time[1]) == 0):
            if(int(correct_time[0]) >= 2 and int(correct_time[0]) <= 4):
                return "Сейчас ровно {} утра.".format(int(correct_time[0]))
            else:
                return "Сейчас ровно {} утра.".format(int(correct_time[0]))

        else:
            return localtime_support_func(correct_time)
    #День

    elif (int(correct_time[0]) >= 13 and int(correct_time[0]) < 17):

        
        correct_time[0] = int(correct_time[0]) - 12
        if (int(correct_time[1]) == 0):
            if (int(correct_time[0]) == 1):
                return "Сейчас ровно час дня."
            elif(int(correct_time[0]) >= 2 and int(correct_time[0]) <= 4):
                return "Сейчас ровно {} часа дня.".format(int(correct_time[0]))
            else:
                return "Сейчас ровно {} часов дня.".format(int(correct_time[0]))

        else: 
            return localtime_support_func(correct_time)

    #Вечер

    elif (int(correct_time[0]) >= 17 and int(correct_time[0]) <= 23):

        correct_time[0] = int(correct_time[0]) - 12

        if (int(correct_time[1]) == 0):
            if(int(correct_time[0]) >= 2 and int(correct_time[0]) <= 4):
                return "Сейчас ровно {} вечера.".format(int(correct_time[0]))
            else:
                return "Сейчас ровно {} вечера.".format(int(correct_time[0]))

        else:
            return localtime_support_func(correct_time)

    #Ночь

    elif (int(correct_time[0]) >= 0 and int(correct_time[0]) < 4):

        if (correct_time[0] == 0):
            correct_time[0] = 12

        if (int(correct_time[1]) == 0):
            if (int(correct_time[0]) == 1):
                return "Сейчас ровно час н+очи."
            elif(int(correct_time[0]) >= 2 and int(correct_time[0]) <= 4):
                return "Сейчас ровно {} часа н+очи.".format(int(correct_time[0]))
            else:
                return "Сейчас ровно {} часов н+очи.".format(int(correct_time[0]))

        else:
            return localtime_support_func(correct_time)

def GetData():
    return datetime.now().strftime('%d день %m месяц %Y года')