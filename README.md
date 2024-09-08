# DeathCounter
A simple deathcounter, usable on streams and recordings.

# How obtain the files
Just click the download button.
A .zip file containing the files is then being downloaded.
Extract the .zip file to your desktop or something, and you're ready to go!

# How to run the program
There are 2 ways to start the program:
1. In the 'dist' directory is an .exe file. simply open the .exe file and the program is activated. Feel free to copy the .exe to anywhere you want!
2. For the coding die-hards that refuse to use .exe files, you can always run the .py file through a terminal XD

# How to import the death counter into OBS Studio/OBS Streamlabs (and possibly other streaming/recording clients)
There are a few easy steps to do this:
1. Start the program.
2. Locate a file named "Deaths.txt". This file is located, depending on where the .exe or .py of the deathcounter is.
3. Set the Deaths.txt file as a text (GDI+) file in your OBS.

It should now show the death counter on your stream/recording!

# Controls
These controls are also shown in a terminal, but here's a breakdown of all the controls:
- CTRL + SHIFT + D: Increases the Death Counter by 1.
- CTRL + Shift + R: Resets the Death Counter to 0.
- CTRL + Shift + Q: Quits the program.

# FAQ
Q: Is this file safe to run?
A: The file is 100% safe. Feel free to open the deathcounter.py file with a text-editor (such as Visual Code Studio or Notepad) to inspect the code yourself!

Q: Do I have to update the source in OBS every single time I interact with the counter?
A: No. OBS constantly checks the contents of the Deaths.txt file. If anything changes in that file, OBS will immediately update it!

Q: Can I put the .exe on my desktop for easy access, without having to put the entire file folder on it?
A: Yes you can! The .exe file contains the code itself and works independently from the other files (with the exception of the Deaths.txt file, of course!)

Q: Where can I find the Deaths.txt file?
A: The Deaths.txt file is created when you run the program for the first time. the .txt file is created in the same location as the .exe file. (So if you place the .exe file in a folder, the .txt file will appear in the exact same folder.)

Q: Why is it opening a terminal?
A: The terminal is part of the program. You don't have to interact with it though. The terminal's main purpose is keeping track of the interactions with the program. It'll show you the hotkeys for the counter and sends a response every single time the counter is updated.

Q: Can I get rid of the terminal?
A: Closing the terminal will shut down the program. If you want to have the program running, you'll have to minimize the terminal or something.

Q: Can I customize the hotkeys?
A: No, the hotkeys are hardcoded, but it may be a future feature!