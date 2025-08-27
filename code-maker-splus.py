import random
import sys
from subprocess import call
from sys import platform
import time
from colorama import Fore, Style

# This function clears the terminal screen for better display.
def clear():
    """Clears the terminal screen."""
    if platform not in ('win32', 'cygwin'):
        command = 'clear'
    else:
        command = 'cls'
    try:
        call(command, shell=True)
    except OSError as e:
        print(f"Error clearing screen: {type(e).__name__}, {e}")

# Define color codes for better readability
red = Fore.RED
green = Fore.GREEN
blue = Fore.CYAN  # Using CYAN for a distinct blue color
pink = Fore.MAGENTA
bold = Style.BRIGHT
reset = Style.RESET_ALL

# List of strings for the generated message
goxzarsh = [
    'This-account-mocks-Islamic-affairs',
    'This-account-promotes-pornography',
    'Hello-this-person-has-an-inappropriate-profile',
    'This-account-promotes-nakedness-and-veiling',
    'This-account-is-a-spammer',
    'This account-is-not-good-for-Soroush Plus-messenger-because-it-is-a-real-bully'
]

# Print banner with colorama and a slight delay for dramatic effect
print(pink)
x = f"""
⠀⠀⠀⠀⠀⢀⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣠⣄⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠙⢿⣷⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⣿⣿⠋⠁⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⣸⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣟⣿⣄⡀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⢀⣠⣾⣯⣽⡿⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠻⢿⣿⣽⣿⣦⣀⠀⠀⠀⠀⠀
⠀⠀⠀⣴⣿⣟⣻⡿⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⢿⣟⣭⣿⣷⣄⠀⠀⠀
⠀⢠⣾⣿⣿⣿⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⢿⣿⣫⣿⣷⡀⠀
⢠⣿⣿⣟⣛⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⣿⣿⡄
⣺⣿⣿⣿⣿⣇⠀⠀⠀⠀⠀⠀⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢴⠀⠀⠀⠀⠀⠀⠀⢀⣾⣿⣿⣿⣿⣿⡷
⢹⣿⣿⡿⣿⣻⣆⠀⠀⠀⠀⠀⢻⡷⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⢎⣿⠀⠀⠀⠀⠀⢀⣠⠾⣿⣿⣿⣿⣿⣿⠇
⠈⠻⣿⣷⣿⣿⣿⠿⣦⣤⣀⠀⢠⣷⣿⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣸⢺⣿⣦⣀⣠⣴⣾⡿⣿⣿⣷⣶⣶⣶⡿⠋⠀
⠀⠀⠙⠿⣿⣟⣵⣿⣿⣿⢿⣷⣼⣧⣿⣧⣠⣤⣤⣤⣤⣤⣤⡤⣤⢤⣾⣯⣿⣿⣿⣿⣭⣽⣿⣶⣿⣿⡿⠟⠋⠀⠀⠀
⠀⠀⠀⠀⠈⠛⢿⣯⣵⠶⠟⢛⣋⠭⢭⡐⠖⠤⠥⠔⠲⠰⠊⠥⠭⠨⣅⣀⣅⡚⢭⡙⠻⢿⣷⣿⣟⠁⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⢠⣾⠟⢫⣼⠵⠊⠅⡡⠄⡂⠀⠀⡐⢒⠢⡔⠢⢒⠤⣢⢖⠲⠦⣜⢍⠓⢌⠳⡐⢌⣍⣻⣦⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⣼⡧⣼⠷⣵⣆⠴⡃⠀⠀⢡⢓⠠⠄⣩⡞⣍⣣⠀⣼⠣⠈⠁⠱⣈⢷⡀⠂⠐⢀⠒⣫⢙⢻⣧⡀⠀⠀⠀⠀
⠀⠀⣀⣴⣿⣶⣷⣼⣡⠌⡳⣕⢢⠐⢦⠋⠠⣞⠁⠸⡯⢈⠸⣇⠧⣀⠀⢤⡘⢦⡷⣼⠻⠩⠶⢶⣭⣤⠹⣷⣦⡀⠀⠀
⠀⢸⡟⣩⣿⠳⣿⣦⣝⡩⣆⠐⠂⢘⣰⡶⢶⡏⠄⡐⠀⠲⠦⣬⣓⠣⠏⠖⣩⠏⢀⠈⣰⣶⣿⣿⢻⣿⡻⣜⣿⢿⣄⠀
⠀⢸⡿⣧⢻⣄⣿⣿⣿⣿⣿⣯⣕⣚⡁⣾⡋⣠⢐⠿⠷⣶⡀⣷⠈⠓⢄⣂⣴⣚⣤⣾⣿⣿⣿⢣⡟⣼⡗⣿⣺⣗⢻⡆
⠀⢿⣧⡷⣆⡟⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣶⣶⣿⣶⣿⣿⣿⣿⣿⣿⣿⣿⡟⣁⡟⡆⠠⣏⣧⣸⡧⣼⡇
⠀⠀⢻⣧⡟⢷⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠏⣄⢻⡽⣛⡽⡛⣏⢌⣿⠟⠁
⠀⠀⠀⢻⣿⢸⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡁⡼⡁⣞⢐⡎⠓⣞⣿⠿⠁⠀⠀
⠀⠀⠀⢸⣿⣺⣽⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡯⢟⣵⣃⣿⡉⣆⡧⢌⣿⠇⠀⠀⠀⠀
⠀⠀⠀⢸⣿⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⣻⡟⢱⡼⠋⣋⡯⢵⡟⣑⣼⠟⠀⠀⠀⠀⠀
⠀⠀⠀⢿⣧⣸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⣫⡿⢁⡼⢫⡜⣱⠏⣠⣏⣶⡿⠃⠀⠀⠀⠀⠀⠀
⠀⠀⠀⣾⢿⣸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣋⣽⠟⣠⡯⡿⢏⡼⣣⣾⡿⠟⠁⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠠⣿⢿⣧⡻⢽⡿⡿⣿⣿⣿⣿⣿⣿⣿⣿⠿⣟⢻⢿⣿⡿⠛⡝⣩⣾⣿⡾⣿⠟⠏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⢿⣶⣏⡟⣧⣉⠿⢛⠿⠯⣬⡿⠦⠷⠚⣖⢿⢷⢞⢋⣴⣷⣿⠿⠛⠁⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠙⠿⣿⣟⣿⣯⠽⢯⠵⣤⣕⣭⣤⣾⠿⢿⠿⠟⠛⠋⠁⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠈⠉⠉⠋⠛⠛⠛⠋⠋⠋⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
█▀▀ █▀█ █▀▄ █▀▀   █▀▄▀█ ▄▀█ █▄▀ █▀▀   █▀▀ █ █░░ ▀█▀ █▀▀ █▀█ █   █▀ █▀█ █░░ █░█ █▀
█▄▄ █▄█ █▄▀ ██▄   █░▀░█ █▀█ █░█ ██▄   █▀░ █ █▄▄ ░█░ ██▄ █▀▄ █   ▄█ █▀▀ █▄▄ █▄█ ▄█ v1.1
"""
for c in x:
    sys.stdout.write(c)
    sys.stdout.flush()
    time.sleep(0.0000001)

# Display welcome messages
print(reset)
time.sleep(1)
print(f"{bold}{red}programing by DMNHACKER")
print(f"{red}supports soroush plus 7.2.0 version!")
print(f"{red}servers.....ON")
print(f"{blue}")
time.sleep(2.5)
print("")

# Progress animation
progress = [".........", "........", ".......", "......", ".....", "....", "...", "..", "."]
for i in progress:
    print(i)
    time.sleep(0.1)

print(f"{bold}{red}installed!{reset}")
time.sleep(3)
print("")

# Get user input and generate the link
try:
    idta3get = input(f'{blue}id target ro bedoon @ vared con >>> {reset}')
    print(f"{blue}")
    print(f"{random.choice(goxzarsh)}https://splus.ir/{idta3get}")
    print(f"{reset}")

    time.sleep(5)
    print(f"{green}30 sayer 40 mostahjan{reset}")
    time.sleep(10.6)
except Exception as e:
    print(f"{red}An error occurred: {e}{reset}")

