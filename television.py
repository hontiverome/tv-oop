# Given: A UML Class Diagram:
# Required: Create a Python Code for creating the Class named TV and a Test Driver program named TestTV that
# will create two objects from Class TV and will #produce the following output:
# tv1's channel is 30 and volume level is 3
# tv2's channel is 3 and volume level is 2

# Create class television
class TV:
    def __init__(self, channel_no, volume) -> None:
        # Create attributes
        self.channel = channel_no
        self.volume_level = volume
        self.on = False

    # Create methods:

    # turn_on
    def turn_on(self):
        self.on = True

    # turn_off
    def turn_off(self):
        self.on = False

    # get_channel
    def get_channel(self):
        return self.channel

    # set_channel (channels are only within 1 and 120 only)
    def set_channel(self, channel_no):
        try:
            if channel_no < 1 or channel_no > 120:
                print ("Channels are between 1 and 120 only.")
            else:
                self.channel = int(channel_no)
                print(f"Channel has been set to {channel_no}")
        except:
            raise ValueError(
                "Integers only.\nChannels are between 1 and 120 only.")

    # get_volume
    def get_volume(self):
        return self.volume_level

    # set_volume (volume levels are between 1 and 7 only)
    def set_volume(self, volume):
        try:
            if volume < 1 or volume > 7:
                print ("Volume levels are between 1 and 7 only.")
            else:
                self.volume_level = int(volume)
                print(f"Volume level has been set to {volume}")
        except:
            raise ValueError(
                "Integers only.\nVolume levels are between 1 and 7 only.")

    # channel_up
    def channel_up(self):
        try:
            if self.channel < 120:
                self.channel += 1
                print("Channel has been increased by 1")
            else:
                print("Channels are between 1 and 120 only.")
        except:
            raise ValueError("Integers only.\nChannels are between 1 and 120 only.")

    # channel_down
    def channel_down(self):
        try:
            if self.channel > 1:
                self.channel -= 1
                print("Channel has been decreased by 1")  
            else:
                print("Channels are between 1 and 120 only.")
        except:
            raise ValueError("Integers only.\nChannels are between 1 and 120 only.")

    # volume_up
    def volume_up(self):
        try:
            if self.volume_level < 7:
                self.volume_level += 1
                print("Volume level has been increased by 1")  
            else:
                print ("Volume levels are between 1 and 7 only.")
        except:
            raise ValueError("Integers only.\nVolume levels are between 1 and 7 only.")

    # volume_down
    def volume_down(self):
        try:
            if self.volume_level > 1:
                self.volume_level -= 1
                print("Volume level has been decreased by 1")  
            else:
                print("Volume levels are between 1 and 7 only.")
        except:
            raise ValueError("Integers only.\nVolume levels are between 1 and 7 only.")
            

# HONTIVEROS, JEROME ANDREI O.
# BSCPE 1-5
