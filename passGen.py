import random
import time

lenChoice = [4,5,6,7,8,9]
valChoice = [1,2,3,4,5,6,7,8,9,,0,'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','!','@','#','$','%','^','&','*','(',')']

class password:
    def Create(self, lenCreate):
        a = 1
        print("New password: ")
        while a <= lenCreate:
            val = random.choice(valChoice)  #random value is chosen
            assert isinstance(val, object)      #then printed in a sequence
            print(val)
            a += 1
    def Time(self, t):
        assert t > 0
        while t >= 0:
            print("Deleting new password in " + str(t)) #user has a designated
            time.sleep(1)                                   #amount of time to commit the
            t -= 1                                          #given password to memory

def main():
    p = password()
    choiceLen = raw_input("Designate a password length? (y/n): ") #user has the option to
    if choiceLen == 'y':                                            #create a custom password length
        lenDes = input("Desired password length: ")
        assert isinstance(lenDes, object)
        p.Create(lenDes)
    elif choiceLen == 'n':
        long = random.choice(lenChoice) #if user doesn't designate a password length
        assert isinstance(long, object)     #the computer chooses a random length between
        p.Create(long)                      #4 and 9
    time.sleep(5)   #user is given 5 seconds before
    b = 5               #the countdown timer begins
    p.Time(5)   #given password is deleted after a designated amount of time

main()