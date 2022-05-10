##_-~*!by Nathan A. Horak!*~-_

from VideoPokerClass import Card, Deck, User, HandCheck
import sys


if __name__ == '__main__':

    def is_positive(p):
        '''function checks whether a value is positive- if not, returns value which will error'''
        if p > 0:
            return True
        else:
            return p/0 ##as this is used in try blocks, if is_positive() isn't True,
##this will lead to an exception                     

    def jack_or_better():
        '''function checks whether a pair has a value of jacks or better'''
        if checker.get_pair_list() > [9]: ##input is in form list, so compare against [9]
            return True
        else:
            return False

    ##program start
    ##initialize user and deck. shuffle deck. print opening message.
    user=User('user')    
    deck=Deck()
    deck.shuffle()
    print("Welcome to VideoPokerGame 1.0! The game today is Five Card Draw \
and the pay-out is inspired by the casino archetype Jacks or Better.")
    while True:
    ##enter while loop. try block to check for valid input. breaks out of while loop
    ##if input is valid
        chip_input=input("Please enter \
how many credits you would like to start with, with no commas: ")
        if ',' in chip_input: ##no commas!
            print("\nPlease try again without entering any commas.")
        else:
            try:
                int_check=int(chip_input) ##checks that input can be an int
                q=int(chip_input) 
                is_positive(q) ##checks that input is positive
                break ##if makes through, breaks out
            except:
                print("\n{} is not a valid input! Please try again.".format(chip_input))
                continue ##else continue and re-prompt
    while q>0: ## another while loop, that continues to run as long as you have credits
        while True: ##enter another while loop
            print("\nYour current credit balance is {}.".format(q))
            chip_bet=input("Please enter how many credits you would like to wager \
on the next hand in the form of an integer, with no commas. If you would like to cash out, \
you can do so by entering 'QUIT' with no ' ': ")
            ##allows user to quit program by entering 'QUIT'. any other input needs
            ##to be int and positive
            if chip_bet=='QUIT':
                print()
                print(user._User__cashOut(q)) ##cashes out with current chip value if 'QUIT'
                sys.exit()
            else:
                try:
                    int_check=int(chip_bet) ##checks that input can be an int
                    b=int(chip_bet)
                    is_positive(b) ##checks that input is positive 
                    if q-b<0: ##checks that user doesn't go into debt with game credits
                        print("\nUnfortunately, you can't borrow credits from the house. \
Please enter a number less than or equal to your current credit count, {}.".format(q))
                    else:
                        break ##if makes through, breaks out
                except:
                    print("\n{} is not a valid input! Please try again.".format(chip_bet))
                    continue ##else ccontinue and re-prompt
        
        q=q-b ##sets new credit count as your starting pool minus your bet 
        
        ##deals user 5 cards and displays them
        print("\nYour first five cards are: ")
        user.drawNumber(5,user,deck)
        print()
        print(user._User__showHand())

        ##enter another while loop
        while True:
                k=input("Please specify which cards you would like to throw back. \
For each card to keep, indicate a '0'. For each to throw back, indicate a '1'. Seperate \
each card position with a space. For example, if you wanted to throw back your first \
and last card, you would enter: '1 0 0 0 1' (with no quotations): ").split( ) 
                ##splits out spaces in a list
                ##describes how user controls which cards go back
                k_list=['0','1'] ##make sure only '0' or '1' in input
                if len(k)!=5: ##checks that user only entered five digits
                    print("\n{} is not a valid input! Please try again.".format(k))      
                elif k[0] not in k_list:
                    print("\n{} is not a valid input! Please try again.".format(k))
                elif k[1] not in k_list:
                    print("\n{} is not a valid input! Please try again.".format(k))
                elif k[2] not in k_list:
                    print("\n{} is not a valid input! Please try again.".format(k))
                elif k[3] not in k_list:
                    print("\n{} is not a valid input! Please try again.".format(k))
                elif k[4] not in k_list:
                    print("\n{} is not a valid input! Please try again.".format(k))
                else: ##checks that each position in list is '0' or '1'
                    try: ##try block turns into indeces from string to int
                        for j in range(0, len(k)):
                            k[j]=int(k[j])            
                        break ##if makes through, breaks out
                    except:
                        print("\n{} is not a valid input! Please try again.".format(k))
                        continue ##else continue and re-prompt       
        
        ##for loop to replace cards in user hand with cards in deck
        ##use enumerate because we need to iterate through each index regardless
        ##if we replaced a card previously or not
        for e,i in enumerate(k): 
            if k[e]==1:
                user.replace(e,deck) ##use User.replace() method
        ##get ready to calculate winnings, return to user their final hand
        ##initialize checker
        w=0
        print()        
        print(user._User__showHand())
        print()
        checker=HandCheck(user.cards)
        
        ##if,elif,elif...,else block going through each possible hand combiation.
        ##starts at highest payout and goes down. used standard payout values from
        ##9-6 jacks or better poker game (9-6 refers to pay at full house and flush)
        
        ##Royal Flush Payout
        if checker.check_royal_flush():
            w=800*b
            print("You scored a Royal Flush. Wow! Celebrations are in order!")
        ##Straight Flush Payout
        elif checker.check_straight_flush():
            w=50*b
            print("You scored a Straight Flush. Wow! Great job!")
        ##Four of a Kind Payout
        elif checker.check_four_kind():
            w=25*b
            print("You scored a Four of a Kind. Wow! Great job!")        
        ##Full House Payout
        elif checker.check_full_house():
            w=9*b
            print("You scored a Full House. Keep it up!")        
        ##Flush Payout#
        elif checker.check_flush():
            w=6*b
            print("You scored a Flush. Keep it up!")        
        ##Straight Payout#
        elif checker.check_straight():
            w=4*b
            print("You scored a Straight. Congratulations!")        
        ##Three of a Kind Payout
        elif checker.check_three_kind():
            w=3*b
            print("You scored a Three of a Kind. Congratulations!")           
        ##Two Pair Payout
        elif checker.check_two_pair():
            w=2*b
            print("You scored a Two Pair. Congratulations!")        
        ##Pair of Jacks or Better Payout
        elif checker.check_one_pair() and jack_or_better():
            w=1*b
            print("You scored a {}. Good job!".format
                  (checker.output_pair_list(checker.get_pair_list())))
        ##Pair of Tens or Less - No Payout
        elif checker.check_one_pair():
            w=0 ##if you get a pair that doesn't pay out, game will notify you
            print("Sorry! You don't get credit for a {}. Try again!".format
                  (checker.output_pair_list(checker.get_pair_list())))     
        ##High Card - No Payout
        else:
            print("Sorry! You didn't gain any credits from this hand.")
        
        ##adds winnings to credits, giving new value of total credits
        q=q+w
        
        ## if you're out of credits, run private method _User__cashOut() with input
        ##as q-0. user will get a message returned as well as an output .txt file created
        ##then quit program
        if q==0:
            print()
            print(user._User__cashOut(q))       
            sys.exit()
        else: ##if you still have credits, reset deck and shuffle it and then
        ##reset user
        ##goes back to line 46
            deck.resetDeck()
            deck.shuffle() 
            user.resetUser()
            
