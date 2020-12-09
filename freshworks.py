import time
dict={}
// create operation
def create(key,value,timeout=0):
    if key in dict:
        print("ERROR: Key already exist")
    else:
        if key.isalpha():
            if len(dict)<(1024*1024*1024) and value<(16*1024*1024):
                if timeout==0:
                    l=[value,timeout]
                else:
                    l=[value,time.time()+timeout]
                if(len(key)<=32):
                    dict[key]=l 
                    print(key,":","File created")
            else:
                print("ERROR: Memory limit exceeded")
        else:
            print("ERROR: Invalid key name")
// read operation
def read(key):
    if key not in dict:
        print("ERROR: Key does not exist")
    else:
        b=dict[key]
        if b[1]==0:
            print(str(key)+":"+str(b[0]))
        else:
            if time.time()<b[1]:
                print(str(key)+":"+str(b[0]))
            else:
                print("ERROR: Time to live exceeded")
// delete operation
def delete(key):
    if key not in dict:
        print("error: given key does not exist in database. Please enter a valid key") 
    else:
        b=dict[key]
        if b[1]!=0:
            if time.time()<b[1]:
                del dict[key]
                print("key is successfully deleted")
            else:
                print("error: time-to-live of",key,"has expired")
        else:
            del dict[key]
            print("key is successfully deleted")
def display(): 
    print(dict)
            
create("subha",20)
create("abi",16)
read("subha")
read("abi")
delete("subha")
read("abi")
display()
