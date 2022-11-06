from CBD.Core import CBD
from CBD.lib.std import ConstantBlock, AdderBlock, DelayBlock
from CBD.simulator import Simulator


class FibonacciGen(CBD):
    def __init__(self, block_name):
        CBD.__init__(self, block_name, input_ports=[], output_ports=['OUT1'])

        # Create the Blocks
        self.addBlock(DelayBlock("delay1"))
        self.addBlock(DelayBlock("delay2"))
        self.addBlock(AdderBlock("sum"))

        # Create the Connections
        self.addConnection("delay1", "delay2")
        self.addConnection("delay1", "sum")
        self.addConnection("delay2", "sum")
        self.addConnection("sum", "delay1", input_port_name='IN1')
        self.addConnection("sum", "OUT1")

        self.addBlock(ConstantBlock("zero", value=0))
        self.addBlock(ConstantBlock("one", value=1))

        self.addConnection("zero", "delay1", input_port_name='IC')
        self.addConnection("one", "delay2", input_port_name='IC')


cbd = FibonacciGen("FibonacciGen")
sim = Simulator(cbd)
sim.run(10)
data = cbd.getSignalHistory('OUT1')
t, v = [t for t, _ in data], [v for _, v in data]

print(v)  # prints [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]