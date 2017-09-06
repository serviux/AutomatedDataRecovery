import os,shutil
import datetime as dt
import sys
def get_size(path):
    size = 0
    try:
        it = os.listdir(path)
        for entry in it:
      
            file_path = os.path.join(path,entry)
            if entry[0] == ".":
                pass
            elif os.path.isfile(file_path) or os.path.isdir(file_path):
                stats = os.stat(file_path)
                size += stats.st_size
        return size
    except Exception:
            pass
    
path = "/media/administrator/Windows/Users"
try:
    users = os.listdir(path)
except NotADirectoryError:
    pass
delUsers = []
main_user = ""
main_user_path = ""
print(users)
clients= {}
for user in users:
    file_path = os.path.join(path,user)
    byte_size = get_size(file_path)
    clients[user] = byte_size
for client in clients:
    if client == "All Users" or "Default" in client or client == "desktop.ini" or client == "Public":
        delUsers.append(client)
    else:
        pass
for user in delUsers:
    del clients[user]
print(clients)

bool_clients ={}
keys = clients.keys()

if len(clients) == 0:
    print("No data to recover")
    sys.exit(1)

elif len(clients) == 1:
    blah =''
    print(str(clients.keys()))
    a = clients.keys()
    for key in a:
        blah = key
    main_user = blah
    
elif len(clients) > 1:
    mask =''
    array = ['0','b']
    for client in clients:
        bigger_than["0","b"]
        for i in range(len(keys)):
            if(client == keys[i]):
                pass
            elif(clients[client] > clients[keys[i]]):
                bigger_than.append("1")
            elif(clients[client] < clients[keys[i]]):
                bigger_than.append("0")
            
        bits = "".join(bigger_than)
        bool_clients[client] = bits
       
    
    for i in range(len(cleints)-1):
        array.append('1')
    mask = "".join(array)
        
    for client in bool_clients:
        if(bool_client[client] & mask == 15):
            main_user = client
else:
    print("Main User not found")
    sys.exit(1)

print(main_user)
main_path = os.path.join(path,main_user)
print(main_path)

date = dt.date.today()
dDate = {"Day": str(date.day), "Month": str(date.month), "Year": str(date.year)}
file_storage = main_user + " " + dDate["Month"] + "-" + dDate["Day"] + "-" + dDate["Year"] 
try:
    tim = os.path.join('/home/administrator/Desktop/Teacher Data', file_storage)
    os.mkdir(tim)
except FileExistsError:
    print("That data has already been recovered")
    sys.exit(1)

print("Beginning data recovery....")

try:
    dirs = ["Documents","Desktop","Pictures"]
    for directory in dirs:
        shutil.copytree(os.path.join(main_path,directory), os.path.join(tim,directory))
    print("data recovery complete")
except Exception as e:
    print("An error was encountered")
    print(e)
    sys.exit(1)

