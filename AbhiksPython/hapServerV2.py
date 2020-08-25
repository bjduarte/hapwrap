from websocket import create_connection
import json
import time

class hapserver2:
    def __init__(self,ip = "192.168.43.24"):
        self.ws = create_connection("ws://"+ ip +"/ws")

    def sendBWFrame(self,lit, size, intensity):
        frame = {}
        r = [0]*size
        g = [0]*size
        b = [0]*size

        for l in lit:
            r[l]=intensity
            g[l]=intensity
            b[l]=intensity
        
        frame['red'] = r
        frame['blue'] = b
        frame['green'] = g

        print(json.dumps(frame))
        self.ws.send(json.dumps(frame))
        time.sleep(.5)#adjust latency fore reliabilityX
        print("Sent")

        
