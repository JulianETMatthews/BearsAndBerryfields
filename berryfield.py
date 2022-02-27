class berryfield(object):
    def __init__(self, values):
        self.grid=dict()
        self.numrows=len(values)
        self.numcolumns=len(values[0])
        for i in range(self.numrows):
            for j in range(self.numcolumns):
                self.grid[(i,j)]=dict()
                self.grid[(i,j)]['berries']=values[i][j]

    def __str__(self):
        returner=''
        for i in range(self.numrows):
            for j in range(self.numcolumns):
                if self.grid[(i,j)]['bear_there'] and self.grid[(i,j)]['tourist_there']:
                    returner+='{:>4}'.format('X')
                elif self.grid[(i,j)]['bear_there']:
                    returner+='{:>4}'.format('B')
                elif self.grid[(i,j)]['tourist_there']:
                    returner+='{:>4}'.format('T')
                else:
                    returner+='{:>4}'.format(self.grid[(i,j)]['berries'])
                if j==self.numcolumns-1:
                    returner+='\n'
        self.returner=returner
        return returner

    def adjacent_to_10(self,i,j): 
        if j-1>0:
            if self.grid[(i,j-1)]['berries']==10:
                return True
        if i-1>0:
            if self.grid[(i-1,j)]['berries']==10:
                return True
        if j+2<=self.numcolumns:
            if self.grid[(i,j+1)]['berries']==10:
                return True
        if i+2<=self.numrows:
            if self.grid[(i+1,j)]['berries']==10:
                return True
        return False

    def grow(self):
        for i in range(self.numrows):
            for j in range(self.numcolumns):
                if self.grid[(i,j)]['berries'] >=1 and self.grid[(i,j)]['berries'] < 10:
                    self.grid[(i,j)]['berries']+=1
        for i in range(self.numrows):
            for j in range(self.numcolumns):
                if self.adjacent_to_10(i,j):
                    self.grid[(i,j)]['berries']+=1
        for i in range(self.numrows):
            for j in range(self.numcolumns):
                if self.grid[(i,j)]['berries'] > 10:
                    self.grid[(i,j)]['berries']=10
    def count_berries(self):
        count=0
        for i in range(self.numrows):
            for j in range(self.numcolumns):
                count+=self.grid[(i,j)]['berries']
        return count

if __name__ == "__main__":
    jzsdfj;alsdjfl;asjd;lfajsdf
    askdfasdf
    
