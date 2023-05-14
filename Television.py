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

    def set_volume(self,volume_level) -> int:

    def channel_uP(self) -> None:

    def channel_down(self) -> None:
    
    def volume_up(self) -> None:

    def volume_down(self) -> None: