import random
import json

#DEFINE FUNCTIONS/METHODS - could split these out into seperate file

#function to validate users yes/no choices
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

#function to check if user is happy with output or whether to regenerate options
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

#create function / method to randomly select a value for each key from the dictionary for chosen categories
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

def write_dic(dic):
    json = json.dumps(dic)
    f = open("categories.json","w")
    f.write(json)
    f.close()

def load_dic():
    f = open("categories.json","r")
    dic = json.load(f)
    return dic



def new_cats():
    # give user facility to input how many decisions they want help with and save as integer
    print("How many decisions do you need to make?")
    num_lists = input()
    my_lists = {}

    #give user a way to input names of categories for the number of decisions they want help with
    #add categories to my_lists
    for i in range(int(num_lists)):
        print("Please name the decision category "+str(i+1)+":")
        cat_key = input()
        
        print("Please add an option for "+cat_key+":")
        cat_option = input()
        
        #create list and add cat_option to the list
        options_list = []
        options_list.append(cat_option)
    
        print("Do you want to add another option for "+cat_key+": (yes or no)")
        more_options = input().lower().strip()
        more_options = check_y_n(more_options)
        
        #check if user wants to add any more options and allow input if true
        while more_options == "yes" or more_options =="Yes":
            print("Please add an option for "+cat_key+":")
            cat_option = input()
            options_list.append(cat_option)
            print("Do you want to add another option for "+cat_key+": (yes or no)")
            more_options = input().lower().strip()
            more_options = check_y_n(more_options)

        #write key:value pairs into the my_lists dictionary
        my_lists[cat_key] = options_list
        write_dic(my_lists)
        return my_lists
    
#MAIN BODY OF CODE
print("Would you like to load previously defined categories? (yes/no)")
load_choice=input().lower().strip()
load_choice = check_y_n(all)

if load_choice == "yes":
    try:
        my_lists = load_dic()
    except:
        print("no file to load, please define categories.")
        new_cats()
else:
    new_cats()


#ask if user wants to generate for all or a subset
print("Would you like to generate options for all categories? (yes/no)")
all=input().lower().strip()
all = check_y_n(all)

#generate options for subset of defined categories
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
    
    
    while more_options == "yes":
        print("Please choose a category from the below to generate a choice: \n" + str(my_lists.keys()))
        #need to validate user input
        picked = input()
        pick_cat.append(picked)
        print("Do you want to generate options for another category (yes or no)")
        more_options = input().lower().strip()
        more_options = check_y_n(more_options)


    make_choice(pick_cat)
    happy_with_choice(pick_cat)
    
    
    #need tocheck if the length of the picked list is less than or equal to the number of unique keys and stop them if they are saying yes to too many

#generate options for all categories
else:
    print("Here are the choices we have generated for you:")
    make_choice(all)
    happy_with_choice(all)



print("Enjoy!")

#print(my_lists)