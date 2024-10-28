import subprocess
import time

def screen_start(name):
    log_file = "/home/rampage/server_start.log"
    print(f"Starting {name} Screen Session...")
    subprocess.run(["screen", "-dmS", name])
    time.sleep(1)
    write_menu("Server Start Initiated...", "", "")

def screen_stop(req, session_id):
    if req == "rampage":
        screen_list = screen_get_list("rampage")
        print("Terminating all rampage screen sessions...")
        for session in screen_list:
            print(f"Terminating {session}...")
            subprocess.run(["screen", "-S", session, "-X", "quit"])
            time.sleep(1)
    elif req == "all":
        screen_list = screen_get_list("all")
        print("Terminating all screen sessions...")
        for session in screen_list:
            print(f"Terminating {session}...")
            subprocess.run(["screen", "-S", session, "-X", "quit"])
            time.sleep(1)
    elif req == "specific":
        if session_id is None:
            print("No session ID provided")
            return
        else:
            print(f"Terminating screen session {session_id}...")
            subprocess.run(["screen", "-S", session_id, "-X", "quit"])
    write_menu("Server Stop Process Completed...", "", "")

def screen_count(type):
    if type == "all":
        screen_num = subprocess.run(["screen", "-ls"], capture_output=True, text=True)
        screen_num = screen_num.stdout.count("\n") - 2
    elif type == "rampage":
        screen_num = (
            subprocess.run(["screen", "-ls"], capture_output=True, text=True)
            .stdout.lower()
            .count("rampage")
        )
    return screen_num

def screen_get_list(type):
    screen_array = []
    if type == "all":
        screen_output = subprocess.run(["screen", "-ls"], capture_output=True, text=True)
        lines = screen_output.stdout.split("\n")
        for line in lines:
            if "." in line:
                screen_array.append(line.split(".")[0])
    elif type == "rampage":
        screen_output = subprocess.run(
            ["screen", "-ls"], capture_output=True, text=True
        )
        lines = screen_output.stdout.split("\n")
        for line in lines:
            if "rampage" in line.lower():
                screen_array.append(line.split(".")[0])
    return screen_array

# Utility function, assumed to be defined elsewhere
def write_menu(message1, message2, message3):
    pass

# Example usage
if __name__ == "__main__":
    screen_start("example")
    screen_stop("rampage")
    print(screen_count("all"))