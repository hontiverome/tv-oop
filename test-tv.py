from television import TV
import time

# print the outputs: tv1's channel is 30 and volume level is 3, tv2's channel is 3 and volume level is 2
# television 1
# initializes class
def Television1():
    # makes use of class
    television1=TV(1,1)
    # turns tv 1 on
    television1.turn_on()
    # sets channel for television1 to 30
    television1.set_channel(30)
    # sets volume level for television1 to 7
    television1.set_volume(3)
    # prints output, also checks if tv is on.
    if television1.on:
        print(f"tv1's channel is {television1.get_channel()} and volume level is {television1.get_volume()}")
    else:
        print("Please turn television 1 on.")
    
# television 2
# initializes class
def Television2():
    # makes use of class
    television2=TV(1,1)
    # turns tv 1 on
    television2.turn_on()
    # sets channel for television1 to 3
    television2.set_channel(3)
    # sets volume level for television1 to 2
    television2.set_volume(2)
    # prints output, also checks if tv is on.
    if television2.on:
        print(f"tv2's channel is {television2.get_channel()} and volume level is {television2.get_volume()}")
    else:
        print("Please turn television 1 on.")

def Television3():
    # makes use of class
    television3=TV(1,1)
    # iterated switch on/off
    while True:
        power=str(input("\nTurn TV on? (y/n only)\n: "))
        if power=='y':
            television3.turn_on()
            print("You turned the TV on.")
            break
        elif power=='n':
            print("You did not turn the TV on.")
            break
        else:
            print("Invalid.")
    # iteration for channel and volume
    while True:
        option=int(input("\nWhat would you like to do?\n1: Set the Channel\n2: Set the Volume\n3: Channel Up\n4: Channel down\n5: Volume up\n6: Volume down\n7: Print the output.\n: "))
        if option==1:
            print("You chose option 1.")
            time.sleep(1)
            channel_no=int(input("Set the channel to? (1-120 only.)\n: "))
            television3.set_channel(channel_no)
            time.sleep(1)
        elif option==2:
            print("You chose option 2.")
            time.sleep(1)
            volume_level=int(input("Set the volume to? (1-7 only.)\n: "))
            television3.set_volume(volume_level)    
            time.sleep(1)
        elif option==3:
            print("You chose option 3.")
            time.sleep(1)
            television3.channel_up()
            time.sleep(1)
        elif option==4:
            print("You chose option 4.")
            time.sleep(1)
            television3.channel_down()
            time.sleep(1)    
        elif option==5:
            print("You chose option 5.")
            time.sleep(1)
            television3.volume_up()
            time.sleep(1)    

def Custom():
    while True:
        custom=str(input("\nWould you like to try setting up a Television (TV3) yourself? (y/n only)\n: "))
        if custom=='y':
            Television3()
        elif custom=='n':
            print("Thank you!")
            exit()
        else:
            print("Invalid.")
            
            

Television1()
Television2()
Custom()


