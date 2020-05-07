#!/usr/bin/env python

from rt6 import *
from math import *

steps = 200

for f in range(steps):
    print(f)
    phi = 2 * pi * f / steps
    x, z = 2.15 * sin(phi), 2.15 * cos(phi)
    scene = [ 
    Sphere(vec3(-1 + x, .1, 2.25 + z), .6, rgb(0, 0, 1)),
    Sphere(vec3(-.75, .1, 2.25), .6, rgb(.5, .223, .5)),
    Sphere(vec3(-1 - x, .1, 2.25 - z), .6, rgb(1, .572, .184)),
    CheckeredSphere(vec3(0,-99999.5, 0), 99999, rgb(.75, .75, .75), 0.25),
    ]
    render(scene, "test%03u.png" % f)


