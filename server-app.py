import os
import sys
import time

# Explicitly set the PATH variable
os.environ['PATH'] = '/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin'

srcdir = os.path.join(os.environ['HOME'], 'ServerManager')

# Assuming global_import.py exists in the utils directory
sys.path.append(os.path.join(srcdir, 'utils'))
import global_import  # This will import your global-import.sh equivalent

def program_start(arg1):
    print(srcdir)
    # Assuming these variables are defined in global_import
    print(global_import.menudir)
    print(global_import.defdir)
    print(global_import.funcdir)
    print(global_import.handir)
    print(global_import.logdir)
    print(global_import.tempdir)

    # Main execution
    if arg1 is None:
        global_import.menu_names["MAIN,FUNC"]()
    elif arg1 == '1':
        boot_server_proc()
        sys.exit()
    elif arg1 == '2':
        hourly_check_proc()
        sys.exit()
    else:
        error_handler("Invalid Argument", "program_start", global_import.menu_names["MAIN,FUNCTION"], global_import.menu_names["MAIN,STRING"], arg1)

    program_error_exit("Out of Bounds", "program_start", "Reached Out of Bounds in program_start...")

def program_error_exit(type, function, message):
    write_menu(type)
    time.sleep(2)
    print(f"From: {function}")
    time.sleep(2)
    print(f"Error Message: {message}")
    time.sleep(2)
    program_exit()

def program_exit():
    text_divider()
    print("Exiting Program...")
    text_divider()
    time.sleep(2)
    sys.exit()

arg1 = sys.argv[1] if len(sys.argv) > 1 else None
program_start(arg1)

program_error_exit("App Execution: Out of Bounds", "program_start", "Reached out of bounds in main execution...")