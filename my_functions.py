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
def happy_with_choice(picked,my_list):
    print("Are you happy with these choices? (yes or no)")
    happy = input()
    happy = check_y_n(happy)
    while happy == "no" or happy == "No":
        print("Here are some alternative choices we have generated for you:")
        make_choice(picked,my_list)
        print("Are you happy with these choices? (yes or no)")
        happy = input()
        happy = check_y_n(happy)

#create function / method to randomly select a value for each key from the dictionary for chosen categories
def make_choice(all,my_lists):
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

#function to write user defined categories to json file
def write_dic(dic):
    j = json.dumps(dic)
    f = open("categories.json","w")
    f.write(j)
    f.close()

#function to read previous categories in
def load_dic():
    f = open("categories.json","r")
    dic = json.load(f)
    return dic


#function for user to define new categories
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