
def create_budget():
    print("Lets create a new budget!")
    budget_name = input("Give your budget a name: \n")
    print(
        f"The name of your new budget is {budget_name}. Now lets enter the values for each category."
    )
    sum_shopping = input("How much do you want to budget for shopping? \n")
    sum_food = input("How much do you want to budget for food? \n")
    sum_entertainment = input("How much do you want to budget for entertainment? \n")
    sum_other = input("How much do you want to budget for other things? \n")
    
    print(f"Your budget is as follow: \nShopping: {sum_shopping:>15} \nFood: {sum_food:>19} \nEntertainment: {sum_entertainment:>10} \nOther things: {sum_other:>11}")
     
def start_program():
    # Present user with options over what choises they have and what they can do in this program.
    print("Welcome to your budget program")
    print("What do you want to do?")
    print("1. Create a new budget")
    print("2. Add purchase to ongoing budget")
    print("3. Get a summary of budget")
    print("4. End ongoing budget")

    selected_option = input("Please enter the number of your chooise: \n")
    # Depending on what choice the user choose it will lead to different "pages". Every page has its a own function.
    if selected_option == "1":
        create_budget()
    elif selected_option == "2":
        print(selected_option)
    elif selected_option == "3":
        print(selected_option)
    elif selected_option == "4":
        print(selected_option)
    elif selected_option == "5":
        print(selected_option)
  

start_program()




