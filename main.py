# Imports
import pick
import os
import subprocess

def clear_terminal():
    subprocess.run(["cls" if os.name == "nt" else "clear"], check=False)
    
# Give time so a while loop or other things don't instantly clear things
def give_time():
    input("Press enter to return...")

print("Developer Command Center")
print("DCC is the new way for developers to keep track of their projects. It tracks progress, roadblocks, and when you last worked on somehting so you\n know when it is time to jump back in")
user_input = ( "Would you like to: \n"
              "Open a new project \n"
              "Overview of current projects \n"
              "Update a project " 
)
options = [
    "new_project"
    "overview_current_projects"
    "update_proj"
]

option, index = pick(options, user_input, indicator="=>", default_index=0)

if option == "new_project":
    clear_terminal()
    
    new_proj_name = input("What do you want to name your new project? \n")
    new_proj_des = input("Give a brief description of your project: \n")
    
elif option == "overview_current_projects":
    clear_terminal()
    
    
