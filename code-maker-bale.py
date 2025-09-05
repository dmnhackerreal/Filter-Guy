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
    'This-account-is-writing-spam',
    'This-account-is-blasphemous',
    'This-account-bale-creates-content-that-violates-the-laws-of-the-Islamic-Republic-of-Iran',
    'This-account-insults-people-and-ethnicities',
    'This-account-posts-content-that-includes-nudity-and-sexual-content',
    'This-account-posts-content-that-includes-violence-and-bloodshed',
    'This-account-posts-content-that-includes-alcohol-and-drug-content',
    'This-account-bale-trades-prohibited-goods-and-any-illegal-buying-and-selling',
    'This-account-sells-drugs-and-alcoholic-beverages',
    'This-account-is-engaged-in-human-trafficking-gambling-child-abuse-and-pornography',
    'This-bale-account-sends-phishing-scam-links',
    'This-bale-account-publishes-pictures-and-messages-from-customers-without-permission',
]


serversxs = [
    'bale.ir/phishingxxx',
    'web.balle.ir/login',
    'bbale.com/login',
    'bale.ir/fil/acc',
    'bale.xxx/login',
    'bale.xosewo',
    'blle.com/eewwe',
    'ble.yt/w',
    'vvblw.ir/bale.ir',
    'bale.ytf/log',
    'bale.blog.co',
    'realbale.ai/log',
]

bugz = [
    'h/tr/453/4252',
    'h/hyjuy/6y/636/576/567',
    'xsxs.903.4549094',
    'xsd.433435',
    'cw4565/565/565',
    'hy65/6557676/6',
    'y56tt4th/h786/85',
    '78.5879.578.787.876',
    '34.4566jyu5335.355',
    'flre.pble.32345.345',
    'fckble.ir.9340543',
    'fr45.tg45.bale.ai.t5342',
]







# Print banner with colorama and a slight delay for dramatic effect
# With autoreset=True, there's no need to manually reset at the end of lines; colors reset automatically.
print(red)
x = f"""⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
█▀▀ █▀█ █▀▄ █▀▀   █▀▄▀█ ▄▀█ █▄▀ █▀▀ █▀█   █▄▄ ▄▀█ █░░ █▀▀
█▄▄ █▄█ █▄▀ ██▄   █░▀░█ █▀█ █░█ ██▄ █▀▄   █▄█ █▀█ █▄▄ ██▄ V1.0
"""
for c in x:
    sys.stdout.write(c)
    sys.stdout.flush()
    time.sleep(0.0000001)

# Display welcome messages
# The 'reset' is now redundant due to autoreset=True, but can be kept if desired for explicit resets.
time.sleep(1)
print(f"{Fore.RED}Programming by DMNHACKER") # Directly using Fore.RED
print(f"{Fore.RED}Supports Bale 9.92.39 version!") # Directly using Fore.RED
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
    print(f"{random.choice(goxzarsh)}{random.choice(serversxs)}{random.choice(bugz)}https://ble.ir/{idta3get}")

    time.sleep(5)
    print(f"{Fore.GREEN}30 gozaresh, 40 mostahjan")
    time.sleep(10.6)
except Exception as e:
    print(f"{Fore.RED}An error occurred: {e}")
