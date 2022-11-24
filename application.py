import time
from yeelight import Bulb
from yeelight import discover_bulbs
from yeelight import LightType

# just hardcoded the IP address of my bulb
bulb = Bulb("192.168.0.179")
discoMode = False

# function to let the bulb change color every second
def discoMode():
    bulb.set_brightness(100)
    discoMode = True
    while discoMode:
        bulb.set_rgb(255, 0, 0)
        time.sleep(1)
        bulb.set_rgb(0, 255, 0)
        time.sleep(1)
        bulb.set_rgb(0, 0, 255)
        time.sleep(1)
    return discoMode

def stopDiscoMode():
    discoMode = False
    return discoMode

# function to turn the bulb on
def turnOn():
    try:
        bulb.turn_on()
        return True
    except:
        return False


# function to turn the bulb off
def turnOff():
    try:
        bulb.turn_off()
        return True
    except:
        return False

# function to set the brightness of the bulb
def setBrightness(brightness):
    try:
        bulb.set_brightness(brightness, light_type=LightType.Ambient)
        return True
    except:
        return False

# function to set the rgb of the bulb
def setRGB(red, green, blue):
    try:
        bulb.set_rgb(red, green, blue)
        return True
    except:
        return False

# function to get the rgb of the bulb
def getRGB():
    try:
        return bulb.get_properties()['rgb']
    except:
        return False

# function to get the brightness of the bulb
def getBrightness():
    try:
        return bulb.get_properties()['bright']
    except:
        return False

# function to get the state of the bulb
def getState():
    try:
        return bulb.get_properties()['power']
    except:
        return False

# function to set the state of the bulb
def setState(state):
    try:
        if state == "on":
            bulb.turn_on()
            return True
        elif state == "off":
            bulb.turn_off()
            return True
        else:
            return False
    except:
        return False