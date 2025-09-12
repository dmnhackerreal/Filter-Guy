import random
import sys
from subprocess import call
from sys import platform
import time
from colorama import Fore, Style, init

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

# Define color codes for better readability
red = Fore.RED
green = Fore.GREEN
blue = Fore.CYAN  # Using CYAN for a distinct blue color
pink = Fore.MAGENTA
bold = Style.BRIGHT
reset = Style.RESET_ALL # With autoreset, direct use of this is often not needed, but kept for clarity.

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

flxtxr = [
    'xxx.eitaa.com.32',
    'fuck.irgc.ir.islam.eitta.com',
    '1010.eitaa.hack',
    'eitaa.phishing',
    'eitaa.porn',
    'eitaa.co/hack',
    'eitaa.ir/fuckkhamenei',
    'eitaa.ir/xxx/ddd',
    'eitaa.com/11/32/4/craddd',
    'eitaa.virus/2edf4',
    'eitaa.ru/selldrugs',
    'fuck.eitaa.com',
    'eitaa.xxx/filtering',
    'blodeitaa.com',
    'eitaa.dxdx/main',
    'web.eitaaa.com',
    'web.eitaaaa.com',
    'web.realeitaa.co',
    'web.eitaa.xxx',
    'web.eitaa.hack' ]

# Print banner with colorama and a slight delay for dramatic effect
# With autoreset, there's no need to manually reset at the end of lines, but Fore.MAGENTA will be applied automatically.
print(pink)
x = f"""
█▀▀ █▀█ █▀▄ █▀▀  █▀▄▀█ ▄▀█ █▄▀ █▀▀ █▀█  █▀▀ █ █░░ ▀█▀ █▀▀ █▀█ █  █▀▀ █ ▀█▀ ▄▀█ ▄▀█
█▄▄ █▄█ █▄▀ ██▄  █░▀░█ █▀█ █░█ ██▄ █▀▄  █▀░ █ █▄▄ ░█░ ██▄ █▀▄ █  ██▄ █ ░█░ █▀█ █▀█ v1.1
"""
for c in x:
    sys.stdout.write(c)
    sys.stdout.flush()
    time.sleep(0.0000001)

# Display welcome messages
# With autoreset, there's no need for Style.RESET_ALL at the beginning of new lines.
# 'reset' is now only used for explicit resets, but usually handled by autoreset.
time.sleep(1)
print(f"{bold}{red}programming by DMNHACKER")
print(f"{red}supports eitaa 6.6.10 version!")
print(f"{red}servers...............ON")

# Progress animation
print(f"{blue}")
time.sleep(2.5)
print("")
progress = [".........", "........", ".......", "......", ".....", "....", "...", "..", "."]
for i in progress:
    print(i)
    time.sleep(0.1)

print(f"{bold}{red}installed!")
time.sleep(3)
print("")

# Get user input and generate the link
try:
    idta4get = input(f'{blue}Enter target channel ID without @ >>> ')
    oppsz = idta4get+')'
    print(f"{blue}")
    print(f"{random.choice(flxtxr)}{random.choice(govxzarsh)}(https://eitaa.com/{oppsz}")
    print(f"{green}30 general, 40 obscene") 
    time.sleep(5)
    time.sleep(10.6)
except Exception as e:
    print(f"{red}An error occurred: {e}") # autoreset handles reset
