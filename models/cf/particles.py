# This file was automatically created by FeynRules 1.7.69
# Mathematica version: 8.0 for Mac OS X x86 (64-bit) (November 6, 2010)
# Date: Mon 1 Oct 2012 14:58:25
# UFO files for the chiF formalism for the CAFE extension for MG5
# Naming convention for any new particles is as follows:
# The particle musc be denoted as a scalar in the UFO files
# and the final 3 symbols of its name should be xyz, with
# x denoting the chiral charge: L for left, R for right, and 0 for a scalar or vector (usually)
# y denoting the type of particle it should actually be: s for scalar, f for fermion, and v for vector
# z denoting electric charge: + for +1, - for -1, and 0 for 0


from __future__ import division
from object_library import all_particles, Particle
import parameters as Param

# AL: Photons first

# AL: first the non-chiral photon
a = Particle(pdg_code = 90022,
             name = 'a',
             antiname = 'a',
             spin = 3,
             color = 1,
             mass = Param.ZERO,
             width = Param.ZERO,
             texname = 'a',
             antitexname = 'a',
             charge = 0,
             GhostNumber = 0,
             LeptonNumber = 0,
             line='double',
             Y = 0)

# AL: Now left-chiral photon
aL = Particle(pdg_code = 90023,
             name = 'aL',
             antiname = 'aL',
             spin = 3,
             color = 1,
             mass = Param.ZERO,
             width = Param.ZERO,
             texname = 'aL',
             antitexname = 'aL',
             charge = 0,
             GhostNumber = 0,
             LeptonNumber = 0,
             line='double',
             Y = 0)

# AL: Now right-chiral photon
aR = Particle(pdg_code = 90024,
             name = 'aR',
             antiname = 'aR',
             spin = 3,
             color = 1,
             mass = Param.ZERO,
             width = Param.ZERO,
             texname = 'aR',
             antitexname = 'aR',
             charge = 0,
             GhostNumber = 0,
             LeptonNumber = 0,
             line='double',
             Y = 0)

# Chiral Leptons

eL__minus__ = Particle(pdg_code = 90001,
                      name = 'eL-',
                      antiname = 'eL+',
                      spin = 2,
                      color = 1,
                      mass = Param.Me,
                      width = Param.ZERO,
                      texname = 'eL-',
                      antitexname = 'eL+',
                      charge = -1,
                      GhostNumber = 0,
                      LeptonNumber = 1,
                      line='dotted',
                      Y = 0)

eL__plus__ = eL__minus__.anti()


eR__minus__ = Particle(pdg_code = 90003,
                      name = 'eR-',
                      antiname = 'eR+',
                      spin = 2,
                      color = 1,
                      mass = Param.Me,
                      width = Param.ZERO,
                      texname = 'eR-',
                      antitexname = 'eR+',
                      charge = -1,
                      GhostNumber = 0,
                      LeptonNumber = 1,
                      line='straight',
                      Y = 0)

eR__plus__ = eR__minus__.anti()

muL__minus__ = Particle(pdg_code = 90005,
                       name = 'muL-',
                       antiname = 'muL+',
                       spin = 2,
                       color = 1,
                       mass = Param.MM,
                       width = Param.ZERO,
                       texname = 'muL-',
                       antitexname = 'muL+',
                       charge = -1,
                       GhostNumber = 0,
                       LeptonNumber = 1,
                       line='dotted',
                       Y = 0)
                       
muL__plus__ = muL__minus__.anti()

muR__minus__ = Particle(pdg_code = 90007,
                       name = 'muR-',
                       antiname = 'muR+',
                       spin = 2,
                       color = 1,
                       mass = Param.MM,
                       width = Param.ZERO,
                       texname = 'muR-',
                       antitexname = 'muR+',
                       charge = -1,
                       GhostNumber = 0,
                       LeptonNumber = 1,
                       line='straight',
                       Y = 0)

muR__plus__ = muR__minus__.anti()
