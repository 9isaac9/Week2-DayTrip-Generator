
import random
#DESTINATION
destination = ["Paris", "Italy", "Germany", "Ireland"]

# randomly_selected_destination = random.choice(destination)
# print(f"We have chosen {randomly_selected_destination}")

#The Welcome sign
def display_welcome():
    print("Welcome to Day Trip Generator")
display_welcome()

#The moment I choose/select Destination for User and User "reselects" choice
def Bz_chooses_destination_for_user():

    user_validator = False
    while user_validator is False:  
        randomly_selected_destination = random.choice(destination)
        #print(f"We have selected, {randomly_selected_destination} for you ")
        user_input = input(f"We have selected, {randomly_selected_destination} for you, do you like this option? y/n?  ")
        if user_input == "y":
            print("We have confirmed your choice")
            return randomly_selected_destination
        elif user_input == "n":
            print("Sorry we will regenerate your options")

#Bz_chooses_destination_for_user()
rechoosing_destination = Bz_chooses_destination_for_user()
print(f"Great selection, enjoy {rechoosing_destination}.")


#TRANSPORTATION
transportation = ["vehicle_rental", "train", "plane", "cruise liner"]

randomly_selected_transportation = random.choice(transportation)
print(f"We have chosen {randomly_selected_transportation}")

def Bz_chooses_transportaion_for_user():
    user_validator = False
    while user_validator is False:  
        randomly_selected_transportation = random.choice(transportation)
        #print(f"We have selected, {randomly_selected_transportation} for you ")
        user_input = input(f"We have selected, {randomly_selected_transportation} for you, do you like this option? y/n?  ")
        if user_input == "y":
            print("We have confirmed your choice")
            return randomly_selected_transportation
        elif user_input == "n":
            print("Sorry we will regenerate your options")

#Bz_chooses_transportation_for_user()
rechoosing_transportation = Bz_chooses_transportaion_for_user()
print(f"Have a wonderful journey on the {rechoosing_transportation}.")


#RESTAURANT
restaurant = ["Jaques Bistro", "Brunos Olive Garden", "Schnetzels Place", "Leprechauns Pot of Gold"]

# randomly_selected_restaurant = random.choice(restaurant)
# print(f"We have chosen {randomly_selected_restaurant}")

def Bz_chooses_restaurant_for_user():
    user_validator = False
    while user_validator is False:  
        randomly_selected_restaurant = random.choice(restaurant)
        #print(f"We have selected, {randomly_selected_restaurant} for you ")
        user_input = input(f"We have selected, {randomly_selected_restaurant} for you, do you like this option? y/n?  ")
        if user_input == "y":
            print("We have confirmed your choice")
            return randomly_selected_restaurant
        elif user_input == "n":
            print("Sorry we will regenerate your options")

#Bz_chooses_restaurant_for_user()
rechoosing_restaurant = Bz_chooses_restaurant_for_user()
print(f"Good day this is {rechoosing_restaurant}. Have a delightful meal!")



#ENTERTAINMENT  
entertainment = ["dance", "theater", "museum", "excurisions"]

# randomly_selected_entertainment = random.choice(entertainment)
# print(f"We have chosen {randomly_selected_entertainment}")

def Bz_chooses_entertainment_for_user():
    user_validator = False
    while user_validator is False:  
        randomly_selected_entertainment = random.choice(entertainment)
        #print(f"We have selected, {randomly_selected_entertainment} for you ")
        user_input = input(f"We have selected, {randomly_selected_entertainment} for you, do you like this option? y/n?  ")
        if user_input == "y":
            print("We have confirmed your choice")
            return randomly_selected_entertainment
        elif user_input == "n":
            print("Sorry we will regenerate your options")

#Bz_chooses_entertainment_for_user()
rechoosing_entertainment = Bz_chooses_entertainment_for_user()
print(f"Have a phenominal time at the {rechoosing_entertainment}!")