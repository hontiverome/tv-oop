# Given: A UML Class Diagram: 
# Required: Create a Python Code for creating the Class named TV and a Test Driver program named TestTV that 
# will create two objects from Class TV and will #produce the following output:
# tv1's channel is 30 and volume level is 3
# tv2's channel is 3 and volume level is 2

# Create class television
class Television:
    def __init__(self) -> None:
        # Create attributes 
        self.channel:1
        self.volume_level:1
        self.on:False

# Create methods:
# turn_on
def turn_on(self):
    self.on=True
    
# turn_off
def turn_off(self):
    self.on=False
    
# get_channel
# set_channel
# get_volume
# set_volume
# channel_up
# channel_down
# volume_up
# volume_down