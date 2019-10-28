name = input(str("Please Enter Your Name: ")) #User input for names

all_initials = [] 
n = int(len(name.split())) #finds the amount of names (first, middle, last) in the user's input and changes it into an integer

for i in range (0,n):   
    all_names = (name.split()[i]) #Chooses the first name in the user's input (then chooses the second name after the loop is finished)
    initials = (all_names[0]) #Takes the first letter of the first name (second name, third name etc.)
    all_initials.append(initials.capitalize()) #Adds the letter into the array 

b = int(len(all_initials)) #finds the amount of initials in the array and capitalizes it

for i in range (0,b):
    print (all_initials[i], end = '') #prints all of the initials in the array


