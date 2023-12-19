import random

def check_y_n(choice):
    while True:
        if choice == "yes" or choice ==  "y" :
            break
        elif choice =="no" or choice == "n": 
            break
        else:
            print("Please input Yes/No.")
            choice = input().lower().strip()
    return choice

def happy_with_choice(picked):
    print("Are you happy with these choices? (yes or no)")
    happy = input()
    happy = check_y_n(happy)
    while happy == "no" or happy == "No":
        print("Here are some alternative choices we have generated for you:")
        make_choice(picked)
        print("Are you happy with these choices? (yes or no)")
        happy = input()
        happy = check_y_n(happy)


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
    more_options = input().lower().strip()
    more_options = check_y_n(more_options)
    
    while more_options == "yes" or more_options =="Yes":
        print("Please add an option for "+cat_key+":")
        cat_option = input()
        options_list.append(cat_option)
        print("Do you want to add another option for "+cat_key+": (yes or no)")
        more_options = input().lower().strip()
        more_options = check_y_n(more_options)

    my_lists[cat_key] = options_list

def make_choice(all):
    if all == "yes":
        for category, options in my_lists.items():
            choice = random.randint(0,len(options)-1)
            print(category +" : "+options[choice])
    else:
        for i in all:
            for category, options in my_lists.items():
                if category == i:
                    choice = random.randint(0,len(options)-1)
                    print(category +" : "+options[choice])

print("Would you like to generate options for all categories? (yes/no)")
all=input().lower().strip()
all = check_y_n(all)

if all == "no":
    pick_cat = []
    print("Please choose a category from the below to generate a choice: \n" + str(my_lists.keys()))
    #need to validate user input
    picked = input()
    pick_cat.append(picked)

    #ask if they want to pick another category
    print("Do you want to generate options for another category (yes or no)")
    more_options = input().lower().strip()
    more_options = check_y_n(more_options)
    
    while more_options == "yes" or more_options =="Yes":
        print("Please choose a category from the below to generate a choice: \n" + str(my_lists.keys()))
        #need to validate user input
        picked = input()
        pick_cat.append(picked)
        print("Do you want to generate options for another category (yes or no)")
        more_options = input().lower().strip()
        more_options = check_y_n(more_options)


    make_choice(pick_cat)
    happy_with_choice(pick_cat)
    
    
    #check if the length of the picked list is less than or equal to the number of unique keys and stop them if they are saying yes to too many

else:
    print("Here are the choices we have generated for you:")
    make_choice(all)
    happy_with_choice(all)



print("Enjoy!")

#print(my_lists)