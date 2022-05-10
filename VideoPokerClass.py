##_-~*!by Nathan A. Horak!*~-_

import random
import os

##dict for associating values with names for Card object, as well as list for suits
card_value_dict = {"Two":1, "Three":2, "Four":3, "Five":4, "Six":5,"Seven":6,
"Eight":7, "Nine":8, "Ten":9, "Jack":10, "Queen":11, "King":12, "Ace":13 }  
suits_list=['Clubs','Diamonds','Hearts','Spades']

class Card:
    '''This class constructs the Card object and contains attributes name, value, and suit'''
    def __init__(self,name,value,suit):
        self.__name=name ##private attribute
        self.value=value
        self.suit=suit
               
    def __repr__(self):
        '''repr'''
        return ("{} of {}".format(self.__name,self.suit)) 
##returns only card name and suit, not value
     
class Deck:
    '''This class constructs the Deck object which contains Cards'''
    def __init__(self):
        self.card_deck=[]    ##blank deck list    
        for _Card__name in card_value_dict:
            for suit in suits_list:
                self.card_deck.append(Card(_Card__name, card_value_dict[_Card__name], suit))
##create deck of 52 cards, giving each card a name, value, and suit
                
    def __getitem__(self,item): ##__getitem__, used to enable Deck.shuffle()
        '''__getitem__'''
        return self.card_deck[item]

    def __setitem__(self,suit,value): ##__setitem__, used to enable Deck.shuffle()
        '''__setitem__'''
        self.card_deck[suit]= value
    
    def __len__(self): ##__len__, used in unit test
        '''__len___'''
        return len(self.card_deck)
    
    def __lt__(self,other): ##__lt__, used to sort() in HandCheck()
        '''__lt__'''
        return (self.value<other)    

    def __gt__(self,other): ##__gt__,used to sort() in HandCheck()
        '''__gt__'''
        return (self.value>other)    
    
    def shuffle(self): ##used by program to replicate a user shuffling
        '''This method uses the random module to shuffle a deck object'''
        random.shuffle(self)
     
    def drawCard(self): ##draws a card from deck, used in unit test and in program
        '''This method draws a card from the deck, reducing the number of cards in the deck'''
        return self.card_deck.pop(0)
    
    def showDeck(self): ##can be used to quickly display all cards remaining in the deck
        '''This method shows every card in the deck'''
        for card in self.card_deck:
           print(card.__repr__())
        
    def resetDeck(self): ##used to reset deck after each round such that players start fresh
        '''This method clears the deck of cards and creates a new deck'''
        self.card_deck=[]
        for _Card__name in card_value_dict:
            for suit in suits_list:
                self.card_deck.append(Card(_Card__name, card_value_dict[_Card__name], suit))
                
class User:
    '''This class constructs the User object to represent the player in the poker game'''
    def __init__(self,name):
        self.__name=name ##private attribute
        self.cards=[]
        
    def draw(self,deck): ##adds card to user's hand from deck
        '''This method removes a card from the specified deck and adds it to the
User's hand'''
        self.cards.append(deck.drawCard())

    def drawNumber(self,number,user,deck): ##used in unit test and in program
        '''This method utilizes the draw method described above to draw as many cards
as one would like from a given deck to a given user'''
        self.number=number
        for t in range(number):
            user.draw(deck)

    def __showHand(self): ##private method that shows user cards in hand. heavily used
        '''This method shows the contents of the user's hand'''
        hand_list=[]
        for card in self.cards:
            hand_list.append(card)
        return hand_list

    def discard(self,position): ##used in unit test and in program as part of replace method
        '''This method removes a card from the user's hand from a specific position'''
        self.cards.pop(position)
         
    def replace(self,position,deck): ##used in program to replace specific cards in user's hand
        '''This method uses the discard method described above to remove a card from
a position and then replaces it in position with a card from a specific deck'''
        deck.shuffle() ##throws in an extra shuffle per replace
        self.discard(position) ##discard by position
        self.cards.insert(position,deck.drawCard()) ##replace in position by
##drawing card from deck to user's hand
                
    def removeAllofSuit(self,suit): ##used in unit test and is useful to check HandCheck() methods
        '''This method removes from user's hand all cards that share the inputted suit.
The suits are 'Clubs','Diamonds','Hearts',and 'Spades'.
Example: user.removeAllofSuit('Spades')'''
        self.suit=suit
        for card in self.cards:
            if card.suit == suit:
                self.cards.remove(card)
        
    def resetUser(self): ##used in unit test and program
        '''This method removes all cards from the user's hand'''
        self.cards=[]

    def __cashOut(self,credit): ##private method that returns a message to user and writes output
        '''This method is used when the user would like to quit or when they are out
of credits. It returns a specific message to user dependent on number of credits 
they had and it outputs a specific str to a .txt file dependent on user's number of credits'''
        self.credit=credit ##credits seem to be built-in Python
        w=credit
        v=""
        win=False
        dir_name=os.getcwd()
        file_name=os.path.join(dir_name,'output_project.txt')
        r="We hope to you again soon! \n -Nathan A. Horak"
        if w ==0:
            v="We're sorry you're out of credits. Thanks for playing!"
        else:
            win=True
            v="This coupon can be redeemed for ${} at the nearest help desk.".format(w)
        text_file=open(file_name, 'w')
        text_file.write(v + "\n"+"\n")
        text_file.write(r)
        if win==True:
            return "You have successfully cashed out. Your final balance is {} \
credits. Please check your local directory for your virtual prize.".format(w)
        else: ##Possibly not the best verbiage to get people to play again
            return "You are out of credits. Game over!" 
        
class HandCheck:
    '''This class constructs the HandCheck object that scores the user's poker hands'''
    def __init__(self, cards):
        self.cards=cards
        ##HandCheck methods use mainly len() function, count() method, and sort() method
    def check_flush(self):
        '''This method checks for a flush'''
        flush_check_list=[]
        flush_check_list=[card.suit for card in self.cards]          
        if len(set(flush_check_list))==1 and len(list(flush_check_list))==5:
            return True
        else: ##utilizes fact that if all cards have the same suit, len(set())=1          
            return False
        
    def check_straight(self):
        '''This method checks for a straight'''
        value_list=[]
        value_list=[card.value for card in self.cards]  
        value_list.sort()
        if len(set(value_list))!=5:
            return False ##utilizes fact that each card has a unique value in a straight
        if value_list[0]==1 and value_list[1]==2 and value_list[2]==3 \
            and value_list[3]==4 and value_list[4]==13:
                return True ##special case where Ace also can be lower bound on straight
        if value_list[4]-value_list[3]!=1: 
        ##checking that each subsequent value is 1 greater in list
            return False
        if value_list[3]-value_list[2]!=1:
            return False
        if value_list[2]-value_list[1]!=1:
            return False
        if value_list[1]-value_list[0]!=1:
            return False
        else:
            return True
      
    def check_straight_flush(self): ##checks both straight and flush    
        '''This method checks for a straight flush'''
        return HandCheck.check_flush(self) and HandCheck.check_straight(self)

    def check_royal_flush(self): ##checks straight,flush, and royal value
        '''This method checks for a royal flush'''
        royal_list=[]
        royal_list=[card.value for card in self.cards]  
        royal_list.sort()        
        return HandCheck.check_straight_flush(self) and royal_list[4]==13 ##royal check
    
    def check_four_kind(self):
        '''This method checks for four of a kind'''
        four_kind_list=[]
        four_kind_list=[card.value for card in self.cards]  
        for value in four_kind_list:
            if four_kind_list.count(value) ==4:
                return True
            else: ##utilizes fact that count() method for four of a kind is 4  
                return False
            
    def check_full_house(self):
        '''This method checks for a full house'''
        full_house=False
        fh_set=False
        full_house_list=[]
        full_house_list=[card.value for card in self.cards]  
        for value in full_house_list:
            if full_house_list.count(value) ==3:
                full_house=True
        if len(set(full_house_list))==2:
                fh_set=True        
        if full_house and fh_set:
            return True
        else: 
            return False
        ##utilizes count() method for full house is 4 as well as len() of values
        ##as a full house is 2 as full house only has two distinct values within
        
    def check_three_kind(self):
        '''This method checks for three of a kind'''
        three_kind=False
        thk_set=False        
        three_kind_list=[]
        three_kind_list=[card.value for card in self.cards]  
        for value in three_kind_list:
            if three_kind_list.count(value) ==3:
                three_kind=True                
        if len(set(three_kind_list))==3:
                thk_set=True
        if three_kind and thk_set:
            return True
        else:
            return False
        ##similar to the check for full house, but len() of values as a three kind is
        ##3 as opposed to 2 for full house
        
    def check_two_pair(self):
        '''This method checks for two pairs'''
        two_pair=False
        twk_set=False        
        two_pair_list=[]
        two_pair_list=[card.value for card in self.cards]  
        for value in two_pair_list:
            if two_pair_list.count(value) ==2:
                two_pair=True
        if len(set(two_pair_list))==3:
            twk_set=True
        if two_pair and twk_set:
            return True
        else:
            return False
        ##similar to check for full house and three of a kind except count() method
        ##is 2 and len() of values is 3
    def check_one_pair(self):
        '''This method checks for a single pair'''
        one_pair=False
        one_set=False        
        one_pair_list=[]
        one_pair_list=[card.value for card in self.cards]        
        for value in one_pair_list:
            if one_pair_list.count(value) ==2:
                one_pair=True
        if len(set(one_pair_list))==4:
            one_set=True
        if one_pair and one_set:
            return True
        else:
            return False
        ##similar to cehck for full house, three of a kind, and two pair except
        ##count() method is 2 and len() of values is 4
    def get_pair_list(self):
        '''This method returns the value of a single pair if it exists'''
        pair_list=[]
        pair_value=[card.value for card in self.cards]
        for value in pair_value:
            if pair_value.count(value) ==2 and value not in pair_list:
                pair_list.append(value)                
        return pair_list
        ##uses count() method to find values of a pair in a user's hand
        
    def output_pair_list(self,pair_value):
        '''This method takes in a value associated with a single pair from the
HandCheck.get_pair_list() method and it returns the name of the value associated with
the pair.'''
        self.pair_value=pair_value
        pair_value=pair_value[0]
        swap_dict= dict(zip(card_value_dict.values(), card_value_dict.keys()))
        return "Pair of {}s".format(swap_dict[pair_value])
        ##uses dict used to build the card deck, and flips around keys and values
        ##such that the name can be called

if __name__=='__main__': ##if name == main Unit Test!

    ##create two test decks and two test users
    test_deck_1=Deck()
    test_deck_2=Deck()
    user_1=User('user_1')     
    user_2=User('user_2')
    
    ##CONSTANTS
    STANDARD_DECK_LEN=52
    HAND_SIZE=5
    CARDS_IN_SUIT=13
    
    ##use "for k in range()" loop to deal cards to user_1
    for k in range(HAND_SIZE):
        user_1.draw(test_deck_1)
     
    ##check that the private method _User__showHand() functions correctly    
    assert user_1._User__showHand() == user_1.cards, ("Error matching user hand {} \
!= {}".format(user_1._User__showHand(), user_1.cards))
    
    ##check that cards are being removed from test_deck_1 when dealt to user_1 by
    ##checking User.draw() method
    assert len(user_1._User__showHand()) == STANDARD_DECK_LEN - len(test_deck_1), ("\
Error matching {} + {} == {}".format(user_1._User__showHand(),test_deck_1.card_deck,
    test_deck_2.card_deck))
    
    ##use method to deal cards to user_2
    user_2.drawNumber(HAND_SIZE,user_2,test_deck_2)
    
    ##check that User.drawNumber() method properly deals number of cards
    assert len(user_2._User__showHand()) == HAND_SIZE and len(user_2._User__showHand())
    + len(test_deck_2) == STANDARD_DECK_LEN, ("Error with \
User.drawNumber(number,user,deck). {} != {}".format(user_2._User__showHand(),
    user_2.cards))   
    
    ##create lists of test_deck_1 and test_deck_2 
    deck_string_1=""
    deck_string_2=""
    deck_string_1=':'.join([str(e) for e in test_deck_1])
    deck_string_2=':'.join([str(e) for e in test_deck_2])
    test_deck_list_1=deck_string_1.split(':')
    test_deck_list_2=deck_string_2.split(':')
     
    ##checks whether User.drawNumber() removes cards the same way as
    ##User.draw() method does from deck
    assert test_deck_list_1 == test_deck_list_2, ("Error matching test decks \
{} and {}".format(test_deck_1.card_deck, test_deck_2.card_deck))
    
    ##create lists of user_1.cards and user_2.cards
    user_string_1=""
    user_string_2=""
    user_string_1=':'.join([str(e) for e in user_1.cards])
    user_string_2=':'.join([str(e) for e in user_2.cards])
    test_user_list_1=user_string_1.split(':')
    test_user_list_2=user_string_2.split(':')
    
    ##checks whether User.drawNumber() deals cards the same way as
    ##User.draw() method does to user
    assert test_user_list_1 == test_user_list_2, ("Error matching user hands \
{} and {}".format(user_1.cards, user_2.cards))
    
    ##replaces first card of user_2 with a random card from test_deck_2
    user_2.replace(0,test_deck_2)
    
    ##updates user_string_2 to reflect User.replace(position)
    user_string_2=':'.join([str(e) for e in user_2.cards])
    test_user_list_2=user_string_2.split(':')
    
    ##checks whether replace function correctly removed a card from user_2 and
    ##replaced it with a card from test_deck_2
    assert len(test_user_list_1) == len(test_user_list_2) and test_user_list_1[1:4] \
    == test_user_list_2[1:4] and test_user_list_1[0] != test_user_list_2[1:4] \
    ,("Error with User.replace(position,deck)! {} == {}.".format(user_1.cards,
    user_2.cards))
    
    ##reset both user_1 and user_2 as well as their decks test_deck_1 and test_deck_2
    ##initialize checkers for user_1 and user_2    
    test_deck_1.resetDeck()
    test_deck_2.resetDeck()
    user_1.resetUser()
    user_2.resetUser()    
    checker_1=HandCheck(user_1.cards)
    checker_2=HandCheck(user_2.cards)
    
    ##give each user 5 cards from their respective deck
    ##deck is created from a suit and a value, then all the other suits for that value,
    ##and lastly by changing the value. starts at Two of Clubs and goes up. Thus,
    ##both user's hands should be 2,2,2,2 and the Three of Clubs.
    user_1.drawNumber(HAND_SIZE,user_1,test_deck_1)
    user_2.drawNumber(HAND_SIZE,user_2,test_deck_2)
    
    ##check that HandCheck() methods work correctly. picked methods that checked counts,
    ##pairs,flush, and straight
    assert checker_1.check_four_kind() == True and checker_1.check_royal_flush()\
    == False and checker_1.check_one_pair() == False, ("HandCheck not operating \
correctly. {} is a {}, not a {}, and is more than just a {}.".format(
    user_2._User__showHand(),'Four of a Kind','Royal Flush','Single Pair'))

    ##draw all cards in deck
    user_2.drawNumber(int(STANDARD_DECK_LEN-HAND_SIZE),user_2,test_deck_2)
    
    ##remove all cards except 'Spades' cards
    user_2.removeAllofSuit('Clubs')
    user_2.removeAllofSuit('Diamonds')
    user_2.removeAllofSuit('Hearts')
    
    ##removes cards from index[0] until there are only five cards left. Because
    ##first entry is 2 and last is Ace, only 10, J, Q, K, A of spades remain-Royal FLush!
    for t in range(int(CARDS_IN_SUIT-HAND_SIZE)):
        user_2.discard(0)
    
    ##check that HandCheck() methods work correctly. similar to above. check that the
    ##hand is a flush,straight,straight flush, and royal flush as wellas not a four
    ##of a kind or one pair
    assert checker_2.check_flush() == True and checker_2.check_straight()\
    == True and checker_2.check_straight_flush() == True \
    and checker_2.check_royal_flush()== True and checker_2.check_four_kind()\
    == False and checker_2.check_one_pair()== False, ("HandCheck not operating \
    correctly. {} is a {} and a {}, and thus a {}. It is also a {} given the \
    value of the straight. It is not a {}, nor a {}."
    .format(user_2._User__showHand(),'Straight','Flush','Straight Flush','Royal Flush',\
'Four of a Kind','Single Pair'))
    
    ##reset user_2 and test_deck_2, and deal 5 cards to user_2
    user_2.resetUser()
    test_deck_2.resetDeck()
    user_2.drawNumber(HAND_SIZE,user_2,test_deck_2)
    checker_2=HandCheck(user_2.cards)
    
    ##check that User.resetUser() and Deck.resetDeck() work properly. If they don't,
    ##won't pass this assert
    assert checker_2.check_royal_flush() == False and checker_2.check_four_kind()\
    ==True,("Oops! Hand is not resetting properly. {} should be a {} and not a \
{}.".format(user_2._User__showHand(),'Four of a Kind','Royal Flush'))
    
    ##and we're done!
    print("Unit test passed!")




                                                   