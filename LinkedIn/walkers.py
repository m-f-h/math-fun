""" ref: https://www.linkedin.com/feed/update/urn:li:activity:7216087495745163264?utm_source=share&utm_medium=member_desktop

C
| \
|   \
|     \
(10km)  \       __
|         \    |\ 
|           \    \  @ 5 km/h
A --(10km)-- B    (2) 
(1) --> (6km/h)

"""

class Point:
  """Can be of any dimension. Attributes:
  coords: tuple = components/cooordinates.
  len: Euclidean length  
  """
  def __str__(self): return str(self.coords)
  def __repr__(self): return type(self).__name__ + str(self.coords)
  def __round__(self, n=1): return type(self)(round(x,n)for x in self)
  def __iter__(self): return iter(self.coords)
  def __add__(self,other): return type(self)(x+y for x,y in zip(self, other))
  def __sub__(self,other): return type(self)(x-y for x,y in zip(self, other))
  def __mul__(self,other): return type(self)(other*x for x in self)
  def __rmul__(self,other): return type(self)(other*x for x in self)
  def __neg__(self): return type(self)(-x for x in self)
  @property
  def len(self): return sum(x**2 for x in self.coords)**.5
  def __init__(self, *points):
    if len(points) != 1: self.coords = points
    else: # length == 1
      try: self.coords = tuple(points[0]) # iterable ?
      except TypeError: self.coords = points[0],
  #def __or__(a,b): return Vector() # operation '|' is concat

class Arc(dict):
  """A dict that should contain vectors/points 'start' and 'end'."""
  @property
  def len(self): return (self['end']-self['start']).len
  def pos(self, d): # coords of the point at distance d of the start
    t = d/self.len
    return self['start']*(1-t) + t*self['end']

class Curve(list):
    """A curve is a list of Arcs with added speed.
    The object can be called with an argument t, which returns the position at time t.
    """
    #def pos(self, t):
    def __call__(self, t):
        "Return the position at time t."
        for arc in self:
            if arc.len < t*self.speed:
                t -= arc.len / self.speed
            else: return arc.pos(t * self.speed)
        return self[-1][end]

def dist(t, curve1, curve2): return (curve1.pos(t)-curve2.pos(t)).len

def Time(t):
  mins = t % 1 * 60
  secs = mins % 1 * 60
  return "%02d:%02d:%02d" % (int(t),int(mins),int(secs))

def schedule(start, end, num_pts):
  time_step = (end - start) / num_steps
  for i in range(num_steps+1):
      print(f"at {Time( t := start + i * time_step )}, (1) = {round(C1(t))}, (2) = {round(C2(t))}, distance = {dist(t, C1, C2) :.3}")

if 1:
  A = Point(0,0) ; B = Point(10,0) ; C = Point(0, 10)
  AB = Arc(start=A, end=B) ; BC = Arc(start=B, end=C) ; CA = Arc(start=C, end=A)
  C1 = Curve([AB,BC,CA,]); C1.speed=6
  C2 = Curve([BC,CA,AB,]); C2.speed=5
  
  total_length = 10 + 10 + 10*2**.5   # ~ 34 km
  total_time = total_length / 6       # ~ 6 h
  num_steps = 10
  schedule(0,total_time,num_steps)
  
# eof
