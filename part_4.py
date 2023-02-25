# I declare that my work contains no examples of misconduct, such as plagiarism, or collusion. 
# Any code taken from other sources is referenced within my code solution. 
# Student ID: UOW:-19129174(W1912917)| IIT:- 20210038
# Date: 13/04/2022


#Part 1
allowedlist = [0,20,40,60,80,100,120] #List of inputs that are allowed
progress = 0  #Progress, initializing the Count
mod_ret = 0 #Module Retriever, initializing the Count
mod_tra = 0 #Module Trailer, initializing the Count
exclude = 0 #Exclude, initializing the Count
result = []
count=0

def Inputs():
    global Pass, Defer, Fail #https://www.w3schools.com/python/python_variables_global.asp
    while True:
        try:
            Pass = int(input('Please enter your credits at pass: '))
        except ValueError:
            print('ERROR!- A Integer should be required!')
            continue
        if Pass not in allowedlist:
            print('Out of range!')
        else:
            break
    while True:
        try:
            Defer = int(input('Please enter your credit at defer:  '))
        except ValueError:
            print('ERROR!- A Integer should be required!')
            continue
        if Defer not in allowedlist:
            print('Out of range!')
        else:
            break
    while True:
        try:
            Fail = int(input('Please enter your credit at fail: '))
        except ValueError:
            print('ERROR!- A Integer should be required!')
            continue
        if Fail not in allowedlist:
            print('Out of range!')
        else:
            break

def Progression():
    global result
    global Pass,Defer,Fail #https://www.w3schools.com/python/python_variables_global.asp
    global progress, mod_ret, mod_tra, exclude       
    Total = Pass + Defer + Fail
    if Total == 120:
        if Pass == 120:
            print('Progress')
            progress += 1
            result.append('Progress')
            result.append(Pass)
            result.append(Defer)
            result.append(Fail)

        elif (Defer + Fail) == 20 and Pass == 100:
            print('Progress (Module Trailer)')
            mod_tra += 1
            result.append('Trailer')
            result.append(Pass)
            result.append(Defer)
            result.append(Fail)

        elif (Fail >= 80) and (Fail > Defer) and (Pass <= 40):
            print('Exclude')
            exclude += 1
            result.append('Exclude')
            result.append(Pass)
            result.append(Defer)
            result.append(Fail)
        
        elif (Pass < 100):
            print('Do not progress (Module Retriever)')
            mod_ret += 1
            result.append('Retriever')
            result.append(Pass)
            result.append(Defer)
            result.append(Fail)
   


        elif (Pass + Defer + Fail) != 120:
            print('Incorrect Total!')

        else:
            print('Out of range!')
    else:
        print('Incorrect Total!')        


def outcome():
    choice = None
    while True:
        choice = input("Would you like to enter another set of data?\nEnter 'y' for yes or 'q' to quit and view results:")
        
        if choice == 'y':
            print('')
            Inputs()
            print('')    
            Progression()
            print('')     
        elif choice == 'q':
            print(70*'-')
            print('')
            print('Horizontal Histogram')
            Horizontal_His(count)
            print('')
            print(70*'-')
            print('Vertical Histogram')
            Vertical_His()
            print(70*'-')
            the_list(result)
            print(70*'-')
            textfile()
            break
        else:
            print('Wrong input!')


def Horizontal_His(count):
    print('Progress',progress,':',progress*'*')
    print('Module Retriever',mod_ret,':',mod_ret*'*')
    print('Module Trailer',mod_tra,':',mod_tra*'*')
    print('Exclude',exclude,':',exclude*'*')
    total = progress + mod_ret + mod_tra + exclude
    print('Outcomes in total. = ',total)

#Part 2
def Vertical_His():
    global progress,mod_ret,mod_tra,exclude #https://www.programiz.com/python-programming/global-keyword / https://stackoverflow.com/questions/53285446/how-do-i-make-print-vertically-on-python-loops
    result_list = [progress, mod_ret, mod_tra, exclude]
    print('Progress',3*'','Retriever',3*'','Trailer',3*'','Exclude',3*'')
    for i in range(max(result_list)): #https://www.w3schools.com/python/ref_func_max.asp
        result_list[0] -= 1
        result_list[1] -= 1
        result_list[2] -= 1
        result_list[3] -= 1
        if result_list[0] >= 0:
            print('*'.center(8), end='') #centering the stars(https://www.w3schools.com/python/ref_string_center.asp)
        else:
            print(' '.center(10), end='')
        if result_list[1] >= 0:
            print('*'.center(10), end='')
        else:
            print(' '.center(10), end='')
        if result_list[2] >= 0:
            print('*'.center(10), end='')
        else:
            print(' '.center(10), end='')
        if result_list[3] >= 0:
            print('*'.center(10))
        else:
            print(' '.center(10))
    total = progress + mod_ret + mod_tra + exclude        
    print('Outcomes in total. = ',total) 

# Part 3 List
def the_list(result):
    for i in range(0,len(result),4):
        print(str(result[i]), str(result[i+1]), str(result[i+2]), str(result[i+3]))
    return
# Part 4 Text File
def textfile(): 
    file = open('Results.txt', 'w+')    
    for f in range(0, len(result), 4):
        file = open('Results.txt', 'a')
        file.write(str(result[f])+' '+' '+str(result[f+1])+' '+' '+str(result[f+2])+' '+' '+str(result[f+3])+'\n' )
        file.close()
    file = open('Results.txt', 'r')  
    print(file.read())
    file.close()
    
option = 0
options = [1, 2] #List for initial menu choices2
while option not in options:
    try:
        print("For students press 1\nFor teachers press 2")
        option = int(input('Please enter the option 1 or 2: '))
        if option == 1:
            print('')
            Inputs()
            print('')
            Progression()
    
        if option == 2:
            print('')
            Inputs()
            print('')
            Progression()
            print('')
            outcome()
    except ValueError:
        print('Invalid Input!')

