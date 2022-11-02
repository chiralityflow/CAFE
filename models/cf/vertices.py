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

V_37 = Vertex(name = 'V_37',
              particles = [ P.g, P.g, P.g ],
              color = [ 'f(1,2,3)' ],
              lorentz = [ L.VVV1 ],
              couplings = {(0,0):C.GC_10})

V_38 = Vertex(name = 'V_38',
              particles = [ P.g, P.g, P.gL ],
              color = [ 'f(1,2,3)' ],
              lorentz = [ L.VVV1 ],
              couplings = {(0,0):C.GC_10})

V_39 = Vertex(name = 'V_39',
              particles = [ P.g, P.g, P.gR ],
              color = [ 'f(1,2,3)' ],
              lorentz = [ L.VVV1 ],
              couplings = {(0,0):C.GC_10})

V_40 = Vertex(name = 'V_40',
              particles = [ P.g, P.gR, P.gR ],
              color = [ 'f(1,2,3)' ],
              lorentz = [ L.VVV1 ],
              couplings = {(0,0):C.GC_10})

V_41 = Vertex(name = 'V_41',
              particles = [ P.g, P.gL, P.gL ],
              color = [ 'f(1,2,3)' ],
              lorentz = [ L.VVV1 ],
              couplings = {(0,0):C.GC_10})

V_42 = Vertex(name = 'V_42',
              particles = [ P.g, P.gL, P.gR ],
              color = [ 'f(1,2,3)' ],
              lorentz = [ L.VVV1 ],
              couplings = {(0,0):C.GC_10})

# AW: Quadruple gluon vertex. Ask ML or AL which chrialities are allowed. Adding all possible now to make sure

V_43 = Vertex(name = 'V_43',
              particles = [ P.g, P.g, P.g, P.g ],
              color = [ 'f(-1,1,2)*f(3,4,-1)', 'f(-1,1,3)*f(2,4,-1)', 'f(-1,1,4)*f(2,3,-1)' ],
              lorentz = [ L.VVVV1, L.VVVV3, L.VVVV4 ],
              couplings = {(1,1):C.GC_12,(0,0):C.GC_12,(2,2):C.GC_12})

V_44 = Vertex(name = 'V_44',
              particles = [ P.g, P.g, P.g, P.gL ],
              color = [ 'f(-1,1,2)*f(3,4,-1)', 'f(-1,1,3)*f(2,4,-1)', 'f(-1,1,4)*f(2,3,-1)' ],
              lorentz = [ L.VVVV1, L.VVVV3, L.VVVV4 ],
              couplings = {(1,1):C.GC_12,(0,0):C.GC_12,(2,2):C.GC_12})
            
V_45 = Vertex(name = 'V_45',
              particles = [ P.g, P.g, P.g, P.gR ],
              color = [ 'f(-1,1,2)*f(3,4,-1)', 'f(-1,1,3)*f(2,4,-1)', 'f(-1,1,4)*f(2,3,-1)' ],
              lorentz = [ L.VVVV1, L.VVVV3, L.VVVV4 ],
              couplings = {(1,1):C.GC_12,(0,0):C.GC_12,(2,2):C.GC_12})
            
V_46 = Vertex(name = 'V_46',
              particles = [ P.g, P.g, P.gL, P.gR ],
              color = [ 'f(-1,1,2)*f(3,4,-1)', 'f(-1,1,3)*f(2,4,-1)', 'f(-1,1,4)*f(2,3,-1)' ],
              lorentz = [ L.VVVV1, L.VVVV3, L.VVVV4 ],
              couplings = {(1,1):C.GC_12,(0,0):C.GC_12,(2,2):C.GC_12})

V_47 = Vertex(name = 'V_47',
              particles = [ P.g, P.g, P.gL, P.gL ],
              color = [ 'f(-1,1,2)*f(3,4,-1)', 'f(-1,1,3)*f(2,4,-1)', 'f(-1,1,4)*f(2,3,-1)' ],
              lorentz = [ L.VVVV1, L.VVVV3, L.VVVV4 ],
              couplings = {(1,1):C.GC_12,(0,0):C.GC_12,(2,2):C.GC_12})
            
V_48 = Vertex(name = 'V_48',
              particles = [ P.g, P.g, P.gR, P.gR ],
              color = [ 'f(-1,1,2)*f(3,4,-1)', 'f(-1,1,3)*f(2,4,-1)', 'f(-1,1,4)*f(2,3,-1)' ],
              lorentz = [ L.VVVV1, L.VVVV3, L.VVVV4 ],
              couplings = {(1,1):C.GC_12,(0,0):C.GC_12,(2,2):C.GC_12})

V_49 = Vertex(name = 'V_49',
              particles = [ P.g, P.gL, P.gL, P.gL ],
              color = [ 'f(-1,1,2)*f(3,4,-1)', 'f(-1,1,3)*f(2,4,-1)', 'f(-1,1,4)*f(2,3,-1)' ],
              lorentz = [ L.VVVV1, L.VVVV3, L.VVVV4 ],
              couplings = {(1,1):C.GC_12,(0,0):C.GC_12,(2,2):C.GC_12})

V_50 = Vertex(name = 'V_50',
              particles = [ P.g, P.gL, P.gL, P.gR ],
              color = [ 'f(-1,1,2)*f(3,4,-1)', 'f(-1,1,3)*f(2,4,-1)', 'f(-1,1,4)*f(2,3,-1)' ],
              lorentz = [ L.VVVV1, L.VVVV3, L.VVVV4 ],
              couplings = {(1,1):C.GC_12,(0,0):C.GC_12,(2,2):C.GC_12})
            
V_51 = Vertex(name = 'V_51',
              particles = [ P.g, P.gL, P.gR, P.gR ],
              color = [ 'f(-1,1,2)*f(3,4,-1)', 'f(-1,1,3)*f(2,4,-1)', 'f(-1,1,4)*f(2,3,-1)' ],
              lorentz = [ L.VVVV1, L.VVVV3, L.VVVV4 ],
              couplings = {(1,1):C.GC_12,(0,0):C.GC_12,(2,2):C.GC_12})

V_52 = Vertex(name = 'V_52',
              particles = [ P.g, P.gR, P.gR, P.gR ],
              color = [ 'f(-1,1,2)*f(3,4,-1)', 'f(-1,1,3)*f(2,4,-1)', 'f(-1,1,4)*f(2,3,-1)' ],
              lorentz = [ L.VVVV1, L.VVVV3, L.VVVV4 ],
              couplings = {(1,1):C.GC_12,(0,0):C.GC_12,(2,2):C.GC_12})

V_53 = Vertex(name = 'V_53',
              particles = [ P.gL, P.gL, P.gL, P.gL ],
              color = [ 'f(-1,1,2)*f(3,4,-1)', 'f(-1,1,3)*f(2,4,-1)', 'f(-1,1,4)*f(2,3,-1)' ],
              lorentz = [ L.VVVV1, L.VVVV3, L.VVVV4 ],
              couplings = {(1,1):C.GC_12,(0,0):C.GC_12,(2,2):C.GC_12})
            
V_54 = Vertex(name = 'V_54',
              particles = [ P.gL, P.gL, P.gL, P.gR ],
              color = [ 'f(-1,1,2)*f(3,4,-1)', 'f(-1,1,3)*f(2,4,-1)', 'f(-1,1,4)*f(2,3,-1)' ],
              lorentz = [ L.VVVV1, L.VVVV3, L.VVVV4 ],
              couplings = {(1,1):C.GC_12,(0,0):C.GC_12,(2,2):C.GC_12})

V_55 = Vertex(name = 'V_55',
              particles = [ P.gL, P.gL, P.gR, P.gR ],
              color = [ 'f(-1,1,2)*f(3,4,-1)', 'f(-1,1,3)*f(2,4,-1)', 'f(-1,1,4)*f(2,3,-1)' ],
              lorentz = [ L.VVVV1, L.VVVV3, L.VVVV4 ],
              couplings = {(1,1):C.GC_12,(0,0):C.GC_12,(2,2):C.GC_12})
            
V_56 = Vertex(name = 'V_56',
              particles = [ P.gL, P.gR, P.gR, P.gR ],
              color = [ 'f(-1,1,2)*f(3,4,-1)', 'f(-1,1,3)*f(2,4,-1)', 'f(-1,1,4)*f(2,3,-1)' ],
              lorentz = [ L.VVVV1, L.VVVV3, L.VVVV4 ],
              couplings = {(1,1):C.GC_12,(0,0):C.GC_12,(2,2):C.GC_12})

V_57 = Vertex(name = 'V_57',
              particles = [ P.gR, P.gR, P.gR, P.gR ],
              color = [ 'f(-1,1,2)*f(3,4,-1)', 'f(-1,1,3)*f(2,4,-1)', 'f(-1,1,4)*f(2,3,-1)' ],
              lorentz = [ L.VVVV1, L.VVVV3, L.VVVV4 ],
              couplings = {(1,1):C.GC_12,(0,0):C.GC_12,(2,2):C.GC_12})