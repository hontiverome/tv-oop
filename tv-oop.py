# Given: A UML Class Diagram: 
# Required: Create a Python Code for creating the Class named TV and a Test Driver program named TestTV that 
# will create two objects from Class TV and will #produce the following output:
# tv1's channel is 30 and volume level is 3
# tv2's channel is 3 and volume level is 2

# Create class television
class Television:
    def __init__(self) -> None:
        # Create attributes 
        self.channel=channel_no
        self.volume_level=volume
        self.on=False

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
def set_channel(self, channel_no):
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
def set_volume(self, volume):
    try:
        if volume<1 or volume>7:
            raise ValueError("Volume levels are between 1 and 7 only.")
        self.volume_level=volume
    except:
        raise ValueError("Integers only.\nVolume levels are between 1 and 7 only.")
    
# channel_up
def channel_up(self):
    try:
        if self.channel<120:
            self.channel+=1
        else:
            raise ValueError("Channels  are between 1 and 120 only.")
    except:
        raise ValueError("Integers only.\nChannels are between 1 and 120 only.")
    
# channel_down
def channel_down(self):
    try:
        if self.channel>1:
            self.channel-=1
        else:
            raise ValueError("Chanells are are between 1 and 120 only.")
    except:
        raise ValueError("Integers only.\nChannels are between 1 and 120 only.")
    
# volume_up
# volume_down