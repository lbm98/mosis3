#!/usr/bin/python3
# This file was automatically generated from drawio2cbd with the command:
#   __main__.py -F CBD -e SineGen -sSrgv sinegen.drawio -E delta=0.1

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


