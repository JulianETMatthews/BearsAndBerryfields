class bear(object):
    def __init__(self, row, column, direction, onfield):
        self.row=row
        self.column=column
        self.direction=direction
        self.onfield=onfield
        self.asleepcount=0
        self.tourist_on_spot=False
        self.num_eaten=0
        self.killed=False
    def pos(self):
        return (self.row,self.column)
    def __str__(self):
        return 'Bear at ({},{}) moving {}'.format(self.row,self.column,self.direction)
    def move(self):
        if 'N' in self.direction:
            self.row-=1
        if 'S' in self.direction:
            self.row+=1
        if 'E' in self.direction:
            self.column+=1
        if 'W' in self.direction:
            self.column-=1

    def take_turn(self, tourist_there, numrows, numcolumns, berryfield):
        berryfield.removeberry(2)
        
        self.killed=False
        if self.onfield==False:
            return
        if tourist_there:
            self.killed=True
            self.asleepcount=3
        else:
            if self.asleepcount>0:
                self.asleepcount-=1
            self.num_eaten+=1
            if self.asleepcount==0:
                self.move()
        if self.row<0 or self.column<0 or self.row>numrows-1 or self.column>numcolumns-1:
            self.onfield=False
            self.row=numrows-1
            self.column=numcolumns-1