# Imports
from pathlib import Path
from pick import pick
import os
import subprocess
import json

# Function to clear terminal to make things cleaner
def clear_terminal():
    print("\033[2J\033[H", end="")

# Makes it so that the user has time to actually read/interact with what is happening on screen
def give_time():
    input("Press enter to return...")

# project paths

PROJECT_DIR = Path(__file__).resolve().parent

SETTINGS_FILE = PROJECT_DIR / "saved_settings.json"

def load_saved_settings():

    if not SETTINGS_FILE.exists():
        return {}

    with open(SETTINGS_FILE, "r") as file:
        return json.load(file)

    # Load saved settings
    saved_projs = load_saved_settings()
    input("Press enter to return...")

def load_saved_projs():

    if not SETTINGS_FILE.exists():
        return {}

    with open(SETTINGS_FILE, "r") as file:
        return json.load(file)

def save_saved_projs(saved_projs):

    with open(SETTINGS_FILE, "w") as file:
        json.dump(saved_settings, file, indent=4)

# make a new project
def new_proj():

    global saved_settings

    clear_terminal()

    print("Create New Project\n")

    # Project name
    name = input("What would you like to name this project? ")

    # Description of project
    clear_terminal()
    print(f"Creating {name}\n")
    print("Description of project(Goals, Timeframe, Why you are building it, etc)")
    desc = input()

    # Save it to JSON
    save_saved_projs(saved_projs)

    clear_terminal()

    print(f"Project '{name}' has been created successfully!")

    give_time()

# overview of current projects
def view_current():
    pass
def main():
    
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
    
    elif option == "Update a project":
        # update_proj()
        pass
    elif option == "Exit":
        exit()
        
main()