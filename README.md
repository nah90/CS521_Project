# CS521_Project
Video Poker implementation in Python

The idea for my project is a Video Poker game based off of the casino archetype 'Jacks or Better'. The game is essentially Five Card Draw where the user plays against the house and payout is structured with rarer poker hands giving a larger payout than more common ones. Five Card Draw is a classic poker archetype where each player is dealt five cards and can discard any number of cards from their hand. They then get fresh cards from the deck equal to the number of the cards they discarded, such that they end up with five cards. Concerning the payout structure, single pairs only pay out if their value is that of Jacks or better. 

The program starts by asking the user how many credits they would like to begin with and then how many credits they would like to wager or if they'd like to cash out by inputting 'QUIT'. They are then dealt five cards. The user then selects which cards they would like to keep and which cards they would like to return by entering five digits seperated by a space. Each digit must be a 0 or a 1. 0 keeps the card in the given position, and 1 sets it to be replaced. For example, '0 1 1 0 1'  would keep the first and fourth card, and replace the second, third, and fifth cards. Following the second phase, the user receives a pay-out dependent on their wager and the poker hand they ended up with, with the payout equal to the amount bid multiplied by the payout for their poker hand. If the user is out of credits, they receive a return message and a print output to a .txt file thanking them for playing, followed by the program exiting. If the user still has credits, they are able to wager credits again or cash out by typing in 'QUIT'. If the user quits, they receive a return message and a print output to a .txt file with a coupon for redemption of their earned credits, followed by the program exiting. 

To run, the program only requires the Class file, VideoPokerClass, the program file, video_poker_game, and a blank .txt file named 'output_project.txt' in the same location as Class file and program file.  The Class file and program file both import modules needed to run the program. The Class file imports the 'random' module to enable shuffling the deck during the game. It also imports the 'os'  module so that a .txt file outputted by program can easily be located by the user. The program file imports Class objects Card, Deck, User, and HandCheck from 'VideoPokerClass' module for use as well as the 'sys' module to exit the program. To run the program, open both 'VideoPokerClass.py' and 'video_poker_game.py' in a IDE such as Spyder and have a blank .txt file named 'output_project.txt' present in your local directory. Then, run the program 'video_poker_game.py' and follow instructions related to input.
