from CBD.Core import CBD
from CBD.lib.std import *
from CBD.simulator import Simulator

class LCG(CBD):
    def __init__(self, block_name, a, c, m, x0):
        CBD.__init__(self, block_name, input_ports=[], output_ports=["OUT1"])

        # Create the Blocks
        self.addBlock(ConstantBlock("a", value=a))
        self.addBlock(ConstantBlock("x0", value=x0))
        self.addBlock(ConstantBlock("c", value=c))
        self.addBlock(ConstantBlock("m", value=m))
        self.addBlock(DelayBlock("delay"))
        self.addBlock(ProductBlock("mult"))
        self.addBlock(AdderBlock("sum"))
        self.addBlock(ModuloBlock("mod"))

        # Create the Connections
        self.addConnection("x0", "delay", input_port_name='IC')
        self.addConnection("a", "mult")
        self.addConnection("delay", "mult")
        self.addConnection("mult", "sum")
        self.addConnection("c", "sum")
        self.addConnection("sum", "mod", input_port_name='IN1')
        self.addConnection("m", "mod", input_port_name='IN2')
        self.addConnection("mod", "delay", input_port_name='IN1')
        self.addConnection("delay", "OUT1")


def term(model, curIt):
    signals = [y for _, y in model.getSignalHistory("OUT1")]
    unique_signals = set(signals)
    return len(signals) > len(unique_signals)


lcg = LCG("LCG", 1, 4, 9, 0)
sim = Simulator(lcg)
sim.setTerminationCondition(term)
sim.run()

# Print a full cycle: [0, 4, 8, 3, 7, 2, 6, 1, 5]
print([v for _, v in lcg.getSignalHistory("OUT1")])