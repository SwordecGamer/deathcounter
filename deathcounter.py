import os
import keyboard

class DeathCounter:
    def __init__(self, filename='deaths.txt'):
        self.filename = filename
        self.deaths = 0
        self.load_deaths()

    def load_deaths(self):
        if os.path.exists(self.filename):
            with open(self.filename, 'r') as file:
                self.deaths = int(file.read().strip())
        else:
            self.save_deaths()

    def save_deaths(self):
        with open(self.filename, 'w') as file:
            file.write(str(self.deaths))

    def increment(self):
        self.deaths += 1
        self.save_deaths()
        print(f"Deaths: {self.deaths}")
        return self.deaths

    def reset(self):
        self.deaths = 0
        self.save_deaths()
        print(f"Deaths have been reset to {self.deaths}!")
        return self.deaths

counter = DeathCounter()

# Set up hotkeys (you can change the keys as needed)
keyboard.add_hotkey('ctrl+shift+d', counter.increment)  # Increment with CTRL + SHIFT + D
keyboard.add_hotkey('ctrl+shift+r', counter.reset)      # Reset with CTRL + SHIFT + R

print("Press Ctrl+Shift+D to increase death count, and Ctrl+Shift+R to reset.")
print("When done, press Ctrl+Shift+Q to quit the program.")
print("This program will be running in the background, so don't worry about having to ALT + TAB back to the console :)")

# Keep the program running to listen for hotkeys.
keyboard.wait('ctrl+shift+q')  # You can press 'CTRL + SHIFT + Q' to exit the script if needed.