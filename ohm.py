#
# MIT License
# 
# Copyright (c) 2020 cron-ix
# 
# Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"),
# to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense,
# and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:
# 
# The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS
# IN THE SOFTWARE.

#
# Python Class for using Ohm's law
#

import math

#
# Static methods for calculating voltage, current, resistance and power
# using Ohms Law
#
class Ohm:

    # return voltage or empty 
    @staticmethod
    def getVoltage(i:float=0, r:float=0, p:float=0, threePhase:bool=False):
        # v = Squareroot(p*r)
        if p>0 and r>0:
            return math.sqrt(p*r)
        # v = p / i
        elif p>0 and i>0:
            return p/i
        # v = i * r
        elif i>0 and r>0:
            return i*r
        else:
            return ""

    # return current or empty
    @staticmethod
    def getCurrent(v:float=0, r:float=0, p:float=0, threePhase:bool=False):
        # i = v / r
        if v>0 and r>0:
            return v/r
        # i = p / v
        elif p>0 and v>0:
            return p/v
        # i = Squareroot (p / r)
        elif p>0 and r>0:
            return math.sqrt(p/r)
        else:
            return ""

    # return power or empty
    @staticmethod
    def getPower(v:float=0, i:float=0, r:float=0, threePhase:bool=False):
        # p = v * i
        if v>0 and i>0:
            return v*i
        # p = i² * r
        elif i>0 and r>0:
            return math.pow(i, 2)*r
        # p = v²/r
        elif v>0 and r>0:
            return math.pow(v, 2)/r
        else:
            return ""

    # return resitance or empty
    @staticmethod
    def getResistance(v:float=0, i:float=0, p:float=0, threePhase:bool=False):
        # r = v / i
        if v>0 and i>0:
            return v/i
        # r = v² / p
        elif v>0 and p>0:
            return math.pow(v, 2)/p
        # r = p / i²
        elif p>0 and i>0:
            return p/math.pow(i, 2)
        else:
            return ""
