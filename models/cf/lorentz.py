# This file was automatically created by FeynRules 1.7.69
# Mathematica version: 8.0 for Mac OS X x86 (64-bit) (November 6, 2010)
# Date: Mon 1 Oct 2012 14:58:26


from object_library import all_lorentz, Lorentz

from function_library import complexconjugate, re, im, csc, sec, acsc, asec
try:
   import form_factors as ForFac 
except ImportError:
   pass

# AL: Left and right chiral projector vertices for building chiral Feynman diagrams
RLV1 = Lorentz(name = 'RLV1',
               spins = [ 2, 2, 3 ],
               structure = 'Gamma(3,2,-1)*ProjM(-1,1)' )
              
LRV1 = Lorentz(name = 'LRV1',
               spins = [ 2, 2, 3],
               structure = 'Gamma(3,2,-1)*ProjP(-1,1)' )

# AL: New Lorentz structures to give to vertices based on which fermion is left, which is right
# The name will be used to know if an off-shell fermion is left/right chiral.
# The structure argument is irrelivent. It will be overwritten with the correct chirality-flow
# values during the aloha stage (TODO: double check exact stage, it will be before running make for Helas/Model)
LLV1 = Lorentz(name = 'LLV1',
               spins = [ 2, 2, 3 ],
               structure = 'Gamma(3,2,-1)*ProjM(-1,1)' )

RRV1 = Lorentz(name = 'RRV1',
               spins = [ 2, 2, 3],
               structure = 'Gamma(3,2,-1)*ProjP(-1,1)' )




# AL: I have commented out all other lorentz structures that we don't yet use in building
# chirality-flow diagrams

# AW: I uncommented the structures needed for QCD

VVV1 = Lorentz(name = 'VVV1',
                spins = [ 3, 3, 3 ],
                structure = 'P(3,1)*Metric(1,2) - P(3,2)*Metric(1,2) - P(2,1)*Metric(1,3) + P(2,3)*Metric(1,3) + P(1,2)*Metric(2,3) - P(1,3)*Metric(2,3)')

VVVV1 = Lorentz(name = 'VVVV1',
                spins = [ 3, 3, 3, 3 ],
                structure = 'Metric(1,4)*Metric(2,3) - Metric(1,3)*Metric(2,4)')

VVVV3 = Lorentz(name = 'VVVV3',
                spins = [ 3, 3, 3, 3 ],
                structure = 'Metric(1,4)*Metric(2,3) - Metric(1,2)*Metric(3,4)')

VVVV4 = Lorentz(name = 'VVVV4',
                spins = [ 3, 3, 3, 3 ],
                structure = 'Metric(1,3)*Metric(2,4) - Metric(1,2)*Metric(3,4)')

# VVVV2 = Lorentz(name = 'VVVV2',
#                 spins = [ 3, 3, 3, 3 ],
#                 structure = 'Metric(1,4)*Metric(2,3) + Metric(1,3)*Metric(2,4) - 2*Metric(1,2)*Metric(3,4)')

# UUS1 = Lorentz(name = 'UUS1',
#                spins = [ -1, -1, 1 ],
#                structure = '1')

# UUV1 = Lorentz(name = 'UUV1',
#                spins = [ -1, -1, 3 ],
#                structure = 'P(3,2) + P(3,3)')

# SSS1 = Lorentz(name = 'SSS1',
#                spins = [ 1, 1, 1 ],
#                structure = '1')

# SSS2 = Lorentz(name = 'SSS2',
#                spins = [ 1, 1, 1, ],
#                structure = '1')

# SSS3 = Lorentz(name = 'SSS3',
#                spins = [ 1, 1, 1, ],
#                structure = '1')

# FFS1 = Lorentz(name = 'FFS1',
#                spins = [ 2, 2, 1 ],
#                structure = 'ProjM(2,1)')

# FFS2 = Lorentz(name = 'FFS2',
#                spins = [ 2, 2, 1 ],
#                structure = 'ProjM(2,1) - ProjP(2,1)')

# FFS3 = Lorentz(name = 'FFS3',
#                spins = [ 2, 2, 1 ],
#                structure = 'ProjP(2,1)')

# FFS4 = Lorentz(name = 'FFS4',
#                spins = [ 2, 2, 1 ],
#                structure = 'ProjM(2,1) + ProjP(2,1)')

# FFV1 = Lorentz(name = 'FFV1',
#                spins = [ 2, 2, 3 ],
#                structure = 'Gamma(3,2,1)')

# FFV2 = Lorentz(name = 'FFV2',
#                spins = [ 2, 2, 3 ],
#                structure = 'Gamma(3,2,-1)*ProjM(-1,1)')

# FFV3 = Lorentz(name = 'FFV3',
#                spins = [ 2, 2, 3 ],
#                structure = 'Gamma(3,2,-1)*ProjM(-1,1) - 2*Gamma(3,2,-1)*ProjP(-1,1)')

# FFV4 = Lorentz(name = 'FFV4',
#                spins = [ 2, 2, 3 ],
#                structure = 'Gamma(3,2,-1)*ProjM(-1,1) + 2*Gamma(3,2,-1)*ProjP(-1,1)')

# FFV5 = Lorentz(name = 'FFV5',
#                spins = [ 2, 2, 3 ],
#                structure = 'Gamma(3,2,-1)*ProjM(-1,1) + 4*Gamma(3,2,-1)*ProjP(-1,1)')
              
# FFV6 = Lorentz(name = 'FFV6',
#                spins = [ 2, 2, 3],
#                structure = 'Gamma(3,2,-1)*ProjP(-1,1)')
               

# VSS1 = Lorentz(name = 'VSS1',
#                spins = [ 3, 1, 1 ],
#                structure = 'P(1,2) - P(1,3)')

# VSS2 = Lorentz(name = 'VSS2',
#                spins = [3, 1, 1 ],
#                structure = '1' )

# VVS1 = Lorentz(name = 'VVS1',
#                spins = [ 3, 3, 1 ],
#                structure = 'Metric(1,2)')

# SSSS1 = Lorentz(name = 'SSSS1',
#                 spins = [ 1, 1, 1, 1 ],
#                 structure = '1')

# SSSS2 = Lorentz(name = 'SSSS2',
#                 spins = [ 1, 1, 1, 1 ],
#                 structure = 'P(1,1) + P(1,4)')

# VVSS1 = Lorentz(name = 'VVSS1',
#                 spins = [ 3, 3, 1, 1 ],
#                 structure = 'Metric(1,2)')

# VVVV5 = Lorentz(name = 'VVVV5',
#                 spins = [ 3, 3, 3, 3 ],
#                 structure = 'Metric(1,4)*Metric(2,3) - (Metric(1,3)*Metric(2,4))/2. - (Metric(1,2)*Metric(3,4))/2.')

