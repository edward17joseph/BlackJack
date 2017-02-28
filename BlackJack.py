from random import randrange
print('BlackJack')
NewGame=str(input('New game?(Y for yes, N for no):'))

while NewGame=='y' or NewGame=='Y':
    suit=['A','2','3','4','5','6','7','8','9','10','J','Q','K']
    deck=4*suit

    Value=['A',1,'2',2,'3',3,'4',4,'5',5,'6',6,'7',7,'8',8,'9',9,'10',10,'J',10,'Q',10,'K',10]

    dealers_hand=[]
    player_hand=[]

    result=0

    def reset_deck():
        global deck
        deck=4*suit

    def result_bet(bet):
        global buy_in
        if result==0:
            buy_in=buy_in-bet
        else:
            buy_in=buy_in+bet
        print('Money remaining: $ %s' %(buy_in))

    def deal():
        while len(dealers_hand)<2:
            card=randrange(0,len(deck))
            player_hand.append(deck[card])
            del deck[card]
            card=randrange(0,len(deck))
            dealers_hand.append(deck[card])
            del deck[card]
        return player_hand

    def sum_cards(x):
        sum,k,n=0,0,0
        while k<len(Value):
            while n<len(x):
                if x[n]==Value[k]:
                    sum=sum+Value[k+1]
                n+=1
            n,k=0,k+1
        return sum

    def sum_accounting_ace(x):
        lst_sum=[sum_cards(x)]
        if 'A' in x:
            k=0
            while k<x.count('A'):
                lst_sum.append(lst_sum[k]+10)
                k+=1
        n=len(lst_sum)-1
        while 0<=n:
            if lst_sum[n]>21:
                lst_sum.remove(lst_sum[n])
            n-=1
        return lst_sum

    def check_over(x):
        if x==[]:
            return True
        return False

    def check_21(x):
        for i in x:
            if i==21:
                return True
            return False

    def hit(x):
        if x=='y' or x=='Y':
            card=randrange(0,len(deck))
            player_hand.append(deck[card])
            del deck[card]
            print(player_hand)
        else:
            dealers_choice()

    def dealers_choice():
        global result
        if check_over(sum_accounting_ace(dealers_hand)):
            print(dealers_hand)
            print('You win')
            result=1
        elif max(sum_accounting_ace(dealers_hand))>max(sum_accounting_ace(player_hand)):
            print(dealers_hand)
            print('You lose')
            result=0
        else:
            card=randrange(0,len(deck))
            dealers_hand.append(deck[card])
            del deck[card]
            dealers_choice()

    def first_play():
        global result
        deal()
        print(player_hand)
        if 21 in sum_accounting_ace(player_hand):
            print('You win')
            result=1
            return 0

    def rest_myturn():
        global result
        if check_over(sum_accounting_ace(player_hand)):
            print('You lose')
            result=0
            return 0
        if check_21(sum_accounting_ace(player_hand)):
            print('You win')
            result=1
            return 0
        move=str(input('Hit?(Y for yes, N for no):'))
        hit(move)
        if move=='y' or move=='Y':
            rest_myturn()

    buy_in=int(input('How much is your buy in?:'))
    while buy_in>0:
        bet=int(input('How much would you like to bet?:'))
        while bet>buy_in:
            bet=int(input('Not enough funds.How much would you like to bet?:'))
        first_play()
        if result!=1:
            rest_myturn()
        result_bet(bet)
        result=0
        dealers_hand,player_hand=[],[]
        if len(deck)<26:
            reset_deck()
    print('Game Over')
    NewGame=str(input('New game?(Y for yes, N for no):'))
