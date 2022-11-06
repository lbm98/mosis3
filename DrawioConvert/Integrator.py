#!/usr/bin/python3
# This file was automatically generated from drawio2cbd with the command:
#   __main__.py -F CBD -e Integrator -sSrgv Integrator.drawio -E delta=0.1

from CBD.Core import *
from CBD.lib.std import *

DELTA_T = 0.1

class Integrator(CBD):
    def __init__(self, block_name):
        super().__init__(block_name, input_ports=[], output_ports=['OUT1'])

        # Create the Blocks
        self.addBlock(IntegratorBlock("SlGjHfAaz0ckTXi2P8GK-1"))
        self.addBlock(IntegratorBlock("SlGjHfAaz0ckTXi2P8GK-5"))
        self.addBlock(ConstantBlock("v0", value=(1)))
        self.addBlock(ConstantBlock("x0", value=(0)))
        self.addBlock(ProductBlock("SlGjHfAaz0ckTXi2P8GK-16", numberOfInputs=(2)))
        self.addBlock(ConstantBlock("minus1", value=(-1)))

        # Create the Connections
        self.addConnection("v0", "SlGjHfAaz0ckTXi2P8GK-1", output_port_name='OUT1', input_port_name='IC')
        self.addConnection("x0", "SlGjHfAaz0ckTXi2P8GK-5", output_port_name='OUT1', input_port_name='IC')
        self.addConnection("SlGjHfAaz0ckTXi2P8GK-1", "SlGjHfAaz0ckTXi2P8GK-5", output_port_name='OUT1', input_port_name='IN1')
        self.addConnection("minus1", "SlGjHfAaz0ckTXi2P8GK-16", output_port_name='OUT1', input_port_name='IN1')
        self.addConnection("SlGjHfAaz0ckTXi2P8GK-5", "SlGjHfAaz0ckTXi2P8GK-16", output_port_name='OUT1', input_port_name='IN2')
        self.addConnection("SlGjHfAaz0ckTXi2P8GK-5", "OUT1", output_port_name='OUT1')
        self.addConnection("SlGjHfAaz0ckTXi2P8GK-16", "SlGjHfAaz0ckTXi2P8GK-1", output_port_name='OUT1', input_port_name='IN1')


