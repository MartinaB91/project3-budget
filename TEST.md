# Test and validations
## Introduction
During the development process, unit testing has been done to check if functionality is as expected. Same test has been executed again later on when new features has been added. This you can see as a type of regression testing. 

Exploratory testing has been done. If a bug was found in one function same test has been executed on a similar or related function to find out if same bug can be found. For example, when bug “User can add a username that is empty or contains only spaces” was found the same test was done to the function that lets the user write in budget name. This led to the same bug being found. This you can see as a type of error guessing. 

All performed test hasn’t been documented because the extensive documentation that would require. 
## Test
Some tests aren’t attached to a requirement. All requirements can’t be specified, some functions of a system can be seen as obvious. 
### Test cases

|Test id: 1|Test name: Create a new user|
|--------|------------------------------|
|**Purpose:**|Check if can create a user new user.|
|**Requirements:**| As a user, I want to be able to create a user account so that I can use the budget system. [(Requirements)](/README.md) 
|**Data:**| First name: Test, last name: Testsson, username: Testuser|
|**Procedure step:**|**Expected result:**| |
|**Step 1:** Start application |Application starts. Text “Welcome to your budget program” and menu option 1-2 is shown.|
|**Step 2:** Choose option 2.	|Text “Let's create a new user!” and “Enter your first name:” is shown.                 |
|**Step 3:** Enter first name. |Text “Enter your last name:” is shown.                                                  |
|**Step 4:** Enter last name.	|Text “Enter your username:” is shown.                                                   |
|**Step 5:** Enter username.		|Text “Your user Testuser has been saved!”.                                          |

|**Test id:** 2|**Test name:** Create new budgets|
-----------|------------------------------
|**Purpose:** |Check if user can create several new budgets|
|**Requirements:**| As a user, I want to create a new budget so I can track my budget goal.|
|                 |As a user, I want to have multiple budgets so that I can have different budgets goals. [(Requirements)](/README.md) |
|**Data:**| Username: Testuser, budget name 1: Test Budget 1, budget name 2: Test Budget 2, shopping: 200, food: 1500, entertainment: 570, other: 10|
|**Procedure step:**|**Expected result:**|
|**Step 1:** Start application |Application starts.  Text “Welcome to your budget program” and menu option 1-2 is shown.|
|**Step 2:** Choose option 1.	|Text “Enter your username:” is shown.|
|**Step 3:** Enter username.	|Welcome text and menu otion 1-4 is shown. |
|**Step 4:** Choose option 1.	|Text “Let's create a new budget!” and “Give your budget a name:” is shown.|
|**Step 5:** Enter budget name 1.	|Text “The name of your new budget is Test Budget 1. Now let's enter the amount for each category.” and “How much do you want to budget for shopping?” is shown.|
|**Step 6:** Enter amount shopping.	|Text “How much do you want to budget for food?” is shown.|
|**Step 7:** Enter amount food.	|Text “How much do you want to budget for entertainment?” is shown.|
|**Step 8:** Enter amount entertainment. |Text “How much do you want to budget for other things?” is shown.|
|**Step 9:** Enter amount other. |Summary for each category is shown. |
|**Step 10:** Redo step 4-9 with suffix 2.|Same as before but with suffix 2. |¨

|Test id: 3	|Test name: Add purchase to budget|
|----------------|-------------------------------------|
|**Purpose:** |Check if user can add purchase to ongoing budget.| 
|**Requirements:** |As a user, I want to add purchase to my budget so that my purchase is saved.,        |
|	| As a user, I want to see the budgets connected to my user account so that I can chose budget.     |
|	|As a user, I want to purchase to different budgets so that my purchase is saved in chosen budget. [(Requirements)](/README.md)   |
|**Data:** |Username: Testuser, budget name 1: Test Budget 1, budget name 2: Test Budget 2 , shopping: 50|
|**Procedure step:**	|**Expected result:**|
|**Step 1:** Start application 	|Application starts.  Text “Welcome to your budget program” and menu option 1-2 is shown. |
|**Step 2:** Choose option 1.	|Text “Enter your username:” is shown.     |
|**Step 3:** Enter username.	|Welcome text and menu otion 1-4 is shown. |
|**Step 4:** Choose option 2.	|	Text “Which budget would you like to add purchase to?”, “1. Test Budget 1 [active]” and “2. Test Budget 2 [active]” is shown.|
|**Step 5:** Choose option 1.	|Text “Your current budget is Test Budget 1. Now let's choose a category for your purchase:” and category menu options is shown. |
|**Step 6:** Choose option 1.	|Text “How much have you spent on shopping:” is shown.                 |
|**Step 7:** Enter shopping.	|Text “Your purchase has been saved!” and same text as in Step 5.      |
|**Step 8:** Choose option 5. 	|Menu option 1-4 is shown.                                             |
|**Step 9:** Redo step 4-7 but choose option 2(Test Budget 2).|	Same as before but with Test Budget 2. |

|Test id: 4	|Test name: Get summary of budget  |
|-----------|----------------------------------|                                                       
|**Purpose:** |Check if user can get a summary of budget.|
|**Requirements:** |As a user, I want to get a summary of my budget progress whenever I want so that I can follow my spendings. [(Requirements)](/README.md) |
|**Data:** |Username: Testuser, budget name 1: Test Budget 1 |
|**Procedure step:**|	Expected result:| 
|**Step 1:** Start application |Application starts.  Text “Welcome to your budget program” and menu option 1-2 is shown. |
|**Step 2:** Choose option 1.	|Text “Enter your username:” is shown.|
|**Step 3:** Choose option 3.	|Text “Which budget would you like a summary of?“ ,“1. Test Budget 1 [active]” and “2. Test Budget 2 [active]” is shown.|
|**Step 4:** Choose option 1.	|Summary of Test Budget 1 is shown. |

|Test id: 5|	Test name: End ongoing budget|
|----------|---------------------------------|
|**Purpose:** |Check if user can end ongoing budget. |
|**Requirements:**| As a user, I want to end chosen budget whenever I want so that the budget is not active because I am done. [(Requirements)](/README.md) |
|**Data:** |Username: Testuser, budget name 1: Test Budget 1|
|**Procedure step:**|	Expected result:|
|**Step 1:** Start application |	Application starts.  Text “Welcome to your budget program” and menu option 1-2 is shown. |
|**Step 2:** Choose option 1.|	Text “Enter your username:” is shown.|
|**Step 3:** Choose option 4.|	Text “Which budget do you want to end?” ,“1. Test Budget 1 [active]” and “2. Test Budget 2 [active]” is shown.|
|**Step 4:** Choose option 1.|	Text “Your budget Test Budget 1 is now ended” is shown.|

### Other tests
**Test id:** 6 **Test name:** Menu testing
All menus have been tested by selecting first and last valid menu option. The first invalid menu option has always been tested by that I mean if the first menu option is one, zero has also been tested. If last menu option is four, five also has been tested.

**Test id:** 7 **Test name:** Error messages usability testing 
All error messages usability has been tested. Which mean that the user when doing wrong is shown a message containing error description and information of what to do next. 

**Test id:**  8 **Test name:** Error provoking testing
Testing trying to provoke errors has been done. For example, entering empty strings or blank spaces in different input scenarios and entering very large numbers when creating a budget or budget entries. 

**Test id:** 9 **Test name:** Usability testing
In this test three independent users has been presented with some tasks to do in the budget system. Through testing the person has been observed to see if any usability improvements can be found. 
The user was tasked to perform the following:
1.	Create a user.
2.	Create a budget.
3.	Add three different purchases to the budget you have created.
4.	Get a summary of your created budget.
5.	End your budget.

## Test result


## Validations 
