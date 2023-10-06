#Ramiro Bazan

#1. Display "Assignment 1" as the first line and then skips a line
assign = "Assignment 1"
print(assign + "\n")

#2. Prompt the user for their name, age, and number of hours they sleep and store their answers into program variables
name = input("Enter your name: ")
users_age = int(input("Enter your age: "))
hours_slept = int(input("Enter hours that you sleep: "))

# 3. Use the following mathematical formula to determine how many years of their life has been wasted sleeping
wasted_years = (hours_slept/24) * users_age

#4. Format a String message that is in a format similar to what's shown below and display it on the Console.
#5. Make sure that the period appears directly after the name in the display!  (Must be "Hello Steve." , not "Hello Steve .")
print("Hello "+name+".\nYou have been unconscious for "+str(wasted_years)+" years!")
