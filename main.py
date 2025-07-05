from colorama import Fore, init
import ctypes, pyautogui, keyboard, os, time, platform
from datetime import datetime
from pystyle import Colors, Colorate

init(autoreset=True)

ascii_text = Fore.YELLOW + """
⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⣤⣶⣶⣶⣶⣤⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢀⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⡀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀
⠀⠀⠀⢀⣀⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⣀⡀⠀⠀⠀
⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀    
⠀⠀⠀⠈⠙⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⠋⠁⠀⠀⠀
⠀⠀⠀⣀⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⣀⠀⠀⠀
⢠⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⡄
⠘⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠃
⠀⠀⠉⠉⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠉⠉⠀⠀
⠀⠀⠀⠀⠈⠛⠛⠋⠙⠿⣿⣿⣿⣿⣿⣿⠿⠋⠙⠛⠛⠁⠀⠀⠀
"""

dedi = (Colorate.Horizontal(Colors.green_to_black, "SnapScore boost by virexpy"))

def on_linux():
    return platform.system() == "Linux"

class Snapchat:

    def __init__(self):
        self.snaps_sent = 0
        self.delay = 0.3
        self.start_time = None

    def capture_positions(self):
        self.log("Place your mouse over *camera* and press G")
        self.button_camera = self.wait_for_g()

        self.log("Place your mouse over *take photo* and press G")
        self.button_photo = self.wait_for_g()

        self.log("Place your mouse over *send to* and press G")
        self.button_send_to = self.wait_for_g()

        self.log("Place your mouse over your *shortcut* and press G")
        self.shortcut = self.wait_for_g()

        self.log("Place your mouse over *select all* and press G")
        self.button_select_all = self.wait_for_g()

        self.log("Place your mouse over *send snap* and press G")
        self.button_send_snap = self.wait_for_g()

    def wait_for_g(self):
        while True:
            if keyboard.is_pressed("G"):
                pos = pyautogui.position()
                time.sleep(0.5)
                return pos

    def send_snap(self, num_people):
        self.update_title(num_people)
        pyautogui.moveTo(self.button_camera)
        pyautogui.click()
        time.sleep(self.delay)

        pyautogui.moveTo(self.button_photo)
        pyautogui.click()
        time.sleep(self.delay)

        pyautogui.moveTo(self.button_send_to)
        pyautogui.click()
        time.sleep(self.delay)

        pyautogui.moveTo(self.shortcut)
        pyautogui.click()
        time.sleep(self.delay)

        pyautogui.moveTo(self.button_select_all)
        pyautogui.click()
        time.sleep(self.delay)

        pyautogui.moveTo(self.button_send_snap)
        pyautogui.click()

        self.snaps_sent += 1
        self.update_title(num_people)

    def update_title(self, num_people):
        now = time.time()
        elapsed = str(now - self.start_time).split(".")[0]
        total = self.snaps_sent * num_people
        if not on_linux():
            ctypes.windll.kernel32.SetConsoleTitleW(
                f"SnapScore boost | Snaps sent: {total} | Time: {elapsed}s | Dev: virexpy"
            )

    def log(self, txt):
        print(f"{Fore.BLUE}\n[{Fore.MAGENTA}Console{Fore.BLUE}] {txt}")

    def run(self):
        os.system("cls" if not on_linux() else "clear")
        print(ascii_text)
        print(dedi)
        self.capture_positions()

        while True:
            try:
                num_people = int(input(f"\n       {Fore.CYAN}[{Fore.MAGENTA}Console{Fore.CYAN}] How many people in the shortcut? "))
                break
            except ValueError:
                self.log("Error, enter a real number")

        self.log("Slow PC = press 1")
        self.log("Fast PC = press 2")
        choice = input(f"\n       {Fore.CYAN}[{Fore.MAGENTA}Console{Fore.CYAN}] Your choice: ")
        if choice == "1":
            self.delay = 2

        self.log("Go to the chats and press G when ready")
        while not keyboard.is_pressed("G"):
            pass

        os.system("cls" if not on_linux() else "clear")
        print(ascii_text)
        self.log("Sending...")
        self.start_time = time.time()

        while not keyboard.is_pressed("F4"):
            self.send_snap(num_people)
            time.sleep(4)

        self.log(f"Finished sending {self.snaps_sent} snaps")

bot = Snapchat()
bot.run()
