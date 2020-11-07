import time,random
k=0
print("---------------------------------Welcome to the Game of Cricket------------------------------")
def main():
    Players=[]
    for i in range(1,3):
        Players.append(input(f"Enter player{i} name\n"))
    overs = int(input("Enter number overs\n"))
    print("-----------------Toss starts in 10 seconds 😍------------------")
    for i in range(10,0,-1):
         print("\r"+str(i))
         time.sleep(1)

    print(f"Coin is in the hands of {Players[0]}")
    time.sleep(1)
    a = random.choice(['Heads', 'Tails'])
    print(f"{a} is the call")
    time.sleep(1)
    b = random.choice(['Heads','Tails'])
    print(f"{b} ups")
    time.sleep(1)
    if a==b:
        print(f"{Players[1]} wins the toss")
        time.sleep(1)
        c = random.choice(['Bat','Bowl'])
        print(f"and choose to {c} first")
        if c=='Bat':
            t=Players[1]
        else:
            t=Players[0]
    else:
        print(f"{Players[0]} wins the toss")
        time.sleep(1)
        c = random.choice(['Bat','Bowl'])
        print(f"and choose to {c} first")
        if c=='Bat':
            t=Players[0]
        else:
            t=Players[1]
    time.sleep(1)
    print(f"-----------------------{t.upper()} is on the strike---------------------------")
    time.sleep(1)
    runs = score1 = 0
    for i in range(overs):
        x = random.randint(1,6)
        for j in range(1,7):
            input("Press Enter to Bowl")
            if j==x:
                out = random.choice(['Yes','No'])
                if out=='Yes':
                    x=0
                    print("HOWZZZATTT!!!!!!!!!!!!!!!")
                    time.sleep(1)
                    break
            runs = random.randint(0,6)
            if runs == 4:
                print("Brilliant! It\'s a Four")
                time.sleep(1)
            if runs == 6:
                print("Hurray!!! Great it\'s a Six")
                time.sleep(1)
            score1 = score1 + runs
            print(f"score = {score1}")
            if j==6:
                print(f"Over = {str(i+1)+'.'+str(0)}")
            else:
                print(f"Over = {str(i)+'.'+str(j)}")
            time.sleep(1)
        if x==0:
            print(f"{t} got out on {score1}")
            break
    if t==Players[0]:
        l=Players[1]
    else:
        l=Players[0]
    time.sleep(1)
    print(f"-----------------------Now {l.upper()} is on the strike---------------------------")
    time.sleep(1)
    runs = score2 = 0
    for i in range(overs):
        x = random.randint(1,6)
        for j in range(1,7):
            input("Press Enter to Bowl")
            if j==x:
                out = random.choice(['Yes','No'])
                if out=='Yes':
                    x=0
                    print("HOWZZZATTT!!!!!!!!!!!!!!!")
                    time.sleep(1)
                    break
            runs = random.randint(0,6)
            if runs == 4:
                print("Brilliant! It\'s a Four")
                time.sleep(1)
            if runs == 6:
                print("Hurray!!! Great it\'s a Six")
                time.sleep(1)
            score2 = score2 + runs
            print(f"score = {score2}")
            if j==6:
                print(f"Over = {str(i+1)+'.'+str(0)}")
            else:
                print(f"Over = {str(i)+'.'+str(j)}")
            time.sleep(1)
        if x==0:
            print(f"{l} got out on {score2}")
            break
    time.sleep(1)
    print("---------------------------------Results of the Match---------------------------------------------")
    if score2>score1:
        print(f"{l.upper()} WON THE MATCH BY {score2 - score1} run")
    elif score1>score2:
        print(f"{t.upper()} WON THE MATCH BY {score1 - score2} run")
    else:
        print(f"MATCH TIED AT A SCORE OF {score2}")
        
while 1:
    if k==0:
        k=1
        main()
    else:
        print("Do you wanna play again ?")
        a = input("------------------press 1 for Yes or 0 for No--------------------\n")
        if a=='1':
            main()
        elif a=='0':
            exit()
        else:
            print("Wrong input")