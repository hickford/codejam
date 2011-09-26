#!python
# Irregular cakes http://code.google.com/codejam/contest/dashboard?c=1158485#s=p0
from __future__ import division
import fileinput
f = fileinput.input()
T = int(f.readline())

class Polyline:
    def __init__(self,points):
        self.points = points
        self.left = points[0][0]
        self.right = points[-1][0]
        self.Xes = [x for (x,y) in self.points]
        
    def y(self,x):
        if not self.left <= x <= self.right:
            raise ValueError
        x1,y1 = self.points[0]
        for x2,y2 in self.points[1:]:
            if x2 >= x:
                break
            x1,y1 = x2,y2
        assert x1 <= x <= x2
        y = y1 + (y2-y1)*(x-x1)/(x2-x1)
        assert y1 <= y <= y2 or y1 >= y >= y2
        return y
        
    def __repr__(self):
        return "Polyline(%s)" % self.points

class Cake:
    def __init__(self,Lower,Upper):
        if  Lower.left != Upper.left or Lower.right != Upper.right :
            raise ValueError
        self.Lower = Lower
        self.Upper = Upper
        self.left = Lower.left
        self.right = Lower.right
        self.Xes = sorted(set(Lower.Xes+Upper.Xes))
        self.areas = dict( (a,self.area_left(a)) for a in self.Xes )
        
    def area_left(self,a):
        """Return area to the left of vertical line x=a"""
        # sum trapeziums
        area = 0
        x0 = self.left
        for x1 in sorted(set(self.Xes+[a]))[1:]:
            if x1 > a:
                break
            width = x1 - x0
            height0 = self.Upper.y(x0) - self.Lower.y(x0)
            height1 = self.Upper.y(x1) - self.Lower.y(x1)
            area += width * (height0 + height1) / 2
            x0 = x1       
        return area
        
    def take(self,portion):
        """Return a such that area to the left of vertical line x=a is portion"""
        if portion < 0 or portion > self.areas[self.right]:
            raise ValueError
        # foreplay to binary search
        x0 = self.left
        for x2 in self.Xes:
            if self.areas[x2] > portion:
                break
            x0 = x2
        # binary search using area_left
        error = 10e-6 
        while abs(float(x0) - float(x2)) > error:
            #print x0,x2, x>x2
            x1 = (x0+x2)/2
            if self.area_left(x1) < portion:
                x0, x2 = x1, x2
            else:
                x0, x2 = x0, x1
        return (x0+x2)/2
        
    def cut(self,G):
        """Return a list length G-1 of x co-ordinates for vertical cuts to divide the cake into G equal pieces"""
        # really slow :(
        whole = self.areas[self.right]
        cuts = list()
        for i in range(1,G):
            portion = whole * i/G
            cuts.append( self.take(portion) )
        return cuts
    
for case in range(1,T+1):
    W,L,U,G = [int(x) for x in f.readline().split()]
    Lower = Polyline([ tuple(int(x) for x in f.readline().split()) for i in range(L) ])
    Upper = Polyline([ tuple(int(x) for x in f.readline().split()) for i in range(U) ])
    cake = Cake(Lower,Upper)
   
    print "Case #%d:" % case
    for x in cake.cut(G):
        print x
