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
def get_channel(self):
    return self.channel

# set_channel (channels are only within 1 and 120 only)
def set_channel(self):
    try:
        if channel_no<1 or channel_no>120:
            raise ValueError("Channels are between 1 and 120 only.")
        self.channel=int(channel_no)
    except:
        raise ValueError("Integers only.\nChannels are between 1 and 120 only.")
    
# get_volume
def get_volume(self):
    return self.volume_level

# set_volume (volume levels are between 1 and 7 only)

# channel_up
# channel_down
# volume_up
# volume_down