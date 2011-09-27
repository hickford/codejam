#!python
# Irregular cakes http://code.google.com/codejam/contest/dashboard?c=1158485#s=p0
from __future__ import division
from collections import OrderedDict
import fileinput
import math
f = fileinput.input()
T = int(f.readline())

class Polyline:
    def __init__(self,points):
        self.points = points
        self.left = points[0][0]
        self.right = points[-1][0]
        self.Xes = [x for (x,y) in self.points]
        self.Y = dict(self.points)
        
    def y(self,x):
        try:
            return self.Y[x]
        except KeyError:
            pass
        if not self.left <= x <= self.right:
            raise ValueError
        x1,y1 = self.points[0]
        for x2,y2 in self.points[1:]:
            if x2 >= x:
                break
            x1,y1 = x2,y2
        y = y1 + (y2-y1)*(x-x1)/(x2-x1)
        return y
        
    def __repr__(self):
        return "Polyline(%s)" % self.points

class Cake:
    def __init__(self,Lower,Upper):
        if  Lower.left != Upper.left or Lower.right != Upper.right :
            raise ValueError
        self.Xes = sorted(set(Lower.Xes+Upper.Xes))
        self.Lower1 = Lower
        self.Upper1 = Upper
        self.Lower = Polyline([ (x,Lower.y(x))  for x in self.Xes ])
        self.Upper = Polyline([ (x,Upper.y(x))  for x in self.Xes ])
        self.left = Lower.left
        self.right = Lower.right
        self.areas = OrderedDict()
        self.areas[self.left] = 0
        x0 = self.left
        area = 0
        for x1 in self.Xes[1:]:
            width = x1 - x0
            height0 = self.Upper.y(x0) - self.Lower.y(x0)
            height1 = self.Upper.y(x1) - self.Lower.y(x1)
            area += width * (height0 + height1) / 2
            self.areas[x1] = area
            x0 = x1
        self.whole = area
        
    def area_left(self,a):
        """Return area to the left of vertical line x=a"""
        # sum trapeziums
        try:
            return self.areas[a]
        except KeyError:
            pass
        x0, area0 = self.left, 0
        x1 = a
        for x,area in self.areas.items():
            if x > a:
                break
            x0, area0 = x, area
        width = x1 - x0
        height0 = self.Upper.y(x0) - self.Lower.y(x0)
        height1 = self.Upper.y(x1) - self.Lower.y(x1)
        return area0 + width * (height0 + height1) / 2
        
    def take(self,portion):
        """Return a such that area to the left of vertical line x=a is portion"""
        if portion < 0 or portion > self.whole:
            raise ValueError
        # foreplay to binary search
        x0 = self.left
        for x2 in self.Xes:
            if self.areas[x2] > portion:
                break
            x0 = x2
            
        remaining = portion - self.areas[x0]
        assert remaining >= 0
        height0 = self.Upper.y(x0) - self.Lower.y(x0)
        height2 = self.Upper.y(x2) - self.Lower.y(x2)
        width = x2-x0
            
        # height1 = (1-r)*height0+r*height2    
        
        # remaining = r*width*(height0+height1)/2
        # 2*remaining = r*width*((2-r)*height0+r*height2)
        # 0 = (width*height2-width*height0)*r**2 + (width*2*height0)*r - 2*remaining
        # 0 = a*r**2 + b*r + c
        a = (width*height2-width*height0)
        b = (width*2*height0)
        c = -2*remaining
        
        if a == 0:  # linear
            r = -c/b
        else:   # a > 1e-6:       # quadratic
            r = (-b+math.sqrt(b**2-4*a*c))/(2*a)
        x1 = x0+r*width
        if abs(self.area_left(x1)-portion)<1e-6:
            # all is good
            return x1
        else:   # precision error
            print "BOO"
            # binary search using area_left SLOW
            error = 10e-6 / 4
            while abs(x0 - x2) > error:
                #print x0,x2, x>x2
                x1 = (x0+x2)/2
                if self.area_left(x1) < portion:
                    x0, x2 = x1, x2
                else:
                    x0, x2 = x0, x1
            return (x0+x2)/2
        
    def cut(self,G):
        """Return a list length G-1 of x co-ordinates for vertical cuts to divide the cake into G equal pieces"""
        cuts = list()
        for i in range(1,G):
            portion = self.whole * i/G
            cuts.append( self.take(portion) )
        return cuts
        
    def __repr__(self):
        return "Cake(%s,%s)" % (repr(self.Lower1,self.Upper1))
    
for case in range(1,T+1):
    W,L,U,G = [int(x) for x in f.readline().split()]
    Lower = Polyline([ tuple(int(x) for x in f.readline().split()) for i in range(L) ])
    Upper = Polyline([ tuple(int(x) for x in f.readline().split()) for i in range(U) ])
    cake = Cake(Lower,Upper)
   
    print "Case #%d:" % case
    cuts = cake.cut(G)
    for x in cuts:
        print x
