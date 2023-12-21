import random
import json
import my_functions
    
#MAIN BODY OF CODE
print("Would you like to load previously defined categories? (yes/no)")
load_choice = input().lower().strip()
load_choice = my_functions.check_y_n(load_choice)

if load_choice == "yes":
    try:
        my_lists = my_functions.load_dic()
    except:
        print("no file to load, please define categories.")
        my_lists = my_functions.new_cats()
else:
    my_lists = my_functions.new_cats()


#ask if user wants to generate for all or a subset
print("Would you like to generate options for all categories? (yes/no)")
all=input().lower().strip()
all = my_functions.check_y_n(all)

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
    more_options = my_functions.check_y_n(more_options)
    
    
    while more_options == "yes":
        print("Please choose a category from the below to generate a choice: \n" + str(my_lists.keys()))
        #need to validate user input
        picked = input()
        pick_cat.append(picked)
        print("Do you want to generate options for another category (yes or no)")
        more_options = input().lower().strip()
        more_options = my_functions.check_y_n(more_options)


    my_functions.make_choice(pick_cat,my_lists)
    my_functions.happy_with_choice(pick_cat,my_lists)
    
    
    #need tocheck if the length of the picked list is less than or equal to the number of unique keys and stop them if they are saying yes to too many

#generate options for all categories
else:
    print("Here are the choices we have generated for you:")
    my_functions.make_choice(all,my_lists)
    my_functions.happy_with_choice(all,my_lists)



print("Enjoy!")

#print(my_lists)