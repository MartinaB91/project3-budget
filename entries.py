import utils

def save_budget_entry(active_user_id):
        active_budget = utils.get_active_budget(active_user_id)
        """ Gives the user different entry options(menu options), reads user input, 
        gives the new entry a unique id and save information about the entry, active user and 
        budget and saves to worksheet."""
        menu_options = (f"Your current budget is {active_budget['budget_name']}. Now let's choose a category for your purchase: \n"
        "1. Shopping. \n"
        "2. Food. \n"
        "3. Entertainment. \n"
        "4. Other. \n"
        "5. Done.")
        print(menu_options)
        selected_option = input("Please select a menu option (1-5): \n")

        """ Prints menu options for budgets entries and reads inputs """
        if selected_option == "1":
            budget_category = "shopping"
            budget_entry = input("How much have you spent on shopping:")
        elif selected_option == "2":
            budget_category = "food"
            budget_entry = input("How much have you spent on food:")
        elif selected_option == "3":
            budget_category = "entertainment"
            budget_entry = input("How much have you spent on entertainment:")
        elif selected_option == "4":
            budget_category = "other"
            budget_entry = input("How much have you spent on other:")
        elif selected_option == "5":
            print(selected_option) # Todo: Return to start page or go back
        else:
            print(f"{selected_option} is not a valid menu option. Please try again.")
            selected_option = input("Please select a menu option (1-5): \n")
        
        new_budget_id = utils.give_data_id('budget entries') # Gets the entry a unique id 
        entry = [new_budget_id, active_user_id, active_budget['id'], budget_category, budget_entry] # Saves data in a list
        utils.save_data_to_worksheet('budget entries', entry) 

    

    


    
   









        
            
       
            

  


