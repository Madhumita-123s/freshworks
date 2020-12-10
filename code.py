import threading 
from threading import*
import time

dic={} 


def create(key,value,timeout=0):
    if key in dic:
        print("key exists") 
    else:
        if(key.isalpha()):
            if len(d)<(1024*1020*1024) and value<=(16*1024*1024):  
                if timeout==0:{
                    
                    l=[value,timeout]
                    }
                else:
                    {
                    l=[value,time.time()+timeout]
                    }
                if len(key)<=32: 
                    dic[key]=l
            else:
                print("error: Memory limit exceeded!! ")
      
            
def read(key):
    if key not in dic:
        print("error: given key does not exist in database. Please enter a valid key") 
    else:
        b=d[key]
        if b[1]!=0:
            if time.time()<b[1]: 
                stri=str(key)+":"+str(b[0]) 
                return stri
            else:
                print("error: time-to-live of",key,"has expired") 
        else:
            stri=str(key)+":"+str(b[0])
            return stri
def delete(key):
    if key not in dic:
        print("key does not exist in database. Please enter a valid key") 
    else:
        b=d[key]
        if b[1]!=0:
            if time.time()<b[1]: 
                del d[key]
                print("key deleted")
            else:
                print("error: time-to-live of",key,"has expired") 
        else:
            del dic[key]
            print("key is successfully deleted")
