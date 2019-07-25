import time

from color import HSV as hsv
from grid import TriangleGrid
from .showbase import ShowBase


class CycleHSV(ShowBase):
    def __init__(self, tri_grid: TriangleGrid, frame_delay: float = 0.1):
        self.tri_grid = tri_grid
        self.frame_delay = frame_delay
        self.n_cells = len(self.tri_grid.cells)
#        from IPython import embed; embed()

    def next_frame(self):

        self.tri_grid.clear()
        time.sleep(3)
        
            #Up through V to full white, then up the red axis to max S, then around the color wheel at max S&V.                                                       
        self.cb= hsv(0.0,0.0,0.5)
        
        while self.cb.s < 1.0:
            self.cb.s += 0.01
            self.tri_grid.set_all_cells(self.cb)
            self.tri_grid.go()
            time.sleep(.01)
            print('HSV:', self.cb.hsv, "...RGB:", self.cb.rgb, "...RGBW:", self.cb.rgbw)
            while self.cb.h < 1.0:
                self.cb.h += 0.008
                self.tri_grid.set_all_cells(self.cb)
                self.tri_grid.go()
                time.sleep(.01)
                print('HSV:', self.cb.hsv, "...RGB:", self.cb.rgb, "...RGBW:", self.cb.rgbw)
            self.cb.h = 0.0

        self.tri_grid.clear()
        time.sleep(3)


        while True:
<<<<<<< HEAD
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
=======
            ca = hsv(0.0, 0.0, 0.0)
            while ca.v < 1.0:
                ca.v += 0.0008
                self.tri_grid.set_all_cells(ca)
                self.tri_grid.go()
                time.sleep(.01)
                print('CA', ca.hsv)

            while ca.s < 1.0:
                ca.s += 0.0008
                self.tri_grid.set_all_cells(ca)
                self.tri_grid.go()
                time.sleep(.01)
                print('CA', ca.hsv)

            while ca.h < 1.0:
                ca.h += 0.0008
                self.tri_grid.set_all_cells(ca)
                self.tri_grid.go()
                time.sleep(.01)
                print('CA', ca.hsv)
>>>>>>> b8b8601ed9f11d6eb2ba9c1278bd3e8e5746fbd0

            self.tri_grid.clear()
            time.sleep(3)

<<<<<<< HEAD


=======
>>>>>>> b8b8601ed9f11d6eb2ba9c1278bd3e8e5746fbd0
            yield self.frame_delay
