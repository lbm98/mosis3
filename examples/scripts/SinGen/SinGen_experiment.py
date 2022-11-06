#!/usr/bin/python3
# This file was automatically generated from drawio2cbd with the command:
#   /home/red/git/DrawioConvert/__main__.py Fibonacci.xml -F CBD -e FibonacciGen -gvaf

from SinGen import *
from CBD.simulator import Simulator
import matplotlib.pyplot as plt


sinGen = SinGen("SinGen")
sim = Simulator(sinGen)

# Change this to change the Sin step size
sim.setDeltaT(0.5)

# The termination time can be set as argument to the run call
sim.run(20.0)

data = sinGen.getSignalHistory('OUT1')
x, y = [x for x, _ in data], [y for _, y in data]

plt.plot(x, y)
plt.show()
