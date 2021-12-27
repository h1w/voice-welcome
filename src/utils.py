import wave

def ConvertPcmToWav(name, output_name):
    with open(name, 'rb') as pcmfile:
        pcmdata = pcmfile.read()
    
    with wave.open(output_name, 'wb') as wavfile:
        wavfile.setparams((1, 2, 44100, 1, 'NONE', 'NONE'))
        wavfile.writeframes(pcmdata)

def localtime_support_func(correct_time):
    if (int(correct_time[0]) >= 5 and int(correct_time[0]) <= 20):
        if (int(correct_time[2]) == 0):
            if (int(correct_time[1])%10 == 1 and (int(correct_time[1]) >= 20 or int(correct_time[1]) <= 10)):
                return "Местное время сейчас ровно {} часов и {} минута".format(int(correct_time[0]),int(correct_time[1]),int(correct_time[2]))
            elif(int(correct_time[1])%10 >= 2 and int(correct_time[1])%10 <= 4 and (int(correct_time[1]) >= 20 or int(correct_time[1]) <= 10)):
                return "Местное время сейчас ровно {} часов и {} минуты".format(int(correct_time[0]),int(correct_time[1]),int(correct_time[2]))
            else:
                return "Местное время сейчас ровно {} часов и {} минут".format(int(correct_time[0]),int(correct_time[1]),int(correct_time[2]))

        elif ((int(correct_time[2])%10 == 1  or int(correct_time[2])%10 == 0) or (int(correct_time[2]) >= 10 and int(correct_time[2]) < 20) or (int(correct_time[2])%10 >= 5 and int(correct_time[2])%10 <= 9)):
            if (int(correct_time[1])%10 == 1 and (int(correct_time[1]) >= 20 or int(correct_time[1]) <= 10)):
                return "Местное время сейчас {} часов, {} минута и {} секунд".format(int(correct_time[0]),int(correct_time[1]),int(correct_time[2]))
            elif(int(correct_time[1])%10 >= 2 and int(correct_time[1])%10 <= 4 and (int(correct_time[1]) >= 20 or int(correct_time[1]) <= 10)):
                return "Местное время сейчас {} часов, {} минуты и {} секунд".format(int(correct_time[0]),int(correct_time[1]),int(correct_time[2]))
            else:
                return "Местное время сейчас {} часов, {} минут и {} секунд".format(int(correct_time[0]),int(correct_time[1]),int(correct_time[2]))

        elif (int(correct_time[2])%10 == 1):
            if (int(correct_time[1])%10 == 1 and (int(correct_time[1]) >= 20 or int(correct_time[1]) <= 10)):
                return "Местное время сейчас {} часов, {} минута и {} секунда".format(int(correct_time[0]),int(correct_time[1]),int(correct_time[2]))
            elif (int(correct_time[1])%10 >= 2 and int(correct_time[1])%10 <= 4 and (int(correct_time[1]) >= 20 or int(correct_time[1]) <= 10)):
                return "Местное время сейчас {} часов, {} минуты и {} секунда".format(int(correct_time[0]),int(correct_time[1]),int(correct_time[2]))
            else:
                return "Местное время сейчас {} часов, {} минут и {} секунда".format(int(correct_time[0]),int(correct_time[1]),int(correct_time[2]))

        elif (int(correct_time[2])%10 <= 4):
            if (int(correct_time[1])%10 == 1 and (int(correct_time[1]) >= 20 or int(correct_time[1]) <= 10)):
                return "Местное время сейчас {} часов, {} минута и {} секунды".format(int(correct_time[0]),int(correct_time[1]),int(correct_time[2]))
            elif (int(correct_time[1])%10 >= 2 and int(correct_time[1])%10 <= 4 and (int(correct_time[1]) >= 20 or int(correct_time[1]) <= 10)):
                return "Местное время сейчас {} часов, {} минуты и {} секунды".format(int(correct_time[0]),int(correct_time[1]),int(correct_time[2]))
            else:
                return "Местное время сейчас {} часов, {} минут и {} секунды".format(int(correct_time[0]),int(correct_time[1]),int(correct_time[2]))

    if (int(correct_time[0]) == 1 or int(correct_time[0]) == 21):
        if (int(correct_time[2]) == 0):
            if (int(correct_time[1])%10 == 1 and (int(correct_time[1]) >= 20 or int(correct_time[1]) <= 10)):
                return "Местное время сейчас ровно {} час и {} минута".format(int(correct_time[0]),int(correct_time[1]),int(correct_time[2]))
            elif(int(correct_time[1])%10 >= 2 and int(correct_time[1])%10 <= 4 and (int(correct_time[1]) >= 20 or int(correct_time[1]) <= 10)):
                return "Местное время сейчас ровно {} час и {} минуты".format(int(correct_time[0]),int(correct_time[1]),int(correct_time[2]))
            else:
                return "Местное время сейчас ровно {} час и {} минут".format(int(correct_time[0]),int(correct_time[1]),int(correct_time[2]))

        elif ((int(correct_time[2])%10 == 1  or int(correct_time[2])%10 == 0) or (int(correct_time[2]) >= 10 and int(correct_time[2]) < 20) or (int(correct_time[2])%10 >= 5 and int(correct_time[2])%10 <= 9)):
            if (int(correct_time[1])%10 == 1 and (int(correct_time[1]) >= 20 or int(correct_time[1]) <= 10)):
                return "Местное время сейчас {} час, {} минута и {} секунд".format(int(correct_time[0]),int(correct_time[1]),int(correct_time[2]))
            elif(int(correct_time[1])%10 >= 2 and int(correct_time[1])%10 <= 4 and (int(correct_time[1]) >= 20 or int(correct_time[1]) <= 10)):
                return "Местное время сейчас {} час, {} минуты и {} секунд".format(int(correct_time[0]),int(correct_time[1]),int(correct_time[2]))
            else:
                return "Местное время сейчас {} час, {} минут и {} секунд".format(int(correct_time[0]),int(correct_time[1]),int(correct_time[2]))

        elif (int(correct_time[2])%10 == 1):
            if (int(correct_time[1])%10 == 1 and (int(correct_time[1]) >= 20 or int(correct_time[1]) <= 10)):
                return "Местное время сейчас {} час, {} минута и {} секунда".format(int(correct_time[0]),int(correct_time[1]),int(correct_time[2]))
            elif (int(correct_time[1])%10 >= 2 and int(correct_time[1])%10 <= 4 and (int(correct_time[1]) >= 20 or int(correct_time[1]) <= 10)):
                return "Местное время сейчас {} час, {} минуты и {} секунда".format(int(correct_time[0]),int(correct_time[1]),int(correct_time[2]))
            else:
                return "Местное время сейчас {} час, {} минут и {} секунда".format(int(correct_time[0]),int(correct_time[1]),int(correct_time[2]))

        elif (int(correct_time[2])%10 <= 4):
            if (int(correct_time[1])%10 == 1 and (int(correct_time[1]) >= 20 or int(correct_time[1]) <= 10)):
                return "Местное время сейчас {} час, {} минута и {} секунды".format(int(correct_time[0]),int(correct_time[1]),int(correct_time[2]))
            elif (int(correct_time[1])%10 >= 2 and int(correct_time[1])%10 <= 4 and (int(correct_time[1]) >= 20 or int(correct_time[1]) <= 10)):
                return "Местное время сейчас {} час, {} минуты и {} секунды".format(int(correct_time[0]),int(correct_time[1]),int(correct_time[2]))
            else:
                return "Местное время сейчас {} час, {} минут и {} секунды".format(int(correct_time[0]),int(correct_time[1]),int(correct_time[2]))

    if ((int(correct_time[0])%10 >= 2 and int(correct_time[0]) <= 4) and (int(correct_time[0]) < 10 or int(correct_time[0]) > 20)):
        if (int(correct_time[2]) == 0):
            if (int(correct_time[1])%10 == 1 and (int(correct_time[1]) >= 20 or int(correct_time[1]) <= 10)):
                return "Местное время сейчас ровно {} часа и {} минута".format(int(correct_time[0]),int(correct_time[1]),int(correct_time[2]))
            elif(int(correct_time[1])%10 >= 2 and int(correct_time[1])%10 <= 4 and (int(correct_time[1]) >= 20 or int(correct_time[1]) <= 10)):
                return "Местное время сейчас ровно {} часа и {} минуты".format(int(correct_time[0]),int(correct_time[1]),int(correct_time[2]))
            else:
                return "Местное время сейчас ровно {} часа и {} минут".format(int(correct_time[0]),int(correct_time[1]),int(correct_time[2]))

        elif ((int(correct_time[2])%10 == 1  or int(correct_time[2])%10 == 0) or (int(correct_time[2]) >= 10 and int(correct_time[2]) < 20) or (int(correct_time[2])%10 >= 5 and int(correct_time[2])%10 <= 9)):
            if (int(correct_time[1])%10 == 1 and (int(correct_time[1]) >= 20 or int(correct_time[1]) <= 10)):
                return "Местное время сейчас {} часа, {} минута и {} секунд".format(int(correct_time[0]),int(correct_time[1]),int(correct_time[2]))
            elif(int(correct_time[1])%10 >= 2 and int(correct_time[1])%10 <= 4 and (int(correct_time[1]) >= 20 or int(correct_time[1]) <= 10)):
                return "Местное время сейчас {} часа, {} минуты и {} секунд".format(int(correct_time[0]),int(correct_time[1]),int(correct_time[2]))
            else:
                return "Местное время сейчас {} часа, {} минут и {} секунд".format(int(correct_time[0]),int(correct_time[1]),int(correct_time[2]))

        elif (int(correct_time[2])%10 == 1):
            if (int(correct_time[1])%10 == 1 and (int(correct_time[1]) >= 20 or int(correct_time[1]) <= 10)):
                return "Местное время сейчас {} часа, {} минута и {} секунда".format(int(correct_time[0]),int(correct_time[1]),int(correct_time[2]))
            elif (int(correct_time[1])%10 >= 2 and int(correct_time[1])%10 <= 4 and (int(correct_time[1]) >= 20 or int(correct_time[1]) <= 10)):
                return "Местное время сейчас {} часа, {} минуты и {} секунда".format(int(correct_time[0]),int(correct_time[1]),int(correct_time[2]))
            else:
                return "Местное время сейчас {} часа, {} минут и {} секунда".format(int(correct_time[0]),int(correct_time[1]),int(correct_time[2]))

        elif (int(correct_time[2])%10 <= 4):
            if (int(correct_time[1])%10 == 1 and (int(correct_time[1]) >= 20 or int(correct_time[1]) <= 10)):
                return "Местное время сейчас {} часа, {} минута и {} секунды".format(int(correct_time[0]),int(correct_time[1]),int(correct_time[2]))
            elif (int(correct_time[1])%10 >= 2 and int(correct_time[1])%10 <= 4 and (int(correct_time[1]) >= 20 or int(correct_time[1]) <= 10)):
                return "Местное время сейчас {} часа, {} минуты и {} секунды".format(int(correct_time[0]),int(correct_time[1]),int(correct_time[2]))
            else:
                return "Местное время сейчас {} часа, {} минут и {} секунды".format(int(correct_time[0]),int(correct_time[1]),int(correct_time[2]))