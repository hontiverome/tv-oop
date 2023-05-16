from television import TV

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

def custom():
    while True:
        custom=str(input("\n\nWould you like to try setting up a TV yourself? (y/n only)"))
        if custom=='y':
            
            

Television1()
Television2()


