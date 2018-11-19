import random
import time
import os

print("-----------------------WELCOME TO CALL BRIDGE---------------------")
print("")
print("")
print("Read The Instructions Carefully before start the Game")
print("")
print("In This Command Line Game 4 player will play")
print("")
print("You will play as USER or 4th player")
print("")
print("There are 4 types of Card available in this Game")
print("")
print("Type1: Range 01-->13")
print("Type2: Range 14-->26")
print("Type3: Range 27-->39")
print("Type4: Range 40-->52")
print("")
print("")
print("--First System will choose Any one from the 4 Types of card as COLOUR--")
print("")
print("Then System will give you 13 arbitrary card between 1 to 52")
print("")
print("--Now you have to claim how many rounds(pits) you can win(Total 13 rounds)--")
print("")
print("First look at your cards..To imagine how many rounds(pits) you can win")
print("")
print("1)If There 13/26/39/52 any one of this you can claim 1 pit")
print("")
print("2)If you have 12/25/38/51 any one of this with 1 extra card on this range...you can claim 1 pit")
print("")
print("3)Suppose you have 2 or 1 or 0 card(s) for a particular Type and which is not clour")
print("  And you have more than 3 cards of colour,then you can claim 1 or 2 or 3 pit(s) respectively...")
print("")
print("4)After All those Process still you have some colour card then you can claim your pits")
print("  According to your colour cards...to play safe you should claim (rest of colour cards-2) pit(s)")
print("")
os.system("pause")
os.system("cls")
print("")
print("Now when a player will start a round,you have to play according to his/her card ")
print("It means if you have a card on the range which is played first,you have to play")
print("If you have larger than the bidding card you will play the larger card")
print("Else you will play a smaller card")
print("")
print("IF you don't have a card on this range...")
print("Either you can play a colour card or a small value card of another type")
print("If you play a colour card you will be the winner for this round")
print("")
print("")
print("Supoose your previous player also don't have the type of card which is played first in this round")
print("And he plays a colour card")
print("If you have larger than that colour card you can play to win the round")
print("If don't have larger card on colour this time...you can play any small value card from any type of cards")
print("")
print("")
print("When you will start a round you can play any card from your cards")
print("")
print("")
os.system("pause")
os.system("cls")
print("")
print("After playing 13 rounds: ")
print("If you win exactly same no. of rounds or maximum 2 rounds extra of your claim ")
print("Then you will score +(10*your claming pits) points")
print("Else you will score -(10*your claming pits) points")
print("")
print("")
print("If you claim 1 pit only and can not win a single round....then you will get 0 points")
print("But you claim 1 pit and get more than 3 pits you will reawarded with -10 points")
print("")
print("")
print("Game Will Continue until someone can score 100 and he will also decleared as winner")
print("")
print("-------------------Thank you for listening,Now You can play the Game...Enjoy!!!!----------------")
os.system("pause")
os.system("cls")

p=[]
q=[]
r=[]
s=[]
space=[]

pits1=0
pits2=0
pits3=0
pits4=0

scr1=0
scr2=0
scr3=0
scr4=0

def usr_clm():
    global pits4
    usr=input("Claim your pits User: ")
    try:
        int(usr)
        p=1
    except ValueError:
        print("")
        print("No no!! Digit only")
        print("")
        p=2
    if p==1:
        if int(usr)>=0 and int(usr)<=13:
            pits4=int(usr)
        else:
            print("")
            print("It should be 0 to 13 only!!!!!")
            print("")
            usr_clm()
    elif p==2:
        usr_clm()
    
    
def scorecard():
    global pits1
    global pits2
    global pits3
    global pits4
    global first
    global second
    global third
    global forth
    global scr1
    global scr2
    global scr4
    global scr3

    if pits1>1:
        if first==pits1 or first==pits1+1 or first==pits1+2:
            scr1=scr1+(pits1*10)
        else:
            scr1=scr1-(pits1*10)

    elif pits1==1:
        if first==pits1 or first==pits1+1 or first==pits1+2:
            scr1=scr1+(pits1*10)
        elif first==pits1-1:
            scr1=scr1+0
        else:
            scr1=scr1-10

    if pits2>1:
        if second==pits2 or second==pits2+1 or second==pits2+2:
            scr2=scr2+(pits2*10)
        else:
            scr2=scr2-(pits2*10)

    elif pits2==1:
        if second==pits2 or second==pits2+1 or second==pits2+2:
            scr2=scr2+(pits2*10)
        elif second==pits2-1:
            scr2=scr2+0
        else:
            scr2=scr2-10

    if pits3>1:
        if third==pits3 or third==pits3+1 or third==pits3+2:
            scr3=scr3+(pits3*10)
        else:
            scr3=scr3-(pits3*10)

    elif pits3==1:
        if third==pits3 or third==pits3+1 or third==pits3+2:
            scr3=scr3+(pits3*10)
        elif third==pits3-1:
            scr3=scr3+0
        else:
            scr3=scr3-10

    if pits4>1:
        if forth==pits4 or forth==pits4+1 or forth==pits4+2:
            scr4=scr4+(pits4*10)
        else:
            scr4=scr4-(pits4*10)
    elif pits4==1:
        if forth==pits4 or forth==pits4+1 or forth==pits4+2:
            scr4=scr4+(pits4*10)
        elif forth==pits4-1:
            scr4=scr4+0
        else:
            scr4=scr4-10
            
    print("")
    print("")
    print("---------------Scorecard--------------")
    print("")
    print("")
    print("   Player 1 :                   ",scr1," points")
    print("   Player 2 :                   ",scr2," points")
    print("   Player 3 :                   ",scr3," points")
    print("   User     :                   ",scr4," points")
    print("")
    if scr1>=100 and scr1>scr2 and scr1>scr3 and scr1>scr4:
        print("")
        print("---Player 1 Win---")
    elif scr2>=100 and scr2>scr1 and scr2>scr3 and scr2>scr4:
        print("")
        print("---Player 2 Win---")
    elif scr3>=100 and scr3>scr2 and scr3>scr1 and scr3>scr4:
        print("")
        print("---Player 3 Win---")
    elif scr4>=100 and scr4>scr2 and scr4>scr3 and scr4>scr1:
        print("")
        print("......You Win......")
        print("..Congradulations..")

def spc(max_rt):
    sp1=0
    if max_rt==1:
        if space[1]>0 and space[1]<=13:
            sp1=space[1]
        else:
            sp1=0
            
    elif max_rt==2:
        if space[1]>13 and space[1]<=26:
            sp1=space[1]
        else:
            sp1=0

    elif max_rt==3:
        if space[1]>26 and space[1]<=39:
            sp1=space[1]
        else:
            sp1=0

    elif max_rt==4:
        if space[1]>39 and space[1]<=52:
            sp1=space[1]
        else:
            sp1=0

    if sp1>0:
        return sp1
    else:
        return 0

def spc1(max_rt):
    sp2=0
    if max_rt==1:
        if space[1]>0 and space[1]<=13:
            sp2=space[1]
        elif space[2]>0 and space[2]<=13:
            sp2=space[2]
        else:
            sp2=0
            
    elif max_rt==2:
        if space[1]>13 and space[1]<=26:
            sp2=space[1]
        elif space[2]>13 and space[2]<=26:
            sp2=space[2]
        else:
            sp2=0

    elif max_rt==3:
        if space[1]>26 and space[1]<=39:
            sp2=space[1]
        elif space[2]>26 and space[2]<=39:
            sp2=space[2]
        else:
            sp2=0

    elif max_rt==4:
        if space[1]>39 and space[1]<=52:
            sp2=space[1]
        elif space[2]>39 and space[2]<=52:
            sp2=space[2]
        else:
            sp2=0

    if sp2>0:
        return sp2
    else:
        return 0
    
def find_color1(max_rt):
    fico=0
    x=0
    ty=0
    if max_rt==1:
        while x<len(p):
            if p[x]>0 and p[x]<=13:
                if p[x]>fico:
                    fico=p[x]
                    x=x+1
                else:
                    x=x+1
            else:
                x=x+1
                
    elif max_rt==2:
        while x<len(p):
            if p[x]>13 and p[x]<=26:
                if p[x]>fico:
                    fico=p[x]
                    x=x+1
                else:
                    x=x+1
            else:
                x=x+1

    elif max_rt==3:
        while x<len(p):
            if p[x]>26 and p[x]<=39:
                if p[x]>fico:
                    fico=p[x]
                    x=x+1
                else:
                    x=x+1
            else:
                x=x+1

    elif max_rt==4:
        while x<len(p):
            if p[x]>39 and p[x]<=52:
                if p[x]>fico:
                    fico=p[x]
                    x=x+1
                else:
                    x=x+1
            else:
                x=x+1

    if fico>0 and fico<=13:
        while ty<len(space):
            if space[ty]>0 and space[ty]<=13:
                if space[ty]>fico:
                    fico=0
                    break
                else:
                    ty=ty+1
            else:
                ty=ty+1

    elif fico>13 and fico<=26:
        while ty<len(space):
            if space[ty]>13 and space[ty]<=26:
                if space[ty]>fico:
                    fico=0
                    break
                else:
                    ty=ty+1
            else:
                ty=ty+1                

    elif fico>26 and fico<=39:
        while ty<len(space):
            if space[ty]>26 and space[ty]<=39:
                if space[ty]>fico:
                    fico=0
                    break
                else:
                    ty=ty+1
            else:
                ty=ty+1


    elif fico>39 and fico<=52:
        while ty<len(space):
            if space[ty]>39 and space[ty]<=52:
                if space[ty]>fico:
                    fico=0
                    break
                else:
                    ty=ty+1
            else:
                ty=ty+1
                
    if fico>0:
        return fico
    else:
        return 0


#for q
def find_color2(max_rt):
    fico=0
    x=0
    ty=0
    if max_rt==1:
        while x<len(q):
            if q[x]>0 and q[x]<=13:
                if q[x]>fico:
                    fico=q[x]
                    x=x+1
                else:
                    x=x+1
            else:
                x=x+1
                
    elif max_rt==2:
        while x<len(q):
            if q[x]>13 and q[x]<=26:
                if q[x]>fico:
                    fico=q[x]
                    x=x+1
                else:
                    x=x+1
            else:
                x=x+1

    elif max_rt==3:
        while x<len(q):
            if q[x]>26 and q[x]<=39:
                if q[x]>fico:
                    fico=q[x]
                    x=x+1
                else:
                    x=x+1
            else:
                x=x+1

    elif max_rt==4:
        while x<len(q):
            if q[x]>39 and q[x]<=52:
                if q[x]>fico:
                    fico=q[x]
                    x=x+1
                else:
                    x=x+1
            else:
                x=x+1

    if fico>0 and fico<=13:
        while ty<len(space):
            if space[ty]>0 and space[ty]<=13:
                if space[ty]>fico:
                    fico=0
                    break
                else:
                    ty=ty+1
            else:
                ty=ty+1

    elif fico>13 and fico<=26:
        while ty<len(space):
            if space[ty]>13 and space[ty]<=26:
                if space[ty]>fico:
                    fico=0
                    break
                else:
                    ty=ty+1
            else:
                ty=ty+1                

    elif fico>26 and fico<=39:
        while ty<len(space):
            if space[ty]>26 and space[ty]<=39:
                if space[ty]>fico:
                    fico=0
                    break
                else:
                    ty=ty+1
            else:
                ty=ty+1

    elif fico>39 and fico<=52:
        while ty<len(space):
            if space[ty]>39 and space[ty]<=52:
                if space[ty]>fico:
                    fico=0
                    break
                else:
                    ty=ty+1
            else:
                ty=ty+1
                

    if fico>0:
        return fico
    else:
        return 0
# for r

def find_color3(max_rt):
    fico=0
    x=0
    ty=0
    if max_rt==1:
        while x<len(r):
            if r[x]>0 and r[x]<=13:
                if r[x]>fico:
                    fico=r[x]
                    x=x+1
                else:
                    x=x+1
            else:
                x=x+1
                
    elif max_rt==2:
        while x<len(r):
            if r[x]>13 and r[x]<=26:
                if r[x]>fico:
                    fico=r[x]
                    x=x+1
                else:
                    x=x+1
            else:
                x=x+1

    elif max_rt==3:
        while x<len(r):
            if r[x]>26 and r[x]<=39:
                if r[x]>fico:
                    fico=r[x]
                    x=x+1
                else:
                    x=x+1
            else:
                x=x+1

    elif max_rt==4:
        while x<len(r):
            if r[x]>39 and r[x]<=52:
                if r[x]>fico:
                    fico=r[x]
                    x=x+1
                else:
                    x=x+1
            else:
                x=x+1

    if fico>0 and fico<=13:
        while ty<len(space):
            if space[ty]>0 and space[ty]<=13:
                if space[ty]>fico:
                    fico=0
                    break
                else:
                    ty=ty+1
            else:
                ty=ty+1
    
    elif fico>13 and fico<=26:
        while ty<len(space):
            if space[ty]>13 and space[ty]<=26:
                if space[ty]>fico:
                    fico=0
                    break
                else:
                    ty=ty+1
            else:
                ty=ty+1                
    
    elif fico>26 and fico<=39:
        while ty<len(space):
            if space[ty]>26 and space[ty]<=39:
                if space[ty]>fico:
                    fico=0
                    break
                else:
                    ty=ty+1
            else:
                ty=ty+1
    
    elif fico>39 and fico<=52:
        while ty<len(space):
            if space[ty]>39 and space[ty]<=52:
                if space[ty]>fico:
                    fico=0
                    break
                else:
                    ty=ty+1
            else:
                ty=ty+1
                


    if fico>0:
        return fico
    else:
        return 0

def high_prev1():
    hg=0
    pre=0
    while hg<len(p):
        if p[hg]==13 or p[hg]==26 or p[hg]==39 or p[hg]==52:
            pre=p[hg]
            break
        else:
            hg=hg+1

    if pre>0:
        return pre
    else:
        return 0

def high_prev2():
    hg=0
    pre=0
    while hg<len(q):
        if q[hg]==13 or q[hg]==26 or q[hg]==39  or q[hg]==52:
            pre=q[hg]
            break
        else:
            hg=hg+1

    if pre>0:
        return pre
    else:
        return 0

#declare r
    
def high_prev3():
    hg=0
    pre=0
    while hg<len(r):
        if r[hg]==13 or r[hg]==26 or r[hg]==39 or r[hg]==52:
            pre=r[hg]
            break
        else:
            hg=hg+1

    if pre>0:
        return pre
    else:
        return 0


def clr_trmp(max_rt):
    i=0
    max_clr=0
    if max_rt==1:
        while i<4:
            if space[i]>0 and space[i]<=13:
                if space[i]>max_clr:
                    max_clr=space[i]
                    i=i+1
                else:
                    i=i+1
            else:
                i=i+1
    
    if max_rt==2:
        while i<4:
            if space[i]>13 and space[i]<=26:
                if space[i]>max_clr:
                    max_clr=space[i]
                    i=i+1
                else:
                    i=i+1
            else:
                i=i+1
    if max_rt==3:
        while i<4:
            if space[i]>26 and space[i]<=39:
                if space[i]>max_clr:
                    max_clr=space[i]
                    i=i+1
                else:
                    i=i+1
            else:
                i=i+1

    if max_rt==4:
        while i<4:
            if space[i]>39 and space[i]<=52:
                if space[i]>max_clr:
                    max_clr=space[i]
                    i=i+1
                else:
                    i=i+1
            else:
                i=i+1
    if max_clr>0:
        return max_clr
    else:
        return 0
    
    
def check(dg):
    s2=[]
    ik=0
    p=0
    global rm4
    if dg>0 and dg<=13:
        while ik<len(s):
            if s[ik]>0 and s[ik]<=13:
                s2.append(s[ik])
                ik=ik+1
            else:
                ik=ik+1
                
    elif dg>13 and dg<=26:
        while ik<len(s):
            if s[ik]>13 and s[ik]<=26:
                s2.append(s[ik])
                ik=ik+1
            else:
                ik=ik+1

    elif dg>26 and dg<=39:
        while ik<len(s):
            if s[ik]>26 and s[ik]<=39:
                s2.append(s[ik])
                ik=ik+1
            else:
                ik=ik+1

    elif dg>39 and dg<=52:
        while ik<len(s):
            if s[ik]>39 and s[ik]<=52:
                s2.append(s[ik])
                ik=ik+1
            else:
                ik=ik+1
                
    inpu=input("Play your card User:        ")
    print("")
    try:
        int(inpu)
        p=1
    except ValueError:
        print("")
        print("No no!! Please choose from your card only")
        print("")
        p=2
    if p==1:
        if int(inpu) in s:
            if int(inpu) in s2:
                rm4=int(inpu)
            else:
                if s2==[]:
                    rm4=int(inpu)
                else:
                    print("")
                    print("!!!Wrong choice of cards!!!")
                    print("")
                    check(dg)
        else:
            print("")
            print("No no!! Please choose from your card only")
            print("")
            check(dg)
    elif p==2:
        check(dg)
    while s2!=[]:
        s2.pop()

def check1():
    p=0
    global rm4
    inpu=input("Play your card User:        ")
    print("")
    try:
        int(inpu)
        p=1
    except ValueError:
        print("")
        print("No no!! Please choose from your card only")
        print("")
        p=2
    if p==1:
        if int(inpu) in s:
            rm4=int(inpu)
        else:
            print("")
            print("No no!! Please choose from your card only")
            print("")
            check1()
    elif p==2:
        check1()

def claim():
    cl=0
    clm1=0
    clm2=0
    clm3=0
    clm4=0
    color1=0
    color2=0
    color3=0
    np1=0
    np2=0
    np3=0
    global pits1
    global pits2
    global pits3
    global pits4
    if max_rt==1:
        while cl<13:
            if p[cl]>0 and p[cl]<13:
                color1=color1+1
            cl=cl+1
        if 12 in p and color1>1:
            clm1=clm1+1
            color1=color1-1
        #
        cl=0
        while cl<13:
            if p[cl]>13 and p[cl]<=26:
                np1=np1+1
                cl=cl+1
            else:
                cl=cl+1

        if 25 in p and np1>1 and np1<4:
            clm1=clm1+1

        if np1==0:
            if color1>=3:
                clm1=clm1+3
                color1=color1-3
            elif color1<3:
                clm1=clm1+color1
                color1=0
        elif np1==1:
            if color1>=2:
                clm1=clm1+2
                color1=color1-2
            elif color1<2:
                clm1=clm1+color1
                color1=0
        elif np1==2:
            if color1>=1:
                clm1=clm1+1
                color1=color1-1

    
        cl=0
        np1=0
        #
        while cl<13:
            if p[cl]>26 and p[cl]<=39:
                np1=np1+1
                cl=cl+1
            else:
                cl=cl+1

        if 38 in p and np1>1 and np1<4:
            clm1=clm1+1

        if np1==0:
            if color1>=3:
                clm1=clm1+3
                color1=color1-3
            elif color1<3:
                clm1=clm1+color1
                color1=0
        elif np1==1:
            if color1>=2:
                clm1=clm1+2
                color1=color1-2
            elif color1<2:
                clm1=clm1+color1
                color1=0
        elif np1==2:
            if color1>=1:
                clm1=clm1+1
                color1=color1-1
        cl=0
        np1=0
        #
        while cl<13:
            if p[cl]>39 and p[cl]<=52:
                np1=np1+1
                cl=cl+1
            else:
                cl=cl+1

        if 51 in p and np1>1 and np1<4:
            clm1=clm1+1

        if np1==0:
            if color1>=3:
                clm1=clm1+3
                color1=color1-3
            elif color1<3:
                clm1=clm1+color1
                color1=0
        elif np1==1:
            if color1>=2:
                clm1=clm1+2
                color1=color1-2
            elif color1<2:
                clm1=clm1+color1
                color1=0
        elif np1==2:
            if color1>=1:
                clm1=clm1+1
                color1=color1-1

        if color1>=3:
            clm1=clm1+(color1-2)

        #start q
        cl=0
        while cl<13:
            if q[cl]>0 and q[cl]<13:
                color2=color2+1
            cl=cl+1
        if 12 in q and color2>1:
            clm2=clm2+1
            color2=color2-1
        cl=0
        while cl<13:
            if q[cl]>13 and q[cl]<=26:
                np2=np2+1
                cl=cl+1
            else:
                cl=cl+1

        if 25 in q and np2>1 and np2<4:
            clm2=clm2+1

        if np2==0:
            if color2>=3:
                clm2=clm2+3
                color2=color2-3
            elif color2<3:
                clm2=clm2+color2
                color2=0
        elif np2==1:
            if color2>=2:
                clm2=clm2+2
                color2=color2-2
            elif color2<2:
                clm2=clm2+color2
                color2=0
        elif np2==2:
            if color2>=1:
                clm2=clm2+1
                color2=color2-1
        cl=0
        np2=0
        #
        while cl<13:
            if q[cl]>26 and q[cl]<=39:
                np2=np2+1
                cl=cl+1
            else:
                cl=cl+1

        if 38 in q and np2>1 and np2<4:
            clm2=clm2+1

        if np2==0:
            if color2>=3:
                clm2=clm2+3
                color2=color2-3
            elif color2<3:
                clm2=clm2+color2
                color2=0
        elif np2==1:
            if color2>=2:
                clm2=clm2+2
                color2=color2-2
            elif color2<2:
                clm2=clm2+color2
                color2=0
        elif np2==2:
            if color2>=1:
                clm2=clm2+1
                color2=color2-1
        cl=0
        np2=0
        #
        while cl<13:
            if q[cl]>39 and q[cl]<=52:
                np2=np2+1
                cl=cl+1
            else:
                cl=cl+1

        if 51 in q and np2>1 and np2<4:
            clm2=clm2+1

        if np2==0:
            if color2>=3:
                clm2=clm2+3
                color2=color2-3
            elif color2<3:
                clm2=clm2+color2
                color2=0
        elif np2==1:
            if color2>=2:
                clm2=clm2+2
                color2=color2-2
            elif color2<2:
                clm2=clm2+color2
                color2=0
        elif np2==2:
            if color2>=1:
                clm2=clm2+1
                color2=color2-1

        if color2>=3:
            clm2=clm2+(color2-2)
            
        #start r
        cl=0
        while cl<13:
            if r[cl]>0 and r[cl]<13:
                color3=color3+1
            cl=cl+1
        if 12 in r and color3>1:
            clm3=clm3+1
            color3=color3-1
        cl=0
        while cl<13:
            if r[cl]>13 and r[cl]<=26:
                np3=np3+1
                cl=cl+1
            else:
                cl=cl+1

        if 25 in r and np3>1 and np3<4:
            clm3=clm3+1

        if np3==0:
            if color3>=3:
                clm3=clm3+3
                color3=color3-3
            elif color3<3:
                clm3=clm3+color3
                color3=0
        elif np3==1:
            if color3>=2:
                clm3=clm3+2
                color3=color3-2
            elif color3<2:
                clm3=clm3+color3
                color3=0
        elif np3==2:
            if color3>=1:
                clm3=clm3+1
                color3=color3-1
        cl=0
        np3=0
        #
        while cl<13:
            if r[cl]>26 and r[cl]<=39:
                np3=np3+1
                cl=cl+1
            else:
                cl=cl+1

        if 38 in r and np3>1 and np3<4:
            clm3=clm3+1

        if np3==0:
            if color3>=3:
                clm3=clm3+3
                color3=color3-3
            elif color3<3:
                clm3=clm3+color3
                color3=0
        elif np3==1:
            if color3>=2:
                clm3=clm3+2
                color3=color3-2
            elif color3<2:
                clm3=clm3+color3
                color3=0
        elif np3==2:
            if color3>=1:
                clm3=clm3+1
                color3=color3-1
        cl=0
        np3=0
        #
        while cl<13:
            if r[cl]>39 and r[cl]<=52:
                np3=np3+1
                cl=cl+1
            else:
                cl=cl+1

        if 51 in r and np3>1 and np3<4:
            clm3=clm3+1

        if np3==0:
            if color3>=3:
                clm3=clm3+3
                color3=color3-3
            elif color3<3:
                clm3=clm3+color3
                color3=0
        elif np3==1:
            if color3>=2:
                clm3=clm3+2
                color3=color3-2
            elif color3<2:
                clm3=clm3+color3
                color3=0
        elif np3==2:
            if color3>=1:
                clm3=clm3+1
                color3=color3-1

        if color3>=3:
            clm3=clm3+(color3-2)
     ###       
    if max_rt==2:
        cl=0
        while cl<13:
            if p[cl]>13 and p[cl]<26:
                color1=color1+1
            cl=cl+1
        if 25 in p and color1>1:
            clm1=clm1+1
            color1=color1-1
        #
        cl=0
        while cl<13:
            if p[cl]>0 and p[cl]<=13:
                np1=np1+1
                cl=cl+1
            else:
                cl=cl+1

        if 12 in p and np1>1 and np1<4:
            clm1=clm1+1

        if np1==0:
            if color1>=3:
                clm1=clm1+3
                color1=color1-3
            elif color1<3:
                clm1=clm1+color1
                color1=0
        elif np1==1:
            if color1>=2:
                clm1=clm1+2
                color1=color1-2
            elif color1<2:
                clm1=clm1+color1
                color1=0
        elif np1==2:
            if color1>=1:
                clm1=clm1+1
                color1=color1-1
        cl=0
        np1=0
        #
        while cl<13:
            if p[cl]>26 and p[cl]<=39:
                np1=np1+1
                cl=cl+1
            else:
                cl=cl+1

        if 38 in p and np1>1 and np1<4:
            clm1=clm1+1

        if np1==0:
            if color1>=3:
                clm1=clm1+3
                color1=color1-3
            elif color1<3:
                clm1=clm1+color1
                color1=0
        elif np1==1:
            if color1>=2:
                clm1=clm1+2
                color1=color1-2
            elif color1<2:
                clm1=clm1+color1
                color1=0
        elif np1==2:
            if color1>=1:
                clm1=clm1+1
                color1=color1-1
        cl=0
        np1=0
        #
        while cl<13:
            if p[cl]>39 and p[cl]<=52:
                np1=np1+1
                cl=cl+1
            else:
                cl=cl+1

        if 51 in p and np1>1 and np1<4:
            clm1=clm1+1

        if np1==0:
            if color1>=3:
                clm1=clm1+3
                color1=color1-3
            elif color1<3:
                clm1=clm1+color1
                color1=0
        elif np1==1:
            if color1>=2:
                clm1=clm1+2
                color1=color1-2
            elif color1<2:
                clm1=clm1+color1
                color1=0
        elif np1==2:
            if color1>=1:
                clm1=clm1+1
                color1=color1-1


        if color1>=3:
            clm1=clm1+(color1-2)
        #start q
        cl=0
        while cl<13:
            if q[cl]>13 and q[cl]<26:
                color2=color2+1
            cl=cl+1
        if 25 in q and color2>1:
            clm2=clm2+1
            color2=color2-1
        cl=0
        while cl<13:
            if q[cl]>0 and q[cl]<=13:
                np2=np2+1
                cl=cl+1
            else:
                cl=cl+1

        if 12 in q and np2>1 and np2<4:
            clm2=clm2+1

        if np2==0:
            if color2>=3:
                clm2=clm2+3
                color2=color2-3
            elif color2<3:
                clm2=clm2+color2
                color2=0
        elif np2==1:
            if color2>=2:
                clm2=clm2+2
                color2=color2-2
            elif color2<2:
                clm2=clm2+color2
                color2=0
        elif np2==2:
            if color2>=1:
                clm2=clm2+1
                color2=color2-1
        cl=0
        np2=0
        #
        while cl<13:
            if q[cl]>26 and q[cl]<=39:
                np2=np2+1
                cl=cl+1
            else:
                cl=cl+1

        if 38 in q and np2>1 and np2<4:
            clm2=clm2+1

        if np2==0:
            if color2>=3:
                clm2=clm2+3
                color2=color2-3
            elif color2<3:
                clm2=clm2+color2
                color2=0
        elif np2==1:
            if color2>=2:
                clm2=clm2+2
                color2=color2-2
            elif color2<2:
                clm2=clm2+color2
                color2=0
        elif np2==2:
            if color2>=1:
                clm2=clm2+1
                color2=color2-1
        cl=0
        np2=0
        #
        while cl<13:
            if q[cl]>39 and q[cl]<=52:
                np2=np2+1
                cl=cl+1
            else:
                cl=cl+1

        if 51 in q and np2>1 and np2<4:
            clm2=clm2+1

        if np2==0:
            if color2>=3:
                clm2=clm2+3
                color2=color2-3
            elif color2<3:
                clm2=clm2+color2
                color2=0
        elif np2==1:
            if color2>=2:
                clm2=clm2+2
                color2=color2-2
            elif color2<2:
                clm2=clm2+color2
                color2=0
        elif np2==2:
            if color2>=1:
                clm2=clm2+1

        if color2>=3:
            clm2=clm2+(color2-2)
            
        #start r
        cl=0
        while cl<13:
            if r[cl]>13 and r[cl]<26:
                color3=color3+1
            cl=cl+1
        if 25 in r and color3>1:
            clm3=clm3+1
            color3=color3-1
        cl=0
        while cl<13:
            if r[cl]>0 and r[cl]<=13:
                np3=np3+1
                cl=cl+1
            else:
                cl=cl+1

        if 12 in r and np3>1 and np3<4:
            clm3=clm3+1

        if np3==0:
            if color3>=3:
                clm3=clm3+3
                color3=color3-3
            elif color3<3:
                clm3=clm3+color3
                color3=0
        elif np3==1:
            if color3>=2:
                clm3=clm3+2
                color3=color3-2
            elif color3<2:
                clm3=clm3+color3
                color3=0
        elif np3==2:
            if color3>=1:
                clm3=clm3+1
                color3=color3-1
        cl=0
        np3=0
        #
        while cl<13:
            if r[cl]>26 and r[cl]<=39:
                np3=np3+1
                cl=cl+1
            else:
                cl=cl+1

        if 38 in r and np3>1 and np3<4:
            clm3=clm3+1

        if np3==0:
            if color3>=3:
                clm3=clm3+3
                color3=color3-3
            elif color3<3:
                clm3=clm3+color3
                color3=0
        elif np3==1:
            if color3>=2:
                clm3=clm3+2
                color3=color3-2
            elif color3<2:
                clm3=clm3+color3
                color3=0
        elif np3==2:
            if color3>=1:
                clm3=clm3+1
                color3=color3-1
        cl=0
        np3=0
        #
        while cl<13:
            if r[cl]>39 and r[cl]<=52:
                np3=np3+1
                cl=cl+1
            else:
                cl=cl+1

        if 51 in r and np3>1 and np3<4:
            clm3=clm3+1

        if np3==0:
            if color3>=3:
                clm3=clm3+3
                color3=color3-3
            elif color3<3:
                clm3=clm3+color3
                color3=0
        elif np3==1:
            if color3>=2:
                clm3=clm3+2
                color3=color3-2
            elif color3<2:
                clm3=clm3+color3
                color3=0
        elif np3==2:
            if color3>=1:
                clm3=clm3+1
                color3=color3-1

        if color3>=3:
            clm3=clm3+(color3-2)
#####
        
    if max_rt==3:
        cl=0
        while cl<13:
            if p[cl]>26 and p[cl]<39:
                color1=color1+1
            cl=cl+1
        if 38 in p and color1>1:
            clm1=clm1+1
            color1=color1-1
        #
        cl=0
        while cl<13:
            if p[cl]>13 and p[cl]<=26:
                np1=np1+1
                cl=cl+1
            else:
                cl=cl+1

        if 25 in p and np1>1 and np1<4:
            clm1=clm1+1

        if np1==0:
            if color1>=3:
                clm1=clm1+3
                color1=color1-3
            elif color1<3:
                clm1=clm1+color1
                color1=0
        elif np1==1:
            if color1>=2:
                clm1=clm1+2
                color1=color1-2
            elif color1<2:
                clm1=clm1+color1
                color1=0
        elif np1==2:
            if color1>=1:
                clm1=clm1+1
                color1=color1-1
        cl=0
        np1=0
        #
        while cl<13:
            if p[cl]>0 and p[cl]<=13:
                np1=np1+1
                cl=cl+1
            else:
                cl=cl+1

        if 12 in p and np1>1 and np1<4:
            clm1=clm1+1

        if np1==0:
            if color1>=3:
                clm1=clm1+3
                color1=color1-3
            elif color1<3:
                clm1=clm1+color1
                color1=0
        elif np1==1:
            if color1>=2:
                clm1=clm1+2
                color1=color1-2
            elif color1<2:
                clm1=clm1+color1
                color1=0
        elif np1==2:
            if color1>=1:
                clm1=clm1+1
                color1=color1-1
        cl=0
        np1=0
        #
        while cl<13:
            if p[cl]>39 and p[cl]<=52:
                np1=np1+1
                cl=cl+1
            else:
                cl=cl+1

        if 51 in p and np1>1 and np1<4:
            clm1=clm1+1

        if np1==0:
            if color1>=3:
                clm1=clm1+3
                color1=color1-3
            elif color1<3:
                clm1=clm1+color1
                color1=0
        elif np1==1:
            if color1>=2:
                clm1=clm1+2
                color1=color1-2
            elif color1<2:
                clm1=clm1+color1
                color1=0
        elif np1==2:
            if color1>=1:
                clm1=clm1+1
                color1=color1-1

        if color1>=3:
            clm1=clm1+(color1-2)

        #start q
        cl=0
        while cl<13:
            if q[cl]>26 and q[cl]<39:
                color2=color2+1
            cl=cl+1
        if 38 in q and color2>1:
            clm2=clm2+1
            color2=color2-1
        cl=0
        while cl<13:
            if q[cl]>13 and q[cl]<=26:
                np2=np2+1
                cl=cl+1
            else:
                cl=cl+1

        if 25 in q and np2>1 and np2<4:
            clm2=clm2+1

        if np2==0:
            if color2>=3:
                clm2=clm2+3
                color2=color2-3
            elif color2<3:
                clm2=clm2+color2
                color2=0
        elif np2==1:
            if color2>=2:
                clm2=clm2+2
                color2=color2-2
            elif color2<2:
                clm2=clm2+color2
                color2=0
        elif np2==2:
            if color2>=1:
                clm2=clm2+1
                color2=color2-1
        cl=0
        np2=0
        #
        while cl<13:
            if q[cl]>0 and q[cl]<=13:
                np2=np2+1
                cl=cl+1
            else:
                cl=cl+1

        if 12 in q and np2>1 and np2<4:
            clm2=clm2+1

        if np2==0:
            if color2>=3:
                clm2=clm2+3
                color2=color2-3
            elif color2<3:
                clm2=clm2+color2
                color2=0
        elif np2==1:
            if color2>=2:
                clm2=clm2+2
                color2=color2-2
            elif color2<2:
                clm2=clm2+color2
                color2=0
        elif np2==2:
            if color2>=1:
                clm2=clm2+1
                color2=color2-1
        cl=0
        np2=0
        #
        while cl<13:
            if q[cl]>39 and q[cl]<=52:
                np2=np2+1
                cl=cl+1
            else:
                cl=cl+1

        if 51 in q and np2>1 and np2<4:
            clm2=clm2+1

        if np2==0:
            if color2>=3:
                clm2=clm2+3
                color2=color2-3
            elif color2<3:
                clm2=clm2+color2
                color2=0
        elif np2==1:
            if color2>=2:
                clm2=clm2+2
                color2=color2-2
            elif color2<2:
                clm2=clm2+color2
                color2=0
        elif np2==2:
            if color2>=1:
                clm2=clm2+1
                color2=color2-1

        if color2>=3:
            clm2=clm2+(color2-2)
        #start r
        cl=0
        while cl<13:
            if r[cl]>26 and r[cl]<39:
                color3=color3+1
            cl=cl+1
        if 38 in r and color3>1:
            clm3=clm3+1
            color3=color3-1
        cl=0
        while cl<13:
            if r[cl]>13 and r[cl]<=26:
                np3=np3+1
                cl=cl+1
            else:
                cl=cl+1

        if 25 in r and np3>1 and np3<4:
            clm3=clm3+1

        if np3==0:
            if color3>=3:
                clm3=clm3+3
                color3=color3-3
            elif color3<3:
                clm3=clm3+color3
                color3=0
        elif np3==1:
            if color3>=2:
                clm3=clm3+2
                color3=color3-2
            elif color3<2:
                clm3=clm3+color3
                color3=0
        elif np3==2:
            if color3>=1:
                clm3=clm3+1
                color3=color3-1
        cl=0
        np3=0
        #
        while cl<13:
            if r[cl]>0 and r[cl]<=13:
                np3=np3+1
                cl=cl+1
            else:
                cl=cl+1

        if 12 in r and np3>1 and np3<4:
            clm3=clm3+1

        if np3==0:
            if color3>=3:
                clm3=clm3+3
                color3=color3-3
            elif color3<3:
                clm3=clm3+color3
                color3=0
        elif np3==1:
            if color3>=2:
                clm3=clm3+2
                color3=color3-2
            elif color3<2:
                clm3=clm3+color3
                color3=0
        elif np3==2:
            if color3>=1:
                clm3=clm3+1
                color3=color3-1
        cl=0
        np3=0
        #
        while cl<13:
            if r[cl]>39 and r[cl]<=52:
                np3=np3+1
                cl=cl+1
            else:
                cl=cl+1

        if 51 in r and np3>1 and np3<4:
            clm3=clm3+1

        if np3==0:
            if color3>=3:
                clm3=clm3+3
                color3=color3-3
            elif color3<3:
                clm3=clm3+color3
                color3=0
        elif np3==1:
            if color3>=2:
                clm3=clm3+2
                color3=color3-2
            elif color3<2:
                clm3=clm3+color3
                color3=0
        elif np3==2:
            if color3>=1:
                clm3=clm3+1
                color3=color3-1

        if color3>=3:
            clm3=clm3+(color3-2)
                
    if max_rt==4:
        cl=0
        while cl<13:
            if p[cl]>39 and p[cl]<52:
                color1=color1+1
            cl=cl+1
        if 51 in p and color1>1:
            clm1=clm1+1
            color1=color1-1
        #
        cl=0
        while cl<13:
            if p[cl]>13 and p[cl]<=26:
                np1=np1+1
                cl=cl+1
            else:
                cl=cl+1

        if 25 in p and np1>1 and np1<4:
            clm1=clm1+1

        if np1==0:
            if color1>=3:
                clm1=clm1+3
                color1=color1-3
            elif color1<3:
                clm1=clm1+color1
                color1=0
        elif np1==1:
            if color1>=2:
                clm1=clm1+2
                color1=color1-2
            elif color1<2:
                clm1=clm1+color1
                color1=0
        elif np1==2:
            if color1>=1:
                clm1=clm1+1
                color1=color1-1
        cl=0
        np1=0
        #
        while cl<13:
            if p[cl]>26 and p[cl]<=39:
                np1=np1+1
                cl=cl+1
            else:
                cl=cl+1

        if 38 in p and np1>1 and np1<4:
            clm1=clm1+1

        if np1==0:
            if color1>=3:
                clm1=clm1+3
                color1=color1-3
            elif color1<3:
                clm1=clm1+color1
                color1=0
        elif np1==1:
            if color1>=2:
                clm1=clm1+2
                color1=color1-2
            elif color1<2:
                clm1=clm1+color1
                color1=0
        elif np1==2:
            if color1>=1:
                clm1=clm1+1
                color1=color1-1
        cl=0
        np1=0
        #
        while cl<13:
            if p[cl]>0 and p[cl]<=13:
                np1=np1+1
                cl=cl+1
            else:
                cl=cl+1

        if 12 in p and np1>1 and np1<4:
            clm1=clm1+1

        if np1==0:
            if color1>=3:
                clm1=clm1+3
                color1=color1-3
            elif color1<3:
                clm1=clm1+color1
                color1=0
        elif np1==1:
            if color1>=2:
                clm1=clm1+2
                color1=color1-2
            elif color1<2:
                clm1=clm1+color1
                color1=0
        elif np1==2:
            if color1>=1:
                clm1=clm1+1
                color1=color1-1

        if color1>=3:
            clm1=clm1+(color1-2)
        #start q
        cl=0
        while cl<13:
            if q[cl]>39 and q[cl]<52:
                color2=color2+1
            cl=cl+1
        if 38 in q and color2>1:
            clm2=clm2+1
            color2=color2-1
        cl=0
        while cl<13:
            if q[cl]>13 and q[cl]<=26:
                np2=np2+1
                cl=cl+1
            else:
                cl=cl+1

        if 25 in q and np2>1 and np2<4:
            clm2=clm2+1

        if np2==0:
            if color2>=3:
                clm2=clm2+3
                color2=color2-3
            elif color2<3:
                clm2=clm2+color2
                color2=0
        elif np2==1:
            if color2>=2:
                clm2=clm2+2
                color2=color2-2
            elif color2<2:
                clm2=clm2+color2
                color2=0
        elif np2==2:
            if color2>=1:
                clm2=clm2+1
                color2=color2-1
        cl=0
        np2=0
        #
        while cl<13:
            if q[cl]>26 and q[cl]<=39:
                np2=np2+1
                cl=cl+1
            else:
                cl=cl+1

        if 38 in q and np2>1 and np2<4:
            clm2=clm2+1

        if np2==0:
            if color2>=3:
                clm2=clm2+3
                color2=color2-3
            elif color2<3:
                clm2=clm2+color2
                color2=0
        elif np2==1:
            if color2>=2:
                clm2=clm2+2
                color2=color2-2
            elif color2<2:
                clm2=clm2+color2
                color2=0
        elif np2==2:
            if color2>=1:
                clm2=clm2+1
                color2=color2-1
        cl=0
        np2=0
        #
        while cl<13:
            if q[cl]>0 and q[cl]<=13:
                np2=np2+1
                cl=cl+1
            else:
                cl=cl+1

        if 12 in q and np2>1 and np2<4:
            clm2=clm2+1

        if np2==0:
            if color2>=3:
                clm2=clm2+3
                color2=color2-3
            elif color2<3:
                clm2=clm2+color2
                color2=0
        elif np2==1:
            if color2>=2:
                clm2=clm2+2
                color2=color2-2
            elif color2<2:
                clm2=clm2+color2
                color2=0
        elif np2==2:
            if color2>=1:
                clm2=clm2+1
                color2=color2-1

        if color2>=3:
            clm2=clm2+(color2-2)
        #start r
        cl=0
        while cl<13:
            if r[cl]>39 and r[cl]<52:
                color3=color3+1
            cl=cl+1
        if 38 in r and color3>1:
            clm3=clm3+1
            color3=color3-1
        cl=0
        while cl<13:
            if r[cl]>13 and r[cl]<=26:
                np3=np3+1
                cl=cl+1
            else:
                cl=cl+1

        if 25 in r and np3>1 and np3<4:
            clm3=clm3+1

        if np3==0:
            if color3>=3:
                clm3=clm3+3
                color3=color3-3
            elif color3<3:
                clm3=clm3+color3
                color3=0
        elif np3==1:
            if color3>=2:
                clm3=clm3+2
                color3=color3-2
            elif color3<2:
                clm3=clm3+color3
                color3=0
        elif np3==2:
            if color3>=1:
                clm3=clm3+1
                color3=color3-1
        cl=0
        np3=0
        #
        while cl<13:
            if r[cl]>26 and r[cl]<=39:
                np3=np3+1
                cl=cl+1
            else:
                cl=cl+1

        if 38 in r and np3>1 and np3<4:
            clm3=clm3+1

        if np3==0:
            if color3>=3:
                clm3=clm3+3
                color3=color3-3
            elif color3<3:
                clm3=clm3+color3
                color3=0
        elif np3==1:
            if color3>=2:
                clm3=clm3+2
                color3=color3-2
            elif color3<2:
                clm3=clm3+color3
                color3=0
        elif np3==2:
            if color3>=1:
                clm3=clm3+1
                color3=color3-1
        cl=0
        np3=0
        #
        while cl<13:
            if r[cl]>0 and r[cl]<=13:
                np3=np3+1
                cl=cl+1
            else:
                cl=cl+1

        if 12 in r and np3>1 and np3<4:
            clm3=clm3+1

        if np3==0:
            if color3>=3:
                clm3=clm3+3
                color3=color3-3
            elif color3<3:
                clm3=clm3+color3
                color3=0
        elif np3==1:
            if color3>=2:
                clm3=clm3+2
                color3=color3-2
            elif color3<2:
                clm3=clm3+color3
                color3=0
        elif np3==2:
            if color3>=1:
                clm3=clm3+1
                color3=color3-1

        if color3>=3:
            clm3=clm3+(color3-2)

    cl=0        
    while cl<13:
        if p[cl]==13 or p[cl]==26 or p[cl]==39 or p[cl]==52 :
            clm1=clm1+1
            cl=cl+1
        else:
            cl=cl+1
    cl=0
    while cl<13:
        if q[cl]==13 or q[cl]==26 or q[cl]==39 or q[cl]==52:
            clm2=clm2+1
            cl=cl+1
        else:
            cl=cl+1
    cl=0
    while cl<13:
        if r[cl]==13 or r[cl]==26 or r[cl]==39 or r[cl]==52:
            clm3=clm3+1
            cl=cl+1
        else:
            cl=cl+1

    usr_clm()
    #clm4=int(input("Claim your pits User: "))
    print("")
    pits1=clm1
    pits2=clm2
    pits3=clm3
    clm4=pits4
    print("1st player claim:    ",clm1,"pits")
    print("2nd player claim:    ",clm2,"pits")    
    print("3rd player claim:    ",clm3,"pits")
    print("User claim      :    ",clm4,"pits")
    print("")

def rndmax():
    p=space[0]
    i=0
    if p>0 and p<=13:
       while i<4:
           maxi=space[i]
           if maxi>=p and maxi<=13:
               p=maxi
               i=i+1
           else:
               i=i+1
                
    elif p>13 and p<=26:
        while i<4:
           maxi=space[i]
           if maxi>=p and maxi<=26:
               p=maxi
               i=i+1
           else:
               i=i+1

    elif p>26 and p<=39:
        while i<4:
           maxi=space[i]
           if maxi>=p and maxi<=39:
               p=maxi
               i=i+1
           else:
               i=i+1

    elif p>39 and p<=52:
        while i<4:
           maxi=space[i]
           if maxi>=p and maxi<=52:
               p=maxi
               i=i+1
           else:
               i=i+1
    popup=0
    while popup<4:
        space.pop(0)
        popup+=1
    return p

while scr1<100 and scr2<100 and scr3<100 and scr4<100:
    first=0
    second=0
    third=0
    forth=0
    max_rt=0
    max_rt=random.randint(1,4)
    if max_rt==1:
        print("color is between card no 1 to 13 ")
        print("")
    elif max_rt==2:
        print("color is between card no 14 to 26 ")
        print("")
    elif max_rt==3:
        print("color is between card no 27 to 39 ")
        print("")
    elif max_rt==4:
        print("color is between card no 40 to 52 ")
        print("")
    i=0
    while(i<13):
        a=random.randint(1,52)
        if(a not in p):
            p.append(a)
            i=i+1
    p.sort()
   # print("1st player card",p)
    i=0
    while(i<13):
        b=random.randint(1,52)
        if(b not in p and b not in q):
            q.append(b)
            i=i+1
    q.sort()
  #  print("2nd player card",q)

    i=0
    while(i<13):
        c=random.randint(1,52)
        if(c not in p and c not in q and c not in r):
            r.append(c)
            i=i+1
    r.sort()
 #   print("3rd player card",r)

    i=0
    while(i<13):
        d=random.randint(1,52)
        if(d not in p and d not in q and d not in r and d not in s):
            s.append(d)
            i=i+1
    s.sort()
    print("User your  cards",s)
    print("")
    claim()
    time.sleep(3)
    os.system('cls')
    print("User your  cards: ",s)
    print("")
    a=random.randint(1,4)
    ite=0
    while ite<13:
        b=random.randint(1,len(p))
        rm1=0
        rm2=0
        rm3=0
        rm4=0
        j=0
        prv=0
        fc1=0
        fc2=0
        fc3=0
        sp=0
        vc=0
        dg=0
        if(a==1):
            prv=high_prev1()
            if prv>0:
                rm1=prv
                p.remove(rm1)
            else:
                rm1=p.pop(b-1)
            print("1st player choose card no: ",rm1)
            space.append(rm1)
            if rm1>0 and rm1<=13:
                i=0
                while i<len(q):
                    if q[i]<=13 and q[i]>0 and q[i]>rm1:
                        rm2=q[i]
                        i=i+1
                    else:
                        i=i+1

                i=0
                if rm2<rm1:
                    while i<len(q):
                        if q[i]<=13 and q[i]>0 and q[i]<rm1:
                            rm2=q[i]
                            break
                        else:
                            i=i+1

                if rm2<=13 and rm2>0:
                    print("2nd player choose card no: ",rm2)
                    space.append(rm2)
                    q.remove(rm2)
                elif rm2==0:
                    fc2=find_color2(max_rt)
                    if fc2>0:
                        rm2=fc2
                        print("2nd player choose card no: ",rm2)
                        space.append(rm2)
                        q.remove(rm2)
                    else:
                        j=0
                        while j<len(q):
                            if q[j]==13 or q[j]==26 or q[j]==39 or q[j]==52 or q[j]==12 or q[j]==25 or q[j]==38 or q[j]==51:
                                j+=1
                            else:
                                rm2=q[j]
                                break
                        if rm2!=0:
                            print("2nd player choose card no: ",rm2)
                            space.append(rm2)
                            q.remove(rm2)
                        else:
                            rm2=q[0]
                            print("2nd player choose card no: ",rm2)
                            space.append(rm2)
                            q.remove(rm2)       
                else:
                    rm2=q[0]
                    print("2nd player choose card no: ",rm2)
                    space.append(rm2)
                    q.pop(0)
                
                i=0
                sp=spc(max_rt)
                if sp>0:
                    while i<len(r):
                        if r[i]<=13 and r[i]>0:
                            if max_rt!=1:
                                rm3=r[i]
                                break
                            else:
                                if r[i]>rm1 and r[i]>rm2:
                                    rm3=r[i]
                                    i=i+1
                                else:
                                    rm3=0
                                    i=i+1
                        else:
                            i=i+1
                else:
                    i=0
                    while i<len(r):
                        if r[i]<=13 and r[i]>0 and r[i]>rm1 and r[i]>rm2:
                            rm3=r[i]
                            i=i+1
                        else:
                            i=i+1

                i=0
                if rm3==0:
                    while i<len(r):
                        if r[i]<=13 and r[i]>0:
                            rm3=r[i]
                            break
                        else:
                            i=i+1

                if rm3>0 and rm3<=13:
                    print("3rd player choose card no: ",rm3)
                    space.append(rm3)
                    r.remove(rm3)
                elif rm3==0:
                    fc3=find_color3(max_rt)
                    if fc3>0:
                        rm3=fc3
                        print("3rd player choose card no: ",rm3)
                        space.append(rm3)
                        r.remove(rm3)
                    else:
                        j=0
                        while j<len(r):
                            if r[j]==13 or r[j]==26 or r[j]==39 or r[j]==52 or r[j]==25 or r[j]==38 or r[j]==12 or r[j]==51:
                                j+=1
                            else:
                                rm3=r[j]
                                break
                        if rm3!=0:
                            print("3rd player choose card no: ",rm3)
                            space.append(rm3)
                            r.remove(rm3)
                        else:
                            rm3=r[0]
                            print("3rd player choose card no: ",rm3)
                            space.append(rm3)
                            r.remove(rm3)
                else:
                    rm3=r[0]
                    print("3rd player choose card no: ",rm3)
                    space.append(rm3)
                    r.pop(0)
    
                i=0
                print("")
                dg=rm1
                check(dg)
                print("User choose card no:       ",rm4)
                print("")
                space.append(rm4)
                s.remove(rm4)
                print("New Bidding array: ",space)
                print("")
                time.sleep(3)
            elif rm1>13 and rm1<=26:
                i=0
                while i<len(q):
                    if q[i]<=26 and q[i]>13 and q[i]>rm1:
                        rm2=q[i]
                        i=i+1
                    else:
                        i=i+1

                i=0
                if rm2<rm1:
                    while i<len(q):
                        if q[i]<=26 and q[i]>13 and q[i]<rm1:
                            rm2=q[i]
                            break
                        else:
                            i=i+1

                if rm2>13 and rm2<=26:
                    print("2nd player choose card no: ",rm2)
                    space.append(rm2)
                    q.remove(rm2)
                elif rm2==0:
                    fc2=find_color2(max_rt)
                    if fc2>0:
                        rm2=fc2
                        print("2nd player choose card no: ",rm2)
                        space.append(rm2)
                        q.remove(rm2)
                    else:
                        j=0
                        while j<len(q):
                            if q[j]==13 or q[j]==26 or q[j]==39 or q[j]==52 or q[j]==12 or q[j]==25 or q[j]==38 or q[j]==51:
                                j+=1
                            else:
                                rm2=q[j]
                                break
                        if rm2!=0:
                            print("2nd player choose card no: ",rm2)
                            space.append(rm2)
                            q.remove(rm2)
                        else:
                            rm2=q[0]
                            print("2nd player choose card no: ",rm2)
                            space.append(rm2)
                            q.remove(rm2)       
                else:
                    rm2=q[0]
                    print("2nd player choose card no: ",rm2)
                    space.append(rm2)
                    q.pop(0)
    
                i=0
                sp=spc(max_rt)
                if sp>0:
                    while i<len(r):
                        if r[i]<=26 and r[i]>13:
                            if max_rt!=2:
                                rm3=r[i]
                                break
                            else:
                                if r[i]>rm1 and r[i]>rm2:
                                    rm3=r[i]
                                    i=i+1
                                else:
                                    rm3=0
                                    i=i+1
                        else:
                            i=i+1
                else:   
                    i=0
                    while i<len(r):
                        if r[i]<=26 and r[i]>13 and r[i]>rm1 and r[i]>rm2:
                            rm3=r[i]
                            i=i+1
                        else:
                            i=i+1
    
                i=0
                if rm3==0:
                    while i<len(r):
                        if r[i]<=26 and r[i]>13:
                            rm3=r[i]
                            break
                        else:
                            i=i+1
            
                if rm3>13 and rm3<=26:
                    print("3rd player choose card no: ",rm3)
                    space.append(rm3)
                    r.remove(rm3)
                elif rm3==0:
                    fc3=find_color3(max_rt)
                    if fc3>0:
                        rm3=fc3
                        print("3rd player choose card no: ",rm3)
                        space.append(rm3)
                        r.remove(rm3)
                    else:
                        j=0
                        while j<len(r):
                            if r[j]==13 or r[j]==26 or r[j]==39 or r[j]==52 or r[j]==12 or r[j]==25 or r[j]==38 or r[j]==51:
                                j+=1
                            else:
                                rm3=r[j]
                                break
                        if rm3!=0:
                            print("3rd player choose card no: ",rm3)
                            space.append(rm3)
                            r.remove(rm3)
                        else:
                            rm3=r[0]
                            print("3rd player choose card no: ",rm3)
                            space.append(rm3)
                            r.remove(rm3)
                else:
                    rm3=r[0]
                    print("3rd player choose card no: ",rm3)
                    space.append(rm3)
                    r.pop(0)
                i=0
                print("")
                dg=rm1
                check(dg)
                print("User choose card no:       ",rm4)
                print("")
                space.append(rm4)
                s.remove(rm4)
                print("New Bidding array: ",space)
                print("")
                time.sleep(3)

            elif rm1>26 and rm1<=39:
                i=0
                while i<len(q):
                    if q[i]<=39 and q[i]>26 and q[i]>rm1:
                        rm2=q[i]
                        i=i+1
                    else:
                        i=i+1

                i=0
                if rm2<rm1:
                    while i<len(q):
                        if q[i]<=39 and q[i]>26 and q[i]<rm1:
                            rm2=q[i]
                            break
                        else:
                            i=i+1

                if rm2>26 and rm2<=39:
                    print("2nd player choose card no: ",rm2)
                    space.append(rm2)
                    q.remove(rm2)
                elif rm2==0:
                    fc2=find_color2(max_rt)
                    if fc2>0:
                        rm2=fc2
                        print("2nd player choose card no: ",rm2)
                        space.append(rm2)
                        q.remove(rm2)
                    else:
                        j=0
                        while j<len(q):
                            if q[j]==13 or q[j]==26 or q[j]==39 or q[j]==52 or q[j]==12 or q[j]==25 or q[j]==38 or q[j]==51:
                                j+=1
                            else:
                                rm2=q[j]
                                break
                        if rm2!=0:
                            print("2nd player choose card no: ",rm2)
                            space.append(rm2)
                            q.remove(rm2)
                        else:
                            rm2=q[0]
                            print("2nd player choose card no: ",rm2)
                            space.append(rm2)
                            q.remove(rm2)       
                else:
                    rm2=q[0]
                    print("2nd player choose card no: ",rm2)
                    space.append(rm2)
                    q.pop(0)

                i=0
                sp=spc(max_rt)
                if sp>0:
                    while i<len(r):
                        if r[i]<=39 and r[i]>26:
                            if max_rt!=3:
                                rm3=r[i]
                                break
                            else:
                                if r[i]>rm1 and r[i]>rm2:
                                    rm3=r[i]
                                    i=i+1
                                else:
                                    rm3=0
                                    i=i+1
                        else:
                            i=i+1
                else:
                    i=0
                    while i<len(r):
                        if r[i]<=39 and r[i]>26 and r[i]>rm1 and r[i]>rm2:
                            rm3=r[i]
                            i=i+1
                        else:
                            i=i+1
    
                i=0
                if rm3==0:
                     while i<len(r):
                        if r[i]<=39 and r[i]>26:
                            rm3=r[i]
                            break
                        else:
                            i=i+1

                if rm3>26 and rm3<=39:
                    print("3rd player choose card no: ",rm3)
                    space.append(rm3)
                    r.remove(rm3)
                elif rm3==0:
                    fc3=find_color3(max_rt)
                    if fc3>0:
                        rm3=fc3
                        print("3rd player choose card no: ",rm3)
                        space.append(rm3)
                        r.remove(rm3)
                    else:
                        j=0
                        while j<len(r):
                            if r[j]==13 or r[j]==26 or r[j]==39 or r[j]==52 or r[j]==12 or r[j]==25 or r[j]==38 or r[j]==51:
                                j+=1
                            else:
                                rm3=r[j]
                                break
                        if rm3!=0:
                            print("3rd player choose card no: ",rm3)
                            space.append(rm3)
                            r.remove(rm3)
                        else:
                            rm3=r[0]
                            print("3rd player choose card no: ",rm3)
                            space.append(rm3)
                            r.remove(rm3)
                else:
                    rm3=r[0]
                    print("3rd player choose card no: ",rm3)
                    space.append(rm3)
                    r.pop(0)

                i=0
                print("")
                dg=rm1
                check(dg)
                print("User choose card no:       ",rm4)
                print("")
                space.append(rm4)
                s.remove(rm4)
                print("New Bidding array: ",space)
                print("")
                time.sleep(3)

            elif rm1>39 and rm1<=52:
                i=0
                while i<len(q):
                    if q[i]<=52 and q[i]>39 and q[i]>rm1:
                        rm2=q[i]
                        i=i+1
                    else:
                        i=i+1

                i=0
                if rm2<rm1:
                    while i<len(q):
                        if q[i]<=52 and q[i]>39 and q[i]<rm1:
                            rm2=q[i]
                            break
                        else:
                            i=i+1

                if rm2>39 and rm2<=52:
                    print("2nd player choose card no: ",rm2)
                    space.append(rm2)
                    q.remove(rm2)
                elif rm2==0:
                    fc2=find_color2(max_rt)
                    if fc2>0:
                        rm2=fc2
                        print("2nd player choose card no: ",rm2)
                        space.append(rm2)
                        q.remove(rm2)
                    else:
                        j=0
                        while j<len(q):
                            if q[j]==13 or q[j]==26 or q[j]==39 or q[j]==52 or q[j]==12 or q[j]==25 or q[j]==38 or q[j]==51:
                                j+=1
                            else:
                                rm2=q[j]
                                break
                        if rm2!=0:
                            print("2nd player choose card no: ",rm2)
                            space.append(rm2)
                            q.remove(rm2)
                        else:
                            rm2=q[0]
                            print("2nd player choose card no: ",rm2)
                            space.append(rm2)
                            q.remove(rm2)       
                else:
                    rm2=q[0]
                    print("2nd player choose card no: ",rm2)
                    space.append(rm2)
                    q.pop(0)

                i=0
                sp=spc(max_rt)
                if sp>0:
                    while i<len(r):
                        if r[i]<=52 and r[i]>39:
                            if max_rt!=4:
                                rm3=r[i]
                                break
                            else:
                                if r[i]>rm1 and r[i]>rm2:
                                    rm3=r[i]
                                    i=i+1
                                else:
                                    rm3=0
                                    i=i+1
                        else:
                            i=i+1
                else:
                    i=0
                    while i<len(r):
                        if r[i]<=52 and r[i]>39 and r[i]>rm1 and r[i]>rm2:
                            rm3=r[i]
                            i=i+1
                        else:
                            i=i+1
    
                i=0
                if rm3==0:
                    while i<len(r):
                        if r[i]<=52 and r[i]>39:
                            rm3=r[i]
                            break
                        else:
                            i=i+1

                if rm3>39 and rm3<=52:
                    print("3rd player choose card no: ",rm3)
                    space.append(rm3)
                    r.remove(rm3)
                elif rm3==0:
                    fc3=find_color3(max_rt)
                    if fc3>0:
                        rm3=fc3
                        print("3rd player choose card no: ",rm3)
                        space.append(rm3)
                        r.remove(rm3)
                    else:
                        j=0
                        while j<len(r):
                            if r[j]==13 or r[j]==26 or r[j]==39 or r[j]==52 or r[j]==12 or r[j]==25 or r[j]==38 or r[j]==51:
                                j+=1
                            else:
                                rm3=r[j]
                                break
                        if rm3!=0:
                            print("3rd player choose card no: ",rm3)
                            space.append(rm3)
                            r.remove(rm3)
                        else:
                            rm3=r[0]
                            print("3rd player choose card no: ",rm3)
                            space.append(rm3)
                            r.remove(rm3)
                else:
                    rm3=r[0]
                    print("3rd player choose card no: ",rm3)
                    space.append(rm3)
                    r.pop(0)

                i=0
                print("")
                dg=rm1
                check(dg)
                print("User choose card no:       ",rm4)
                print("")
                space.append(rm4)
                s.remove(rm4)
                print("New Bidding array: ",space)
                print("")
                time.sleep(3)

        elif(a==2):
            prv=high_prev2()
            if prv>0:
                rm2=prv
                q.remove(rm2)
            else:
                rm2=q.pop(b-1)
            print("2nd player choose card no: ",rm2)
            space.append(rm2)
            if rm2>0 and rm2<=13:
                i=0
                while i<len(p):
                    if p[i]<=13 and p[i]>0 and p[i]>rm2:
                        rm1=p[i]
                        i=i+1
                    else:
                        i=i+1

                i=0
                if rm1<rm2:
                    while i<len(p):
                        if p[i]<=13 and p[i]>0 and p[i]<rm2:
                            rm1=p[i]
                            break
                        else:
                            i=i+1
            
                if rm1<=13 and rm1>0:
                    print("1st player choose card no: ",rm1)
                    space.append(rm1)
                    p.remove(rm1)
                elif rm1==0:
                    fc1=find_color1(max_rt)
                    if fc1>0:
                        rm1=fc1
                        print("1st player choose card no: ",rm1)
                        space.append(rm1)
                        p.remove(rm1)
                    else:
                        j=0
                        while j<len(p):
                            if p[j]==13 or p[j]==26 or p[j]==39 or p[j]==52 or p[j]==12 or p[j]==25 or p[j]==38 or p[j]==51:
                                j+=1
                            else:
                                rm1=p[j]
                                break
                        if rm1!=0:
                            print("1st player choose card no: ",rm1)
                            space.append(rm1)
                            p.remove(rm1)
                        else:
                            rm1=p[0]
                            print("1st player choose card no: ",rm1)
                            space.append(rm1)
                            p.remove(rm1)       
                else:   
                    rm1=p[0]
                    print("1st player choose card no: ",rm1)
                    space.append(rm1)
                    p.pop(0)
                
                i=0
                sp=spc(max_rt)
                if sp>0:
                    while i<len(r):
                        if r[i]<=13 and r[i]>0:
                            if max_rt!=1:
                                rm3=r[i]
                                break
                            else:
                                if r[i]>rm1 and r[i]>rm2:
                                    rm3=r[i]
                                    i=i+1
                                else:
                                    rm3=0
                                    i=i+1
                        else:
                            i=i+1
                else:
                    i=0
                    while i<len(r):
                        if r[i]<=13 and r[i]>0 and r[i]>rm1 and r[i]>rm2:
                            rm3=r[i]
                            i=i+1
                        else:
                            i=i+1
    
                i=0
                if rm3==0:
                    while i<len(r):
                        if r[i]<=13 and r[i]>0:
                            rm3=r[i]
                            break
                        else:
                           i=i+1
            
                if rm3>0 and rm3<=13:
                    print("3rd player choose card no: ",rm3)
                    space.append(rm3)
                    r.remove(rm3)
                elif rm3==0:
                    fc3=find_color3(max_rt)
                    if fc3>0:
                        rm3=fc3
                        print("3rd player choose card no: ",rm3)
                        space.append(rm3)
                        r.remove(rm3)
                    else:   
                        j=0
                        while j<len(r):
                            if r[j]==13 or r[j]==26 or r[j]==39 or r[j]==52 or r[j]==12 or r[j]==25 or r[j]==38 or r[j]==51:
                                j+=1
                            else:
                                rm3=r[j]
                                break
                        if rm3!=0:
                            print("3rd player choose card no: ",rm3)
                            space.append(rm3)
                            r.remove(rm3)
                        else:
                            rm3=r[0]
                            print("3rd player choose card no: ",rm3)
                            space.append(rm3)
                            r.remove(rm3)
                else:
                    rm3=r[0]
                    print("3rd player choose card no: ",rm3)
                    space.append(rm3)
                    r.pop(0)

                i=0
                print("")
                dg=rm2
                check(dg)
                print("User choose card no:       ",rm4)
                print("")
                space.append(rm4)
                s.remove(rm4)
                print("New Bidding array: ",space)
                print("")
                time.sleep(3)
            
            elif rm2>13 and rm2<=26:
                i=0
                while i<len(p):
                    if p[i]<=26 and p[i]>13 and p[i]>rm2:
                        rm1=p[i]
                        i=i+1
                    else:
                        i=i+1
    
                i=0
                if rm1<rm2:
                    while i<len(p):
                        if p[i]<=26 and p[i]>13 and p[i]<rm2:
                            rm1=p[i]
                            break
                        else:
                            i=i+1
            
                if rm1>13 and rm1<=26:
                    print("1st player choose card no: ",rm1)
                    space.append(rm1)
                    p.remove(rm1)
                elif rm1==0:
                    fc1=find_color1(max_rt)
                    if fc1>0:
                        rm1=fc1
                        print("1st player choose card no: ",rm1)
                        space.append(rm1)
                        p.remove(rm1)
                    else:
                        j=0
                        while j<len(p):
                            if p[j]==13 or p[j]==26 or p[j]==39 or p[j]==52 or p[j]==12 or p[j]==25 or p[j]==38 or p[j]==51:
                                j+=1
                            else:
                                rm1=p[j]
                                break
                        if rm1!=0:
                            print("1st player choose card no: ",rm1)
                            space.append(rm1)
                            p.remove(rm1)
                        else:
                            rm1=p[0]
                            print("1st player choose card no: ",rm1)
                            space.append(rm1)
                            p.remove(rm1)       
                else:
                    rm1=p[0]
                    print("1st player choose card no: ",rm1)
                    space.append(rm1)
                    p.pop(0)
    
                i=0
                sp=spc(max_rt)
                if sp>0:
                    while i<len(r):
                        if r[i]<=26 and r[i]>13:
                            if max_rt!=2:
                                rm3=r[i]
                                break
                            else:
                                if r[i]>rm1 and r[i]>rm2:
                                    rm3=r[i]
                                    i=i+1
                                else:
                                    rm3=0
                                    i=i+1
                        else:
                            i=i+1
                else:
                    i=0
                    while i<len(r):
                        if r[i]<=26 and r[i]>13 and r[i]>rm1 and r[i]>rm2:
                            rm3=r[i]
                            i=i+1
                        else:
                            i=i+1

                i=0
                if rm3==0:
                    while i<len(r):
                        if r[i]<=26 and r[i]>13:
                            rm3=r[i]
                            break
                        else:
                            i=i+1
               
                if rm3>13 and rm3<=26:
                    print("3rd player choose card no: ",rm3)
                    space.append(rm3)
                    r.remove(rm3)
                elif rm3==0:
                    fc3=find_color3(max_rt)
                    if fc3>0:
                        rm3=fc3
                        print("3rd player choose card no: ",rm3)
                        space.append(rm3)
                        r.remove(rm3)
                    else:
                        j=0
                        while j<len(r):
                            if r[j]==13 or r[j]==26 or r[j]==39 or r[j]==52 or r[j]==12 or r[j]==25 or r[j]==38 or r[j]==51:
                                j+=1
                            else:
                                rm3=r[j]
                                break
                        if rm3!=0:
                            print("3rd player choose card no: ",rm3)
                            space.append(rm3)
                            r.remove(rm3)
                        else:
                            rm3=r[0]
                            print("3rd player choose card no: ",rm3)
                            space.append(rm3)
                            r.remove(rm3)
                else:
                    rm3=r[0]
                    print("3rd player choose card no: ",rm3)
                    space.append(rm3)
                    r.pop(0)

                i=0
                print("")
                dg=rm2
                check(dg)
                print("User choose card no:       ",rm4)
                print("")
                space.append(rm4)
                s.remove(rm4)
                print("New Bidding array: ",space)
                print("")
                time.sleep(3)
            elif rm2>26 and rm2<=39:
                i=0
                while i<len(p):
                    if p[i]<=39 and p[i]>26 and p[i]>rm2:
                        rm1=p[i]
                        i=i+1
                    else:
                        i=i+1
    
                i=0
                if rm1<rm2:
                    while i<len(p):
                        if p[i]<=39 and p[i]>26 and p[i]<rm2:
                            rm1=p[i]
                            break
                        else:
                            i=i+1
    
                if rm1>26 and rm1<=39:
                    print("1st player choose card no: ",rm1)
                    space.append(rm1)
                    p.remove(rm1)
                elif rm1==0:
                    fc1=find_color1(max_rt)
                    if fc1>0:
                        rm1=fc1
                        print("1st player choose card no: ",rm1)
                        space.append(rm1)
                        p.remove(rm1)
                    else:
                        j=0
                        while j<len(p):
                            if p[j]==13 or p[j]==26 or p[j]==39 or p[j]==52 or p[j]==12 or p[j]==25 or p[j]==38 or p[j]==51:
                                j+=1
                            else:
                                rm1=p[j]
                                break
    
                        if rm1!=0:
                            print("1st player choose card no: ",rm1)
                            space.append(rm1)
                            p.remove(rm1)
                        else:
                            rm1=p[0]
                            print("1st player choose card no: ",rm1)
                            space.append(rm1)
                            p.remove(rm1)       
                else:
                    rm1=p[0]
                    print("1st player choose card no: ",rm1)
                    space.append(rm1)
                    p.pop(0)
    
                i=0
                sp=spc(max_rt)
                if sp>0:
                    while i<len(r):
                        if r[i]<=39 and r[i]>26:
                            if max_rt!=3:
                                rm3=r[i]
                                break
                            else:
                                if r[i]>rm1 and r[i]>rm2:
                                    rm3=r[i]
                                    i=i+1
                                else:
                                    rm3=0
                                    i=i+1
                        else:
                            i=i+1
                else:
                    i=0
                    while i<len(r):
                        if r[i]<=39 and r[i]>26 and r[i]>rm1 and r[i]>rm2:
                            rm3=r[i]
                            i=i+1
                        else:
                            i=i+1
    
                i=0
                if rm3==0:
                    while i<len(r):
                        if r[i]<=39 and r[i]>26:
                            rm3=r[i]
                            break
                        else:
                            i=i+1
    
                if rm3>26 and rm3<=39:
                    print("3rd player choose card no: ",rm3)
                    space.append(rm3)
                    r.remove(rm3)
                elif rm3==0:
                    fc3=find_color3(max_rt)
                    if fc3>0:
                        rm3=fc3
                        print("3rd player choose card no: ",rm3)
                        space.append(rm3)
                        r.remove(rm3)
                    else:
                        j=0
                        while j<len(r):
                            if r[j]==13 or r[j]==26 or r[j]==39 or r[j]==52 or r[j]==12 or r[j]==25 or r[j]==38 or r[j]==51:
                                j+=1
                            else:
                                rm3=r[j]
                                break
                        
                        if rm3!=0:
                            print("3rd player choose card no: ",rm3)
                            space.append(rm3)
                            r.remove(rm3)
                        else:
                            rm3=r[0]
                            print("3rd player choose card no: ",rm3)
                            space.append(rm3)
                            r.remove(rm3)
                else:
                    rm3=r[0]
                    print("3rd player choose card no: ",rm3)
                    space.append(rm3)
                    r.pop(0)

                i=0
                print("")
                dg=rm2
                check(dg)
                print("User choose card no:       ",rm4)
                print("")
                space.append(rm4)
                s.remove(rm4)
                print("New Bidding array: ",space)
                print("")
                time.sleep(3)
    
            elif rm2>39 and rm2<=52:
                i=0
                while i<len(p):
                    if p[i]<=52 and p[i]>39 and p[i]>rm2:
                        rm1=p[i]
                        i=i+1
                    else:
                        i=i+1

                i=0
                if rm1<rm2:
                    while i<len(p):
                        if p[i]<=52 and p[i]>39 and p[i]<rm2:
                            rm1=p[i]
                            break
                        else:
                            i=i+1
    
                if rm1>39 and rm1<=52:
                    print("1st player choose card no: ",rm1)
                    space.append(rm1)
                    p.remove(rm1)
                elif rm1==0:
                    fc1=find_color1(max_rt)
                    if fc1>0:
                        rm1=fc1
                        print("1st player choose card no: ",rm1)
                        space.append(rm1)
                        p.remove(rm1)
                    else:
                        j=0
                        while j<len(p):
                            if p[j]==13 or p[j]==26 or p[j]==39 or p[j]==52 or p[j]==12 or p[j]==25 or p[j]==38 or p[j]==51:
                                j+=1
                            else:
                                rm1=p[j]
                                break
                        
                        if rm1!=0:
                            print("1st player choose card no: ",rm1)
                            space.append(rm1)
                            p.remove(rm1)
                        else:
                            rm1=p[0]
                            print("1st player choose card no: ",rm1)
                            space.append(rm1)
                            p.remove(rm1)       
                else:
                    rm1=p[0]
                    print("1st player choose card no: ",rm1)
                    space.append(rm1)
                    p.pop(0)

                i=0
                sp=spc(max_rt)
                if sp>0:
                    while i<len(r):
                        if r[i]<=52 and r[i]>39:
                            if max_rt!=4:
                                rm3=r[i]
                                break
                            else:
                                if r[i]>rm1 and r[i]>rm2:
                                    rm3=r[i]
                                    i=i+1
                                else:
                                    rm3=0
                                    i=i+1
                        else:
                            i=i+1
                else:
                    i=0
                    while i<len(r):
                        if r[i]<=52 and r[i]>39 and r[i]>rm1 and r[i]>rm2:
                            rm3=r[i]
                            i=i+1
                        else:
                            i=i+1

                i=0
                if rm3==0:
                    while i<len(r):
                        if r[i]<=52 and r[i]>39:
                            rm3=r[i]
                            break
                        else:
                            i=i+1
            
                if rm3>39 and rm3<=52:
                    print("3rd player choose card no: ",rm3)
                    space.append(rm3)
                    r.remove(rm3)
                elif rm3==0:
                    fc3=find_color3(max_rt)
                    if fc3>0:
                        rm3=fc3
                        print("3rd player choose card no: ",rm3)
                        space.append(rm3)
                        r.remove(rm3)
                    else:
                        j=0
                        while j<len(r):
                            if r[j]==13 or r[j]==26 or r[j]==39 or r[j]==52 or r[j]==12 or r[j]==25 or r[j]==38 or r[j]==51:
                                j+=1
                            else:
                                rm3=r[j]
                                break
                        if rm3!=0:
                            print("3rd player choose card no: ",rm3)
                            space.append(rm3)
                            r.remove(rm3)
                        else:
                            rm3=r[0]
                            print("3rd player choose card no: ",rm3)
                            space.append(rm3)
                            r.remove(rm3)
                else:   
                    rm3=r[0]
                    print("3rd player choose card no: ",rm3)
                    space.append(rm3)
                    r.pop(0)

                i=0
                print("")
                dg=rm2
                check(dg)
                print("User choose card no:       ",rm4)
                print("")
                space.append(rm4)
                s.remove(rm4)
                print("New Bidding array: ",space)
                print("")
                time.sleep(3)
    
        if(a==3):
            prv=high_prev3()
            if prv>0:
                rm3=prv
                r.remove(rm3)
            else:
                rm3=r.pop(b-1)
            print("3rd player choose card no: ",rm3)
            space.append(rm3)
            if rm3>0 and rm3<=13:
                i=0
                while i<len(q):
                    if q[i]<=13 and q[i]>0 and q[i]>rm3:
                        rm2=q[i]
                        i=i+1
                    else:
                        i=i+1

                i=0
                if rm2<rm3:
                    while i<len(q):
                        if q[i]<=13 and q[i]>0 and q[i]<rm3:
                            rm2=q[i]
                            break
                        else:
                            i=i+1
            
                if rm2<=13 and rm2>0:
                    print("2nd player choose card no: ",rm2)
                    space.append(rm2)
                    q.remove(rm2)
                elif rm2==0:
                    fc2=find_color2(max_rt)
                    if fc2>0:
                        rm2=fc2
                        print("2nd player choose card no: ",rm2)
                        space.append(rm2)
                        q.remove(rm2)
                    else:
                        j=0
                        while j<len(q):
                            if q[j]==13 or q[j]==26 or q[j]==39 or q[j]==52 or q[j]==12 or q[j]==25 or q[j]==38 or q[j]==51:
                                j+=1
                            else:
                                rm2=q[j]
                                break
                        if rm2!=0:
                            print("2nd player choose card no: ",rm2)
                            space.append(rm2)
                            q.remove(rm2)
                        else:
                            rm2=q[0]
                            print("2nd player choose card no: ",rm2)
                            space.append(rm2)
                            q.remove(rm2)       
                else:
                    rm2=q[0]
                    print("2nd player choose card no: ",rm2)
                    space.append(rm2)
                    q.pop(0)
                
                i=0
                sp=spc(max_rt)
                if sp>0:
                    while i<len(p):
                        if p[i]<=13 and p[i]>0:
                            if max_rt!=1:
                                rm1=p[i]
                                break
                            else:
                                if p[i]>rm3 and p[i]>rm2:
                                    rm1=p[i]
                                    i=i+1
                                else:
                                    rm1=0
                                    i=i+1
                        else:
                            i=i+1
                else:
                    i=0
                    while i<len(p):
                        if p[i]<=13 and p[i]>0 and p[i]>rm3 and p[i]>rm2:
                            rm1=p[i]
                            i=i+1
                        else:
                            i=i+1
    
                i=0
                if rm1==0:
                    while i<len(p):
                        if p[i]<=13 and p[i]>0:
                            rm1=p[i]
                            break
                        else:
                              i=i+1
               
                if rm1>0 and rm1<=13:
                    print("1st player choose card no: ",rm1)
                    space.append(rm1)
                    p.remove(rm1)
                elif rm1==0:
                    fc1=find_color1(max_rt)
                    if fc1>0:
                        rm1=fc1
                        print("1st player choose card no: ",rm1)
                        space.append(rm1)
                        p.remove(rm1)
                    else:
                        j=0
                        while j<len(p):
                            if p[j]==13 or p[j]==26 or p[j]==39 or p[j]==52 or p[j]==12 or p[j]==25 or p[j]==38 or p[j]==51:
                                j+=1
                            else:
                                rm1=p[j]
                                break
                        if rm1!=0:
                            print("1st player choose card no: ",rm1)
                            space.append(rm1)
                            p.remove(rm1)
                        else:
                            rm1=p[0]
                            print("1st player choose card no: ",rm1)
                            space.append(rm1)
                            p.remove(rm1)
                else:
                    rm1=p[0]
                    print("1st player choose card no: ",rm1)
                    space.append(rm1)
                    p.pop(0)

                i=0
                print("")
                dg=rm3
                check(dg)
                print("User choose card no:       ",rm4)
                print("")
                space.append(rm4)
                s.remove(rm4)
                print("New Bidding array: ",space)
                print("")
                time.sleep(3)
            
            elif rm3>13 and rm3<=26:
                i=0
                while i<len(q):
                    if q[i]<=26 and q[i]>13 and q[i]>rm3:
                        rm2=q[i]
                        i=i+1
                    else:
                        i=i+1

                i=0
                if rm2<rm3:
                    while i<len(q):
                        if q[i]<=26 and q[i]>13 and q[i]<rm3:
                            rm2=q[i]
                            break
                        else:
                            i=i+1

                if rm2>13 and rm2<=26:
                    print("2nd player choose card no: ",rm2)
                    space.append(rm2)
                    q.remove(rm2)
                elif rm2==0:
                    fc2=find_color2(max_rt)
                    if fc2>0:
                        rm2=fc2
                        print("2nd player choose card no: ",rm2)
                        space.append(rm2)
                        q.remove(rm2)
                    else:
                        j=0
                        while j<len(q):
                            if q[j]==13 or q[j]==26 or q[j]==39 or q[j]==52 or q[j]==12 or q[j]==25 or q[j]==38 or q[j]==51:
                                j+=1
                            else:
                                rm2=q[j]
                                break
                    
                        if rm2!=0:
                            print("2nd player choose card no: ",rm2)
                            space.append(rm2)
                            q.remove(rm2)
                        else:
                            rm2=q[0]
                            print("2nd player choose card no: ",rm2)
                            space.append(rm2)
                            q.remove(rm2)       
                else:   
                     rm2=q[0]  
                     print("2nd player choose card no: ",rm2)
                     space.append(rm2)
                     q.pop(0)
    
                i=0
                sp=spc(max_rt)
                if sp>0:
                    while i<len(p):
                        if p[i]<=26 and p[i]>13:
                            if max_rt!=2:
                                rm1=p[i]
                                break
                            else:
                                if p[i]>rm3 and p[i]>rm2:
                                    rm1=p[i]
                                    i=i+1
                                else:
                                    rm1=0
                                    i=i+1
                        else:
                            i=i+1
                else:
                    i=0
                    while i<len(p):
                        if p[i]<=26 and p[i]>13 and p[i]>rm3 and p[i]>rm2:
                            rm1=p[i]
                            i=i+1
                        else:   
                            i=i+1
    
                i=0
                if rm1==0:
                    while i<len(p):
                        if p[i]<=26 and p[i]>13:
                            rm1=p[i]
                            break
                        else:
                            i=i+1
    
                if rm1>13 and rm1<=26:
                    print("1st player choose card no: ",rm1)
                    space.append(rm1)
                    p.remove(rm1)
                elif rm1==0:
                    fc1=find_color1(max_rt)
                    if fc1>0:
                        rm1=fc1
                        print("1st player choose card no: ",rm1)
                        space.append(rm1)
                        p.remove(rm1)
                    else:
                        j=0
                        while j<len(p):
                            if p[j]==13 or p[j]==26 or p[j]==39 or p[j]==52 or p[j]==12 or p[j]==25 or p[j]==38 or p[j]==51:
                                j+=1
                            else:
                                rm1=p[j]
                                break
                        if rm1!=0:
                            print("1st player choose card no: ",rm1)
                            space.append(rm1)
                            p.remove(rm1)
                        else:
                            rm1=p[0]
                            print("1st player choose card no: ",rm1)
                            space.append(rm1)
                            p.remove(rm1)
                else:
                    rm1=p[0]
                    print("1st player choose card no: ",rm1)
                    space.append(rm1)
                    p.pop(0)

                i=0
                print("")
                dg=rm3
                check(dg)
                print("User choose card no:       ",rm4)
                print("")
                space.append(rm4)
                s.remove(rm4)
                print("New Bidding array: ",space)
                print("")
                time.sleep(3)
    
            elif rm3>26 and rm3<=39:
                i=0
                while i<len(q):
                    if q[i]<=39 and q[i]>26 and q[i]>rm3:
                        rm2=q[i]
                        i=i+1
                    else:
                        i=i+1
                i=0
    
                if rm2<rm3:
                    while i<len(q):
                        if q[i]<=39 and q[i]>26 and q[i]<rm3:
                            rm2=q[i]
                            break
                        else:
                            i=i+1
        
                if rm2>26 and rm2<=39:
                    print("2nd player choose card no: ",rm2)
                    space.append(rm2)
                    q.remove(rm2)
                elif rm2==0:
                    fc2=find_color2(max_rt)
                    if fc2>0:
                        rm2=fc2
                        print("2nd player choose card no: ",rm2)
                        space.append(rm2)
                        q.remove(rm2)
                    else:
                        j=0
                        while j<len(q):
                            if q[j]==13 or q[j]==26 or q[j]==39 or q[j]==52 or q[j]==12 or q[j]==25 or q[j]==38 or q[j]==51:
                                j+=1
                            else:
                                rm2=q[j]
                                break
    
                        if rm2!=0:
                            print("2nd player choose card no: ",rm2)
                            space.append(rm2)
                            q.remove(rm2)
                        else:
                            rm2=q[0]
                            print("2nd player choose card no: ",rm2)
                            space.append(rm2)
                            q.remove(rm2)       
                else:
                    rm2=q[0]
                    print("2nd player choose card no: ",rm2)
                    space.append(rm2)
                    q.pop(0)

                i=0
                sp=spc(max_rt)
                if sp>0:
                    while i<len(p):
                        if p[i]<=39 and p[i]>26:
                            if max_rt!=3:
                                rm1=p[i]
                                break
                            else:
                                if p[i]>rm3 and p[i]>rm2:
                                    rm1=p[i]
                                    i=i+1
                                else:
                                    rm1=0
                                    i=i+1
                        else:
                            i=i+1
                else:
                    i=0
                    while i<len(p):
                        if p[i]<=39 and p[i]>26 and p[i]>rm3 and p[i]>rm2:
                            rm1=p[i]
                            i=i+1
                        else:
                            i=i+1
    
                i=0
                if rm1==0:
                    while i<len(p):
                        if p[i]<=39 and p[i]>26:
                            rm1=p[i]
                            break
                        else:
                            i=i+1
    
                if rm1>26 and rm1<=39:
                    print("1st player choose card no: ",rm1)
                    space.append(rm1)
                    p.remove(rm1)
                elif rm1==0:
                    fc1=find_color1(max_rt)
                    if fc1>0:
                        rm1=fc1
                        print("1st player choose card no: ",rm1)
                        space.append(rm1)
                        p.remove(rm1)
                    else:
                        j=0
                        while j<len(p):
                            if p[j]==13 or p[j]==26 or p[j]==39 or p[j]==52 or p[j]==12 or p[j]==25 or p[j]==38 or p[j]==51:
                                j+=1
                            else:
                                rm1=p[j]
                                break
                        if rm1!=0:
                            print("1st player choose card no: ",rm1)
                            space.append(rm1)
                            p.remove(rm1)
                        else:
                            rm1=p[0]
                            print("1st player choose card no: ",rm1)
                            space.append(rm1)
                            p.remove(rm1)
                else:
                    rm1=p[0]
                    print("1st player choose card no: ",rm1)
                    space.append(rm1)
                    p.pop(0)

                i=0
                print("")
                dg=rm3
                check(dg)
                print("User choose card no:       ",rm4)
                print("")
                space.append(rm4)
                s.remove(rm4)
                print("New Bidding array: ",space)
                print("")
                time.sleep(3)
            elif rm3>39 and rm3<=52:
                i=0
                while i<len(q):
                    if q[i]<=52 and q[i]>39 and q[i]>rm3:
                        rm2=q[i]
                        i=i+1
                    else:
                        i=i+1
    
                i=0
                if rm2<rm3:
                    while i<len(q):
                        if q[i]<=52 and q[i]>39 and q[i]<rm3:
                            rm2=q[i]
                            break
                        else:
                            i=i+1
    
                if rm2>39 and rm2<=52:
                    print("2nd player choose card no: ",rm2)
                    space.append(rm2)
                    q.remove(rm2)
                elif rm2==0:
                    fc2=find_color2(max_rt)
                    if fc2>0:
                        rm2=fc2
                        print("2nd player choose card no: ",rm2)
                        space.append(rm2)
                        q.remove(rm2)
                    else:
                        j=0
                        while j<len(q):
                            if q[j]==13 or q[j]==26 or q[j]==39 or q[j]==52 or q[j]==12 or q[j]==25 or q[j]==38 or q[j]==51:
                                j+=1
                            else:
                                rm2=q[j]
                                break
                        
                        if rm2!=0:
                            print("2nd player choose card no: ",rm2)
                            space.append(rm2)
                            q.remove(rm2)
                        else:
                            rm2=q[0]
                            print("2nd player choose card no: ",rm2)
                            space.append(rm2)
                            q.remove(rm2)       
                else:   
                    rm2=q[0]
                    print("2nd player choose card no: ",rm2)
                    space.append(rm2)
                    q.pop(0)          
    
                i=0
                sp=spc(max_rt)
                if sp>0:
                    while i<len(p):
                        if p[i]<=52 and p[i]>39:
                            if max_rt!=4:
                                rm1=p[i]
                                break
                            else:
                                if p[i]>rm3 and p[i]>rm2:
                                    rm1=p[i]
                                    i=i+1
                                else:
                                    rm1=0
                                    i=i+1
                        else:
                            i=i+1
                else:   
                    i=0
                    while i<len(p):
                        if p[i]<=52 and p[i]>39 and p[i]>rm3 and p[i]>rm2:
                            rm1=p[i]
                            i=i+1
                        else:
                            i=i+1
    
                i=0
                if rm1==0:
                    while i<len(p):
                        if p[i]<=52 and p[i]>39:
                            rm1=p[i]
                            break
                        else:
                             i=i+1
        

                if rm1>39 and rm1<=52:
                    print("1st player choose card no: ",rm1)
                    space.append(rm1)
                    p.remove(rm1)
                elif rm1==0:
                    fc1=find_color1(max_rt)
                    if fc1>0:
                        rm1=fc1
                        print("1st player choose card no: ",rm1)
                        space.append(rm1)
                        p.remove(rm1)
                    else:
                        j=0
                        while j<len(p):
                            if p[j]==13 or p[j]==26 or p[j]==39 or p[j]==52 or p[j]==12 or p[j]==25 or p[j]==38 or p[j]==51:
                                j+=1
                            else:
                                rm1=p[j]
                                break
                        if rm1!=0:
                            print("1st player choose card no: ",rm1)  
                            space.append(rm1)
                            p.remove(rm1)
                        else:
                            rm1=p[0]
                            print("1st player choose card no: ",rm1)
                            space.append(rm1)
                            p.remove(rm1)
                else:
                    rm1=p[0]
                    print("1st player choose card no: ",rm1)
                    space.append(rm1)
                    p.pop(0)
    
                i=0
                print("")
                dg=rm3
                check(dg)
                print("User choose card no:       ",rm4)
                print("")
                space.append(rm4)
                s.remove(rm4)
                print("New Bidding array: ",space)
                print("")
                time.sleep(3)
        if(a==4):
            print("")
            check1()
            print("User choose card no:       ",rm4)
            print("")
            space.append(rm4)
            s.remove(rm4)
            time.sleep(3)
            if rm4>0 and rm4<=13:
                i=0
                while i<len(q):
                    if q[i]<=13 and q[i]>0 and q[i]>rm4:
                        rm2=q[i]
                        i=i+1
                    else:
                        i=i+1
    
                i=0
                if rm2<rm4:
                    while i<len(q):
                        if q[i]<=13 and q[i]>0 and q[i]<rm4:
                            rm2=q[i]
                            break
                        else:
                            i=i+1
    
                if rm2<=13 and rm2>0:
                    print("2nd player choose card no: ",rm2)
                    space.append(rm2)
                    q.remove(rm2)
                elif rm2==0:
                    fc2=find_color2(max_rt)
                    if fc2>0:
                        rm2=fc2
                        print("2nd player choose card no: ",rm2)
                        space.append(rm2)
                        q.remove(rm2)
                    else:
                        j=0
                        while j<len(q):
                            if q[j]==13 or q[j]==26 or q[j]==39 or q[j]==52 or q[j]==12 or q[j]==25 or q[j]==38 or q[j]==51:
                                j+=1
                            else:
                                rm2=q[j]
                                break
                        if rm2!=0:
                            print("2nd player choose card no: ",rm2)
                            space.append(rm2)
                            q.remove(rm2)
                        else:
                            rm2=q[0]
                            print("2nd player choose card no: ",rm2)
                            space.append(rm2)
                            q.remove(rm2)       
                else:
                    rm2=q[0]
                    print("2nd player choose card no: ",rm2)
                    space.append(rm2)
                    q.pop(0)
                    
                i=0
                sp=spc(max_rt)
                if sp>0:
                    while i<len(p):
                        if p[i]<=13 and p[i]>0:
                            if max_rt!=1:
                                rm1=p[i]
                                break
                            else:
                                if p[i]>rm4 and p[i]>rm2:
                                    rm1=p[i]
                                    i=i+1
                                else:
                                    rm1=0
                                    i=i+1
                        else:
                            i=i+1
                else:
                    i=0
                    while i<len(p):
                        if p[i]<=13 and p[i]>0 and p[i]>rm4 and p[i]>rm2:
                            rm1=p[i]
                            i=i+1
                        else:
                            i=i+1
    
                i=0
                if rm1==0:
                    while i<len(p):
                        if p[i]<=13 and p[i]>0:
                            rm1=p[i]
                            break
                        else:
                            i=i+1
    
                if rm1>0 and rm1<=13:
                    print("1st player choose card no: ",rm1)
                    space.append(rm1)
                    p.remove(rm1)
                elif rm1==0:
                    fc1=find_color1(max_rt)
                    if fc1>0:
                        rm1=fc1
                        print("1st player choose card no: ",rm1)
                        space.append(rm1)
                        p.remove(rm1)
                    else:
                        j=0
                        while j<len(p):
                            if p[j]==13 or p[j]==26 or p[j]==39 or p[j]==52 or p[j]==12 or p[j]==25 or p[j]==38 or p[j]==51:
                                j+=1
                            else:
                                 rm1=p[j]
                                 break
                        if rm1!=0:
                            print("1st player choose card no: ",rm1)
                            space.append(rm1)
                            p.remove(rm1)
                        else:
                            rm1=p[0]
                            print("1st player choose card no: ",rm1)
                            space.append(rm1)
                            p.remove(rm1)
                else:
                    rm1=p[0]
                    print("1st player choose card no: ",rm1)
                    space.append(rm1)
                    p.pop(0)

                i=0
                sp=spc1(max_rt)
                if sp>0:
                    while i<len(r):
                        if r[i]<=13 and r[i]>0:
                            if max_rt!=1:
                                rm3=r[i]
                                break
                            else:
                                if r[i]>rm4 and r[i]>rm2 and r[i]>rm1:
                                    rm3=r[i]
                                    i=i+1
                                else:
                                    rm3=0
                                    i=i+1
                        else:
                            i=i+1
                else:   
                    i=0
                    while i<len(r):
                        if r[i]<=13 and r[i]>0 and r[i]>rm4 and r[i]>rm2 and r[i]>rm1:
                            rm3=r[i]
                            i=i+1
                        else:
                            i=i+1

                i=0
                if rm3==0:
                    while i<len(r):
                        if r[i]<=13 and r[i]>0:
                            rm3=r[i]
                            break
                        else:
                            i=i+1
    

                if rm3>0 and rm3<=13:
                    print("3rd player choose card no: ",rm3)
                    space.append(rm3)
                    r.remove(rm3)
                elif rm3==0:
                    fc3=find_color3(max_rt)
                    if fc3>0:
                        rm3=fc3
                        print("3rd player choose card no: ",rm3)
                        space.append(rm3)
                        r.remove(rm3)
                    else:
                        j=0
                        while j<len(r):
                            if r[j]==13 or r[j]==26 or r[j]==39 or r[j]==52 or r[j]==12 or r[j]==25 or r[j]==38 or r[j]==51:
                                j+=1
                            else:
                                rm3=r[j]
                                break
                        if rm3!=0:
                            print("3rd player choose card no: ",rm3)
                            space.append(rm3)
                            r.remove(rm3)
                        else:
                            rm3=r[0]
                            print("3rd player choose card no: ",rm3)
                            space.append(rm3)
                            r.remove(rm3)
                else:
                    rm3=r[0]
                    print("3rd player choose card no: ",rm3)
                    space.append(rm3)
                    r.pop(0)

                time.sleep(3)
                print("")
                print("New Bidding array: ",space)
                print("")
                
            elif rm4>13 and rm4<=26:
                i=0
                while i<len(q):
                    if q[i]<=26 and q[i]>13 and q[i]>rm4:
                        rm2=q[i]
                        i=i+1
                    else:
                        i=i+1
    
                i=0
                if rm2<rm4:
                    while i<len(q):
                        if q[i]<=26 and q[i]>13 and q[i]<rm4:
                            rm2=q[i]
                            break
                        else:
                            i=i+1
    
                if rm2>13 and rm2<=26:
                    print("2nd player choose card no: ",rm2)
                    space.append(rm2)
                    q.remove(rm2)
                elif rm2==0:
                    fc2=find_color2(max_rt)
                    if fc2>0:
                        rm2=fc2
                        print("2nd player choose card no: ",rm2)
                        space.append(rm2)
                        q.remove(rm2)
                    else:
                        j=0
                        while j<len(q):
                            if q[j]==13 or q[j]==26 or q[j]==39 or q[j]==52 or q[j]==12 or q[j]==25 or q[j]==38 or q[j]==51:
                                j+=1
                            else:
                                rm2=q[j]
                                break
                            
                        if rm2!=0:
                            print("2nd player choose card no: ",rm2)
                            space.append(rm2)
                            q.remove(rm2)
                        else:
                            rm2=q[0]
                            print("2nd player choose card no: ",rm2)
                            space.append(rm2)
                            q.remove(rm2)       
                else:
                    rm2=q[0]
                    print("2nd player choose card no: ",rm2)
                    space.append(rm2)   
                    q.pop(0)
    
                i=0
                sp=spc(max_rt)
                if sp>0:
                    while i<len(p):
                        if p[i]<=26 and p[i]>13:
                            if max_rt!=2:
                                rm1=p[i]
                                break
                            else:
                                if p[i]>rm4 and p[i]>rm2:
                                    rm1=p[i]
                                    i=i+1
                                else:
                                    rm1=0
                                    i=i+1
                        else:
                            i=i+1
                else:
                    i=0
                    while i<len(p):
                        if p[i]<=26 and p[i]>13 and p[i]>rm4 and p[i]>rm2:
                            rm1=p[i]
                            i=i+1
                        else:
                            i=i+1
    
                i=0
                if rm1==0:
                    while i<len(p):
                        if p[i]<=26 and p[i]>13:
                            rm1=p[i]
                            break
                        else:
                            i=i+1

                if rm1>13 and rm1<=26:
                    print("1st player choose card no: ",rm1)  
                    space.append(rm1)
                    p.remove(rm1)
                elif rm1==0:
                    fc1=find_color1(max_rt)
                    if fc1>0:
                        rm1=fc1
                        print("1st player choose card no: ",rm1)
                        space.append(rm1)
                        p.remove(rm1)
                    else:
                        j=0
                        while j<len(p):
                            if p[j]==13 or p[j]==26 or p[j]==39 or p[j]==52 or p[j]==12 or p[j]==25 or p[j]==38 or p[j]==51:
                                j+=1
                            else:
                                rm1=p[j]
                                break
                        if rm1!=0:
                            print("1st player choose card no: ",rm1)
                            space.append(rm1)
                            p.remove(rm1)
                        else:
                            rm1=p[0]
                            print("1st player choose card no: ",rm1)
                            space.append(rm1)
                            p.remove(rm1)
                else:   
                    rm1=p[0]
                    print("1st player choose card no: ",rm1)
                    space.append(rm1)
                    p.pop(0)
    
                i=0
                sp=spc1(max_rt)
                if sp>0:
                    while i<len(r):
                        if r[i]<=26 and r[i]>13:
                            if max_rt!=2:
                                rm3=r[i]
                                break
                            else:
                                if r[i]>rm4 and r[i]>rm2 and r[i]>rm1:
                                    rm3=r[i]
                                    i=i+1
                                else:
                                    rm3=0
                                    i=i+1
                        else:
                            i=i+1
                else:
                    i=0
                    while i<len(r):
                        if r[i]<=26 and r[i]>13 and r[i]>rm4 and r[i]>rm2 and r[i]>rm1:
                            rm3=r[i]
                            i=i+1
                        else:
                            i=i+1
    
                i=0
                if rm3==0:
                    while i<len(r):
                        if r[i]<=26 and r[i]>13:
                            rm3=r[i]
                            break
                        else:
                            i=i+1
    
                if rm3>13 and rm3<=26:
                    print("3rd player choose card no: ",rm3)
                    space.append(rm3)
                    r.remove(rm3)
                elif rm3==0:
                    fc3=find_color3(max_rt)
                    if fc3>0:
                        rm3=fc3
                        print("3rd player choose card no: ",rm3)
                        space.append(rm3)
                        r.remove(rm3)
                    else:
                        j=0
                        while j<len(r):
                            if r[j]==13 or r[j]==26 or r[j]==39 or r[j]==52 or r[j]==12 or r[j]==25 or r[j]==38 or r[j]==51:
                                j+=1
                            else:
                                rm3=r[j]
                                break
                        if rm3!=0:
                            print("3rd player choose card no: ",rm3)
                            space.append(rm3)
                            r.remove(rm3)
                        else:
                            rm3=r[0]
                            print("3rd player choose card no: ",rm3)
                            space.append(rm3)
                            r.remove(rm3)
                else:
                    rm3=r[0]
                    print("3rd player choose card no: ",rm3)
                    space.append(rm3)
                    r.pop(0)

                time.sleep(3)
                print("")
                print("New Bidding array: ",space)
                print("")
            elif rm4>26 and rm4<=39:
                i=0
                while i<len(q):
                    if q[i]<=39 and q[i]>26 and q[i]>rm4:
                        rm2=q[i]
                        i=i+1
                    else:
                        i=i+1

                i=0
                if rm2<rm4:
                    while i<len(q):
                        if q[i]<=39 and q[i]>26 and q[i]<rm4:
                            rm2=q[i]
                            break
                        else:   
                            i=i+1
                
                if rm2>26 and rm2<=39:
                    print("2nd player choose card no: ",rm2)
                    space.append(rm2)
                    q.remove(rm2)
                elif rm2==0:
                    fc2=find_color2(max_rt)
                    if fc2>0:
                        rm2=fc2
                        print("2nd player choose card no: ",rm2)
                        space.append(rm2)
                        q.remove(rm2)
                    else:
                        j=0
                        while j<len(q):
                            if q[j]==13 or q[j]==26 or q[j]==39 or q[j]==52 or q[j]==12 or q[j]==25 or q[j]==38 or q[j]==51:
                                j+=1
                            else:
                                rm2=q[j]
                                break
    
                        if rm2!=0:
                            print("2nd player choose card no: ",rm2)
                            space.append(rm2)
                            q.remove(rm2)
                        else:
                            rm2=q[0]
                            print("2nd player choose card no: ",rm2)
                            space.append(rm2)
                            q.remove(rm2)       
                else:
                    rm2=q[0]
                    print("2nd player choose card no: ",rm2)
                    space.append(rm2)
                    q.pop(0)

                i=0
                sp=spc(max_rt)
                if sp>0:
                    while i<len(p):
                        if p[i]<=39 and p[i]>26:
                            if max_rt!=3:
                                rm1=p[i]
                                break
                            else:
                                if p[i]>rm4 and p[i]>rm2:
                                    rm1=p[i]
                                    i=i+1
                                else:
                                    rm1=0
                                    i=i+1
                        else:
                            i=i+1
                else:
                    i=0
                    while i<len(p):
                        if p[i]<=39 and p[i]>26 and p[i]>rm4 and p[i]>rm2:
                            rm1=p[i]
                            i=i+1
                        else:
                            i=i+1

                i=0
                if rm1==0:
                    while i<len(p):
                        if p[i]<=39 and p[i]>26:
                            rm1=p[i]
                            break
                        else:
                            i=i+1
                
                if rm1>26 and rm1<=39:
                    print("1st player choose card no: ",rm1)
                    space.append(rm1)
                    p.remove(rm1)
                elif rm1==0:
                    fc1=find_color1(max_rt)
                    if fc1>0:
                        rm1=fc1
                        print("1st player choose card no: ",rm1)
                        space.append(rm1)
                        p.remove(rm1)
                    else:
                        j=0
                        while j<len(p):
                            if p[j]==13 or p[j]==26 or p[j]==39 or p[j]==52 or p[j]==12 or p[j]==25 or p[j]==38 or p[j]==51:
                                j+=1
                            else:
                                rm1=p[j]
                                break
                        if rm1!=0:
                            print("1st player choose card no: ",rm1)
                            space.append(rm1)
                            p.remove(rm1)
                        else:
                            rm1=p[0]
                            print("1st player choose card no: ",rm1)
                            space.append(rm1)
                            p.remove(rm1)
                else:
                    rm1=p[0]
                    print("1st player choose card no: ",rm1)
                    space.append(rm1)
                    p.pop(0)

                i=0
                sp=spc1(max_rt)
                if sp>0:
                    while i<len(r):
                        if r[i]<=39 and r[i]>26:
                            if max_rt!=3:
                                rm3=r[i]
                                break
                            else:
                                if r[i]>rm4 and r[i]>rm2 and r[i]>rm1:
                                    rm3=r[i]
                                    i=i+1
                                else:
                                    rm3=0
                                    i=i+1
                        else:
                            i=i+1
                else:
                    i=0
                    while i<len(r):
                        if r[i]<=39 and r[i]>26 and r[i]>rm4 and r[i]>rm2 and r[i]>rm1:
                            rm3=r[i]
                            i=i+1
                        else:
                            i=i+1
    
                i=0
                if rm3==0:
                    while i<len(r):
                        if r[i]<=39 and r[i]>26:
                            rm3=r[i]
                            break
                        else:
                            i=i+1

                if rm3>26 and rm3<=39:
                    print("3rd player choose card no: ",rm3)
                    space.append(rm3)
                    r.remove(rm3)
                elif rm3==0:
                    fc3=find_color3(max_rt)
                    if fc3>0:
                        rm3=fc3
                        print("3rd player choose card no: ",rm3)
                        space.append(rm3)
                        r.remove(rm3)
                    else:
                        j=0
                        while j<len(r):
                            if r[j]==13 or r[j]==26 or r[j]==39 or r[j]==52 or r[j]==12 or r[j]==25 or r[j]==38 or r[j]==51:
                                j+=1
                            else:
                                rm3=r[j]
                                break
                        if rm3!=0:
                            print("3rd player choose card no: ",rm3)
                            space.append(rm3)
                            r.remove(rm3)
                        else:
                            rm3=r[0]
                            print("3rd player choose card no: ",rm3)
                            space.append(rm3)
                            r.remove(rm3)
                else:   
                    rm3=r[0]
                    print("3rd player choose card no: ",rm3)
                    space.append(rm3)
                    r.pop(0)

                time.sleep(3)
                print("")
                print("New Bidding array: ",space)
                print("")
            elif rm4>39 and rm4<=52:
                i=0
                while i<len(q):
                    if q[i]<=52 and q[i]>39 and q[i]>rm4:
                        rm2=q[i]
                        i=i+1
                    else:
                        i=i+1
    
                i=0
                if rm2<rm4:
                    while i<len(q):
                        if q[i]<=52 and q[i]>39 and q[i]<rm4:
                            rm2=q[i]
                            break
                        else:
                            i=i+1

                if rm2>39 and rm2<=52:
                    print("2nd player choose card no: ",rm2)
                    space.append(rm2)
                    q.remove(rm2)
                elif rm2==0:
                    fc2=find_color2(max_rt)
                    if fc2>0:
                        rm2=fc2
                        print("2nd player choose card no: ",rm2)
                        space.append(rm2)
                        q.remove(rm2)
                    else:
                        j=0
                        while j<len(q):
                            if q[j]==13 or q[j]==26 or q[j]==39 or q[j]==52 or q[j]==12 or q[j]==25 or q[j]==38 or q[j]==51:
                                j+=1
                            else:
                                rm2=q[j]
                                break
                        
                        if rm2!=0:
                            print("2nd player choose card no: ",rm2)
                            space.append(rm2)
                            q.remove(rm2)
                        else:
                            rm2=q[0]
                            print("2nd player choose card no: ",rm2)
                            space.append(rm2)
                            q.remove(rm2)       
                else:
                    rm2=q[0]
                    print("2nd player choose card no: ",rm2)
                    space.append(rm2)
                    q.pop(0)
    
                i=0
                sp=spc(max_rt)
                if sp>0:
                    while i<len(p):
                        if p[i]<=52 and p[i]>39:
                            if max_rt!=4:
                                rm1=p[i]
                                break
                            else:
                                if p[i]>rm4 and p[i]>rm2:
                                    rm1=p[i]
                                    i=i+1
                                else:
                                    rm1=0
                                    i=i+1
                        else:
                            i=i+1
                else:
                    i=0
                    while i<len(p):
                        if p[i]<=52 and p[i]>39 and p[i]>rm4 and p[i]>rm2:
                            rm1=p[i]
                            i=i+1
                        else:
                            i=i+1
    
                i=0
                if rm1==0:
                    while i<len(p):
                        if p[i]<=52 and p[i]>39:
                            rm1=p[i]
                            break
                        else:
                            i=i+1

                if rm1>39 and rm1<=52:
                    print("1st player choose card no: ",rm1)
                    space.append(rm1)
                    p.remove(rm1)
                elif rm1==0:    
                    fc1=find_color1(max_rt)
                    if fc1>0:
                        rm1=fc1
                        print("1st player choose card no: ",rm1)
                        space.append(rm1)
                        p.remove(rm1)
                    else:
                        j=0
                        while j<len(p):
                            if p[j]==13 or p[j]==26 or p[j]==39 or p[j]==52 or p[j]==12 or p[j]==25 or p[j]==38 or p[j]==51:
                                j+=1
                            else:
                                rm1=p[j]
                                break
                        if rm1!=0:
                            print("1st player choose card no: ",rm1)
                            space.append(rm1)
                            p.remove(rm1)
                        else:
                            rm1=p[0]
                            print("1st player choose card no: ",rm1)
                            space.append(rm1)
                            p.remove(rm1)
                else:
                    rm1=p[0]
                    print("1st player choose card no: ",rm1)
                    space.append(rm1)
                    p.pop(0)
                
                i=0
                sp=spc1(max_rt)
                if sp>0:
                    while i<len(r):
                        if r[i]<=52 and r[i]>39:
                            if max_rt!=4:
                                rm3=r[i]
                                break
                            else:
                                if r[i]>rm4 and r[i]>rm2 and r[i]>rm1:
                                    rm3=r[i]
                                    i=i+1
                                else:
                                    rm3=0
                                    i=i+1
                        else:
                            i=i+1
                else:
                    i=0
                    while i<len(r):
                        if r[i]<=52 and r[i]>39 and r[i]>rm4 and r[i]>rm2 and r[i]>rm1:
                            rm3=r[i]
                            i=i+1
                        else:
                            i=i+1
    
                i=0
                if rm3==0:
                    while i<len(r):
                        if r[i]<=52 and r[i]>39:
                            rm3=r[i]
                            break
                        else:
                            i=i+1
    
                if rm3>39 and rm3<=52:
                    print("3rd player choose card no: ",rm3)
                    space.append(rm3)
                    r.remove(rm3)
                elif rm3==0:
                    fc3=find_color3(max_rt)
                    if fc3>0:
                        rm3=fc3
                        print("3rd player choose card no: ",rm3)
                        space.append(rm3)
                        r.remove(rm3)
                    else:
                        j=0
                        while j<len(r):
                            if r[j]==13 or r[j]==26 or r[j]==39 or r[j]==52 or r[j]==12 or r[j]==25 or r[j]==38 or r[j]==51:
                                j+=1
                            else:
                                rm3=r[j]
                                break
                        if rm3!=0:
                            print("3rd player choose card no: ",rm3)
                            space.append(rm3)
                            r.remove(rm3)
                        else:
                            rm3=r[0]
                            print("3rd player choose card no: ",rm3)
                            space.append(rm3)
                            r.remove(rm3)
                else:
                    rm3=r[0]
                    print("3rd player choose card no: ",rm3)
                    space.append(rm3)
                    r.pop(0)

                time.sleep(3)
                print("")
                print("New Bidding array: ",space)
                print("")
        jkl=clr_trmp(max_rt)        
        if jkl==rm1:
            first+=1
            print("")
            print("1st player won this round   [Total=",first,"pits]")
            print("")
            space.pop()
            space.pop()
            space.pop()
            space.pop()
            a=1
            time.sleep(4)
            os.system('cls')
        elif jkl==rm2:
            second+=1
            print("")
            print("2nd player won this round   [Total=",second,"pits]")
            print("")
            space.pop()
            space.pop()
            space.pop()
            space.pop()
            a=2
            time.sleep(4)
            os.system('cls')
        elif jkl==rm3:
            third+=1
            print("")
            print("3rd player won this round   [Total=",third,"pits]")
            print("")
            space.pop()
            space.pop()
            space.pop()
            space.pop()
            a=3
            time.sleep(4)
            os.system('cls')
        elif jkl==rm4:
            forth+=1
            print("")
            print("User won this round          [Total=",forth,"pits]")
            print("")
            space.pop()
            space.pop()
            space.pop()
            space.pop() 
            a=4
            time.sleep(2)
            os.system('cls')

        elif jkl==0:
            hj=rndmax()
            if hj==rm1:
                first+=1
                print("")
                print("1st player won this round   [Total=",first,"pits]")
                print("")
                a=1
                time.sleep(4)
                os.system('cls')
            elif hj==rm2:
                second+=1
                print("")
                print("2nd player won this round   [Total=",second,"pits]")
                print("")
                a=2
                time.sleep(4)
                os.system('cls')
            elif hj==rm3:
                third+=1
                print("")
                print("3rd player won this round   [Total=",third,"pits]")
                print("")
                a=3
                time.sleep(4)
                os.system('cls')
            elif hj==rm4:
                forth+=1
                print("")
                print("User won this round          [Total=",forth,"pits]")
                print("")
                a=4
                time.sleep(2)
                os.system('cls')

        print("")
        if s!=[]:
            print("New cards for  User: ",s)
            print("")

        ite=ite+1
    os.system("cls")
    print("1st player claim ",pits1,"pits and get ",first,"pits")
    print("2nd player claim ",pits2,"pits and get ",second,"pits")
    print("3rd player claim ",pits3,"pits and get ",third,"pits")
    print("User claim       ",pits4,"pits and get ",forth,"pits")
    time.sleep(1)  
    scorecard()
    os.system("pause")
    os.system("cls")
