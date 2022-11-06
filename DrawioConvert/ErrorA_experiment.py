#!/usr/bin/python3
# This file was automatically generated from drawio2cbd with the command:
#   __main__.py -F CBD -e ErrorA -sSrgv ErrorA.drawio -E delta=0.1

from ErrorA import *
from CBD.simulator import Simulator

DELTA_T = 0.001

cbd = ErrorA("ErrorA")

# Run the Simulation
sim = Simulator(cbd)
sim.setDeltaT(DELTA_T)
sim.run(50)

# TODO: Process Your Simulation Results

if __name__ == "__main__":
    import matplotlib.pyplot as plt
    data = cbd.getSignalHistory('OUT1')
    x, y = [x for x, _ in data], [y for _, y in data]

    plt.plot(x, y)
    plt.show()