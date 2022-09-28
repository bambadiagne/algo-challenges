def timeConversion(s):
    hours,minutes,seconds=s.split(':')
    if('AM' in seconds):
        if(int(hours)==12):
            hours='00'
        return f'{hours}:{minutes}:{seconds[:2]}'
    if('PM' in seconds): 
        if(int(hours)==12):
            pass
        elif(int(hours) <12):
            hours=(int(hours)+12)%24
            if(hours<10):
                hours='0'+str(hours)
        
        return f'{hours}:{minutes}:{seconds[:2]}'