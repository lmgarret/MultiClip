# MultiClip
A portable Python solution to a multiple clipboard.

Originally made for my sister, which had to copy the 5/6 same text (mainly emails) for the whole day at her job; now I may find some use to it too!

##Installation
Download it, launch the MultiClip.exe and you're basically done! The core written in Python, mainly using Windows specifics libs, but no need to install Python as it is included (in a custom lightened version), so no possible compatibility/dependency issues and no extra installation : this is fully plug and play and portable.

##Configuration
Select your text, press Right_Control and X (X being a number, not on the keypad) to assign it to a a shortcut. Left_Ctrl + X (the number) paste your content wherever you want. Congrats, you now have 10 clipboards :)
You can also go to the Data folder and edit directly the corresponding txt files.

##Known issues
- After using Ctrl+Shift+Esc shortcut or Ctrl+Alt+Del, MultiClip won't work anymore. It is a known issue with PYHK an pyHook that haven't been fixed since, and I may not be able to fix it. Hence the restart button.
- Some mouse lags appears while MultiClip is launched, still working to find out why, it may be in PYHK or pyHook code.

##About
This utility is made using [PYHK](https://github.com/schurpf/pyhk) and [pyHook](http://sourceforge.net/projects/pyhook/) libs/scripts; all based on Windows' Python's 2.7.10 distribution. 
