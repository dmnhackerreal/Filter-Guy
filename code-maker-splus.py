import random
import sys
from subprocess import call
from sys import platform
import time
import datetime
from colorama import Fore, init # Added init

# Initializes colorama to support colors in various terminals (especially Windows).
# autoreset=True automatically resets the color to the default after each print.
init(autoreset=True)

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

# Define color codes using colorama for cross-platform support
red = Fore.RED
green = Fore.GREEN
blue = Fore.BLUE
pink = Fore.MAGENTA
white = Fore.WHITE
yellow = Fore.YELLOW
light_green = Fore.LIGHTGREEN_EX
light_blue = Fore.LIGHTBLUE_EX
light_yellow = Fore.LIGHTYELLOW_EX
# reset = Fore.RESET # With autoreset=True, this is often not strictly needed, but kept for reference.

# List of strings for the generated message
goxzarsh = [
    'This-account-mocks-Islamic-affairs',
    'This-account-promotes-pornography',
    'Hello-this-person-has-an-inappropriate-profile',
    'This-account-promotes-nakedness-and-veiling',
    'This-account-is-a-spammer',
    'This account-is-not-good-for-Soroush-Plus-messenger-because-it-is-a-real-bully'
]

# Print banner with colorama and a slight delay for dramatic effect
# With autoreset=True, there's no need to manually reset at the end of lines; colors reset automatically.
print(pink)
x = f"""⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
█▀▀ █▀█ █▀▄ █▀▀  █▀▄▀█ ▄▀█ █▄▀ █▀▀  █▀▀ █ █░░ ▀█▀ █▀▀ █▀█ █  █▀ █▀█ █░░ █░█ █▀
█▄▄ █▄█ █▄▀ ██▄  █░▀░█ █▀█ █░█ ██▄  █▀░ █ █▄▄ ░█░ ██▄ █▀▄ █  ▄█ █▀▀ █▄▄ █▄█ ▄█ v1.1
"""
for c in x:
    sys.stdout.write(c)
    sys.stdout.flush()
    time.sleep(0.0000001)

# Display welcome messages
# The 'reset' is now redundant due to autoreset=True, but can be kept if desired for explicit resets.
time.sleep(1)
print(f"{Fore.RED}Programming by DMNHACKER") # Directly using Fore.RED
print(f"{Fore.RED}Supports Soroush Plus 7.2.0 version!") # Directly using Fore.RED
print(f"{Fore.RED}Servers.....ON") # Directly using Fore.RED
print(f"{Fore.BLUE}") # Directly using Fore.BLUE
time.sleep(2.5)
print("")

# Progress animation
progress = [".........", "........", ".......", "......", ".....", "....", "...", "..", "."]
for i in progress:
    print(i)
    time.sleep(0.1)

print(f"{Fore.RED}Installed!") # Directly using Fore.RED
time.sleep(3)
print("")

# Get user input and generate the link
try:
    idta3get = input(f'{Fore.BLUE}Enter target ID without @ >>> ')
    print(f"{Fore.BLUE}")
    print(f"{random.choice(goxzarsh)}https://splus.ir/{idta3get}")

    time.sleep(5)
    print(f"{Fore.GREEN}30 gozaresh, 40 mostahjan")
    time.sleep(10.6)
except Exception as e:
    print(f"{Fore.RED}An error occurred: {e}")
