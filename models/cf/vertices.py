# This file was automatically created by FeynRules 1.7.69
# Mathematica version: 8.0 for Mac OS X x86 (64-bit) (November 6, 2010)
# Date: Mon 1 Oct 2012 14:58:25

from object_library import all_vertices, Vertex
import particles as P
import couplings as C
import lorentz as L


V_1 = Vertex(name = 'V_1',
              particles = [ P.eR__plus__, P.eL__minus__, P.a ],
              color = [ '1' ],
              lorentz = [ L.FFV2 ],
              couplings = {(0,0):C.GC_3})

V_2 = Vertex(name = 'V_2',
              particles = [ P.eL__plus__, P.eR__minus__, P.a ],
              color = [ '1' ],
              lorentz = [ L.FFV6 ],
              couplings = {(0,0):C.GC_3})

V_3 = Vertex(name = 'V_3',
              particles = [ P.muR__plus__, P.muL__minus__, P.a ],
              color = [ '1' ],
              lorentz = [ L.FFV2 ],
              couplings = {(0,0):C.GC_3})

V_4 = Vertex(name = 'V_4',
              particles = [ P.muL__plus__, P.muR__minus__, P.a ],
              color = [ '1' ],
              lorentz = [ L.FFV6 ],
              couplings = {(0,0):C.GC_3})

V_5 = Vertex(name = 'V_5',
              particles = [P.eLf__minus__, P.eRf__plus__, P.a0v0 ],
              color = [ '1' ],
              lorentz = [ L.SSS2 ],
              couplings = {(0,0):C.GC_3})

V_6 = Vertex(name = 'V_6',
              particles = [ P.eLf__plus__, P.eRf__minus__, P.a0v0],
              color = [ '1' ],
              lorentz = [ L.SSS3 ],
              couplings = {(0,0):C.GC_3})

V_7 = Vertex(name = 'V_7',
              particles = [ P.muRf__plus__, P.muLf__minus__, P.a0v0 ],
              color = [ '1' ],
              lorentz = [ L.SSS2 ],
              couplings = {(0,0):C.GC_3})

V_8 = Vertex(name = 'V_8',
              particles = [ P.muLf__plus__, P.muRf__minus__, P.a0v0 ],
              color = [ '1' ],
              lorentz = [ L.SSS3 ],
              couplings = {(0,0):C.GC_3})



