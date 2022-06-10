
####################################################################
def replacing(line,a,b):
    x = line.replace(a,b)
    return x

def search(list, platform):
    for i in range(len(list)):
        if list[i] == platform:
            return True
    return False

def snake_to_camel_case(snake_str):
   components = snake_str.split("_")
   return components[0]+''.join(x.title() for x in components)

def snake_to_kebab_case(kebabStr):
   return kebabStr.replace("_","-")

def kebab_to_snake_case(snakeStr):
   return snakeStr.replace("-","_")

def kebab_to_camel_case(kebab):
    components = kebab.split('-')
    return components[0] + ''.join(x.title() for x in components[1:])

def camel_to_snake_case(str):
    return ''.join(['_'+i.lower() if i.isupper()
                                  else i for i in str]).lstrip('_')

def camel_to_kebab_case(str):
    return ''.join(['-'+i.lower() if i.isupper()
                                  else i for i in str]).lstrip('-')
####################################################################




#!  write the correct file name  !#
openFile = open("hello.txt","r")

arr  = []
look = []
for line in openFile:
    newF = line.split(" ")
    look = list(newF[5])
    snake = "_"
    kebab = "-"
    
    if search(look,snake):
        print("Snake to ...")
        opt = input("Enter your choice (c,k): ")
        print(opt)
        while opt !="c" and opt !="k":
            opt = input("Enter a valid choice (c,k):")
        if opt == "c":
            new = snake_to_camel_case(newF[5])
            replaced = replacing(line,newF[5],new)
        else:
            new = snake_to_kebab_case(newF[5])
            replaced = replacing(line,newF[5],new)
            
    if search(look,kebab):
        print("Kebab to ...")
        opt = input("Enter your choice (s,c): ")
        print(opt)
        while opt !="c" and opt !="s":
            opt = input("Enter a valid choice (s,c):")
        if opt == "c":
            new = kebab_to_camel_case(newF[5])
            replaced = replacing(line,newF[5],new)
        else:
            new = kebab_to_snake_case(newF[5])
            replaced = replacing(line,newF[5],new)
    
    if search(look,kebab) != True and search(look,snake) != True : 
        print("Camel to ...")
        opt = input("Enter your choice (s,k): ")
        print(opt)
        while opt !="k" and opt !="s":
            opt = input("Enter a valid choice (s,k):")
        if opt == "s":
            new = camel_to_kebab_case(newF[5])
            replaced = replacing(line,newF[5],new)
        else:
            new = camel_to_snake_case(newF[5])
            replaced = replacing(line,newF[5],new)
    
    arr.append(line)
    
    
with open("renamedVersion.txt","w") as f:
    for i in arr:
        f.write(i)
        
        
        
    
