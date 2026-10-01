# Imports
from pathlib import Path
from pick import pick
import json

# Function to clear terminal to make things cleaner
def clear_terminal():
    print("\033[2J\033[H", end="")

# Makes it so that the user has time to actually read/interact with what is happening on screen
def give_time():
    input("Press enter to return...")

# project paths

PROJECT_DIR = Path(__file__).resolve().parent

PROJECTS_FILE = PROJECT_DIR / "saved_projs.json"

# Loads saved projects
def load_saved_projects():

    if not PROJECTS_FILE.exists():
        return {}

    with open(PROJECTS_FILE, "r") as file:
        return json.load(file)

# Load saved settings
saved_projects = load_saved_projects()

def save_saved_projects(saved_projects):

    with open(PROJECTS_FILE, "w") as file:
        json.dump(saved_projects, file, indent=4)

# make a new project
def new_proj():

    clear_terminal()

    print("Create New Project\n")

    # Project name
    name = input("What would you like to name this project? ")

    # Description of project
    clear_terminal()
    print(f"Creating {name}\n")
    print("Description of project(Goals, Timeframe, Why you are building it, etc)")
    desc = input()

    # project layout
    saved_projects[name] = {
        "desc": desc
    }
    
    # Save it to JSON
    save_saved_projects(saved_projects)

    clear_terminal()

    print(f"Project '{name}' has been created successfully!")

    give_time()

# overview of current projects
def view_current():
    pass # build this out
def update_proj():
    
    global saved_settings
    
    load_saved_projects()
    
    if not saved_settings: # not means it will execute if the file is empty
        print("No saved projects yet")
    else: 
        for name in saved_projects:
            print(f"- {name}")
    print("What project do you want to edit")
def main():
    while True:
        clear_terminal()
        print("Developer Command Center")
        print("DCC is the new way for developers to keep track of their projects. It tracks progress, roadblocks, and when you last worked on somehting so you\n know when it is time to jump back in")
        user_input = ("Would you like to: \n"
                    "Open a new project \n"
                    "See overview of current projects \n"
                    "Update a project \n" 
                    "Exit DCC "
        )
        options = [
            "New project",
            "Overview of current projects",
            "Update a project",
            "Exit"
        ]

        option, index = pick(options, user_input, indicator="=>", default_index=0)

        if option == "New project":
            new_proj()
        elif option == "Overview of current projects":
            clear_terminal()
            pass
        elif option == "Update a project":
            update_proj()
            pass
        elif option == "Exit":
            exit()
        
main()