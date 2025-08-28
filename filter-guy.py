import sys
from subprocess import call, run
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
        print(f"{Fore.RED}Error clearing screen: {type(e).__name__}, {e}")

# Define color codes for better readability
red = Fore.RED
green = Fore.GREEN
blue = Fore.CYAN  # Using CYAN for a distinct blue color
pink = Fore.MAGENTA
bold = Style.BRIGHT
yellow = Fore.YELLOW
white = Fore.WHITE

# Banner for Filter Guy - Corrected to "FILTER GUY" and added "Programmed by DMNHACKER"
banner = f"""
{pink}{bold}
⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⠖⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡀⠤⠀⠀⠠⠄⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢶⠐⠲⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⡀⠀⠀⣰⠟⠁⠀⠀⠀⠀⠀⠀⠀⠀⢀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠑⠄⣀⠀⠀⠀⠀⠀⠀⠘⠷⠁⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠁⠀⠀⠁⠀⠀⠀⠀⠀⢀⠤⠒⠈⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠁⠂⢄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⡰⠀⠀⠀⠀⠀⡠⠊⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠒⢄⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⠜⠀⠀⠀⠀⠀⠀⠀⠀⣠⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠢⣀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⣰⠎⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠰⡀⠀⠀⠀
⠀⠀⠀⠀⠀⡴⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠀⠀⠀⠀⠉⢐⡆⠀
⠀⠀⠀⠀⢠⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠞⠀⠀⠀⠀⠀⢸⠃⠀
⢀⡠⠤⡄⠈⣇⠀⠀⠀⠀⠀⠀⠀⡄⠀⠀⠀⠀⣀⢠⠀⠀⠀⠀⠀⠀⠀⢀⣠⢀⠀⠀⠀⠀⢀⣾⡞⠀⠀⠀⠀⠀⠀⡸⠀⢀
⠹⡄⠀⠘⡀⠘⢧⣆⡴⣠⢆⠶⡹⣜⢳⡜⣦⠻⣌⠳⣯⣓⢶⣰⢢⡔⣮⢿⡐⢏⡞⢶⢦⠷⡛⡞⣧⣔⣤⠀⠀⢀⠜⠁⡠⠂
⠀⠰⠀⢀⠁⠀⠀⠈⠙⠳⢮⣏⡵⣌⢶⣹⡶⣽⣬⣷⣧⣿⣾⣧⣿⣽⣾⣷⣿⣎⣾⣧⣞⣧⡱⣜⣹⣿⡷⢤⡎⡡⠄⠂⠁⠀
⠀⠀⠡⠰⠀⠀⠀⣤⡒⠐⠄⡈⠙⠋⠋⠁⠀⠀⣠⣾⣿⣿⣿⣿⣿⣻⣷⣿⡿⣿⣿⣧⡀⠈⠙⠋⠉⠁⠀⠀⠉⠑⠒⠠⠤⠂
⠀⠀⠀⠀⠀⠀⠀⠈⢷⡀⠀⠑⡄⠀⠀⠀⠀⢸⣿⣧⣯⣘⣤⣤⣼⣯⣭⣭⣥⣽⣬⣷⡹⠀⢀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⣀⣀⡙⠒⢈⣴⣿⣶⠔⠒⢮⣉⣉⣿⣿⢿⣿⣿⣿⣿⣿⣿⣿⠙⣉⣠⣴⣿⡿⢶⣯⣵⡂⢀⣄⡀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⣠⣿⣷⣿⡽⠋⢻⡿⠁⠀⠀⠀⠙⠛⠉⠷⣦⣼⣏⣙⡿⣥⣤⠟⠋⠀⠉⠀⠈⠁⠀⠙⠻⣿⣿⠷⠿⣿⠀⠀
⠀⠀⠀⠀⢸⡏⠉⠀⠈⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⠋⠈⠋⠀⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠁⠀⠀⠈⢺⠃
⠀⠀⠀⠀⠀⣇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣰⣀⣀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣀⣀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡎⠀
⠀⠀⠀⠀⠀⢸⠀⠀⠀⠀⠀⠀⠀⠀⣠⣾⣿⣿⣿⣿⣿⣷⣄⠀⠀⠀⠀⣴⣿⣿⣿⣿⣿⣷⣦⡀⠀⠀⠀⠀⠀⠀⠀⢸⠁⠀
⠀⠀⠀⠀⠀⠀⡇⠀⠀⠀⠀⠀⢀⣸⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⣸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣄⠀⠀⠀⠀⠀⠀⡞⠀⠀
⠀⠀⠀⠀⠀⠀⠘⡄⠀⠀⡄⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⢹⣿⣿⣿⣿⣿⣿⣿⣿⣿⡏⠀⠀⠀⠀⠀⡰⠁⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠱⠀⢰⢸⠀⠀⢹⡿⣹⢎⡷⢯⣿⣿⣿⠏⠀⠀⠀⠈⢿⣿⣿⠿⣝⢮⢳⢏⣿⠃⠀⠀⢠⠀⢠⠁⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠱⣘⢸⠀⠀⠀⠻⣗⣮⡝⣯⣾⡿⠋⠀⠀⢀⡀⠀⠀⠙⢿⣿⡹⣎⣷⡻⠋⠀⠀⠀⠘⢠⠊⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⢾⡀⠀⠀⠀⠈⠉⠉⠉⠁⠀⠀⢀⣾⣿⣿⣦⡀⠀⠀⠉⠉⠉⠉⠀⠀⠀⠀⢸⡰⠃⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠳⢤⣀⡀⠀⠀⠀⠀⠀⠀⠀⠈⠛⠉⠙⠛⠀⠀⠀⠀⠀⠀⠀⠀⣀⣠⠴⠊⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠉⣷⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡟⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣀⣼⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠠⣏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠨⠀⠈⣽⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠶⠰⠆⠰⠇⠀⠸⠆⠀⠷⠰⠸⠰⠎⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⡎⢂⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠎⢱⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⣇⠈⠂⢀⡀⠀⠀⠀⠀⢀⠀⠊⠀⡼⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⢶⡀⢀⠃⠀⠠⠀⠀⡄⠀⣠⡞⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠫⠭⢒⢋⣓⠋⠩⠙⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀



█▀▀ █ █░░ ▀█▀ █▀▀ █▀█   █▀▀ █░█ █▄█
█▀░ █ █▄▄ ░█░ ██▄ █▀▄   █▄█ █▄█ ░█░ {white}v1.1
{yellow}Programmed by DMNHACKER{red}
"""

def main_menu():
    while True:
        clear()
        print(banner)
        print(f"{green}Programming by DMNHACKER") # This line was redundant due to the banner change, but kept as per user request context.
        print(f"{yellow}Filter-Guy v1.1\n") # This line was redundant due to the banner change, but kept as per user request context.

        print(f"{blue}Please select one of the following options:{white}")
        print(f"1. Code filter for Eitaa (code-maker-eitaa.py)")
        print(f"2. Code filter for Rubika (code-maker-rubika.py)")
        print(f"3. Code filter for Soroush Plus (code-maker-splus.py)")
        print(f"4. Exit")

        try:
            choice = input(f"\n{yellow}Enter option number >>> {white}")
            choice = int(choice)

            if choice == 1:
                print(f"{green}Executing Eitaa filter...")
                # Ensure the script is executable and in the same directory, or provide full path
                run_script('code-maker-eitaa.py')
            elif choice == 2:
                print(f"{green}Executing Rubika filter...")
                run_script('code-maker-rubika.py')
            elif choice == 3:
                print(f"{green}Executing Soroush Plus filter...")
                run_script('code-maker-splus.py')
            elif choice == 4:
                print(f"{red}Exiting program. Goodbye!")
                time.sleep(1)
                sys.exit()
            else:
                print(f"{red}Invalid input. Please enter a number between 1 and 4.")
            time.sleep(2) # Give user time to read messages before clearing
        except ValueError:
            print(f"{red}Invalid input. Please enter a number.")
            time.sleep(2)
        except FileNotFoundError as e:
            print(f"{red}Error: Script file not found: {e}. Make sure the files are in the same directory.")
            time.sleep(3)
        except Exception as e:
            print(f"{red}An error occurred: {e}")
            time.sleep(3)

def run_script(script_name):
    """
    Executes the specified Python script.
    Uses sys.executable to ensure the script is run with the current Python interpreter.
    """
    try:
        # Pass the full path to the Python interpreter and then the script name
        # Using sys.executable ensures the script is run with the same Python interpreter that is running this main script.
        # check=True will raise CalledProcessError if the script exits with a non-zero status.
        run([sys.executable, script_name], check=True)
        print(f"{green}Execution of {script_name} finished. Returning to main menu.")
    except FileNotFoundError:
        print(f"{Fore.RED}Error: File '{script_name}' not found. Please ensure the script is in the correct path.")
    except Exception as e:
        print(f"{Fore.RED}Error executing script '{script_name}': {e}")
    time.sleep(2)


if __name__ == "__main__":
    main_menu()
