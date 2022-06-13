
from operator import truediv
import shutil
import os 
import pathlib

#************************************************************************************************
def index_in_list(a_list, index):
    if(index < len(a_list)):
        return True
    return False

def snake_to_camel_case(snake_str):
    components = snake_str.split("_")
    if index_in_list(components,1):
        return components[0]+''.join(x.title() for x in components[1:])
    return components[0]

def snake_to_kebab_case(kebabStr):
   return kebabStr.replace("_","-")

def kebab_to_snake_case(snakeStr):
   return snakeStr.replace("-","_")

def kebab_to_camel_case(kebab):
    components = kebab.split('-')
    if index_in_list(components,1):
        return components[0] + ''.join(x.title() for x in components[1:])
    return components[0]

def camel_to_snake_case(str):
    return ''.join(['_'+i.lower() if i.isupper()
                                  else i for i in str]).lstrip('_')

def camel_to_kebab_case(str):
    return ''.join(['-'+i.lower() if i.isupper()
                                  else i for i in str]).lstrip('-')

def copy(a,b):
    return shutil.copyfile(a,b)


#!Add exception file extensions or files here
def check(a):
    #! add here a specific file
    b = False
    
    exceptionsF = []
    exceptionsF.append(".git")
    exceptionsF.append("README.md")
    exceptionsF.append("convert.py")
    
    #! add here only extensions
    exceptionsE = []
    exceptionsE.append(".git") 
    
    for i in exceptionsF:
        if(i == a):
            b = True
            
    
    for l in exceptionsE:
        if(a.endswith(l)):
            b = True
    
    return b   
#************************************************************************************************



original = pathlib.Path(__file__).parent.absolute()


arr = []
arr = os.listdir(original)

print ("select x to y convert (snake:s,camel:c,kebab:k)\n")
selection = input(" (c s)\n (c k)\n (s k)\n (s c)\n (k c)\n (k s)\n Enter your selection:")

selection = selection.split()




#? validation
while (selection[0] != "s") and (selection[0] != "c") and (selection[0] != "k") or (selection[1] != "c") and (selection[1] != "k") and (selection[1] != "s"):

    print ("Enter a valid selection\n")
    selection = input(" (c s)\n (c k)\n (s k)\n (s c)\n (k c)\n (k s)\nEnter your selection:")
    continue
#? validation end
a = False
new = []
if selection[0] == "s" and selection[1] == "c":
    print("s to c")
    for val in arr:
        valC = check(val)
        if(valC == True):
            continue
        val = val.split(".")
        new = snake_to_camel_case(val[0])+"."+val[1]
        originals = str(original)+"\\"+val[0]+"."+val[1]
        target = str(original)+"\\renamedVersions\\"+new
        copy(originals,target)
        print("Successfull")

if selection[0] == "s" and selection[1] == "k":
    print("s to k")
    for val in arr:
        valC = check(val)
        if(valC == True):
            continue
        val = val.split(".")
        new = snake_to_kebab_case(val[0])+"."+val[1]
        originals = str(original)+"\\"+val[0]+"."+val[1]
        target = str(original)+"\\renamedVersions\\"+new
        copy(originals,target)
        print("Successfull")

if selection[0] == "c" and selection[1] == "s":
    print("c to s")
    for val in arr:
        valC = check(val)
        if(valC == True):
            continue
        val = val.split(".")
        new = camel_to_snake_case(val[0])+"."+val[1]
        originals = str(original)+"\\"+val[0]+"."+val[1]
        target = str(original)+"\\renamedVersions\\"+new
        copy(originals,target)
        print("Successfull")
        
if selection[0] == "c" and selection[1] == "k":
    print("c to s")
    for val in arr:
        valC = check(val)
        if(valC == True):
            continue
        val = val.split(".")
        new = camel_to_kebab_case(val[0])+"."+val[1]
        originals = str(original)+"\\"+val[0]+"."+val[1]
        target = str(original)+"\\renamedVersions\\"+new
        copy(originals,target)
        print("Successfull")
        

if selection[0] == "k" and selection[1] == "s":
    print("k to s")
    for val in arr:
        valC = check(val)
        if(valC == True):
            continue
        val = val.split(".")
        new = kebab_to_snake_case(val[0])+"."+val[1]
        originals = str(original)+"\\"+val[0]+"."+val[1]
        target = str(original)+"\\renamedVersions\\"+new
        copy(originals,target)
        print("Successfull")

if selection[0] == "k" and selection[1] == "c":
    print("k to c")
    for val in arr:
        valC = check(val)
        if(valC == True):
            continue
        val = val.split(".")
        new = kebab_to_camel_case(val[0])+"."+val[1]
        originals = str(original)+"\\"+val[0]+"."+val[1]
        target = str(original)+"\\renamedVersions\\"+new
        copy(originals,target)
        print("Successfull")
