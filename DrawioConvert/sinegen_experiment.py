#!/usr/bin/python3
# This file was automatically generated from drawio2cbd with the command:
#   __main__.py -F CBD -e SineGen -sSrgv sinegen.drawio -E delta=0.1

from sinegen import *
from CBD.simulator import Simulator
import matplotlib.pyplot as plt

DELTA_T = 0.1

cbd = SineGen("SineGen")

# Run the Simulation
sim = Simulator(cbd)
sim.setDeltaT(DELTA_T)
sim.run(10)

# TODO: Process Your Simulation Results

if __name__ == "__main__":
    data = cbd.getSignalHistory('OUT1')
    x, y = [x for x, _ in data], [y for _, y in data]

    plt.plot(x, y)
    plt.show()