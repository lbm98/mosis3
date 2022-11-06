from CBD.Core import CBD
from CBD.lib.std import TimeBlock
from CBD.lib.std import ProductBlock, ConstantBlock
from CBD.simulator import Simulator
import matplotlib.pyplot as plt


class EvenNumberGen(CBD):
    def __init__(self, name="EvenNumberGen"):
        CBD.__init__(self, name, input_ports=[], output_ports=["OUT1"])

        self.addBlock(TimeBlock("time"))
        self.addBlock(Double("double"))

        self.addConnection("time", "double", output_port_name='OUT1',
                                             input_port_name='IN1')
        self.addConnection("double", "OUT1", output_port_name='OUT1')


class Double(CBD):
    def __init__(self, name="Double"):
        CBD.__init__(self, name, input_ports=["IN1"], output_ports=["OUT1"])

        # Create the blocks
        self.addBlock(ConstantBlock("two", 2))
        self.addBlock(ProductBlock("mult"))

        # Connect the blocks
        # Default ports are "INx" and "OUT1", with 'x' the index of the connection
        self.addConnection("two", "mult")
        self.addConnection("IN1", "mult")
        self.addConnection("mult", "OUT1")


numGen = EvenNumberGen("NumGen")

if __name__ == '__main__':
    cbd = EvenNumberGen("cbd")
    cbd.flatten()
    from CBD.converters.CBDDraw import gvDraw
    gvDraw(cbd, "text.gv")



# sim = Simulator(numGen)
#
# sim.setDeltaT(0.1)
# # The termination time can be set as argument to the run call
# sim.run(20.0)
#
# data = numGen.getSignalHistory('OUT1')
# x, y = [x for x, _ in data], [y for _, y in data]
#
# plt.plot(x, y)
# plt.show()