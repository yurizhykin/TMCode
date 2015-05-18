class Tape:
    """
    Tape is a list of cells that contain symbols of the current machine;
    """
    def __init__(self, init, endsym):
        self._cells = list(init)
        self._endsym = endsym
        self._current = 0

    def __str__(self):
        return str(self._cells)

    # -----> begin 'current_cell' property
    # pointer to the cell that is currently under
    # the head
    @property
    def current_cell(self):
        return self._cells[self._current]
    @current_cell.setter
    def current_cell(self, val):
        self._cells[self._current] = val
    # <----- end 'current_cell' property

    def shift_left(self):
        if self._current >= len(self._cells):
            self._cells += [self._endsym]
        self._current += 1

    def shift_right(self):
        if self._current == 0:
            self._cells = [self._endsym] + self._cells
        else:
            self._current -= 1
                
