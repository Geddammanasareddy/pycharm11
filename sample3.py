from sample1 import *
from sample2 import div
while(True):
    try:
        a=int(input("enter the number:"))
        b=int(input("enter the number"))
        res=div(a,b)
    except ValueError:
        print("it is value a error")
    except kvrdivisionError:
        print("it dont take the isalpha,str,space")
    else:
        print("div({},{})={}".format(a,b,res))