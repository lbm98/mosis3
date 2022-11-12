#!/usr/bin/python3
# This file was automatically generated from drawio2cbd with the command:
#   __main__.py -F CBD -e Derivator -sSrgv Derivator.drawio -E delta=0.1

from CBD.Core import *
from CBD.lib.std import *

DELTA_T = 0.1

class OscillatorWithDerivators(CBD):
    def __init__(self, block_name):
        super().__init__(block_name, input_ports=[], output_ports=['OUT1'])

        # Create the Blocks
        self.addBlock(ConstantBlock("v0", value=(1)))
        self.addBlock(ConstantBlock("x0", value=(0)))
        self.addBlock(ProductBlock("prod", numberOfInputs=(2)))
        self.addBlock(ConstantBlock("minus1", value=(-1)))
        self.addBlock(DerivatorBlock("der1"))
        self.addBlock(DerivatorBlock("der2"))

        # Create the Connections
        self.addConnection("v0", "der1", output_port_name='OUT1', input_port_name='IC')
        self.addConnection("minus1", "prod", output_port_name='OUT1', input_port_name='IN1')
        self.addConnection("prod", "der1", output_port_name='OUT1', input_port_name='IN1')
        self.addConnection("prod", "OUT1", output_port_name='OUT1')
        self.addConnection("der1", "der2", output_port_name='OUT1', input_port_name='IN1')
        self.addConnection("x0", "der2", output_port_name='OUT1', input_port_name='IC')
        self.addConnection("der2", "prod", output_port_name='OUT1', input_port_name='IN2')


if __name__ == '__main__':
    from CBD.converters.latexify import CBD2Latex
    model = OscillatorWithDerivators("SinGen")
    cbd2latex = CBD2Latex(model, show_steps=True, render_latex=False)
    cbd2latex.simplify_links()
    cbd2latex.substitute()
    cbd2latex.substitute()
    cbd2latex.substitute()
    #cbd2latex.simplify()
    print("RESULT IS:")
    print(cbd2latex.render())