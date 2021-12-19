from __future__ import division
from object_library import all_propagators, Propagator
import parameters as Param

VO = Propagator(name = 'VO',
                numerator = '4 * Metric(1,2)')