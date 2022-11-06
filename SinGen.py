from CBD.Core import *   # To prevent circular dependency
from CBD.lib.std import TimeBlock, GenericBlock
from CBD.simulator import Simulator

import matplotlib.pyplot as plt


class SinGen(CBD):
    def __init__(self, name="SinGen"):
        CBD.__init__(self, name, input_ports=[], output_ports=["OUT1"])

        # Add the 't' parameter
        # Let's call it 'time'
        self.addBlock(TimeBlock("time"))

        # Add the block that computes the actual sine function
        # Let's call it 'sin'
        self.addBlock(GenericBlock("sin", block_operator="sin"))

        # Connect them together
        self.addConnection("time", "sin", output_port_name='OUT1',
                                            input_port_name='IN1')

        # Connect the output port
        self.addConnection("sin", "OUT1", output_port_name='OUT1')


sinGen = SinGen("SinGen")
sim = Simulator(sinGen)

sim.setDeltaT(0.1)
# The termination time can be set as argument to the run call
sim.run(20.0)

data = sinGen.getSignalHistory('OUT1')
x, y = [x for x, _ in data], [y for _, y in data]

plt.plot(x, y)
plt.show()