import random


def get_days():
    days=["pzt","sali","crs","pers","cm","cmt","pzr"]

    return days


def get_weathers():

    for d in get_days():
        print("{0} günü hava sıcaklığı : {1}".format(d,str(random.randint(0,40))))


get_weathers()

