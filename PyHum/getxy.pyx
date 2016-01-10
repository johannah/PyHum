from __future__ import division
import numpy as np
cimport numpy as np
cimport cython
from libc.math cimport sqrt,sin,cos

# =========================================================
cdef class GetXY:

    # =========================================================
    @cython.boundscheck(False)
    @cython.cdivision(True)
    @cython.wraparound(False)
    @cython.nonecheck(False)
    def __init__(self, np.ndarray[np.float64_t, ndim=1] e, np.ndarray[np.float32_t, ndim=1] n, np.ndarray[np.float32_t, ndim=1] d, np.ndarray[np.float32_t, ndim=1] yvec, np.ndarray[np.float64_t, ndim=1] t, int extent):

       x = np.concatenate((np.tile(e,extent) , np.tile(e,extent)))
       rangedist = np.sqrt(np.power(yvec, 2.0) - np.power(d, 2.0))
       y = np.concatenate((n+rangedist, n-rangedist))
       # Rotate line around center point
       xx = e - ((x - e) * np.cos(t)) - ((y - n) * np.sin(t))
       yy = n - ((x - e) * np.sin(t)) + ((y - n) * np.cos(t))
       self.xx, self.yy = self._calc_beam_pos(d, t, xx, yy)
       return #xx, yy 

    # =========================================================
    @cython.boundscheck(False)
    @cython.cdivision(True)
    @cython.wraparound(False)
    @cython.nonecheck(False)    
    def _calc_beam_pos(self, dist, bearing, x, y):

       dist_x, dist_y = (dist*np.sin(bearing), dist*np.cos(bearing))
       xfinal, yfinal = (x + dist_x, y + dist_y)
       return (xfinal, yfinal)
  
       
    # external functions ======================================                        
    # =========================================================
    def getdat(self):
    #def gethumdat(self):    
        """
        returns data in .DAT file
        """  
        return self.xx, self.yy      
        
        
        
