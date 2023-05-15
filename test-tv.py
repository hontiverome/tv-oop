from television import TV

# print the outputs: tv1's channel is 30 and volume level is 3, tv2's channel is 3 and volume level is 2
# television 1
# initializes class
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


