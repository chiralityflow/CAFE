from __future__ import absolute_import
from object_library import all_propagators, Propagator

denominator = "P('mu', id) * P('mu', id) - Mass(id) * Mass(id) + complex(0,1) * Mass(id) * Width(id)"

VO = Propagator(name = 'VO',
                numerator = '-0 * Metric(1,2)',
                denominator = 'P(-1, id)**2')