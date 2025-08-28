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

# Sample data lists (Note: some of the original links and words may be flagged as malicious or inappropriate by some systems)
dscripts = ['https://github.com/Mrhackerha/mrhackergod/blob/main/Dxprit-mrhacker.py','https://github.com/Mrhackerha/mrhackergod/blob/main/Dxprit.py','https://github.com/Mrhackerha/mrhackergod/blob/main/Filter.py','https://github.com/Mrhackerha/mrhackergod/blob/main/Malicious-javascript.js','https://github.com/Mrhackerha/mrhackergod/blob/main/Malicious.zip','https://github.com/Mrhackerha/mrhackergod/blob/main/Mrhacker-god.cs','https://github.com/Mrhackerha/mrhackergod/blob/main/Mrhacker.json','https://github.com/Mrhackerha/mrhackergod/blob/main/Mrhackergod.cs','https://github.com/Mrhackerha/mrhackergod/blob/main/Php-malicious.php','https://github.com/Mrhackerha/mrhackergod/blob/main/Sexy.py','https://github.com/Mrhackerha/mrhackergod/blob/main/Yftt100k','https://github.com/Mrhackerha/mrhackergod/blob/main/Yftt12k.py','https://github.com/Mrhackerha/mrhackergod/blob/main/Yftt15k.py','https://github.com/Mrhackerha/mrhackergod/blob/main/index.html','https://github.com/Mrhackerha/mrhackergod/blob/main/iyftt15k.py','https://github.com/Mrhackerha/mrhackergod/blob/main/malicious%20.html','https://github.com/Mrhackerha/mrhackergod/blob/main/malicious-pdf.py','https://github.com/Mrhackerha/mrhackergod/blob/main/traport.rubika.reset.yttks58k.im009','https://github.com/Mrhackerha/mrhackergod/blob/main/yftt15k-mrhacker-dscript.py','https://github.com/Mrhackerha/mrhackergod/blob/main/yftt15k-rubika-dscript.py','https://github.com/Ytthacker/dscript-rubika','https://github.com/mr-hacker-king/DXPRIT']
linksxs = ['https://github.com/Mrhackerha/mrhackergod/blob/main/4f453f300c2fe-full-6.jpg', 'https://github.com/Mrhackerha/mrhackergod/blob/main/IMG-20220704-WA0032.jpg', 'https://github.com/Mrhackerha/mrhackergod/blob/main/IMG-20220823-WA0054.jpg', 'https://github.com/Mrhackerha/mrhackergod/blob/main/IMG_20220726_041439_396.jpg', 'https://github.com/Mrhackerha/mrhackergod/blob/main/IMG_20220825_030904_525.jpg', 'https://github.com/Mrhackerha/mrhackergod/blob/main/VID-20220712-WA0020.mp4', 'https://github.com/Mrhackerha/mrhackergod/blob/main/VID-20220712-WA0020.mp4', 'https://github.com/Mrhackerha/mrhackergod/blob/main/VID-20220712-WA0054.mp4','https://github.com/Mrhackerha/mrhackergod/blob/main/VID-20220712-WA0057.mp4','https://github.com/Mrhackerha/mrhackergod/blob/main/VID-20220824-WA0072.mp4','https://github.com/Mrhackerha/mrhackergod/blob/main/casey-kisses-grooby-girls-06.jpg','https://github.com/Mrhackerha/mrhackergod/blob/main/images%20(1)%20(3).jpeg','https://github.com/Mrhackerha/mrhackergod/blob/main/images%20(24).jpeg','https://github.com/Mrhackerha/mrhackergod/blob/main/images%20(31).jpeg','https://github.com/mr-hacker-king/DXPRIT/blob/main/photo_2019-03-06_17-26-43.jpg','https://github.com/mr-hacker-king/DXPRIT/blob/main/photo_2019-03-06_17-26-50.jpg','https://github.com/mr-hacker-king/DXPRIT/blob/main/photo_2019-03-06_17-26-55.jpg','https://github.com/mr-hacker-king/DXPRIT/blob/main/photo_2019-03-06_17-27-00.jpg','https://github.com/mr-hacker-king/DXPRIT/blob/main/photo_2019-03-06_17-27-04.jpg','https://github.com/mr-hacker-king/DXPRIT/blob/main/photo_2019-03-06_17-27-10.jpg','https://github.com/mr-hacker-king/DXPRIT/blob/main/photo_%DB%B2%DB%B0%DB%B1%DB%B6-%DB%B0%DB%B6-%DB%B0%DB%B۸_%DB%B0%DB%B۸-%DB%B0%DB%B7-%DB%B1%DB%B۲.jpg','https://github.com/mr-hacker-king/DXPRIT/blob/main/photo_%DB%B2%DB%B0%DB%B1%DB%B6-%DB%B0%DB%B6-%DB%B0%DB%B۸_%DB%B0%DB%B۸-%DB%B0%DB%B7-%DB%B2%DB%B7.jpg','https://github.com/mr-hacker-king/DXPRIT/blob/main/photo_%DB%B۲%DB%B0%DB%B1%DB%B7-%DB%B0%DB%B3-%DB%B1%DB%B0_%DB%B2%DB%B3-%DB%B5%DB%B3-%DB%B2%DB%B1.jpg','https://github.com/mr-hacker-king/DXPRIT/blob/main/photo_%DB%B2%DB%B0%DB%B1%DB%B7-%DB%B0%DB%B5-%DB%B1%DB%B2_%DB%B1%DB%B0-%DB%B5%DB%B9-%DB%B4%DB%B3.jpg','https://github.com/mr-hacker-king/DXPRIT/blob/main/photo_%DB%B۲%DB%B0%DB%B1%DB%B7-%DB%B0%DB%B8-%DB%B0%DB%B6_%DB%B2%DB%B1-%DB%B1%DB%B4-%DB%B1%DB%B5.jpg','https://github.com/mr-hacker-king/DXPRIT/blob/main/photo_%DB%B۲%DB%B0%DB%B1%DB%B8-%DB%B0%DB%B1-%DB%B2%DB%B7_%DB%B1%DB%B4-%DB%B4%DB%B8-%DB%B2%DB%B5.jpg','https://github.com/mr-hacker-king/DXPRIT/blob/main/photo_%DB%B۲%DB%B0%DB%B1%DB%B8-%DB%B0%DB%B1-%DB%B2%DB%B7_%DB%B1%DB%B4-%DB%B4%DB%B8-%DB%B4%DB%B7.jpg','https://github.com/mr-hacker-king/DXPRIT/blob/main/photo_%DB%B۲%DB%B0%DB%B1%DB%B8-%DB%B0%DB%B2-%DB%B1%DB%B9_%DB%B1%DB%B7-%DB%B1%DB%B0-%DB%B2%DB%B7.jpg','https://github.com/mr-hacker-king/DXPRIT/blob/main/photo_%DB%B۲%DB%B0%DB%B1%DB%B8-%DB%B0%DB%B۲-%DB%B2%DB%B1_%DB%B2%DB%B1-%DB%B1%DB%B8-%DB%B0%DB%B۰.jpg','https://github.com/mr-hacker-king/DXPRIT/blob/main/photo_%DB%B۲%DB%B۰%DB%B1%DB%B8-%DB%B0%DB%B۴-%DB%B۰%DB%B1_%DB%B1%DB%B8-%DB%B5%DB%B9-%DB%B۰%DB%B۰.jpg','https://github.com/mr-hacker-king/DXPRIT/blob/main/photo_%DB%B۲%DB%B۰%DB%B1%DB%B۸-%DB%B0%DB%B7-%DB%B۰%DB%B۸_%DB%B1%DB%B1-%DB%B۴%DB%B۶-%DB%B1%DB%B۸.jpg','https://github.com/mr-hacker-king/DXPRIT/blob/main/photo_%DB%B۲%DB%B۰%DB%B1%DB%B۸-%DB%B0%DB%B۸-%DB%B0%DB%B۲_%DB%B2%DB%B3-%DB%B۰%DB%B۱-%DB%B۴%DB%B۶.jpg','https://github.com/mr-hacker-king/DXPRIT/blob/main/photo_%DB%B۲%DB%B۰%DB%B1%DB%B۸-%DB%B۰%DB%B۸-%DB%B۰%DB%B۳_%DB%B0%DB%B3-%DB%B2%DB%B۸-%DB%B1%DB%B۴.jpg','https://github.com/mr-hacker-king/DXPRIT/blob/main/photo_%DB%B۲%DB%B۰%DB%B1%DB%B۸-%DB%B۰%DB%B۸-%DB%B1%DB%B۹_%DB%B1%DB%B5-%DB%B3%DB%B6-%DB%B2%DB%B۸.jpg']
num = ['0','1','2','3','4','5','6','7','8','9','10']
bug_num = ['05','13','62','63','49','l5','64','67','38','39','46','87','4','56','568','795','368','85','658','254','345','775','355','754','447','745','357']
letter = ['a','f','e','n','h','x','u','t','w','m','z']
slashes = ['/', '//', '///']
letterhss = ['sex','xxx','porn','spam','hack','fil','filter',' scamming-users',' violent-content','threaten','intimidate','harass-users','Violation-of-Islamic','fuck-Islamic-Republic','pornhub','fuck-rubika','Malicious-link',]
adad_hasas = 'https://'+random.choice(bug_num)+'.'+random.choice(bug_num)+'.'+random.choice(bug_num)+'.'+random.choice(bug_num)+''+random.choice(slashes)+''+random.choice(letter)+''+random.choice(slashes)+''+random.choice(letter)+''+random.choice(slashes)+''+random.choice(num)+'.'+random.choice(num)+'.'+random.choice(num)+'.'+random.choice(num)+'.'+random.choice(num)+'.'+random.choice(num)+'.'+random.choice(num)+'.'+random.choice(num)+'.'+random.choice(num)+'.'+random.choice(num)+'.'+random.choice(num)+'.'+random.choice(num)+'.'+random.choice(num)+'.'+random.choice(num)+'.'+random.choice(num)+'.'+random.choice(num)+'.'+random.choice(num)+'.'+random.choice(num)+'.'+random.choice(num)+'.'+random.choice(num)+'.'+random.choice(num)+'.'+random.choice(num)+'.'+random.choice(num)+'.'+random.choice(bug_num)+'' # Fixed last element to use bug_num for consistency
bug = 'https://'+random.choice(bug_num)+'.'+random.choice(bug_num)+'.'+random.choice(bug_num)+'.'+random.choice(bug_num)+'/'+random.choice(letter)+'//'+random.choice(letter)+'/'+random.choice(letter)+'/'+random.choice(bug_num)+'.'+random.choice(bug_num)+'.'+random.choice(bug_num)+'.'+random.choice(bug_num)+'.'+random.choice(bug_num)+'.'+random.choice(bug_num)+'.'+random.choice(bug_num)+'.'+random.choice(bug_num)+'.'+random.choice(bug_num)+'.'+random.choice(bug_num)+'.'+random.choice(bug_num)+'.'+random.choice(bug_num)+'.'+random.choice(bug_num)+'.'+random.choice(bug_num)+'.'+random.choice(bug_num)+'.'+random.choice(bug_num)+'/)\''
ltterhss = random.choice(letterhss)+'.'+random.choice(letterhss)+'.'+random.choice(letterhss)+'.'+random.choice(letterhss)
codereal = bug+ltterhss+' '+random.choice(dscripts)+' '+random.choice(linksxs)

# Print banner with colorama
# With autoreset=True, there's no need to manually reset at the end of lines; colors reset automatically.
print(green)
print(f" ")
print (white)
print(blue)
print ("    ")
print (yellow)
print(pink)
x = f"""
█▀▀ █▀█ █▀▄ █▀▀   █▀▀ █ █░░ ▀█▀ █▀▀ █▀█   █▀█ █░█ █▄▄ █ █▄▀ ▄▀█
█▄▄ █▄█ █▄▀ ██▄   █▀░ █ █▄▄ ░█░ ██▄ █▀▄   █▀▄ █▄█ █▄█ █ █░█ █▀█ v1.1
"""
for c in x:
    sys.stdout.write(c)
    sys.stdout.flush()
    time.sleep(0.0000001)

# Display current time
print(green + str(datetime.datetime.now()))
print(red)
time.sleep(1)

# Display welcome messages
print(green + "Welcome ")
print(yellow)
time.sleep(0.1)
print(light_green + " Programming by DMNHACKER     ")
print(blue + "Supports Rubika v3.11 ")
print(red + " Servers.....ON     ")
print(white + '\n' + light_blue)
print(blue)
time.sleep(2.5)
print("")

# Progress animation
progress = [".........", "........", ".......", "......", ".....", "....", "...", "..", "."]
for i in range(len(progress)):
    print(progress[i])
    time.sleep(0.1 + i * 0.05)
print(light_yellow + "Installed!")
time.sleep(3)
print("")

# Corrected input line with a closing parenthesis
try:
    get = int(input(blue + "Enter 1 for new code >>> "))
    if get == 1:
        print(blue + codereal)
        time.sleep(5)
        print('20 general, 30 obscene')
        time.sleep(1)

    time.sleep(0.6)
    exit1 = input(green + "Press Enter to go back >>> ")
    print('OK')
    time.sleep(2)
    clear()
    time.sleep(2)
except ValueError:
    print(red + "Invalid input. Please enter a number.")
except NameError:
    # Handle the case where 'system' is not defined. The original code had `system("clear")` which is not a standard Python function.
    # The `clear()` function I've defined at the top handles this.
    print(red + "An error occurred. Please check the script.")
    exit()
