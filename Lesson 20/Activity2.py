class vehicle:
    def __init__(self, max_speed, milage):
        self.max_speed = max_speed
        self.milage = milage
modelX = vehicle(999, 21)
print ("ModelX Max Speed is:", modelX.max_speed)
print ("ModelX Milage is:", modelX.milage)