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
        self.addBlock(GenericBlock("sin", block_operator=("sin")))

        # Create the Connections
        self.addConnection("time", "sin", output_port_name='OUT1', input_port_name='IN1')
        self.addConnection("sin", "OUT1", output_port_name='OUT1')


class OscillatorWithIntegrators(CBD):
    def __init__(self, block_name):
        super().__init__(block_name, input_ports=[], output_ports=['OUT1'])

        # Create the Blocks
        self.addBlock(IntegratorBlock("vB6EShjai-SGW7rwPxuC-6"))
        self.addBlock(IntegratorBlock("vB6EShjai-SGW7rwPxuC-10"))
        self.addBlock(ConstantBlock("v0", value=(1)))
        self.addBlock(ConstantBlock("x0", value=(0)))
        self.addBlock(ProductBlock("vB6EShjai-SGW7rwPxuC-21", numberOfInputs=(2)))
        self.addBlock(ConstantBlock("minus1", value=(-1)))

        # Create the Connections
        self.addConnection("v0", "vB6EShjai-SGW7rwPxuC-6", output_port_name='OUT1', input_port_name='IC')
        self.addConnection("x0", "vB6EShjai-SGW7rwPxuC-10", output_port_name='OUT1', input_port_name='IC')
        self.addConnection("vB6EShjai-SGW7rwPxuC-6", "vB6EShjai-SGW7rwPxuC-10", output_port_name='OUT1', input_port_name='IN1')
        self.addConnection("minus1", "vB6EShjai-SGW7rwPxuC-21", output_port_name='OUT1', input_port_name='IN1')
        self.addConnection("vB6EShjai-SGW7rwPxuC-10", "vB6EShjai-SGW7rwPxuC-21", output_port_name='OUT1', input_port_name='IN2')
        self.addConnection("vB6EShjai-SGW7rwPxuC-10", "OUT1", output_port_name='OUT1')
        self.addConnection("vB6EShjai-SGW7rwPxuC-21", "vB6EShjai-SGW7rwPxuC-6", output_port_name='OUT1', input_port_name='IN1')


class ErrorA(CBD):
    def __init__(self, block_name):
        super().__init__(block_name, input_ports=[], output_ports=['OUT1'])

        # Create the Blocks
        self.addBlock(SineGen("vB6EShjai-SGW7rwPxuC-1"))
        self.addBlock(OscillatorWithIntegrators("vB6EShjai-SGW7rwPxuC-35"))
        self.addBlock(AdderBlock("vB6EShjai-SGW7rwPxuC-37", numberOfInputs=(2)))
        self.addBlock(NegatorBlock("vB6EShjai-SGW7rwPxuC-41"))
        self.addBlock(AbsBlock("vB6EShjai-SGW7rwPxuC-47"))
        self.addBlock(IntegratorBlock("vB6EShjai-SGW7rwPxuC-51"))
        self.addBlock(ConstantBlock("x0", value=(0)))

        # Create the Connections
        self.addConnection("vB6EShjai-SGW7rwPxuC-35", "vB6EShjai-SGW7rwPxuC-41", output_port_name='OUT1', input_port_name='IN1')
        self.addConnection("vB6EShjai-SGW7rwPxuC-1", "vB6EShjai-SGW7rwPxuC-37", output_port_name='OUT1', input_port_name='IN1')
        self.addConnection("vB6EShjai-SGW7rwPxuC-41", "vB6EShjai-SGW7rwPxuC-37", output_port_name='OUT1', input_port_name='IN2')
        self.addConnection("vB6EShjai-SGW7rwPxuC-37", "vB6EShjai-SGW7rwPxuC-47", output_port_name='OUT1', input_port_name='IN1')
        self.addConnection("vB6EShjai-SGW7rwPxuC-47", "vB6EShjai-SGW7rwPxuC-51", output_port_name='OUT1', input_port_name='IN1')
        self.addConnection("vB6EShjai-SGW7rwPxuC-51", "OUT1", output_port_name='OUT1')
        self.addConnection("x0", "vB6EShjai-SGW7rwPxuC-51", output_port_name='OUT1', input_port_name='IC')


