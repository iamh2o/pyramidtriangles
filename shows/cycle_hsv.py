from .showbase import ShowBase
from color import HSV as hsv

import random as rnd
import time

class CycleHSV(ShowBase):
    def __init__(self, tri_grid, frame_delay = 0.1):
        self.tri_grid = tri_grid
        self.frame_delay = frame_delay
        self.n_cells = len(self.tri_grid.get_cells())
#        from IPython import embed; embed()


    def next_frame(self):

        self.tri_grid.clear()
        time.sleep(3)
        

        while True:
            #Up through V to full white, then up the red axis to max S, then around the color wheel at max S&V.
            self.cb= hsv(0.0,0.0,0.0)

            while self.cb.v < 1.0:
                self.cb.v += 0.0008
                self.tri_grid.set_all_cells(self.cb)
                self.tri_grid.go()
                time.sleep(.01)
                print('HSV:', self.cb.hsv, "...RGB:", self.cb.rgb, "...RGBW:", self.cb.rgbw)


            while self.cb.s < 1.0:
                self.cb.s += 0.0008
                self.tri_grid.set_all_cells(self.cb)
                self.tri_grid.go()
                time.sleep(.01)
                print('HSV:', self.cb.hsv, "...RGB:", self.cb.rgb, "...RGBW:", self.cb.rgbw)


            while self.cb.h < 1.0:
                self.cb.h += 0.0008
                self.tri_grid.set_all_cells(self.cb)
                self.tri_grid.go()
                time.sleep(.01)
                print('HSV:', self.cb.hsv, "...RGB:", self.cb.rgb, "...RGBW:", self.cb.rgbw)

            self.tri_grid.clear()
            time.sleep(3)
            
                        
            #Up through V to full white, then up the red axis to max S, then around the color wheel at max S&V.                      
            self.cb= hsv(0.0,0.0,0.5)

            while self.cb.s < 1.0:
                self.cb.s += 0.0008
                self.tri_grid.set_all_cells(self.cb)
                self.tri_grid.go()
                time.sleep(.01)
                print('HSV:', self.cb.hsv, "...RGB:", self.cb.rgb, "...RGBW:", self.cb.rgbw)
                while self.cb.h < 1.0:
                    self.cb.h += 0.0008
                    self.tri_grid.set_all_cells(self.cb)
                    self.tri_grid.go()
                    time.sleep(.01)
                    print('HSV:', self.cb.hsv, "...RGB:", self.cb.rgb, "...RGBW:", self.cb.rgbw)
                self.cb.h = 0.0

            self.tri_grid.clear()
            time.sleep(3)




            yield self.frame_delay
