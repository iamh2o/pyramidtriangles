from .showbase import ShowBase
from color import RGB


class UpDown(ShowBase):
    def __init__(self, tri_grid, frame_delay=2):
        self.tri_grid = tri_grid
        self.frame_delay = frame_delay

    def next_frame(self):
        a = "up"

        while True:
            self.tri_grid.clear()

            if a == "up":
                print('up')
                for i in self.tri_grid.get_up_cells():
                    print("Up", i.get_id())
                    self.tri_grid.set_cell_by_cellid(i.get_id(), RGB( 0, 255, 255))

            else:
                print('down')
                for i in self.tri_grid.get_down_cells():
                    print("down", i.get_id())
                    self.tri_grid.set_cell_by_cellid(i.get_id(), RGB( 255, 0, 200))


            if a == "up":
                a = "down"
            else:
                a = "up"
            self.tri_grid.go()
            yield self.frame_delay
