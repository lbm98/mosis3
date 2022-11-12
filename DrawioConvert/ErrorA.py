#!/usr/bin/python3
# This file was automatically generated from drawio2cbd with the command:
#   __main__.py -F CBD -e ErrorA -sSrgv ErrorA.drawio -E delta=0.1

from CBD.Core import *
from CBD.lib.std import *

DELTA_T = 0.1

class SineGen(CBD):
    def __init__(self, block_name):
        super().__init__(block_name, input_ports=[], output_ports=['OUT1'])

        # Create the Blocks
        self.addBlock(TimeBlock("time"))
        self.addBlock(GenericBlock("realsin", block_operator=("sin")))

        # Create the Connections
        self.addConnection("time", "realsin", output_port_name='OUT1', input_port_name='IN1')
        self.addConnection("realsin", "OUT1", output_port_name='OUT1')


class OscillatorWithIntegrators(CBD):
    def __init__(self, block_name):
        super().__init__(block_name, input_ports=[], output_ports=['OUT1'])

        # Create the Blocks
        self.addBlock(IntegratorBlock("int1"))
        self.addBlock(IntegratorBlock("int2"))
        self.addBlock(ConstantBlock("v0", value=(1)))
        self.addBlock(ConstantBlock("x0", value=(0)))
        self.addBlock(ProductBlock("prod", numberOfInputs=(2)))
        self.addBlock(ConstantBlock("minus1", value=(-1)))

        # Create the Connections
        self.addConnection("v0", "int1", output_port_name='OUT1', input_port_name='IC')
        self.addConnection("x0", "int2", output_port_name='OUT1', input_port_name='IC')
        self.addConnection("int1", "int2", output_port_name='OUT1', input_port_name='IN1')
        self.addConnection("minus1", "prod", output_port_name='OUT1', input_port_name='IN1')
        self.addConnection("int2", "prod", output_port_name='OUT1', input_port_name='IN2')
        self.addConnection("int2", "OUT1", output_port_name='OUT1')
        self.addConnection("prod", "int1", output_port_name='OUT1', input_port_name='IN1')


class ErrorA(CBD):
    def __init__(self, block_name):
        super().__init__(block_name, input_ports=[], output_ports=['OUT1'])

        # Create the Blocks
        self.addBlock(SineGen("realsininst"))
        self.addBlock(OscillatorWithIntegrators("OWI"))
        self.addBlock(AdderBlock("sum", numberOfInputs=(2)))
        self.addBlock(NegatorBlock("neg"))
        self.addBlock(AbsBlock("abs"))
        self.addBlock(IntegratorBlock("errint"))
        self.addBlock(ConstantBlock("x0", value=(0)))

        # Create the Connections
        self.addConnection("OWI", "neg", output_port_name='OUT1', input_port_name='IN1')
        self.addConnection("realsininst", "sum", output_port_name='OUT1', input_port_name='IN1')
        self.addConnection("neg", "sum", output_port_name='OUT1', input_port_name='IN2')
        self.addConnection("sum", "abs", output_port_name='OUT1', input_port_name='IN1')
        self.addConnection("abs", "errint", output_port_name='OUT1', input_port_name='IN1')
        self.addConnection("errint", "OUT1", output_port_name='OUT1')
        self.addConnection("x0", "errint", output_port_name='OUT1', input_port_name='IC')


