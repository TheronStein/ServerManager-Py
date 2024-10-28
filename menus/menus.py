

menu_info = {
    "Main_Menu": {"choice_limit": 8, "prompt": "Select an option from the menu:"},
    "Confirmation_Menu": {"choice_limit": 2, "prompt": "Are you sure?"},
    "Server_Start": {"choice_limit": 10, "prompt": "Select an option to start the server:"}
}



    "Confirmation_Menu": 2,

    "Server_Start_Main": 10,
    "Server_Start_New": 10,
    "Server_Start_NewSet": 10,

    "Server_Shutdown_Main": 10,
    "Server_Start_New": 10,
    "Server_Start_NewSet": 10,

    "Another_Menu": 10
}


# Define menu names and their corresponding prompts
menu_info = {
    "Main_Menu": "Select an option from the menu:",
    "Another_Menu": "Choose an option from the menu:"
}



# Define function to generate menu options
def generate_menu_options(menu_name):
    # Define menu options as needed
    if menu_name == "Server_Start":
        return ["Start Servers", "Shutdown Servers", "Reset Servers", "Server Status", "Server Troubleshooting", "Back to Previous Menu"]
    elif menu_name == "Another_Menu":
        return ["Option 1", "Option 2", "Option 3", "Option 4", "Option 5", "Exit"]

# Generate menu options for each menu
for menu_name, prompt in menu_info.items():
    menus[menu_name] = {
        "options": generate_menu_options(menu_name),
        "prompt": prompt
    }


# Define function to generate menu options
def generate_menu_options(menu_name, choice_limit):
    menu_options = [f"Option {i}" for i in range(1, choice_limit + 1)]
    menu_options.append("Back to Previous Menu" if menu_name != "Main_Menu" else "Exit")
    return menu_options

# Generate menu options for each menu
for menu_name, menu_data in menu_info.items():
    choice_limit = menu_data["choice_limit"]
    prompt = menu_data["prompt"]
    menus[menu_name] = {
        "options": generate_menu_options(menu_name, choice_limit),
        "prompt": prompt
    }


# Accessing menu options and prompts
print("Menu:", "Server_Start")
print("Prompt:", menus["Server_Start"]["prompt"])
print("Options:", menus["Server_Start"]["options"])
print()

print("Menu:", "Another_Menu")
print("Prompt:", menus["Another_Menu"]["prompt"])
print("Options:", menus["Another_Menu"]["options"])
print()

# You can also dynamically add more options later if needed
#menus["Server_Start"]["options"].append("New Option")