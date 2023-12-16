import random

print("How many decisions do you need to make?")
num_lists = input()
my_lists = {}

for i in range(int(num_lists)):
    print("Please name the decision category "+str(i+1)+":")
    cat_key = input()
    
    print("Please add an option for "+cat_key+":")
    cat_option = input()
    
    options_list = []
    options_list.append(cat_option)
   
    print("Do you want to add another option for "+cat_key+": (yes or no)")
    more_options = input()
    
    while more_options == "yes" or more_options =="Yes":
        print("Please add an option for "+cat_key+":")
        cat_option = input()
        options_list.append(cat_option)
        print("Do you want to add another option for "+cat_key+": (yes or no)")
        more_options = input()

    my_lists[cat_key] = options_list

def make_choice():
    for category, options in my_lists.items():
        choice = random.randint(0,len(options)-1)
        print(category +":"+options[choice])

print("Here are the choices we have generated for you:")
make_choice()

print("Are you happy with these choices? (yes or no)")
happy = input()
while happy == "no" or happy == "No":
    print("Here are some alternative choices we have generated for you:")
    make_choice()
    print("Are you happy with these choices? (yes or no)")
    happy = input()
    print("Enjoy3!")

#print(my_lists)