
def index_in_list(a_list, index):
    if(index < len(a_list)):
        return True
    return False

def spliting(word):
    return [char for char in word]

def search(list, rule):
    for i in list:
        a = spliting(i)
        for one in a:
            if one == rule:
                return True
    return False

def isCamel(list):
    for i in list:
        a = spliting(i)
        for one in a:
            if one.isupper():
                return True
    return False

def snake_to_camel_case(snake_str):
    components = snake_str.split("_")
    if index_in_list(components,1):
        return components[0]+''.join(x.title() for x in components)
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
    
def convert(currentType,newType,array):
    newArray = []
    if currentType == underScore:
        if newType == "c":
            for r in array:
                a = snake_to_camel_case(r)
                newArray.append(a)
        if newType == "k":
            for r in array:
                a = snake_to_kebab_case(r)
                newArray.append(a)
    if currentType == dash:
        if newType == "c":
            for r in array:
                a = kebab_to_camel_case(r)
                newArray.append(a)
        if newType == "s":
            for r in array:
                a = kebab_to_snake_case(r)
                newArray.append(a)
    if currentType == "camel":
        if newType == "s":
            for r in array:
                a = camel_to_snake_case(r)
                newArray.append(a)
        if newType == "k":
            for r in array:
                a = camel_to_kebab_case(r)
                newArray.append(a)
    return newArray
            
            
#!  write the correct file name  !#
openFile = open("hello.txt","r")
#!  write the correct file name  !#


print("\nWelcome...\n")

allArr = []
allNewArr = []
variableNames = []
newVariableNames = []

for line in openFile:
    
    allArr.append(line)
    newF = line.split(" ")
    variableNames.append(newF[5])
    underScore = "_"
    dash = "-"
    varSize = len(variableNames)

    if search(variableNames,underScore):
        typeCurrent = underScore
    if search(variableNames,dash):
        typeCurrent = dash
    if isCamel(variableNames):
        typeCurrent = "camel"
        
if(isCamel(variableNames) == True and search(variableNames, underScore) or isCamel(variableNames) == True and search(variableNames,underScore)):
    print("Could not understand the type please enter type!")
    inputT = input("Type is (camel:c,snake:s,kebab:k) :")
    while inputT != "c" and inputT != "s" and inputT != "k":
        inputT = input("Please enter a valid type:")
    if(inputT == "c"):
        typeCurrent = "camel"
    if(inputT == "s"):
        typeCurrent = underScore
    if(inputT == "k"):
        typeCurrent = dash

if typeCurrent == underScore:
    typeNew = input("Current type is snake, please enter new type:")
    while typeNew != "c" and typeNew != "k":
        typeNew = input("Please enter a valid type(Only 'c' or 'k'):")
    newVariableNames = convert(typeCurrent, typeNew, variableNames)
    
if typeCurrent == dash:
    typeNew = input("Current type is kebab, please enter new type:")
    while typeNew != "c" and typeNew != "s":
        typeNew = input("Please enter a valid type(Only 'c' or 's'):")
    newVariableNames = convert(typeCurrent, typeNew, variableNames)
        
if typeCurrent == "camel":
    typeNew = input("Current type is camel, please enter a new type:")
    while typeNew != "k" and typeNew != "s":
        typeNew = input("Please enter a valid type(Only 'k' or 's'):")
    newVariableNames = convert(typeCurrent, typeNew, variableNames)
    

size = len(allArr)
i=0

for all in allArr:
    
    replaced = all.replace(variableNames[i],newVariableNames[i])
    allNewArr.append(replaced)
    if(i!=size):
        i+=1
    
with open("newVersion","w") as f:
    for abc in allNewArr:
        f.write(abc)