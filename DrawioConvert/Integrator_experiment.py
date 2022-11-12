from CBD.preprocessing.butcher import ButcherTableau as BT
from CBD.preprocessing.rungekutta import RKPreprocessor
from CBD.simulator import Simulator
import matplotlib.pyplot as plt
from Integrator import *

oldModel = OscillatorWithIntegrators("OscillatorWithIntegrators")

oldModel.addFixedRateClock("clock",0.1)

tableau = BT.RKF45()
RKP = RKPreprocessor(tableau, atol=2e-5, hmin=0.1, safety=.84)
newModel = RKP.preprocess(oldModel)


# newModel.flatten()
# from CBD.converters.CBDDraw import gvDraw
# gvDraw(newModel, "rkf45-flatten.gv")

sim = Simulator(newModel)
sim.run(10.0)
data = newModel.getSignalHistory('OUT1')
x, y = [x for x, _ in data], [y for _, y in data]
plt.plot(x, y)
plt.plot(x, y, 'ro')
plt.show()
print(len(x))