import math as Math
Pi = Math.pi
A = 6378245.0
Ee = 0.00669342162296594323

def Transform(wgLat, wgLon):

    dLat = TransformLat(wgLon - 105.0, wgLat - 35.0)
    dLon = TransformLon(wgLon - 105.0, wgLat - 35.0)
    radLat = wgLat / 180.0 * Pi
    magic = Math.sin(radLat)
    magic = 1 - Ee * magic * magic
    sqrtMagic = Math.sqrt(magic)
    dLat = (dLat * 180.0) / ((A * (1 - Ee)) / (magic * sqrtMagic) * Pi)
    dLon = (dLon * 180.0) / (A / sqrtMagic * Math.cos(radLat) * Pi)
    return wgLat + dLat,wgLon + dLon

def TransformLat(x, y):

    ret = -100.0 + 2.0 * x + 3.0 * y + 0.2 * y * y + 0.1 * x * y + 0.2 * Math.sqrt(abs(x))
    ret += (20.0 * Math.sin(6.0 * x * Pi) + 20.0 * Math.sin(2.0 * x * Pi)) * 2.0 / 3.0
    ret += (20.0 * Math.sin(y * Pi) + 40.0 * Math.sin(y / 3.0 * Pi)) * 2.0 / 3.0
    ret += (160.0 * Math.sin(y / 12.0 * Pi) + 320 * Math.sin(y * Pi / 30.0)) * 2.0 / 3.0
    return ret


def TransformLon(x, y):

    ret = 300.0 + x + 2.0 * y + 0.1 * x * x + 0.1 * x * y + 0.1 * Math.sqrt(abs(x))
    ret += (20.0 * Math.sin(6.0 * x * Pi) + 20.0 * Math.sin(2.0 * x * Pi)) * 2.0 / 3.0
    ret += (20.0 * Math.sin(x * Pi) + 40.0 * Math.sin(x / 3.0 * Pi)) * 2.0 / 3.0
    ret += (150.0 * Math.sin(x / 12.0 * Pi) + 300.0 * Math.sin(x / 30.0 * Pi)) * 2.0 / 3.0
    return ret
