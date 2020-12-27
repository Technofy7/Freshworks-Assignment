import threading 
import time

direct={} #'direct' this is directory in which we are storing data



'''Creation Syntax : 

create(key_name, value, time_out_value) 
- Here key_name is string
- time_out_value is optional you can continue by passing two arguments without timeout

'''

def create(key,value,timeout=0):
    if key in direct:
        print("Error:: Key is already Exists") 
    else:
        if(key.isalpha()):
            if len(direct)<(1024*1020*1024) and value<=(16*1024*1024): #Condition to satisfy that file size < 1GB and JSON object < 16kb
                if timeout==0:
                    l=[value,timeout]
                else:
                    l=[value,time.time()+timeout]
                if len(key)<=32: #constraints for input key_name capped at 32chars
                    direct[key]=l
            else:
                print("Error:: Memory Limit Exceeded!!")
        else:
            print("Error:: Invalind key_name!! key_name must contain only alphabets and no special characters or numbers")


'''Creation Syntax : 

read(key_name) 
- Here key_name is string

'''
            
def read(key):
    if key not in direct:
        print("Error:: Given key does not exist in database. Please enter a valid key") 
    else:
        b=direct[key]
        if b[1]!=0:
            if time.time()<b[1]: #comparing the present time with expiry time
                stri=str(key)+":"+str(b[0]) #to return the value in the format of JasonObject i.e.,"key_name:value"
                return stri
            else:
                print("Error:: Time-to-live of",key,"has expired")
        else:
            stri=str(key)+":"+str(b[0])
            return stri

'''Creation Syntax : 

delete(key_name) 
- Here key_name is string

'''

def delete(key):
    if key not in direct:
        print("Error:: Given key does not exist in database. Please enter a valid key") 
    else:
        b=direct[key]
        if b[1]!=0:
            if time.time()<b[1]: #comparing the current time with expiry time
                del direct[key]
                print("key is successfully deleted")
            else:
                print("Error:: time-to-live of",key,"has expired") 
        else:
            del direct[key]
            print("key is successfully deleted")