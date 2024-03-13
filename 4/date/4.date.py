from datetime import datetime as d

def Dif_Time(dt2,dt1):

    delta_time = dt2 - dt1

    return delta_time.days * 24 * 3600 + delta_time.seconds


data1 = d.strptime('2022-11-15 14:32:30','%Y-%m-%d %H:%M:%S')

data2 = d.now()

print(Dif_Time(data2,data1))