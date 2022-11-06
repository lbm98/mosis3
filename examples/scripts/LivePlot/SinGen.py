from CBD.Core import *
from CBD.lib.std import *
from CBD.lib.endpoints import SignalCollectorBlock

DELTA_T = 0.1

class SinGen(CBD):
    def __init__(self, name="SinGen"):
        CBD.__init__(self, name, input_ports=[], output_ports=[])

        # Create the blocks
        self.addBlock(TimeBlock("time"))
        self.addBlock(GenericBlock("sin", block_operator="sin"))
        self.addBlock(SignalCollectorBlock("collector"))

        # Connect the blocks
        self.addConnection("time", "sin")
        self.addConnection("sin", "collector")


