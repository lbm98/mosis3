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


oldModel = SinGen("SinGen")
#sim = Simulator(sinGen)

from CBD.preprocessing.butcher import ButcherTableau as BT
from CBD.preprocessing.rungekutta import RKPreprocessor

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





# from CBD.converters.latexify import CBD2Latex
# cbd2latex = CBD2Latex(model, show_steps=True, render_latex=False)
# cbd2latex.simplify()
# print("RESULT IS:")
# print(cbd2latex.render())




# sim.setDeltaT(0.1)
# # The termination time can be set as argument to the run call
# sim.run(20.0)
#
# data = model.getSignalHistory('OUT1')
# x, y = [x for x, _ in data], [y for _, y in data]
#
# plt.plot(x, y)
# plt.show()