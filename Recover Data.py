import os,shutil
import datetime as dt
import sys

def get_size(path):

    """
    This function gets the byte size of each user, but does not go into
    subdirectories so it may be incorrect some times
    """

    
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
path =''
paths = []
path_base = "/media/administrator/"
full_path = ""
try:
    paths = os.listdir(path_base)
except Exception as e:
    print("No drive found")
    sys.exit(1)
    
#If the path does not exist, navigate to the Users folder and click Properties
#Copy the path and add it to the paths list below. besure to enclose it in quotes
#paths = ["/media/administrator/Windows/Users","/media/administrator/OS/Users",'/media/administrator/C492BE8992BE800A/Users']

for i in paths:
    #get the main windows directory
    if(i != 'SYSTEM' or i != "Recovery"):
        path = i
path = os.path.join(path_base,path)
full_path = os.path.join(path,"Users/")
print(path)
print(full_path)


                    

#if there is no path exit the program
if path == "":
    print('The path does not exist')
    sys.exit(1)
    
try:
    #list each of the users in the path
    users = os.listdir(full_path)
except NotADirectoryError:
    pass
delUsers = []
main_user = ""
main_user_path = ""
print(users)
clients= {}

for user in users:
    #get the size of each user in the users folder
    file_path = os.path.join(full_path,user)
    byte_size = get_size(file_path)
    clients[user] = byte_size
    
for client in clients:
    #Delete all the default windows users
    #if you want to add a user to the black list
    #type in:       or client == "User"
    #where User is the user you want to add to the black list
    
    if client == "All Users" or "Default" in client or client == "desktop.ini" or client == "Public":
        delUsers.append(client)
    else:
        pass
for user in delUsers:
    #loop through each the users in the black and delete them
    del clients[user]
    users.remove(user)
print(clients)

bool_clients ={}
keys = clients.keys()

if len(clients) == 0:
    #if there are no users exit the program
    print("No data to recover")
    sys.exit(1)

elif len(clients) == 1:
    #if there is one user set it as the main user
    blah =''
    print(str(clients.keys()))
    a = clients.keys()
    for key in a:
        blah = key
    main_user = blah



elif len(clients) > 1:
    #if there is more than one user compare them to one another
    #to see who is the biggest user and set that as the main user
    #basically don't touch this
    mask =''
    array = ['0','b']
    for client in clients:
        bigger_than = ["0","b"]
        for i in range(len(users)):
            try:
                if(clients[client] == clients[users[i]]):
                    pass
                elif(clients[client] > clients[users[i]]):
                    bigger_than.append("1")
                elif(clients[client] < clients[users[i]]):
                    bigger_than.append("0")
            except TypeError:
                pass
            
        bits = "".join(bigger_than)
        bool_clients[client] = bits
       
    
    for i in range(len(clients)-1):
        array.append('1')
    mask = "".join(array)
        
    for client in bool_clients:
        if(int(bool_clients[client],2) & int(mask,2) == int(mask,2)):
            main_user = client
    
else:
    print("Main User not found")
    sys.exit(1)

#check to see if the main user is correct
#otherwise loop through the other users until the
#correct one is found
    
print(main_user)
print("\nIs this the correct user? [Y/n]")
ans = input()
ans = ans.strip()
if(ans.lower() == "n" or ans.lower() == "no"):
    for client in clients:
        if client == main_user:
            pass
        else:
            print("Is " +client+" the correct user? [Y/n] \n")
            a = input()
            a = a.strip()
            if(a.lower() == "y" or a == "yes".lower()):
               main_user = client
               break

    
            
main_path = os.path.join(full_path,main_user)
print(main_path)


#create a file based on the date where all the data is to be stored

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
    #copy all the data in in the following directories
    #add a directory to the whitelist by  typing:
    # ,"Directory"
    # where Directory is the directory you want to add
    
    dirs = ["Documents","Desktop","Pictures"]
    for directory in dirs:
        try:
            shutil.copytree(os.path.join(main_path,directory), os.path.join(tim,directory))
        except Exception as e:
            print(e)
        
    print("data recovery complete")
except Exception as e:
    print("An error was encountered")
    print(e)
    sys.exit(1)

