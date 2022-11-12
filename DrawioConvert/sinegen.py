#!/usr/bin/python3
# This file was automatically generated from drawio2cbd with the command:
#   __main__.py -F CBD -e sinegen -sSrgv sinegen.drawio -E delta=0.1

from CBD.Core import *
from CBD.lib.std import *

DELTA_T = 0.1

class SineGen(CBD):
    def __init__(self, block_name):
        super().__init__(block_name, input_ports=[], output_ports=['OUT1'])

        # Create the Blocks
        self.addBlock(TimeBlock("time"))
        self.addBlock(GenericBlock("sin", block_operator=("sin")))

        # Create the Connections
        self.addConnection("time", "sin", output_port_name='OUT1', input_port_name='IN1')
        self.addConnection("sin", "OUT1", output_port_name='OUT1')


class IntSineGen(CBD):
    def __init__(self, block_name):
        super().__init__(block_name, input_ports=[], output_ports=['OUT1'])

        # Create the Blocks
        self.addBlock(IntegratorBlock("int"))
        self.addBlock(ConstantBlock("minusone", value=(-1)))
        self.addBlock(SineGen("sg"))

        # Create the Connections
        self.addConnection("int", "OUT1", output_port_name='OUT1')
        self.addConnection("minusone", "int", output_port_name='OUT1', input_port_name='IC')
        self.addConnection("sg", "int", output_port_name='OUT1', input_port_name='IN1')


oldModel = IntSineGen("IntSineGen")

from CBD.preprocessing.butcher import ButcherTableau as BT
from CBD.preprocessing.rungekutta import RKPreprocessor
from CBD.simulator import Simulator
import matplotlib.pyplot as plt

oldModel.addFixedRateClock("clock", 1e-4)

tableau = BT.RKF45()
RKP = RKPreprocessor(tableau, atol=2e-5, hmin=0.1, safety=.84)
newModel = RKP.preprocess(oldModel)

sim = Simulator(newModel)

sim.run(20.0)
data = newModel.getSignalHistory('OUT1')
x, y = [x for x, _ in data], [y for _, y in data]
plt.plot(x, y)
plt.show()