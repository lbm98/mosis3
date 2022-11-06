#!/usr/bin/python3
# This file was automatically generated from drawio2cbd with the command:
#   __main__.py -F CBD -e OscillatorWithDerivators -sSrgv Derivator.drawio -E delta=0.1

from CBD.Core import *
from CBD.lib.std import *

DELTA_T = 0.1

class OscillatorWithDerivators(CBD):
    def __init__(self, block_name):
        super().__init__(block_name, input_ports=[], output_ports=['OUT1'])

        # Create the Blocks
        self.addBlock(ConstantBlock("v0", value=(1)))
        self.addBlock(ConstantBlock("x0", value=(0)))
        self.addBlock(ProductBlock("SlGjHfAaz0ckTXi2P8GK-16", numberOfInputs=(2)))
        self.addBlock(ConstantBlock("minus1", value=(-1)))
        self.addBlock(DerivatorBlock("QQaXVmWF0gyv2xvVzr-h-7"))
        self.addBlock(DerivatorBlock("QQaXVmWF0gyv2xvVzr-h-15"))

        # Create the Connections
        self.addConnection("v0", "QQaXVmWF0gyv2xvVzr-h-7", output_port_name='OUT1', input_port_name='IC')
        self.addConnection("minus1", "SlGjHfAaz0ckTXi2P8GK-16", output_port_name='OUT1', input_port_name='IN1')
        self.addConnection("SlGjHfAaz0ckTXi2P8GK-16", "QQaXVmWF0gyv2xvVzr-h-7", output_port_name='OUT1', input_port_name='IN1')
        self.addConnection("SlGjHfAaz0ckTXi2P8GK-16", "OUT1", output_port_name='OUT1')
        self.addConnection("QQaXVmWF0gyv2xvVzr-h-7", "QQaXVmWF0gyv2xvVzr-h-15", output_port_name='OUT1', input_port_name='IN1')
        self.addConnection("x0", "QQaXVmWF0gyv2xvVzr-h-15", output_port_name='OUT1', input_port_name='IC')
        self.addConnection("QQaXVmWF0gyv2xvVzr-h-15", "SlGjHfAaz0ckTXi2P8GK-16", output_port_name='OUT1', input_port_name='IN2')


