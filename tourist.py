class tourist(object):
    def __init__(self, row, column, onfield):
        self.row=row
        self.column=column
        self.onfield=onfield
        self.turns_since_no_bear=0
        self.turns_since_bear=1000
        self.bears_seen=0
    def pos(self):
        return (self.row,self.column)
    def __str__(self):
        return 'Tourist at ({},{}), {} turns without seeing a bear.'.format(self.row,self.column,self.turns_since_no_bear)
    def take_turn(self):
        if self.onfield:
            if self.bears_seen==0:
                self.turns_since_no_bear+=1
            if self.bears_seen>0:
                self.turns_since_no_bear=0
        if self.bears_seen>=3 or self.turns_since_no_bear>=3:
            self.onfield=False
        

        