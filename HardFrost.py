# -*- coding: utf-8 -*-
"""
Created on Tue Aug 22 09:30:41 2017

@author: Josh
"""

import datetime as dt
import os, shutil
import traceback, StringIO
import sys,time

def is_schoolyear_over(date):
   if date.month == 8 and date.day <22:
       return True
   if date.month == 7:
       return True
   else:
       return False
   
def clear_dir(path):
    dirs = os.listdir(path)
    print "deleting directory.....\n"
    for fil in dirs:
        file_path = os.path.join(path,fil)
        try:
            if(os.path.isfile(file_path)):
                os.unlink(file_path)
            elif(os.path.isdir(file_path)):
                shutil.rmtree(file_path)
        except Exception as e:
            print "deletion failed\n"
            print e
    print "deletion complete\n"


try:
    
    print is_schoolyear_over(dt.date.today())
    if(is_schoolyear_over(dt.date.today())):
        clear_dir("T:/")
except Exception as e:
    with open("C:/Users/north/Desktop/ErrorLog.txt", "w") as fil:
        fp = StringIO.StringIO()
        traceback.print_ex(file=fp)
        message = fp.getvalue()
        print "Failure!!! The error was: " , repr(message)
        fil.write(repr(message))
        fil.close()
finally:
    print "Exiting"
    time.sleep(2)
    sys.exit(1)
        
        
