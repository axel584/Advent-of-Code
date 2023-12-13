import pytest
from collections import Counter
from enum import Enum
from collections import OrderedDict


value_of_card = {'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,'T':10,'J':11,'Q':12,'K':13,'A':14,}

value_of_card2 = {'J':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,'T':10,'Q':12,'K':13,'A':14,}


class TypeHand(Enum):
    HIGH_CARD = 1
    ONE_PAIR = 2
    TWO_PAIR = 3
    THREE_OF_A_KIND = 4
    FULL_HOUSE = 5
    FOUR_OF_A_KIND = 6
    FIVE_OF_A_KIND = 7

    def __lt__(self,other):
        return self.value<other.value


class Card():

    value : str

    def __init__(self,value):
        self.value = value

    def __lt__(self,other):
        return value_of_card[self.value]<value_of_card[other.value]
    
    def __str__(self):
        return self.value
    
    def __repr__(self):
        return self.value
    
    def __eq__(self,other):
        if other==None:
            return False
        return self.value==other.value
    
    def __hash__(self):
        return hash(self.value)

class Card2():

    value : str

    def __init__(self,value):
        self.value = value

    def __lt__(self,other):
        return value_of_card2[self.value]<value_of_card2[other.value]
    
    def __str__(self):
        return self.value
    
    def __repr__(self):
        return self.value
    
    def __eq__(self,other):
        if other==None :
            return False
        return self.value==other.value
    
    def __hash__(self):
        return hash(self.value)    

class Hand():
    def calcule_type(self):
        counter = Counter(self.values)
        nb_pair = 0
        nb_brelan = 0
        for k,v in counter.items():
            if v==5 :
                #print("five")
                return TypeHand.FIVE_OF_A_KIND
            if v==4 :
                #print("quatre")
                return TypeHand.FOUR_OF_A_KIND
            if v==3 :
                #print("trois")
                nb_brelan +=1
            if v==2 :
                #print("pair")
                nb_pair += 1
        if nb_brelan==1 and nb_pair==1:
            return TypeHand.FULL_HOUSE
        if nb_brelan==1 :
            return TypeHand.THREE_OF_A_KIND
        if nb_pair==2 :
            return TypeHand.TWO_PAIR
        if nb_pair==1 :
            return TypeHand.ONE_PAIR
        return TypeHand.HIGH_CARD



    def __init__(self,values,bid=0):
        self.values = [Card(i) for i in values]
        self.type = self.calcule_type()
        self.bid = int(bid)

    def __lt__(self,other):
        if self.type<other.type :
            return True
        if self.type==other.type:
            for cpt,i in enumerate(self.values) :
                if i!=other.values[cpt] :
                    return i<other.values[cpt]
                
    def __repr__(self):
        return f"{self.values} ({self.type}) {self.bid}$"

class Hand2():
    def calcule_type(self):
        counter = Counter(self.values)
        # cherche si contient un 'J' et la carte avec le plus grand nombre d'occurence != 'J' 
        nb_joker = 0
        card_max = None
        nb_card_max = 0
        for k,v in counter.items():
            if Card2("J")==k:
                #print("trouve un joker")
                nb_joker=v
            else : 
                if v>nb_card_max:
                    nb_card_max=v
                    card_max=k
        # remplace les Joker par la plus haute carte             
        if nb_joker>0 :
            if card_max!=None and card_max != Card('J'):
                counter[card_max] = counter[card_max] + nb_joker

        nb_pair = 0
        nb_brelan = 0
        for k,v in counter.items():
            if v==5 :
                #print("five")
                return TypeHand.FIVE_OF_A_KIND
            if v==4 :
                #print("quatre")
                return TypeHand.FOUR_OF_A_KIND
            if v==3 :
                #print("trois")
                nb_brelan +=1
            if v==2 :
                #print("pair")
                nb_pair += 1
        if nb_brelan==1 and nb_pair==1:
            return TypeHand.FULL_HOUSE
        if nb_brelan==1 :
            return TypeHand.THREE_OF_A_KIND
        if nb_pair==2 :
            return TypeHand.TWO_PAIR
        if nb_pair==1 :
            return TypeHand.ONE_PAIR
        return TypeHand.HIGH_CARD



    def __init__(self,values,bid=0):
        self.values = [Card2(i) for i in values]
        self.type = self.calcule_type()
        self.bid = int(bid)

    def __lt__(self,other):
        if self.type<other.type :
            return True
        if self.type==other.type:
            for cpt,i in enumerate(self.values) :
                if i!=other.values[cpt] :
                    return i<other.values[cpt]
                
    def __repr__(self):
        return f"{self.values} ({self.type}) {self.bid}$"

def enigme_day07(chemin):
    hands = []
    with open(chemin,'r') as fichier :
        for ligne in [i.strip() for i in fichier] :
            hand_value,bid = ligne.split()
            hand = Hand(hand_value,bid)
            hands.append(hand)
    hands.sort()
    somme = 0
    for cpt,hand in enumerate(hands) :
        print("somme",cpt,hand)
        somme += (cpt+1)*hand.bid 
    return somme

def enigme_day07_second_part(chemin):
    hands = []
    with open(chemin,'r') as fichier :
        for ligne in [i.strip() for i in fichier] :
            hand_value,bid = ligne.split()
            hand = Hand2(hand_value,bid)
            hands.append(hand)
    hands.sort()
    somme = 0
    for cpt,hand in enumerate(hands) :
        print("somme",cpt,hand)
        somme += (cpt+1)*hand.bid 
    return somme

@pytest.mark.skip()
def test_Card():
    card_2 = Card('2')
    card_9 = Card('9')
    card_t = Card('T')
    card_q = Card('Q')
    assert card_2<card_9
    assert card_t>card_9
    assert card_t<card_q

@pytest.mark.skip()
def test_Hand():
    hand_1 = Hand('32T3K')
    hand_2 = Hand('T55J5')
    hand_3 = Hand('KK677')
    hand_4 = Hand('KTJJT')
    hand_5 = Hand('QQQJA')
    hand_6 = Hand('JJJJJ')
    assert hand_1<hand_4
    assert hand_4<hand_3
    print("3 et 2")
    assert hand_3<hand_2
    print("2 et 5")
    assert hand_2<hand_5

@pytest.mark.skip()
def test_Hand2():
    print("32T3K")
    hand_1 = Hand2('32T3K')
    print("T55J5")
    hand_2 = Hand2('T55J5')
    print("------")
    hand_3 = Hand2('KK677')
    print("KTJJT")
    hand_4 = Hand2('KTJJT')
    print("QQQJA")
    hand_5 = Hand2('QQQJA')
    print("JJJJJ")
    hand_6 = Hand2('KKKJK')
    assert hand_1.type==TypeHand.ONE_PAIR
    assert hand_2.type==TypeHand.FOUR_OF_A_KIND
    assert hand_3.type==TypeHand.TWO_PAIR
    assert hand_4.type==TypeHand.FOUR_OF_A_KIND
    assert hand_5.type==TypeHand.FOUR_OF_A_KIND
    assert hand_6.type==TypeHand.FIVE_OF_A_KIND
    assert hand_1<hand_3
    assert hand_3<hand_2
    assert hand_2<hand_5
    assert hand_5<hand_4

@pytest.mark.skip()
def test_enigme_day07():
    assert enigme_day07("input-07a-test.txt") == 6440

def test_enigme_day07_second_part():
    assert enigme_day07_second_part("input-07b-test.txt") == 2133

if __name__ == "__main__" :
    print(enigme_day07_second_part("input-07.txt"))