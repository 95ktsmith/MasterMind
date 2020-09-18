# Mastermind - the game

programming a mastermind game!

This is a group hackathon developed by New Haven cohort 11!

Team members present:
Michael George
Carter Clements
Dongtuong Van
Kathleen McKiernan
Kevin Smith
Marcelo Martins
Tim Sninsky
Victor Rivera

There was much initial discussion over which languages to use.  We Decided to use python because It allowed for quick development time and we could implement both a console version and a GUI version.

The algorithm takes input from the players and checks to see if that input is a match the the answer.
If the player input matches the game ends and the player wins, if not the player gets another try up to ten times.  


the checking was done with dedicated function to check for matching digits/colors.  
If the digits don't match the program must also check for existence of the digit/color in the answer in another location.

The user flow for the GUI version is slightly different because the player inputs the oclor order they wish to test, and then the player must press the check button to test it out.  
Implementing it in this way for the GUI version allows the player to change their mind once a color is chose.

To run the GUI version you can use the simple command ./MasterMind.py from the directory on a terminal. 
If you are running a virtual machine such as vagrant you must have display port forwarding enabled to view the GUI.
