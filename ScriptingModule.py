import os
import math
import random
import datetime
import json
import subprocess

## Change directory to current directory BrandonDough
'''
os.chdir("/Users/brandondo/BrandonDough")
print(os.getcwd())
'''

## Make folder in brandondo called Edureka
'''
os.mkdir("/Users/brandondo/Edureka")
'''

# Delete directory/folder Edureka
'''
os.rmdir("/Users/brandondo/Edureka")
'''

# remove file example.py
'''
os.remove("/Users/brandondo/Edureka/example.py")
'''

# send example.py to BrandonDough - Needs clarification
'''
print(os.path.join("/Users/brandondo/Edureka","/Users/brandondo/Edureka/example.py"))
'''

# splits path name into directory name and file name without file type
'''
print(os.path.split("/Users/brandondo/Edureka/example"))
'''

# checks if path exists
'''
print(os.path.exists("/Users/brandondo/Edureka/example"))
'''

# subprocess
'''
subprocess.call()
'''

#math modules
'''
print(math.pi)
print(math.e)
print(math.degrees(0.1))
print(math.acos(0.5))
print(math.asin(0.5))
print(math.atan(5))
print(math.cos(3))
print(math.exp(2))
print(math.log(x,base))
print(math.log(10,10))
'''

#print number that will be 49 or less
'''
print(random.randrange(50))
'''

#print number that will be 0 to 49
'''
print(random.randrange(0,50))
'''

#print number that will be 0 to 49 with step sizes 10's
'''
print(random.randrange(0,50,10))
'''

#print integer between 0 and 19
'''
print(random.randint(0,20))
'''

#print date time of current day
'''
print(datetime.date.today())
'''

#prints now date and specific date and displays difference
'''
now = datetime.datetime.today()
other = datetime.datetime(1994,10,10,17,59)
print(now-other)
'''

#prints 1994-10-10 17:59:00
'''
print(datetime.datetime(1994,10,10,17,59))
'''

#Convert json file into dictonary
'''
employee_data = 
'''

'''
{
"people":[
{
"name":"Brandon",
"email":["brandond80@gmail.com","gg@gmail.com"],
"married":false
},
{
"name":"Bob",
"email":["brandondo98@yahoo.com","gg@yahoo.com"],
"married":false
}
]}
'''
'''

print(employee_data)
## string
data = json.loads(employee_data)
## without string
data = json.load(employee_data)

print(data)


## string
data = json.dumps(employee_data)
## without string5
data = json.dump(employee_data)
'''
# GIT Commands
"""
CREATING ADDING:
cd redo 
git init
git pull
git fetch

STATUS CHECK:
git status
git branch
git branch -d (delete)

COMMITTING REPO:
git add --all *
git commit -m "MESSAGE"
git push
git remote add origin https://github.com/YOUR-USERNAME/YOUR-REPOSITORY-NAME.git
git push [variable name] master  

OTHERS:
git clean 
git merge
git merge master
git log
git revert - remove commit
git checkout anotherBranch
git reflog
git revert yellowName - removes commit
git reset --hard (optional)
git rm (delete files)
git show
"""
'''
def count_bits(x):
    num_bits = 0
    while x:
        num_bits += x & 1
        x >>= 1
    return num_bits

a = 110

print(count_bits(a))
'''

#LIST
'''
intList  = [0,1,2,3,4,5]
p/rint('intList: ',intList)
print('intList last thing on list: ',intList[::-1])
print('intList last thing on list: ',intList[-1::])
print('intList last thing on list: ',intList[:-1:])
'''
