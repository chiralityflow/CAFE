# This file was automatically created by FeynRules 1.7.69
# Mathematica version: 8.0 for Mac OS X x86 (64-bit) (November 6, 2010)
# Date: Mon 1 Oct 2012 14:58:25

from object_library import all_vertices, Vertex
import particles as P
import couplings as C
import lorentz as L

# MS: If we add new particles, we must also add their vertices here
# AL: V1 to V4 used to create diagrams, 
# MS: ...s pecifically for internal photons
# AL: Lorentz structure will be updated when constructing Helas (after constructing diagrams)
# to one of either LRV, RLV, LLV, or RRV depending on process. L/R denote right/left fermions
V_1 = Vertex(name = 'V_1',
              particles = [ P.eR__plus__, P.eL__minus__, P.a ],
              color = [ '1' ], # color singlet
              lorentz = [ L.RLV1 ], # L for Lorentz, see lorentz.py in this folder
              couplings = {(0,0):C.GC_3}) # QCD singlet, see couplings.py

V_2 = Vertex(name = 'V_2',
              particles = [ P.eL__plus__, P.eR__minus__, P.a ],
              color = [ '1' ],
              lorentz = [ L.LRV1 ],
              couplings = {(0,0):C.GC_3})
              

V_3 = Vertex(name = 'V_3',
              particles = [ P.muR__plus__, P.muL__minus__, P.a ],
              color = [ '1' ],
              lorentz = [ L.RLV1 ],
              couplings = {(0,0):C.GC_3})

V_4 = Vertex(name = 'V_4',
              particles = [ P.muL__plus__, P.muR__minus__, P.a ],
              color = [ '1' ],
              lorentz = [ L.LRV1 ],
              couplings = {(0,0):C.GC_3})


####################################################
# AL: Same vertices as above but with chiral photons
# MS: Use this for external photons
####################################################

# TODO: Check if lorentz structure will need any updating (I don't think it will)

V_5 = Vertex(name = 'V_5',
              particles = [ P.eR__plus__, P.eL__minus__, P.aL ],
              color = [ '1' ],
              lorentz = [ L.RLV1 ],
              couplings = {(0,0):C.GC_3})

V_6 = Vertex(name = 'V_6',
              particles = [ P.eR__plus__, P.eL__minus__, P.aR ],
              color = [ '1' ],
              lorentz = [ L.RLV1 ],
              couplings = {(0,0):C.GC_3})


V_7 = Vertex(name = 'V_7',
              particles = [ P.eL__plus__, P.eR__minus__, P.aL ],
              color = [ '1' ],
              lorentz = [ L.LRV1 ],
              couplings = {(0,0):C.GC_3})

V_8 = Vertex(name = 'V_8',
              particles = [ P.eL__plus__, P.eR__minus__, P.aR ],
              color = [ '1' ],
              lorentz = [ L.LRV1 ],
              couplings = {(0,0):C.GC_3})


V_9 = Vertex(name = 'V_9',
              particles = [ P.muR__plus__, P.muL__minus__, P.aL ],
              color = [ '1' ],
              lorentz = [ L.RLV1 ],
              couplings = {(0,0):C.GC_3})

V_10 = Vertex(name = 'V_10',
              particles = [ P.muR__plus__, P.muL__minus__, P.aR ],
              color = [ '1' ],
              lorentz = [ L.RLV1 ],
              couplings = {(0,0):C.GC_3})


V11 = Vertex(name = 'V_11',
              particles = [ P.muL__plus__, P.muR__minus__, P.aL ],
              color = [ '1' ],
              lorentz = [ L.LRV1 ],
              couplings = {(0,0):C.GC_3})

V_12 = Vertex(name = 'V_12',
              particles = [ P.muL__plus__, P.muR__minus__, P.aR ],
              color = [ '1' ],
              lorentz = [ L.LRV1 ],
              couplings = {(0,0):C.GC_3})


# AW: Quark-antiquark-gluon vertices
# V_13-V_16 with non chiral gluons

V_13 = Vertex(name = 'V_13',
               particles = [ P.uL__tilde__, P.uR, P.g ],
               color = [ 'T(3,2,1)' ],
               lorentz = [ L.LRV1 ],
               couplings = {(0,0):C.GC_11})

V_14 = Vertex(name = 'V_14',
               particles = [ P.uR__tilde__, P.uL, P.g ],
               color = [ 'T(3,2,1)' ],
               lorentz = [ L.RLV1 ],
               couplings = {(0,0):C.GC_11})

V_15 = Vertex(name = 'V_15',
               particles = [ P.dL__tilde__, P.dR, P.g ],
               color = [ 'T(3,2,1)' ],
               lorentz = [ L.LRV1 ],
               couplings = {(0,0):C.GC_11})

V_16 = Vertex(name = 'V_16',
               particles = [ P.dR__tilde__, P.dL, P.g ],
               color = [ 'T(3,2,1)' ],
               lorentz = [ L.RLV1 ],
               couplings = {(0,0):C.GC_11})

# Chiral gluons from here

V_17 = Vertex(name = 'V_17',
               particles = [ P.uL__tilde__, P.uR, P.gL ],
               color = [ 'T(3,2,1)' ],
               lorentz = [ L.LRV1 ],
               couplings = {(0,0):C.GC_11})

V_18 = Vertex(name = 'V_18',
               particles = [ P.uL__tilde__, P.uR, P.gR ],
               color = [ 'T(3,2,1)' ],
               lorentz = [ L.LRV1 ],
               couplings = {(0,0):C.GC_11})               

V_19 = Vertex(name = 'V_19',
               particles = [ P.uR__tilde__, P.uL, P.gL ],
               color = [ 'T(3,2,1)' ],
               lorentz = [ L.RLV1 ],
               couplings = {(0,0):C.GC_11})

V_20 = Vertex(name = 'V_20',
               particles = [ P.uR__tilde__, P.uL, P.gR ],
               color = [ 'T(3,2,1)' ],
               lorentz = [ L.RLV1 ],
               couplings = {(0,0):C.GC_11})

V_21 = Vertex(name = 'V_21',
               particles = [ P.dL__tilde__, P.dR, P.gL ],
               color = [ 'T(3,2,1)' ],
               lorentz = [ L.LRV1 ],
               couplings = {(0,0):C.GC_11})

V_22 = Vertex(name = 'V_22',
               particles = [ P.dL__tilde__, P.dR, P.gR ],
               color = [ 'T(3,2,1)' ],
               lorentz = [ L.LRV1 ],
               couplings = {(0,0):C.GC_11})

V_23 = Vertex(name = 'V_23',
               particles = [ P.dR__tilde__, P.dL, P.gL ],
               color = [ 'T(3,2,1)' ],
               lorentz = [ L.RLV1 ],
               couplings = {(0,0):C.GC_11})


V_24 = Vertex(name = 'V_24',
               particles = [ P.dR__tilde__, P.dL, P.gR ],
               color = [ 'T(3,2,1)' ],
               lorentz = [ L.RLV1 ],
               couplings = {(0,0):C.GC_11})


# AW: ADD Q Q PHOTON VERTEX

V_25 = Vertex(name = 'V_25',
               particles = [ P.uL__tilde__, P.uR, P.a ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.LRV1 ],
               couplings = {(0,0):C.GC_2})

V_26 = Vertex(name = 'V_26',
               particles = [ P.uR__tilde__, P.uL, P.a ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.RLV1 ],
               couplings = {(0,0):C.GC_2})

V_27 = Vertex(name = 'V_27',
              particles = [ P.dL__tilde__, P.dR, P.a ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.LRV1 ],
              couplings = {(0,0):C.GC_1})

V_28 = Vertex(name = 'V_28',
              particles = [ P.dR__tilde__, P.dL, P.a ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.RLV1 ],
              couplings = {(0,0):C.GC_1})

V_29 = Vertex(name = 'V_29',
               particles = [ P.uL__tilde__, P.uR, P.aL ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.LRV1 ],
               couplings = {(0,0):C.GC_2})

V_30 = Vertex(name = 'V_30',
               particles = [ P.uL__tilde__, P.uR, P.aR ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.LRV1 ],
               couplings = {(0,0):C.GC_2})

V_31 = Vertex(name = 'V_31',
               particles = [ P.uR__tilde__, P.uL, P.aL ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.RLV1 ],
               couplings = {(0,0):C.GC_2})

V_32 = Vertex(name = 'V_32',
               particles = [ P.uR__tilde__, P.uL, P.aR ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.RLV1 ],
               couplings = {(0,0):C.GC_2})

V_33 = Vertex(name = 'V_33',
              particles = [ P.dL__tilde__, P.dR, P.aL ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.LRV1 ],
              couplings = {(0,0):C.GC_1})

V_34 = Vertex(name = 'V_34',
              particles = [ P.dL__tilde__, P.dR, P.aR ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.LRV1 ],
              couplings = {(0,0):C.GC_1})

V_35 = Vertex(name = 'V_35',
              particles = [ P.dR__tilde__, P.dL, P.aL ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.RLV1 ],
              couplings = {(0,0):C.GC_1})

V_36 = Vertex(name = 'V_36',
              particles = [ P.dR__tilde__, P.dL, P.aR ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.RLV1 ],
              couplings = {(0,0):C.GC_1})

# AW: Tripple gluon vertex
#AW: general vertices
V_37 = Vertex(name = 'V_37', 
	particles = [ P.g, P.g, P.g], 
	color = [ 'f(1,2,3)' ], 
	lorentz = [ L.VVV1 ], 
	couplings = {(0,0):C.GC_10})
V_38 = Vertex(name = 'V_38', 
	particles = [ P.g, P.g, P.gLI], 
	color = [ 'f(1,2,3)' ], 
	lorentz = [ L.VVV1 ], 
	couplings = {(0,0):C.GC_10})
V_39 = Vertex(name = 'V_39', 
	particles = [ P.g, P.g, P.gRI], 
	color = [ 'f(1,2,3)' ], 
	lorentz = [ L.VVV1 ], 
	couplings = {(0,0):C.GC_10})
V_40 = Vertex(name = 'V_40', 
	particles = [ P.g, P.g, P.gL], 
	color = [ 'f(1,2,3)' ], 
	lorentz = [ L.VVV1 ], 
	couplings = {(0,0):C.GC_10})
V_41 = Vertex(name = 'V_41', 
	particles = [ P.g, P.g, P.gR], 
	color = [ 'f(1,2,3)' ], 
	lorentz = [ L.VVV1 ], 
	couplings = {(0,0):C.GC_10})
V_42 = Vertex(name = 'V_42', 
	particles = [ P.g, P.gLI, P.gRI], 
	color = [ 'f(1,2,3)' ], 
	lorentz = [ L.VVLVL1 ], 
	couplings = {(0,0):C.GC_10})
V_43 = Vertex(name = 'V_43', 
	particles = [ P.g, P.gLI, P.gL], 
	color = [ 'f(1,2,3)' ], 
	lorentz = [ L.VVLVL1 ], 
	couplings = {(0,0):C.GC_10})
V_44 = Vertex(name = 'V_44', 
	particles = [ P.g, P.gLI, P.gR], 
	color = [ 'f(1,2,3)' ], 
	lorentz = [ L.VVRVR1 ], 
	couplings = {(0,0):C.GC_10})
V_45 = Vertex(name = 'V_45', 
	particles = [ P.g, P.gRI, P.gL], 
	color = [ 'f(1,2,3)' ], 
	lorentz = [ L.VVLVL1 ], 
	couplings = {(0,0):C.GC_10})
V_46 = Vertex(name = 'V_46', 
	particles = [ P.g, P.gRI, P.gR], 
	color = [ 'f(1,2,3)' ], 
	lorentz = [ L.VVRVR1 ], 
	couplings = {(0,0):C.GC_10})
V_47 = Vertex(name = 'V_47', 
	particles = [ P.g, P.gL, P.gL], 
	color = [ 'f(1,2,3)' ], 
	lorentz = [ L.VVLVL1 ], 
	couplings = {(0,0):C.GC_10})
V_48 = Vertex(name = 'V_48', 
	particles = [ P.g, P.gL, P.gR], 
	color = [ 'f(1,2,3)' ], 
	lorentz = [ L.VVV1 ], 
	couplings = {(0,0):C.GC_10})
V_49 = Vertex(name = 'V_49', 
	particles = [ P.g, P.gR, P.gR], 
	color = [ 'f(1,2,3)' ], 
	lorentz = [ L.VVRVR1 ], 
	couplings = {(0,0):C.GC_10})
V_50 = Vertex(name = 'V_50', 
	particles = [ P.gLI, P.gLI, P.gLI], 
	color = [ 'f(1,2,3)' ], 
	lorentz = [ L.VIVLVR1 ], 
	couplings = {(0,0):C.GC_10})
V_51 = Vertex(name = 'V_51', 
	particles = [ P.gRI, P.gRI, P.gRI], 
	color = [ 'f(1,2,3)' ], 
	lorentz = [ L.VIVLVR1 ], 
	couplings = {(0,0):C.GC_10})
""" V_50 = Vertex(name = 'V_50', 
	particles = [ P.gLI, P.gRI, P.gL], 
	color = [ 'f(1,2,3)' ], 
	lorentz = [ L.VIVLVR1 ], 
	couplings = {(0,0):C.GC_10})
V_51 = Vertex(name = 'V_51', 
	particles = [ P.gLI, P.gRI, P.gR], 
	color = [ 'f(1,2,3)' ], 
	lorentz = [ L.VIVLVR1 ], 
	couplings = {(0,0):C.GC_10}) """
V_52 = Vertex(name = 'V_52', 
	particles = [ P.gLI, P.gL, P.gL], 
	color = [ 'f(1,2,3)' ], 
	lorentz = [ L.VLVLVL1 ], 
	couplings = {(0,0):C.GC_10})
V_53 = Vertex(name = 'V_53', 
	particles = [ P.gLI, P.gL, P.gR], 
	color = [ 'f(1,2,3)' ], 
	lorentz = [ L.VIVLVR1 ], 
	couplings = {(0,0):C.GC_10})
V_54 = Vertex(name = 'V_54', 
	particles = [ P.gLI, P.gR, P.gR], 
	color = [ 'f(1,2,3)' ], 
	lorentz = [ L.VRVRVR1 ], 
	couplings = {(0,0):C.GC_10})
V_55 = Vertex(name = 'V_55', 
	particles = [ P.gRI, P.gL, P.gL], 
	color = [ 'f(1,2,3)' ], 
	lorentz = [ L.VLVLVL1 ], 
	couplings = {(0,0):C.GC_10})
V_56 = Vertex(name = 'V_56', 
	particles = [ P.gRI, P.gL, P.gR], 
	color = [ 'f(1,2,3)' ], 
	lorentz = [ L.VIVLVR1 ], 
	couplings = {(0,0):C.GC_10})
V_57 = Vertex(name = 'V_57', 
	particles = [ P.gRI, P.gR, P.gR], 
	color = [ 'f(1,2,3)' ], 
	lorentz = [ L.VRVRVR1 ], 
	couplings = {(0,0):C.GC_10})
V_58 = Vertex(name = 'V_58', 
	particles = [ P.gL, P.gL, P.gL], 
	color = [ 'f(1,2,3)' ], 
	lorentz = [ L.VLVLVL1 ], 
	couplings = {(0,0):C.GC_10})
V_59 = Vertex(name = 'V_59', 
	particles = [ P.gL, P.gL, P.gR], 
	color = [ 'f(1,2,3)' ], 
	lorentz = [ L.VLVLVR1 ], 
	couplings = {(0,0):C.GC_10})
V_60 = Vertex(name = 'V_60', 
	particles = [ P.gL, P.gR, P.gR], 
	color = [ 'f(1,2,3)' ], 
	lorentz = [ L.VVRVR1 ], 
	couplings = {(0,0):C.GC_10})
V_61 = Vertex(name = 'V_61', 
	particles = [ P.gR, P.gR, P.gR], 
	color = [ 'f(1,2,3)' ], 
	lorentz = [ L.VRVRVR1 ], 
	couplings = {(0,0):C.GC_10})
V_62 = Vertex(name = 'V_62',
	particles = [ P.g, P.g, P.g, P.g],
	color = [ 'f(-1,1,2)*f(3,4,-1)', 'f(-1,1,3)*f(2,4,-1)', 'f(-1,1,4)*f(2,3,-1)' ],
	lorentz = [ L.VVVV1, L.VVVV3, L.VVVV4 ],
	couplings = {(1,1):C.GC_12,(0,0):C.GC_12,(2,2):C.GC_12})
V_63 = Vertex(name = 'V_63',
	particles = [ P.g, P.g, P.g, P.gLI],
	color = [ 'f(-1,1,2)*f(3,4,-1)', 'f(-1,1,3)*f(2,4,-1)', 'f(-1,1,4)*f(2,3,-1)' ],
	lorentz = [ L.VVVV1, L.VVVV3, L.VVVV4 ],
	couplings = {(1,1):C.GC_12,(0,0):C.GC_12,(2,2):C.GC_12})
V_64 = Vertex(name = 'V_64',
	particles = [ P.g, P.g, P.g, P.gRI],
	color = [ 'f(-1,1,2)*f(3,4,-1)', 'f(-1,1,3)*f(2,4,-1)', 'f(-1,1,4)*f(2,3,-1)' ],
	lorentz = [ L.VVVV1, L.VVVV3, L.VVVV4 ],
	couplings = {(1,1):C.GC_12,(0,0):C.GC_12,(2,2):C.GC_12})
V_65 = Vertex(name = 'V_65',
	particles = [ P.g, P.g, P.g, P.gL],
	color = [ 'f(-1,1,2)*f(3,4,-1)', 'f(-1,1,3)*f(2,4,-1)', 'f(-1,1,4)*f(2,3,-1)' ],
	lorentz = [ L.VVVV1, L.VVVV3, L.VVVV4 ],
	couplings = {(1,1):C.GC_12,(0,0):C.GC_12,(2,2):C.GC_12})
V_66 = Vertex(name = 'V_66',
	particles = [ P.g, P.g, P.g, P.gR],
	color = [ 'f(-1,1,2)*f(3,4,-1)', 'f(-1,1,3)*f(2,4,-1)', 'f(-1,1,4)*f(2,3,-1)' ],
	lorentz = [ L.VVVV1, L.VVVV3, L.VVVV4 ],
	couplings = {(1,1):C.GC_12,(0,0):C.GC_12,(2,2):C.GC_12})
V_67 = Vertex(name = 'V_67',
	particles = [ P.g, P.g, P.gLI, P.gRI],
	color = [ 'f(-1,1,2)*f(3,4,-1)', 'f(-1,1,3)*f(2,4,-1)', 'f(-1,1,4)*f(2,3,-1)' ],
	lorentz = [ L.VVVV1, L.VVVV3, L.VVVV4 ],
	couplings = {(1,1):C.GC_12,(0,0):C.GC_12,(2,2):C.GC_12})
V_68 = Vertex(name = 'V_68',
	particles = [ P.g, P.g, P.gLI, P.gL],
	color = [ 'f(-1,1,2)*f(3,4,-1)', 'f(-1,1,3)*f(2,4,-1)', 'f(-1,1,4)*f(2,3,-1)' ],
	lorentz = [ L.VVVIVL1, L.VVVIVL3, L.VVVIVL4 ],
	couplings = {(1,1):C.GC_12,(0,0):C.GC_12,(2,2):C.GC_12})
V_69 = Vertex(name = 'V_69',
	particles = [ P.g, P.g, P.gLI, P.gR],
	color = [ 'f(-1,1,2)*f(3,4,-1)', 'f(-1,1,3)*f(2,4,-1)', 'f(-1,1,4)*f(2,3,-1)' ],
	lorentz = [ L.VVVIVR1, L.VVVIVR3, L.VVVIVR4 ],
	couplings = {(1,1):C.GC_12,(0,0):C.GC_12,(2,2):C.GC_12})
V_70 = Vertex(name = 'V_70',
	particles = [ P.g, P.g, P.gRI, P.gL],
	color = [ 'f(-1,1,2)*f(3,4,-1)', 'f(-1,1,3)*f(2,4,-1)', 'f(-1,1,4)*f(2,3,-1)' ],
	lorentz = [ L.VVVIVL1, L.VVVIVL3, L.VVVIVL4 ],
	couplings = {(1,1):C.GC_12,(0,0):C.GC_12,(2,2):C.GC_12})
V_71 = Vertex(name = 'V_71',
	particles = [ P.g, P.g, P.gRI, P.gR],
	color = [ 'f(-1,1,2)*f(3,4,-1)', 'f(-1,1,3)*f(2,4,-1)', 'f(-1,1,4)*f(2,3,-1)' ],
	lorentz = [ L.VVVIVR1, L.VVVIVR3, L.VVVIVR4 ],
	couplings = {(1,1):C.GC_12,(0,0):C.GC_12,(2,2):C.GC_12})
V_72 = Vertex(name = 'V_72',
	particles = [ P.g, P.g, P.gL, P.gL],
	color = [ 'f(-1,1,2)*f(3,4,-1)', 'f(-1,1,3)*f(2,4,-1)', 'f(-1,1,4)*f(2,3,-1)' ],
	lorentz = [ L.VVVLVL1, L.VVVLVL3, L.VVVLVL4 ],
	couplings = {(1,1):C.GC_12,(0,0):C.GC_12,(2,2):C.GC_12})
V_73 = Vertex(name = 'V_73',
	particles = [ P.g, P.g, P.gL, P.gR],
	color = [ 'f(-1,1,2)*f(3,4,-1)', 'f(-1,1,3)*f(2,4,-1)', 'f(-1,1,4)*f(2,3,-1)' ],
	lorentz = [ L.VVVV1, L.VVVV3, L.VVVV4 ],
	couplings = {(1,1):C.GC_12,(0,0):C.GC_12,(2,2):C.GC_12})
V_74 = Vertex(name = 'V_74',
	particles = [ P.g, P.g, P.gR, P.gR],
	color = [ 'f(-1,1,2)*f(3,4,-1)', 'f(-1,1,3)*f(2,4,-1)', 'f(-1,1,4)*f(2,3,-1)' ],
	lorentz = [ L.VVVRVR1, L.VVVRVR3, L.VVVRVR4 ],
	couplings = {(1,1):C.GC_12,(0,0):C.GC_12,(2,2):C.GC_12})
V_75 = Vertex(name = 'V_75',
	particles = [ P.g, P.gLI, P.gL, P.gR],
	color = [ 'f(-1,1,2)*f(3,4,-1)', 'f(-1,1,3)*f(2,4,-1)', 'f(-1,1,4)*f(2,3,-1)' ],
	lorentz = [ L.VVIVLVR1, L.VVIVLVR3, L.VVIVLVR4 ],
	couplings = {(1,1):C.GC_12,(0,0):C.GC_12,(2,2):C.GC_12})
V_76 = Vertex(name = 'V_76',
	particles = [ P.g, P.gRI, P.gL, P.gR],
	color = [ 'f(-1,1,2)*f(3,4,-1)', 'f(-1,1,3)*f(2,4,-1)', 'f(-1,1,4)*f(2,3,-1)' ],
	lorentz = [ L.VVIVLVR1, L.VVIVLVR3, L.VVIVLVR4 ],
	couplings = {(1,1):C.GC_12,(0,0):C.GC_12,(2,2):C.GC_12})
V_77 = Vertex(name = 'V_77',
	particles = [ P.g, P.gL, P.gL, P.gL],
	color = [ 'f(-1,1,2)*f(3,4,-1)', 'f(-1,1,3)*f(2,4,-1)', 'f(-1,1,4)*f(2,3,-1)' ],
	lorentz = [ L.VVLVLVL1, L.VVLVLVL3, L.VVLVLVL4 ],
	couplings = {(1,1):C.GC_12,(0,0):C.GC_12,(2,2):C.GC_12})
V_78 = Vertex(name = 'V_78',
	particles = [ P.g, P.gL, P.gL, P.gR],
	color = [ 'f(-1,1,2)*f(3,4,-1)', 'f(-1,1,3)*f(2,4,-1)', 'f(-1,1,4)*f(2,3,-1)' ],
	lorentz = [ L.VVLVLVR1, L.VVLVLVR3, L.VVLVLVR4 ],
	couplings = {(1,1):C.GC_12,(0,0):C.GC_12,(2,2):C.GC_12})
V_79 = Vertex(name = 'V_79',
	particles = [ P.g, P.gL, P.gR, P.gR],
	color = [ 'f(-1,1,2)*f(3,4,-1)', 'f(-1,1,3)*f(2,4,-1)', 'f(-1,1,4)*f(2,3,-1)' ],
	lorentz = [ L.VVLVRVR1, L.VVLVRVR3, L.VVLVRVR4 ],
	couplings = {(1,1):C.GC_12,(0,0):C.GC_12,(2,2):C.GC_12})
V_80 = Vertex(name = 'V_80',
	particles = [ P.g, P.gR, P.gR, P.gR],
	color = [ 'f(-1,1,2)*f(3,4,-1)', 'f(-1,1,3)*f(2,4,-1)', 'f(-1,1,4)*f(2,3,-1)' ],
	lorentz = [ L.VVRVRVR1, L.VVRVRVR3, L.VVRVRVR4 ],
	couplings = {(1,1):C.GC_12,(0,0):C.GC_12,(2,2):C.GC_12})
V_81 = Vertex(name = 'V_81',
	particles = [ P.gL, P.gL, P.gL, P.gR],
	color = [ 'f(-1,1,2)*f(3,4,-1)', 'f(-1,1,3)*f(2,4,-1)', 'f(-1,1,4)*f(2,3,-1)' ],
	lorentz = [ L.VLVLVLVR1, L.VLVLVLVR3, L.VLVLVLVR4 ],
	couplings = {(1,1):C.GC_12,(0,0):C.GC_12,(2,2):C.GC_12})
V_82 = Vertex(name = 'V_82',
	particles = [ P.gL, P.gL, P.gR, P.gR],
	color = [ 'f(-1,1,2)*f(3,4,-1)', 'f(-1,1,3)*f(2,4,-1)', 'f(-1,1,4)*f(2,3,-1)' ],
	lorentz = [ L.VLVLVRVR1, L.VLVLVRVR3, L.VLVLVRVR4 ],
	couplings = {(1,1):C.GC_12,(0,0):C.GC_12,(2,2):C.GC_12})
""" V_82 = Vertex(name = 'V_82',
	particles = [ P.gL, P.gL, P.gR, P.gR],
	color = [ 'f(-1,1,3)*f(2,4,-1)+f(-1,1,4)*f(2,3,-1)' ],
	lorentz = [ L.VVVV1 ],
	couplings = {(1,1):C.GC_12,(0,0):C.GC_12,(2,2):C.GC_12}) """
V_83 = Vertex(name = 'V_83',
	particles = [ P.gL, P.gR, P.gR, P.gR],
	color = [ 'f(-1,1,2)*f(3,4,-1)', 'f(-1,1,3)*f(2,4,-1)', 'f(-1,1,4)*f(2,3,-1)' ],
	lorentz = [ L.VLVRVRVR1, L.VLVRVRVR3, L.VLVRVRVR4 ],
	couplings = {(1,1):C.GC_12,(0,0):C.GC_12,(2,2):C.GC_12})

######################## Manually added vertices #########################
######################## TODO: ADD CORRECT LORENTZ STRUCTURES #########################

V_84 = Vertex(name = 'V_84',
	particles = [ P.gLI, P.gL, P.gL, P.gR],
	color = [ 'f(-1,1,2)*f(3,4,-1)', 'f(-1,1,3)*f(2,4,-1)', 'f(-1,1,4)*f(2,3,-1)' ],
	lorentz = [ L.VIVLVLVR1, L.VIVLVLVR3, L.VIVLVLVR4 ],
	couplings = {(1,1):C.GC_12,(0,0):C.GC_12,(2,2):C.GC_12})

V_85 = Vertex(name = 'V_85',
	particles = [ P.gLI, P.gL, P.gR, P.gR],
	color = [ 'f(-1,1,2)*f(3,4,-1)', 'f(-1,1,3)*f(2,4,-1)', 'f(-1,1,4)*f(2,3,-1)' ],
	lorentz = [ L.VIVLVRVR1, L.VIVLVRVR3, L.VIVLVRVR4 ],
	couplings = {(1,1):C.GC_12,(0,0):C.GC_12,(2,2):C.GC_12})

# Check if V_86 and V_87 are used or outdated
V_86 = Vertex(name = 'V_86',
	particles = [ P.g, P.gLI, P.gRI, P.gL],
	color = [ 'f(-1,1,2)*f(3,4,-1)', 'f(-1,1,3)*f(2,4,-1)', 'f(-1,1,4)*f(2,3,-1)' ],
	lorentz = [ L.VVVV1, L.VVVV3, L.VVVV4 ],
	couplings = {(1,1):C.GC_12,(0,0):C.GC_12,(2,2):C.GC_12})

V_87 = Vertex(name = 'V_87',
	particles = [ P.g, P.gLI, P.gRI, P.gR],
	color = [ 'f(-1,1,2)*f(3,4,-1)', 'f(-1,1,3)*f(2,4,-1)', 'f(-1,1,4)*f(2,3,-1)' ],
	lorentz = [ L.VVVV1, L.VVVV3, L.VVVV4 ],
	couplings = {(1,1):C.GC_12,(0,0):C.GC_12,(2,2):C.GC_12})

V_88 = Vertex(name = 'V_88',
	particles = [ P.gRI, P.gL, P.gL, P.gR],
	color = [ 'f(-1,1,2)*f(3,4,-1)', 'f(-1,1,3)*f(2,4,-1)', 'f(-1,1,4)*f(2,3,-1)' ],
	lorentz = [ L.VIVLVLVR1, L.VIVLVLVR3, L.VIVLVLVR4 ],
	couplings = {(1,1):C.GC_12,(0,0):C.GC_12,(2,2):C.GC_12})

V_89 = Vertex(name = 'V_89',
	particles = [ P.gRI, P.gL, P.gR, P.gR],
	color = [ 'f(-1,1,2)*f(3,4,-1)', 'f(-1,1,3)*f(2,4,-1)', 'f(-1,1,4)*f(2,3,-1)' ],
	lorentz = [ L.VIVLVRVR1, L.VIVLVRVR3, L.VIVLVRVR4 ],
	couplings = {(1,1):C.GC_12,(0,0):C.GC_12,(2,2):C.GC_12})

###### BUG FIXES CHANGE LORENTZ STRUCTURE LATER

V_90 = Vertex(name = 'V_90',
	particles = [ P.g, P.gRI, P.gR, P.gR],
	color = [ 'f(-1,1,2)*f(3,4,-1)', 'f(-1,1,3)*f(2,4,-1)', 'f(-1,1,4)*f(2,3,-1)' ],
	lorentz = [ L.VVIVLVL1, L.VVIVLVL3, L.VVIVLVL4 ],
	couplings = {(1,1):C.GC_12,(0,0):C.GC_12,(2,2):C.GC_12})

V_91 = Vertex(name = 'V_91',
	particles = [ P.g, P.gRI, P.gL, P.gL],
	color = [ 'f(-1,1,2)*f(3,4,-1)', 'f(-1,1,3)*f(2,4,-1)', 'f(-1,1,4)*f(2,3,-1)' ],
	lorentz = [ L.VVIVLVL1, L.VVIVLVL3, L.VVIVLVL4 ],
	couplings = {(1,1):C.GC_12,(0,0):C.GC_12,(2,2):C.GC_12})

V_92 = Vertex(name = 'V_92',
	particles = [ P.g, P.gLI, P.gR, P.gR],
	color = [ 'f(-1,1,2)*f(3,4,-1)', 'f(-1,1,3)*f(2,4,-1)', 'f(-1,1,4)*f(2,3,-1)' ],
	lorentz = [ L.VVIVLVL1, L.VVIVLVL3, L.VVIVLVL4 ],
	couplings = {(1,1):C.GC_12,(0,0):C.GC_12,(2,2):C.GC_12})

V_93 = Vertex(name = 'V_93',
	particles = [ P.g, P.gLI, P.gL, P.gL],
	color = [ 'f(-1,1,2)*f(3,4,-1)', 'f(-1,1,3)*f(2,4,-1)', 'f(-1,1,4)*f(2,3,-1)' ],
	lorentz = [ L.VVIVLVL1, L.VVIVLVL3, L.VVIVLVL4 ],
	couplings = {(1,1):C.GC_12,(0,0):C.GC_12,(2,2):C.GC_12})

V_94 = Vertex(name = 'V_94',
	particles = [ P.g, P.gLI, P.gLI, P.gRI],
	color = [ 'f(-1,1,2)*f(3,4,-1)', 'f(-1,1,3)*f(2,4,-1)', 'f(-1,1,4)*f(2,3,-1)' ],
	lorentz = [ L.VLVRVRVR1, L.VLVRVRVR3, L.VLVRVRVR4 ],
	couplings = {(1,1):C.GC_12,(0,0):C.GC_12,(2,2):C.GC_12})

# Special gluons with fermions
V_95 = Vertex(name = 'V_95',
               particles = [ P.uL__tilde__, P.uR, P.gLI ],
               color = [ 'T(3,2,1)' ],
               lorentz = [ L.LRV1 ],
               couplings = {(0,0):C.GC_11})

V_96 = Vertex(name = 'V_96',
               particles = [ P.uL__tilde__, P.uR, P.gRI ],
               color = [ 'T(3,2,1)' ],
               lorentz = [ L.LRV1 ],
               couplings = {(0,0):C.GC_11})               

V_97 = Vertex(name = 'V_97',
               particles = [ P.uR__tilde__, P.uL, P.gLI ],
               color = [ 'T(3,2,1)' ],
               lorentz = [ L.RLV1 ],
               couplings = {(0,0):C.GC_11})

V_98 = Vertex(name = 'V_98',
               particles = [ P.uR__tilde__, P.uL, P.gRI ],
               color = [ 'T(3,2,1)' ],
               lorentz = [ L.RLV1 ],
               couplings = {(0,0):C.GC_11})

############################################################

# Massive QCD vertices

V_99 = Vertex(name = 'V_99', 
			 particles = [ P.tM__tilde__, P.tM, P.g ],
			 color = [ 'T(3,2,1)' ], 
			 lorentz = [ L.FFV1 ], 
			 couplings = {(0,0):C.GC_11})
V_100 = Vertex(name = 'V_100', 
			 particles = [ P.tM__tilde__, P.tM, P.gLI ],
			 color = [ 'T(3,2,1)' ], 
			 lorentz = [ L.FFV1 ], 
			 couplings = {(0,0):C.GC_11})
V_101 = Vertex(name = 'V_101', 
			 particles = [ P.tM__tilde__, P.tM, P.gRI ],
			 color = [ 'T(3,2,1)' ], 
			 lorentz = [ L.FFV1 ], 
			 couplings = {(0,0):C.GC_11})
V_102 = Vertex(name = 'V_102', 
			 particles = [ P.tM__tilde__, P.tM, P.gL ],
			 color = [ 'T(3,2,1)' ], 
			 lorentz = [ L.FFV1 ], 
			 couplings = {(0,0):C.GC_11})
V_103 = Vertex(name = 'V_103', 
			 particles = [ P.tM__tilde__, P.tM, P.gR ],
			 color = [ 'T(3,2,1)' ], 
			 lorentz = [ L.FFV1 ], 
			 couplings = {(0,0):C.GC_11})
V_104 = Vertex(name = 'V_104', 
			 particles = [ P.tM__tilde__, P.tP, P.g ],
			 color = [ 'T(3,2,1)' ], 
			 lorentz = [ L.FFV1 ], 
			 couplings = {(0,0):C.GC_11})
V_105 = Vertex(name = 'V_105', 
			 particles = [ P.tM__tilde__, P.tP, P.gLI ],
			 color = [ 'T(3,2,1)' ], 
			 lorentz = [ L.FFV1 ], 
			 couplings = {(0,0):C.GC_11})
V_106 = Vertex(name = 'V_106', 
			 particles = [ P.tM__tilde__, P.tP, P.gRI ],
			 color = [ 'T(3,2,1)' ], 
			 lorentz = [ L.FFV1 ], 
			 couplings = {(0,0):C.GC_11})
V_107 = Vertex(name = 'V_107', 
			 particles = [ P.tM__tilde__, P.tP, P.gL ],
			 color = [ 'T(3,2,1)' ], 
			 lorentz = [ L.FFV1 ], 
			 couplings = {(0,0):C.GC_11})
V_108 = Vertex(name = 'V_108', 
			 particles = [ P.tM__tilde__, P.tP, P.gR ],
			 color = [ 'T(3,2,1)' ], 
			 lorentz = [ L.FFV1 ], 
			 couplings = {(0,0):C.GC_11})
V_109 = Vertex(name = 'V_109', 
			 particles = [ P.tP__tilde__, P.tM, P.g ],
			 color = [ 'T(3,2,1)' ], 
			 lorentz = [ L.FFV1 ], 
			 couplings = {(0,0):C.GC_11})
V_110 = Vertex(name = 'V_110', 
			 particles = [ P.tP__tilde__, P.tM, P.gLI ],
			 color = [ 'T(3,2,1)' ], 
			 lorentz = [ L.FFV1 ], 
			 couplings = {(0,0):C.GC_11})
V_111 = Vertex(name = 'V_111', 
			 particles = [ P.tP__tilde__, P.tM, P.gRI ],
			 color = [ 'T(3,2,1)' ], 
			 lorentz = [ L.FFV1 ], 
			 couplings = {(0,0):C.GC_11})
V_112 = Vertex(name = 'V_112', 
			 particles = [ P.tP__tilde__, P.tM, P.gL ],
			 color = [ 'T(3,2,1)' ], 
			 lorentz = [ L.FFV1 ], 
			 couplings = {(0,0):C.GC_11})
V_113 = Vertex(name = 'V_113', 
			 particles = [ P.tP__tilde__, P.tM, P.gR ],
			 color = [ 'T(3,2,1)' ], 
			 lorentz = [ L.FFV1 ], 
			 couplings = {(0,0):C.GC_11})
V_114 = Vertex(name = 'V_114', 
			 particles = [ P.tP__tilde__, P.tP, P.g ],
			 color = [ 'T(3,2,1)' ], 
			 lorentz = [ L.FFV1 ], 
			 couplings = {(0,0):C.GC_11})
V_115 = Vertex(name = 'V_115', 
			 particles = [ P.tP__tilde__, P.tP, P.gLI ],
			 color = [ 'T(3,2,1)' ], 
			 lorentz = [ L.FFV1 ], 
			 couplings = {(0,0):C.GC_11})
V_116 = Vertex(name = 'V_116', 
			 particles = [ P.tP__tilde__, P.tP, P.gRI ],
			 color = [ 'T(3,2,1)' ], 
			 lorentz = [ L.FFV1 ], 
			 couplings = {(0,0):C.GC_11})
V_117 = Vertex(name = 'V_117', 
			 particles = [ P.tP__tilde__, P.tP, P.gL ],
			 color = [ 'T(3,2,1)' ], 
			 lorentz = [ L.FFV1 ], 
			 couplings = {(0,0):C.GC_11})
V_118 = Vertex(name = 'V_118', 
			 particles = [ P.tP__tilde__, P.tP, P.gR ],
			 color = [ 'T(3,2,1)' ], 
			 lorentz = [ L.FFV1 ], 
			 couplings = {(0,0):C.GC_11})
