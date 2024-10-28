def main_menu():
    menu_names = {"MAIN,STRING": "Your Menu Title"}  # Replace with your actual menu title
    print(menu_names["MAIN,STRING"])
    print("Choose an option...")
    print("1. Start Servers")
    print("2. Shutdown Servers")
    print("3. Restart Servers")
    print("4. Check and Fix Servers")
    print("5. Server Status")
    print("6. Screen Sessions")
    print("7. Window Options")
    print("8. Exit")
    option = input("Enter Option: ")

    if option == '1':
        server_init_proc("start")
    elif option == '2':
        server_init_proc("stop")
    elif option == '3':
        server_init_proc("restart")
    elif option == '4':
        server_init_proc("check")
    elif option == '5':
        server_init_proc("status")
    elif option == '6':
        menu_screen_main()
    elif option == '7':
        menu_window_main()
    elif option == '8':
        exit()
    else:
        print("Invalid Option")