#=====importing libraries===========
'''This is the section where you will import libraries'''
import datetime
from datetime import date

# Declare variable
file = "tasks.txt"
file1 = "user.txt"
temp_menu = False

username = []
password = []

user_name = ""
passwrd = ""


# Open file "user.txt"
user_file = open(file1, "r")

# Read every line from file
user_file_read = user_file.readlines()

# Cycle for to read file and append inside list "username" and "password" the item
for user_file_read_row in user_file_read :
    user_file_read_row_split = user_file_read_row.strip("\n").split(", ")
    username.append(user_file_read_row_split[0])
    password.append(user_file_read_row_split[1])

# Close file "user.txt"
user_file.close()

#====Login Section====
'''Here you will write code that will allow a user to login.
    - Your code must read usernames and password from the user.txt file
    - You can use a list or dictionary to store a list of usernames and passwords from the file.
    - Use a while loop to validate your user name and password.
'''

# Ask user to enter him username e password
user_name = input("Please, enter your username : ").lower()
passwrd = input("Please, enter your password : ").lower()

# "if" to check "user_name" is inside "username" list and if password is correspondence to user
if (user_name in username) and (password[username.index(user_name)] == passwrd) :
    print(f"Welcome, {username[username.index(user_name)]}")
    username_bool = True
    temp_menu = True
else :
    username_bool = False

# Cycle while: condition to exit username_bool equal to True
while username_bool != True :
    # Ask user to enter him username e password
    print("Sorry, your username or password is not correct!")
    user_name = input("Please, enter your username : ").lower()
    passwrd = input("Please, enter your password : ").lower()
    print("\n")
    # "if" to check is "user_name" is inside "username" list
    if user_name in username:

        # "if" to check "passwrd" match with "password[username.index(user_name)]"
        if password[username.index(user_name)] != passwrd :
            print("Sorry, password is not match!")
            passwrd = input(f"Please, enter password belonging to \"{username[username.index(user_name)]}\" : ")

            # Cycle while: condition to exit "passw" match with "password[username.index(user_name)]"
            while password[username.index(user_name)] != passwrd:
                print("Sorry, password is not match!")
                passwrd = input(f"Please, enter password belonging to \"{username[username.index(user_name)]}\" : ")
            else :
                print(f"Welcome, {username[username.index(user_name)]}")
                username_bool = True
                temp_menu = True
        else :
            print(f"Welcome, {username[username.index(user_name)]}")
            username_bool = True
            temp_menu = True
    else:
        username_bool = False


while temp_menu == True:

    #presenting the menu to the user and
    # making sure that the user input is coneverted to lower case.
    if (username[username.index(user_name)] == "admin") :
        # "s" is the new menu option to display statistics just for "admin" user
        menu = input('''Select one of the following Options below:
r - Registering a user
a - Adding a task
va - View all tasks
vm - View my task
s - Statistic : Prints the number of users and tasks
e - Exit
: ''').lower()
    else :
        # Nes menu if you do not are "admin"
        menu = input('''Select one of the following Options below:
a - Adding a task
va - View all tasks
vm - View my task
e - Exit
: ''').lower()

    if ((menu == 'r') and (username[username.index(user_name)] == "admin")) :
        pass
        '''In this block you will write code to add a new user to the user.txt file
        - You can follow the following steps:
            - Request input of a new username
            - Request input of a new password
            - Request input of password confirmation.
            - Check if the new password and confirmed password are the same.
            - If they are the same, add them to the user.txt file,
            - Otherwise you present a relevant message.'''

        # Ask user to enter new username
        new_user_name = input("Please, enter a new username : ").lower()

        # "if" to check is "new_user_name" is inside "username" list
        if new_user_name in username :
            # While loop: condition to exit "new_user_name" is not in "username"
            while new_user_name in username :
                # Ask user to enter new username and print out message
                print("Sorry, the insert username is already used.")
                new_user_name = input("Please, enter a new username : ").lower()

        # Ask user to enter new password and confirm that
        new_passwrd = input("Please, enter a new password : ").lower()
        new_passwrd_conf = input("Please, confirm password you insert : ").lower()

        # While loop: condition to exit "new_passwrd" equal to "new_passwrd_conf"
        while new_passwrd != new_passwrd_conf:
            # Ask user to confirm password and print out message
            print("Sorry, your password doesn't match.")
            new_passwrd_conf = input("Please, confirm password you insert : ").lower()
        else:

            # Open file "user.txt"
            user_file_write = open(file1, "a")

            # Write "user.txt"
            user_file_write.write(f"\n{new_user_name}, {new_passwrd}")

            # Append "new_user_name" and "new_passwrd" inside the lists
            username.append(new_user_name)
            password.append(new_passwrd)

            # Print out message
            print("Well done! Your password is insert in user.txt")

            # Close file "user.txt"
            user_file_write.close()

    elif menu == 'a':
        pass

        '''In this block you will put code that will allow a user to add a new task to task.txt file
        - You can follow these steps:
            - Prompt a user for the following: 
                - A username of the person whom the task is assigned to,
                - A title of a task,
                - A description of the task and 
                - the due date of the task.
            - Then get the current date.
            - Add the data to the file task.txt and
            - You must remember to include the 'No' to indicate if the task is complete.'''


        print ("This is the users inside user.txt.")
        # Cycle "for" to print username inside "user.txt"
        for count, user_to_txt in enumerate(username, 1) :
            print(f"{count}.{user_to_txt} ", end=" ")
        print("\nMake sure to assign task of one of this users.\n")

        # Ask user to enter username of the person whom the task is assigned to
        assigned_name = input("Please, enter a username of the person whom the task is assigned to : ")

        # Cycle "while": condition to exit "assigned_name" is not in "username" list
        while assigned_name not in username:

            # Ask user to enter username of the person whom the task is assigned to
            # Print a message
            print ("Sorry the user is not in the file user.txt")
            assigned_name = input("Please, enter a username of the person whom the task is assigned to : ")

        # Ask user to enter title and description of a task
        title_task = input("Please, enter a title of a task : ")
        description_task = input("Please, enter a description of the task : ")

        # Ask user to enter the due date of the task
        due_date_task = input("Please, enter the due date of the task (dd-mm-yyyy) : ")
        # Replace incorrect character with "-"
        due_date_task = due_date_task.replace("/", "-").replace(" ", "-")

        # Split the date
        day, month, year = due_date_task.split("-")

        # Assign "this_year" to current year
        #this_day = date.today().strftime("%d")
        this_year = date.today().strftime("%Y")

        # "if" to check is day, month and year is numeric
        if ((day.isnumeric()) and (month.isnumeric()) and (year.isnumeric())) :
            # Cycle "while": condition to exit
            # day less than or equal to 31
            # day greater than "this_day"
            # month less then 12
            # day greater than or equal to "this_year"
            while ((int(day) > 31) or (int(month) > 12) or (int(year) < int(this_year))):

                print("Sorry, uncorrect date. This is the format (dd-mm-yyyy)")
                print("\"day\" should be less than or equal to 31")
                print("\"month\" should be less than or equal to 12")
                print("\"year\" should be greater than or equal to this year")
                due_date_task = input("Please, enter the due date of the task (dd-mm-yyyy) : ")
                due_date_task = due_date_task.replace("/", "-")
                due_date_task = due_date_task.replace(" ", "-")
                day, month, year = due_date_task.split("-")

        else:
            print("Sorry, uncorrect date. The date should be numeric (dd-mm-yyyy)")

        today = date.today()

        # Create variable "current_date"
        current_date = today.strftime("%d-%m-%Y")
        complete_task = "No"

        # Open file "task.txt
        task_file_write = open(file, "a")

        # Write to file "task.txt"
        task_file_write.write(f"\n{assigned_name}, {title_task}, {description_task}, {current_date}, {due_date_task}, {complete_task}")

        print("Well done! Your task is insert in task.txt")

        # Close file "task.txt"
        task_file_write.close()

    elif menu == 'va':
        pass
        '''In this block you will put code so that the program will read the task from task.txt file and
         print to the console in the format of Output 2 in the task PDF(i.e. include spacing and labelling)
         You can do it in this way:
            - Read a line from the file.
            - Split that line where there is comma and space.
            - Then print the results in the format shown in the Output 2 
            - It is much easier to read a file using a for loop.'''

        task_counter = 0
        # Open file "task.txt"
        with open(file, "r") as task_file:
            print()  # Void print
            # Cycle "for" to read file "task.txt"
            for task in task_file :
                # split and strip the line inside file
                strip_task = task.strip("\n").split(", ")
                # Output tasks
                output = "___________________________________________________________\n"
                output += f"Task : \t\t\t {strip_task[1]}\n"
                output += f"Assigned to : \t\t {strip_task[0]}\n"
                output += f"Date assigned : \t {strip_task[3]}\n"
                output += f"Due Date : \t\t {strip_task[4]}\n"
                output += f"Task Complete? : \t {strip_task[5]}\n"
                output += f"Task description : \n"
                output += f"{strip_task[2]}\n"
                output += "___________________________________________________________\n"
                output += "\n"

                # Print out the task
                print(output)
                task_counter += 1
            # "if" condition to check if I have task to show
            if task_counter == 0:
                print("Sorry, no task to show in this moment\n")

    elif menu == 'vm':
        pass
        '''In this block you will put code the that will read the task from task.txt file and
         print to the console in the format of Output 2 in the task PDF(i.e. include spacing and labelling)
         You can do it in this way:
            - Read a line from the file
            - Split the line where there is comma and space.
            - Check if the username of the person logged in is the same as the username you have
            read from the file.
            - If they are the same print it in the format of Output 2 in the task PDF'''

        task_user_counter = 0
        # Open file "task.txt"
        with open(file, "r") as task_file_user :
            print()  # Void print
            # Cycle "for" to read file "task.txt"
            for task_user in task_file_user :
                # split and strip the line inside file
                strip_task_user = task_user.strip("\n").split(", ")
                # "if" condition to check is "strip_task[0]" is equal to "userid"
                if (strip_task_user[0] == username[username.index(user_name)]) :
                    # Output tasks
                    output = "___________________________________________________________\n"
                    output += f"Task : \t\t\t {strip_task_user[1]}\n"
                    output += f"Assigned to : \t\t {strip_task_user[0]}\n"
                    output += f"Date assigned : \t {strip_task_user[3]}\n"
                    output += f"Due Date : \t\t {strip_task_user[4]}\n"
                    output += f"Task Complete? : \t {strip_task_user[5]}\n"
                    output += f"Task description : \n"
                    output += f"{strip_task_user[2]}\n"
                    output += "___________________________________________________________\n"
                    output += "\n"

                    # Print out the task
                    print(output)
                    task_user_counter += 1
                # "if" condition to check if I have task to show
            if task_user_counter == 0:
                print("Sorry, no task to show in this moment\n")


    elif ((menu == 's') and (username[username.index(user_name)] == "admin")):
        pass
        '''
        The admin user is provided with a new menu option that allows
        them to display statistics. When this menu option is selected, the
        total number of tasks and the total number of users should be
        displayed in a user-friendly manner.
        '''


        # Open file "user.txt" and "task.txt"
        task_statistic = open(file, "r")
        user_statistic = open(file1, "r")

        # Read every line from files
        task_statistic_read = task_statistic.readlines()
        user_statistic_read = user_statistic.readlines()

        stati_user = "▄" * len(user_statistic_read)
        stati_task = "▄" * len(task_statistic_read)

        # Print out the number of the users and the numbers of the tasks
        print(f"The total number of users are : {stati_user} {len(user_statistic_read)} ")
        print(f"The total number of tasks are : {stati_task} {len(task_statistic_read)} ")

        # Close file "user.txt" and "task.txt"
        user_statistic.close()
        task_statistic.close()

    elif menu == 'e':
        print('Goodbye!!!')
        exit()

    else:
        print("You have made a wrong choice, Please Try again")
