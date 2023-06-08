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

VIVLVR1 = Lorentz(name = 'VIVLVR1',
                spins = [ 3, 3, 3 ],
                structure = 'P(3,1)*Metric(1,2) - P(3,2)*Metric(1,2) - P(2,1)*Metric(1,3) + P(2,3)*Metric(1,3) + P(1,2)*Metric(2,3) - P(1,3)*Metric(2,3)')


VVLVL1 = Lorentz(name = 'VVLVL1',
                spins = [ 3, 3, 3 ],
                structure = 'P(3,1)*Metric(1,2) - P(3,2)*Metric(1,2) - P(2,1)*Metric(1,3) + P(2,3)*Metric(1,3) + P(1,2)*Metric(2,3) - P(1,3)*Metric(2,3)')

VVRVR1 = Lorentz(name = 'VVRVR1',
                spins = [ 3, 3, 3 ],
                structure = 'P(3,1)*Metric(1,2) - P(3,2)*Metric(1,2) - P(2,1)*Metric(1,3) + P(2,3)*Metric(1,3) + P(1,2)*Metric(2,3) - P(1,3)*Metric(2,3)')

VLVLVL1 = Lorentz(name = 'VLVLVL1',
                spins = [ 3, 3, 3 ],
                structure = 'P(3,1)*Metric(1,2) - P(3,2)*Metric(1,2) - P(2,1)*Metric(1,3) + P(2,3)*Metric(1,3) + P(1,2)*Metric(2,3) - P(1,3)*Metric(2,3)')

VRVRVR1 = Lorentz(name = 'VRVRVR1',
                spins = [ 3, 3, 3 ],
                structure = 'P(3,1)*Metric(1,2) - P(3,2)*Metric(1,2) - P(2,1)*Metric(1,3) + P(2,3)*Metric(1,3) + P(1,2)*Metric(2,3) - P(1,3)*Metric(2,3)')

VLVRVR1 = Lorentz(name = 'VLVRVR1',
                spins = [ 3, 3, 3 ],
                structure = 'P(3,1)*Metric(1,2) - P(3,2)*Metric(1,2) - P(2,1)*Metric(1,3) + P(2,3)*Metric(1,3) + P(1,2)*Metric(2,3) - P(1,3)*Metric(2,3)')

VLVLVR1 = Lorentz(name = 'VLVLVR1',
                spins = [ 3, 3, 3 ],
                structure = 'P(3,1)*Metric(1,2) - P(3,2)*Metric(1,2) - P(2,1)*Metric(1,3) + P(2,3)*Metric(1,3) + P(1,2)*Metric(2,3) - P(1,3)*Metric(2,3)')

#VLVLVR1 = Lorentz(name = 'VLVLVR1',
#                spins = [ 3, 3, 3 ],
#                structure = 'P(3,1)*Metric(1,2) - P(3,2)*Metric(1,2) - P(2,1)*Metric(1,3) + P(2,3)*Metric(1,3) + P(1,2)*Metric(2,3) - P(1,3)*Metric(2,3)')


VVVV1 = Lorentz(name = 'VVVV1',
                spins = [ 3, 3, 3, 3 ],
                structure = 'Metric(1,4)*Metric(2,3) - Metric(1,3)*Metric(2,4)')

VVVV3 = Lorentz(name = 'VVVV3',
                spins = [ 3, 3, 3, 3 ],
                structure = 'Metric(1,4)*Metric(2,3) - Metric(1,2)*Metric(3,4)')

VVVV4 = Lorentz(name = 'VVVV4',
                spins = [ 3, 3, 3, 3 ],
                structure = 'Metric(1,3)*Metric(2,4) - Metric(1,2)*Metric(3,4)')

VVIVLVL1 = Lorentz(name = 'VVIVLVL1',
                spins = [ 3, 3, 3, 3 ],
                structure = 'Metric(1,4)*Metric(2,3) - Metric(1,3)*Metric(2,4)')

VVIVLVL3 = Lorentz(name = 'VVIVLVL3',
                spins = [ 3, 3, 3, 3 ],
                structure = 'Metric(1,4)*Metric(2,3) - Metric(1,3)*Metric(2,4)')

VVIVLVL4 = Lorentz(name = 'VVIVLVL4',
                spins = [ 3, 3, 3, 3 ],
                structure = 'Metric(1,4)*Metric(2,3) - Metric(1,3)*Metric(2,4)')

VLVLVLVR1 = Lorentz(name = 'VLVLVLVR1',
                spins = [ 3, 3, 3, 3 ],
                structure = 'Metric(1,4)*Metric(2,3) - Metric(1,3)*Metric(2,4)')

VLVLVLVR3 = Lorentz(name = 'VLVLVLVR3',
                spins = [ 3, 3, 3, 3 ],
                structure = 'Metric(1,4)*Metric(2,3) - Metric(1,2)*Metric(3,4)')

VLVLVLVR4 = Lorentz(name = 'VLVLVLVR4',
                spins = [ 3, 3, 3, 3 ],
                structure = 'Metric(1,3)*Metric(2,4) - Metric(1,2)*Metric(3,4)')

VLVRVRVR1 = Lorentz(name = 'VLVRVRVR1',
                spins = [ 3, 3, 3, 3 ],
                structure = 'Metric(1,4)*Metric(2,3) - Metric(1,3)*Metric(2,4)')

VLVRVRVR3 = Lorentz(name = 'VLVRVRVR3',
                spins = [ 3, 3, 3, 3 ],
                structure = 'Metric(1,4)*Metric(2,3) - Metric(1,2)*Metric(3,4)')

VLVRVRVR4 = Lorentz(name = 'VLVRVRVR4',
                spins = [ 3, 3, 3, 3 ],
                structure = 'Metric(1,3)*Metric(2,4) - Metric(1,2)*Metric(3,4)')


VLVLVRVR1 = Lorentz(name = 'VLVLVRVR1',
                spins = [ 3, 3, 3, 3 ],
                structure = 'Metric(1,4)*Metric(2,3) - Metric(1,3)*Metric(2,4)')

VLVLVRVR3 = Lorentz(name = 'VLVLVRVR3',
                spins = [ 3, 3, 3, 3 ],
                structure = 'Metric(1,4)*Metric(2,3) - Metric(1,2)*Metric(3,4)')

VLVLVRVR4 = Lorentz(name = 'VLVLVRVR4',
                spins = [ 3, 3, 3, 3 ],
                structure = 'Metric(1,3)*Metric(2,4) - Metric(1,2)*Metric(3,4)')

VVLVRVR1 = Lorentz(name = 'VVLVRVR1',
                spins = [ 3, 3, 3, 3 ],
                structure = 'Metric(1,4)*Metric(2,3) - Metric(1,3)*Metric(2,4)')

VVLVRVR3 = Lorentz(name = 'VVLVRVR3',
                spins = [ 3, 3, 3, 3 ],
                structure = 'Metric(1,4)*Metric(2,3) - Metric(1,2)*Metric(3,4)')

VVLVRVR4 = Lorentz(name = 'VVLVRVR4',
                spins = [ 3, 3, 3, 3 ],
                structure = 'Metric(1,3)*Metric(2,4) - Metric(1,2)*Metric(3,4)')

VVLVLVR1 = Lorentz(name = 'VVLVLVR1',
                spins = [ 3, 3, 3, 3 ],
                structure = 'Metric(1,4)*Metric(2,3) - Metric(1,3)*Metric(2,4)')

VVLVLVR3 = Lorentz(name = 'VVLVLVR3',
                spins = [ 3, 3, 3, 3 ],
                structure = 'Metric(1,4)*Metric(2,3) - Metric(1,2)*Metric(3,4)')

VVLVLVR4 = Lorentz(name = 'VVLVLVR4',
                spins = [ 3, 3, 3, 3 ],
                structure = 'Metric(1,3)*Metric(2,4) - Metric(1,2)*Metric(3,4)')


VLVRVRVR1 = Lorentz(name = 'VLVRVRVR1',
                spins = [ 3, 3, 3, 3 ],
                structure = 'Metric(1,4)*Metric(2,3) - Metric(1,3)*Metric(2,4)')

VLVRVRVR3 = Lorentz(name = 'VLVRVRVR3',
                spins = [ 3, 3, 3, 3 ],
                structure = 'Metric(1,4)*Metric(2,3) - Metric(1,2)*Metric(3,4)')

VLVRVRVR4 = Lorentz(name = 'VLVRVRVR4',
                spins = [ 3, 3, 3, 3 ],
                structure = 'Metric(1,3)*Metric(2,4) - Metric(1,2)*Metric(3,4)')

VVIVLVR1 = Lorentz(name = 'VVIVLVR1',
                spins = [ 3, 3, 3, 3 ],
                structure = 'Metric(1,4)*Metric(2,3) - Metric(1,3)*Metric(2,4)')

VVIVLVR3 = Lorentz(name = 'VVIVLVR3',
                spins = [ 3, 3, 3, 3 ],
                structure = 'Metric(1,4)*Metric(2,3) - Metric(1,2)*Metric(3,4)')

VVIVLVR4 = Lorentz(name = 'VVIVLVR4',
                spins = [ 3, 3, 3, 3 ],
                structure = 'Metric(1,3)*Metric(2,4) - Metric(1,2)*Metric(3,4)')


VVVRVR1 = Lorentz(name = 'VVVRVR1',
                spins = [ 3, 3, 3, 3 ],
                structure = 'Metric(1,4)*Metric(2,3) - Metric(1,3)*Metric(2,4)')

VVVRVR3 = Lorentz(name = 'VVVRVR3',
                spins = [ 3, 3, 3, 3 ],
                structure = 'Metric(1,4)*Metric(2,3) - Metric(1,2)*Metric(3,4)')

VVVRVR4 = Lorentz(name = 'VVVRVR4',
                spins = [ 3, 3, 3, 3 ],
                structure = 'Metric(1,3)*Metric(2,4) - Metric(1,2)*Metric(3,4)')

VVVLVL1 = Lorentz(name = 'VVVLVL1',
                spins = [ 3, 3, 3, 3 ],
                structure = 'Metric(1,4)*Metric(2,3) - Metric(1,3)*Metric(2,4)')

VVVLVL3 = Lorentz(name = 'VVVLVL3',
                spins = [ 3, 3, 3, 3 ],
                structure = 'Metric(1,4)*Metric(2,3) - Metric(1,2)*Metric(3,4)')

VVVLVL4 = Lorentz(name = 'VVVLVL4',
                spins = [ 3, 3, 3, 3 ],
                structure = 'Metric(1,3)*Metric(2,4) - Metric(1,2)*Metric(3,4)')

VVRVRVR1 = Lorentz(name = 'VVRVRVR1',
                spins = [ 3, 3, 3, 3 ],
                structure = 'Metric(1,4)*Metric(2,3) - Metric(1,3)*Metric(2,4)')

VVRVRVR3 = Lorentz(name = 'VVRVRVR3',
                spins = [ 3, 3, 3, 3 ],
                structure = 'Metric(1,4)*Metric(2,3) - Metric(1,2)*Metric(3,4)')

VVRVRVR4 = Lorentz(name = 'VVRVRVR4',
                spins = [ 3, 3, 3, 3 ],
                structure = 'Metric(1,3)*Metric(2,4) - Metric(1,2)*Metric(3,4)')

VVLVLVL1 = Lorentz(name = 'VVLVLVL1',
                spins = [ 3, 3, 3, 3 ],
                structure = 'Metric(1,4)*Metric(2,3) - Metric(1,3)*Metric(2,4)')

VVLVLVL3 = Lorentz(name = 'VVLVLVL3',
                spins = [ 3, 3, 3, 3 ],
                structure = 'Metric(1,4)*Metric(2,3) - Metric(1,2)*Metric(3,4)')

VVLVLVL4 = Lorentz(name = 'VVLVLVL4',
                spins = [ 3, 3, 3, 3 ],
                structure = 'Metric(1,3)*Metric(2,4) - Metric(1,2)*Metric(3,4)')

VVVIVR1 = Lorentz(name = 'VVVIVR1',
                spins = [ 3, 3, 3, 3 ],
                structure = 'Metric(1,4)*Metric(2,3) - Metric(1,3)*Metric(2,4)')

VVVIVR3 = Lorentz(name = 'VVVIVR3',
                spins = [ 3, 3, 3, 3 ],
                structure = 'Metric(1,4)*Metric(2,3) - Metric(1,2)*Metric(3,4)')

VVVIVR4 = Lorentz(name = 'VVVIVR4',
                spins = [ 3, 3, 3, 3 ],
                structure = 'Metric(1,3)*Metric(2,4) - Metric(1,2)*Metric(3,4)')

VVVIVL1 = Lorentz(name = 'VVVIVL1',
                spins = [ 3, 3, 3, 3 ],
                structure = 'Metric(1,4)*Metric(2,3) - Metric(1,3)*Metric(2,4)')

VVVIVL3 = Lorentz(name = 'VVVIVL3',
                spins = [ 3, 3, 3, 3 ],
                structure = 'Metric(1,4)*Metric(2,3) - Metric(1,2)*Metric(3,4)')

VVVIVL4 = Lorentz(name = 'VVVIVL4',
                spins = [ 3, 3, 3, 3 ],
                structure = 'Metric(1,3)*Metric(2,4) - Metric(1,2)*Metric(3,4)')

################################## Add these to misc.py #############################################

VIVLVLVR1 = Lorentz(name = 'VIVLVLVR1',
                spins = [ 3, 3, 3, 3 ],
                structure = 'Metric(1,4)*Metric(2,3) - Metric(1,3)*Metric(2,4)')

VIVLVLVR3 = Lorentz(name = 'VIVLVLVR3',
                spins = [ 3, 3, 3, 3 ],
                structure = 'Metric(1,4)*Metric(2,3) - Metric(1,2)*Metric(3,4)')

VIVLVLVR4 = Lorentz(name = 'VIVLVLVR4',
                spins = [ 3, 3, 3, 3 ],
                structure = 'Metric(1,3)*Metric(2,4) - Metric(1,2)*Metric(3,4)')


VIVLVRVR1 = Lorentz(name = 'VIVLVRVR1',
                spins = [ 3, 3, 3, 3 ],
                structure = 'Metric(1,4)*Metric(2,3) - Metric(1,3)*Metric(2,4)')

VIVLVRVR3 = Lorentz(name = 'VIVLVRVR3',
                spins = [ 3, 3, 3, 3 ],
                structure = 'Metric(1,4)*Metric(2,3) - Metric(1,2)*Metric(3,4)')

VIVLVRVR4 = Lorentz(name = 'VIVLVRVR4',
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

