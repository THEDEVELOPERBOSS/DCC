# Imports
import pick
import os
import subprocess

def clear_terminal():
    subprocess.run(["cls" if os.name == "nt" else "clear"], check=False)
    
# Give time so a while loop or other things don't instantly clear things
def give_time():
    input("Press enter to return...")

# make a new project
def new_proj():

    global saved_settings

    clear_terminal()

    print("Create New Project\n")

    # Project name
    new_proj_name = input("What would you like to name this project? ")

    # Description of project
    clear_terminal()
    print(f"Creating {new_proj_name}\n")
    print("Description of project(Goals, Timeframe, Why you are building it, etc)")
    new_proj_desc = input()

    # Save it to JSON
    save_saved_settings(saved_settings)

    clear_terminal()

    print(f"Project '{name}' has been created successfully!")

    give_time()

# overview of current projects
def view_current():
    
def main():
    print("Developer Command Center")
    print("DCC is the new way for developers to keep track of their projects. It tracks progress, roadblocks, and when you last worked on somehting so you\n know when it is time to jump back in")
    user_input = ( "Would you like to: \n"
                "Open a new project \n"
                "Overview of current projects \n"
                "Update a project \n" 
                "Exit DCC "
    )
    options = [
        "new_project"
        "overview_current_projects"
        "update_proj"
        "exit"
    ]

    option, index = pick(options, user_input, indicator="=>", default_index=0)

    if option == "new_project":
        new_proj()
    elif option == "overview_current_projects":
        clear_terminal()
    
    elif option == "update_proj":
        update_proj()
    elif option == "exit":
        exit()
        
           
    
