# Oscillator with Integrators

The output port of the OscillatorWithIntegrators
comes from the output port of the second integrator block.
See Figure x.
This is done to plot the sine function and not the other functions:
the cosine or the inverse sine.
Note that this is a result of the initial conditions.
That is: sin(0) = 0.

Figure x shows the sine function simulated with a step-size of 0.01.
This roughly approximates the actual sine function.
But when we increase the step-size to 0.01, the function becomes wider
and does not approximate the actual sine function anymore.

# Oscillator with Derivators

The overall structure of the diagram is roughly kept the same
for the oscillator with integrators and for the oscillator with derivators.

One notable difference is the output port used to generate the plots.
To get a sine function again, the outport port had to come
from the output port of the multiplication block.
See Figure x.
This has again to do with the initial conditions.

We also had to be careful with the values of these initial conditions.
The value of the second derivative (in Figure)
had to be derived from the equation:
dv/dt(0) = -x(0)
dv/dt(0) = -0
dv/dt(0) = 0
such that the values of the initial conditions apparently seem the same.

Figure x shows the sine function simulated with a step-size of 0.01.
This roughly approximates the actual sine function.
But when we increase the step-size to 0.01, the function becomes thinner
and does not approximate the actual sine function anymore.


