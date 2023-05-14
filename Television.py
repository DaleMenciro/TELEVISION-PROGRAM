'''
Acquire these arguments
channel - must be an int and current channel should range from 1-120
volumeLevel- must be an int and current volume level should range be from 1-7
on - must be a bool, either on/off.
'''
class TV:
    def __init__(self):
        self.channel = 1 #Channel 1 to be default
        self.volume_level = 1 #Volume 1 to be the dafault
        self.on = False # TV is off at default

    def turn_on(self) -> None:
        self.on = True #True to turn on TV
        
    def turn_off(self) -> None:
        self.on = False #False to turn off TV

    def get_channel(self) -> int:
        return self.channel

    def set_channel(self,channel_number) -> int:
        if channel_number >= 1 and channel_number <= 120: #Set channel to new value within the range (1-120)
            self.channel = channel_number
    
    def get_volume(self) -> int:
        return self.volume_level

    def set_volume(self,volume_level) -> int:
        if volume_level >= 1 and volume_level <= 7: #Set volume level to new value within the range (1-7)
            self.volume_level = volume_level

    def channel_up(self) -> None:
        if self.channel < 120: #Increase the channel by 1, return min value (1) if exceeds max value (120)
            self.channel += 1
        else:
            self.channel = 1

    def channel_down(self) -> None: #Decrease the channel by 1, return to max value (120) if at min value (1)
        if self.channel > :
            self.channel -= 1
        else:
            self.channel = 120
    
    def volume_up(self) -> None: 
        if self.volume_level < 7: #Increase the channel by 1, return min value (1) if exceeds max value (7)
            self.volume_level += 1
        else:
            self.volume_level = 1

    def volume_down(self) -> None: 
        if self.volume_level > 1: #Decrease the channel by 1, return to max value (7) if at min value (1)
            self.volume_level -= 1
        else:
            self.volume_level = 7