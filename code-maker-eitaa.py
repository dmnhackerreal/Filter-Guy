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
govxzarsh = [
    'This-channel-promotes-suicide',
    'This-channel-promotes-violent-scenes',
    'This-channel-promotes-self-abuse-and-other-abuse',
    'This-channel-is-spamming',
    'This-channel-promotes-hacking',
    'This-channel-is-scamming',
    'This-channel-posts-inappropriate-ads',
    'This-channel-posts-videos-about-womens-dance',
    'This channel is insulting',
    'This channel-is-obscene',
    'This-channel-promotes-breaking-norms',
    'This-channel-promotes-nudity',
    'This-channel-is-about-sexual-relations',
    'This-channel-promotes-erotic-scenes',
    'This-channel-insults-Islamic-affairs',
    'This-channel-insults-the-IRGC',
    'This-channel-curses-the-mobilization-of-the-oppressed',
    'This-channel-is-an-anti-Islamic-revolution',
    'This-channel-curses-Imam-Khomeini-and-Khamenei',
    'This-channel-has-an-inappropriate-profile'
]

# Print banner with colorama and a slight delay for dramatic effect
print(pink)
x = f"""
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣤⣠⣤⣠⣄⣤⣠⣤⣠⣤⣠⣤⣀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣴⣾⡿⢛⠭⠿⣛⣛⣭⣭⣭⣟⣋⣩⣉⠉⠉⠉⠉⠉⠉⠉⠉⢈⣭⡭⠭⣥⠭⢥⣥⣉⣈⠭⠙⣿⣿⣶⣶⣄⡀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⢀⣾⣿⢫⡮⣔⠡⠚⢛⣋⣩⣭⣍⣙⡛⢻⠿⣖⡬⣭⠿⠷⣶⣷⣿⣿⣵⢴⣟⡿⢿⣿⣶⣠⡩⣗⠨⡁⢌⠙⡿⢿⣿⣿⣦⡀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⢰⣿⣿⡱⣷⢾⣖⣴⣭⣷⣿⣿⣿⣷⣿⣿⣿⣯⣛⢿⣯⣷⣫⣭⣿⣽⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣽⣮⡌⣿⡆⣳⣿⣿⣿⣷⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢠⣿⣿⣿⢏⣾⣿⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣭⣶⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣮⣧⣜⣿⡿⣿⣿⡇⠀⠀⠀⠀
⠀⠀⠀⠀⠀⢠⣾⣿⣛⣿⢮⣷⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣽⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣽⣿⣿⣼⣧⣿⣿⣧⠀⠀⠀⠀
⠀⠀⠀⠀⣠⣿⣿⣾⣯⢡⡏⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢿⣿⣿⣿⣿⣧⠀⠀⠀
⠀⠀⣠⣾⣿⢟⡭⢊⣝⣹⣾⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠏⠿⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣾⣿⣭⢿⡿⣿⣇⠀⠀
⠀⣰⣿⣽⠗⣽⣲⣿⣖⣬⣉⣉⡹⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠿⣿⢁⠀⠀⠈⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠿⠓⡋⢉⣉⣉⡁⠊⠻⡻⣮⢻⡆⠀
⢠⣿⣿⡏⣼⡿⣟⣽⣿⣿⣿⣶⣿⣦⣙⠯⣿⣿⠿⢿⣿⣿⣿⣿⢁⣀⠸⠀⠀⠀⠀⠀⢛⠋⢀⣈⢻⡿⣿⣟⣛⡿⠟⢁⣠⣶⣯⣷⣿⣿⣿⣿⣷⣄⠙⡝⡞⣿⠀
⢸⣿⢻⢸⣿⣴⣿⣿⣿⣿⣿⣿⣿⢿⣿⣷⣦⣜⣯⣛⣹⣞⣿⣙⡦⢿⣷⣄⡀⠀⠀⠀⠘⣾⣿⠟⣘⣭⣿⣷⣶⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⡏⣿⣿⣧⠘⣾⣽⡆
⢸⣿⣬⢾⡿⣻⢻⣿⣿⣿⣿⣷⣤⣽⣉⠟⡟⡙⠟⣿⢿⣿⣿⣿⣿⣿⣿⣷⣮⣀⣒⣢⣾⣿⣿⣿⣿⡿⣿⠛⠙⡟⡟⢹⣹⣠⣿⣷⣾⣿⣿⡇⣿⣿⢻⡄⢉⣿⡇
⠀⢿⣿⡘⣷⣿⣸⣷⣿⣷⣿⣿⣿⢤⣭⣖⢧⣇⢰⠁⠈⡝⠐⠸⣿⡿⠋⠹⠘⢻⣿⠯⠁⠈⠻⡏⠁⠀⠁⡆⠀⡇⢰⣴⣟⡗⢯⣿⣿⣿⣿⡇⣿⡟⣾⡇⢸⣼⡇
⠀⠈⢿⣷⠈⢿⡏⣿⣿⣿⣿⣿⣾⣘⡫⡏⡟⣿⣿⣦⣰⡅⠀⠀⡇⠀⠀⠀⠀⠀⡃⠀⠀⠀⠀⡅⠀⠀⠀⡇⣀⣼⡿⣿⣮⣿⣿⣿⣿⣿⣿⣇⣿⣿⣿⢃⣶⡿⠀
⠀⠀⠈⠻⣷⣌⣾⢾⢿⣿⣿⣿⣿⣿⣿⣿⣷⣿⣡⡋⠟⣷⣤⣴⣧⣤⣤⣤⣤⣴⣧⣦⣶⣶⣶⡿⣾⣿⣿⢿⣿⣾⣿⣾⡿⣿⣿⣽⣿⣿⣿⢹⣿⣿⠏⡝⢨⠇⠀
⠀⠀⠀⠀⠈⣿⣿⣿⣹⢿⣿⣿⣿⣿⣏⡱⣿⣿⣿⣿⣿⣏⣿⣸⣿⣹⣸⣹⣿⣸⣿⣏⣹⣷⡿⣇⣿⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠇⣿⡿⠁⣸⢀⡏⠀⠀
⠀⠀⠀⠀⠀⠈⠻⣿⣿⣗⢬⡛⢿⢿⣿⣿⣿⣿⣿⣾⣏⡿⣿⣿⣾⣿⣿⣿⣷⣿⣿⣿⣿⣿⣿⣿⣿⣿⢿⣿⣟⣿⣿⣿⢿⣽⣿⣿⣿⣥⡾⢋⣥⣾⣷⠋⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠙⢿⣿⡛⠯⣷⣭⡻⣟⣿⣿⣿⣿⣿⣿⣿⣿⣽⠿⣿⣿⣿⡿⣿⣿⡿⣿⣿⡿⣟⢯⣏⣶⢿⢿⢏⣿⣿⣿⡿⡿⣻⣿⣷⣿⣿⠟⠁⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠻⣿⡦⡌⢷⣝⣯⣷⡝⢿⡿⣿⣾⣿⢿⣿⣿⣾⣹⣣⢏⣽⠹⣹⣘⣹⢠⣿⣾⣿⢃⣮⣾⣿⠟⠛⡩⢎⣼⣿⣿⣿⡿⠃⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠹⣿⣮⣊⠻⣷⣽⣳⡈⢿⣯⢻⠿⢿⠿⣿⣿⣿⣿⣿⣿⡿⣿⣿⣿⠿⢿⠿⠟⡿⡟⣳⢃⡴⠋⣠⢾⣿⣿⣿⠟⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⣿⣿⣦⡙⢳⣿⢧⠈⢿⣿⣄⢸⡄⢸⡄⠀⠀⠀⠞⠀⠀⠀⢸⠀⢸⠀⣤⣣⡵⠣⠀⣠⡞⢡⣾⣿⣿⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⣿⣿⣎⢳⡜⢿⣧⠈⢿⣿⣾⣧⢸⡇⠀⠀⢠⣯⣄⠀⠀⣸⢀⣾⣴⣿⡟⣡⢁⣾⠏⣴⣿⣿⡿⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⣿⣿⡆⠰⠀⡹⡆⠈⢿⣿⣿⣾⣿⣇⣰⣿⣿⣾⣶⣷⣿⣿⣿⣿⡟⣰⢃⡼⠃⣾⣽⣿⠟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠻⣿⣄⠑⡘⣷⣄⠈⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⢠⣯⠟⢁⣼⢿⣿⠏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⢿⣇⠀⠈⣿⢷⣀⠙⠿⢿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠛⡵⣫⡿⢀⣾⢯⣾⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠻⣦⡄⠐⠷⡙⢦⣀⠀⠈⠉⠉⠀⠀⣀⣀⣀⡤⠚⢱⡿⠁⣾⢣⣿⡿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠹⣿⣆⠀⠀⠀⠬⣭⣭⣉⣭⣭⣤⣤⣴⣥⡤⠊⠉⠀⡾⣡⣿⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢿⣦⠀⠀⠒⠿⠿⢿⣿⣿⠿⠿⠟⠋⠀⠀⠀⣸⣿⣿⠟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠹⣷⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣼⣿⠟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠛⢦⣀⣀⠀⠀⠀⠀⠀⢀⣀⣴⡿⠟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠛⠻⠿⠿⠛⠛⠋⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀

█▀▀ █▀█ █▀▄ █▀▀   █▀▄▀█ ▄▀█ █▄▀ █▀▀ █▀█   █▀▀ █ █░░ ▀█▀ █▀▀ █▀█ █   █▀▀ █ ▀█▀ ▄▀█ ▄▀█
█▄▄ █▄█ █▄▀ ██▄   █░▀░█ █▀█ █░█ ██▄ █▀▄   █▀░ █ █▄▄ ░█░ ██▄ █▀▄ █   ██▄ █ ░█░ █▀█ █▀█ v1.0
"""
for c in x:
    sys.stdout.write(c)
    sys.stdout.flush()
    time.sleep(0.0000001)

# Display welcome messages
print(reset)
time.sleep(1)
print(f"{bold}{red}programing by DMNHACKER")
print(f"{red}supports eitaa 6.4.14.0 version!   just for")
print(f"{red}servers...............ON           just for channel.")

# Progress animation
print(f"{blue}")
time.sleep(2.5)
print("")
progress = [".........", "........", ".......", "......", ".....", "....", "...", "..", "."]
for i in progress:
    print(i)
    time.sleep(0.1)

print(f"{bold}{red}installed!{reset}")
time.sleep(3)
print("")

# Get user input and generate the link
try:
    idta4get = input(f'{blue}id target channel ro bedoon @ vared con >>> {reset}')
    print(f"{blue}")
    print(f"{random.choice(govxzarsh)}https://eitaa.com/{idta4get}")
    print(f"{reset}")

    time.sleep(5)
    print(f"{green}30 sayer 40 mostahjan{reset}")
    time.sleep(10.6)
except Exception as e:
    print(f"{red}An error occurred: {e}{reset}")

