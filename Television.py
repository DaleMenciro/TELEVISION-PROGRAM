'''
Acquire these arguments
channel - must be an int and current channel should range from 1-120
volumeLevel- must be an int and current volume level should range be from 1-7
on - must be a bool, either on/off.
'''
class TV:
    def __init__(self):
        self.channel = 1 #Channel 1 to be default
        self.volumeLevel = 1 #Volume 1 to be the dafault
        self.on = False # TV is off at default
