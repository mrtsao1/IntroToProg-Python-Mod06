'''
Title: Assignment 06
Description: Working with functions in a class,
             When the program starts, load each "row" of data
             in "ToDoList.txt" into a python Dictionary.
             Add each dictionary "row" to a python list "table"
Change Log: (Who, When, What)
MTsao, 2022-11-18, Created File
MTsao, 2022-11-19, Completed add new task step
MTsao, 2022-11-21, Completed remove existing task, save file steps
'''

# Data ---------------------------------------------------------------------- #
# Declare variables and constants
file_name_str = "ToDoFile.txt"  # The name of the data file
file_obj = None  # An object that represents a file
row_dic = {}  # A row of data separated into elements of a dictionary {Task,Priority}
table_lst = []  # A list that acts as a 'table' of rows
choice_str = ""  # Captures the user option selection


# Processing  --------------------------------------------------------------- #
class Processor:
    """  Performs Processing tasks """

    @staticmethod
    def read_data_from_file(file_name, list_of_rows):
        """ Reads data from a file into a list of dictionary rows

        :param file_name: (string) with name of file:
        :param list_of_rows: (list) you want filled with file data:
        :return: (list) of dictionary rows
        """
        list_of_rows.clear()  # clear current data
        file = open(file_name, "r")
        for line in file:
            task, priority = line.split(",")
            row = {"Task": task.strip(), "Priority": priority.strip()}
            list_of_rows.append(row)
        file.close()
        return list_of_rows

    @staticmethod
    def add_data_to_list(task, priority, list_of_rows):
        """ Adds data to a list of dictionary rows

        :param task: (string) with name of task:
        :param priority: (string) with name of priority:
        :param list_of_rows: (list) you want filled with file data:
        :return: (list) of dictionary rows
        """
        row = {"Task": str(task).strip(), "Priority": str(priority).strip()}
        list_of_rows.append(row)  # add task/priority to existing list
        return list_of_rows

    @staticmethod
    def remove_data_from_list(task, list_of_rows):
        """ Removes data from a list of dictionary rows

        :param task: (string) with name of task:
        :param list_of_rows: (list) you want filled with file data:
        :return: (list) of dictionary rows
        """
        boolMatch = False  # create a bool to track status of search for task to delete
        for objRow in list_of_rows:  # search each row
            if objRow['Task'] == task:  # task to delete was found
                list_of_rows.remove(objRow)  # delete task/priority from list
                print("Deleted task \"", task, "\" from list\n")  # notify user of status
                print(task)
                boolMatch = True
        if not boolMatch:  # task to delete was NOT found, notify user of status
            print("Unable to delete task. \"", task, "\" was not found.\n")
        return list_of_rows

    @staticmethod
    def write_data_to_file(file_name, list_of_rows):
        """ Writes data from a list of dictionary rows to a File

        :param file_name: (string) with name of file:
        :param list_of_rows: (list) you want filled with file data:
        :return: (list) of dictionary rows
        """
        objFile = open(file_name, "w")  # create/open output file
        for objRow in list_of_rows:  # write data to output file
            objFile.write(objRow["Task"] + ',' + objRow["Priority"] + '\n')
        objFile.close()  # close output file
        print("Data has been saved to \"", file_name, "\".")
        return list_of_rows


# Presentation (Input/Output)  -------------------------------------------- #


class IO:
    """ Performs Input and Output tasks """

    @staticmethod
    def output_menu_tasks():
        """  Display a menu of choices to the user

        :return: nothing
        """
        print('''
        Menu of Options
        1) Add a new Task
        2) Remove an existing Task
        3) Save Data to File        
        4) Exit Program
        ''')
        print()  # Add an extra line for looks

    @staticmethod
    def input_menu_choice():
        """ Gets the menu choice from a user

        :return: string
        """
        choice = str(input("Which option would you like to perform? [1 to 4] - ")).strip()
        print()  # Add an extra line for looks
        return choice

    @staticmethod
    def output_current_tasks_in_list(list_of_rows):
        """ Shows the current Tasks in the list of dictionaries rows

        :param list_of_rows: (list) of rows you want to display
        :return: nothing
        """
        rowCount = 1    # numbering system for printing out current tasks
        print("******* The current tasks ToDo are: *******")
        for row in list_of_rows:
            print(str(rowCount) + ".\t" + row["Task"] + " (" + row["Priority"] + ")")
            rowCount += 1
        print("*******************************************")
        print()  # Add an extra line for looks

    @staticmethod
    def input_new_task_and_priority():
        """  Gets task and priority values to be added to the list

        :return: (string, string) with task and priority
        """
        pass
        print("\t\tAdd a new task")
        strTask = input("\t\tState the task: ")  # prompt user for task
        strPriority = input("\t\tState the Priority level: ")  # prompt user for priority level
        print()  # add an extra line for looks
        return strTask, strPriority

    @staticmethod
    def input_task_to_remove():
        """  Gets the task name to be removed from the list

        :return: (string) with task
        """
        pass
        print("\t\tRemove an existing Task")
        strFindTerm = input("\t\tWhat task do you want to delete?: ")  # prompt user for task to delete
        print()  # add an extra line for looks
        return strFindTerm


# Main Body of Script  ------------------------------------------------------ #

# Step 1 - When the program starts, Load data from ToDoFile.txt.
Processor.read_data_from_file( file_name=file_name_str, list_of_rows=table_lst)  # read file data

# Step 2 - Display a menu of choices to the user
while (True):
    # Step 3 Show current data
    IO.output_current_tasks_in_list(list_of_rows=table_lst)  # Show current data in the list/table
    IO.output_menu_tasks()  # Shows menu
    choice_str = IO.input_menu_choice()  # Get menu option

    # Step 4 - Process user's menu choice
    if choice_str.strip() == '1':  # Add a new Task
        task, priority = IO.input_new_task_and_priority()
        table_lst = Processor.add_data_to_list(task=task, priority=priority, list_of_rows=table_lst)
        continue  # to show the menu

    elif choice_str == '2':  # Remove an existing Task
        task = IO.input_task_to_remove()
        table_lst = Processor.remove_data_from_list(task=task, list_of_rows=table_lst)
        continue  # to show the menu

    elif choice_str == '3':  # Save Data to File
        table_lst = Processor.write_data_to_file(file_name=file_name_str, list_of_rows=table_lst)
        print("\t\tSave Data to File")
        print("\t\tData Saved to \"" + file_name_str + "\"!\n")
        continue  # to show the menu

    elif choice_str == '4':  # Exit Program
        print("\t\tExit Program")
        print("\t\tGoodbye!")
        break  # by exiting loop

    else:   # Invalid choice
        print("\t\tInvalid choice entered. Please try again.\n")
