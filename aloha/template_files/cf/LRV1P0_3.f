      SUBROUTINE LRV1P0_3(F1,LEF1,PF1,MOF1,F2,LEF2
     $ ,PF2,MOF2,NEXTERNAL,MSQR,MANG,COUP,M3,W3,V3L
     $ ,LEV3L,PV3,MO3L,MO3R,V3R,LEV3R,EXTV3)
C     This subroutine computes the four-momentum, inner product vectors,
C     and inner product vector lengths of an internal vector boson
C     comming from a LRV1P0_3 vertex, within the chirality-flow formalism.

      IMPLICIT NONE
      COMPLEX*16 CI
      PARAMETER (CI=(0D0,1D0))
      DOUBLE PRECISION RTWO
      PARAMETER (RTWO=2.0D0)
      INTEGER NEXTERNAL,I,J
C     EB: Length of F1, F2, V3L, and V3R
      INTEGER LEF1,LEF2,LEV3L,LEV3R
C     EB: Left resp. right external mothers of F1 resp. F2.
      INTEGER MOF1(*),MOF2(*)
C     EB: Left and right external mothers of V3.
      INTEGER MO3L(*),MO3R(*)
C     EB: Term needed to be able to treat both internal and external 
C         vector bosons with this subroutine. -1 for external vector 
C         bosons and 0 for internal vector bosons.
      INTEGER EXTV3
C     EB: Vectors carrying innerproducts from previous vertices
C         for the fermions and the boson.
C     EB: V3L has the left-handed part and V3R the right-handed.
C     EB: Coupling constant for the vertex.
      COMPLEX*16 COUP
C     EB: Vectors carrying innerproducts from previous vertices
C         for the fermions and the boson.
C     EB: V3L has the left-handed part and V3R the right-handed.
      COMPLEX*16 F1(*),F2(*),V3L(*),V3R(*)
C     EB: Complex, 2-component version of 
C         momentum of F1, F2, and V3.
C     EB: PV3(3) used to keep the DENOM factor.
      COMPLEX*16 PF1(*),PF2(*),PV3(*)
C     EB: Real version of V3 momentum.
      REAL*8 P3(0:3)
C     EB: Matrices containing all innerproducts for the process.
C         MSQR contains the square innerproducts.
C         MANG contains the angle innerproducts.
      COMPLEX*16, DIMENSION(NEXTERNAL,NEXTERNAL) :: MSQR
      COMPLEX*16, DIMENSION(NEXTERNAL,NEXTERNAL) :: MANG
      REAL*8 M3
      REAL*8 W3
      COMPLEX*16 DENOM
      
C     EB: Calculate the four-momentum of V3.        
      PV3(1) = +PF1(1)+PF2(1)
      PV3(2) = +PF1(2)+PF2(2)
      P3(0) = -DBLE(PV3(1))
      P3(1) = -DBLE(PV3(2))
      P3(2) = -DIMAG(PV3(2))
      P3(3) = -DIMAG(PV3(1))

C     EB: Calculate prefactor of the vertex (coupling*vector boson propagator)
      DENOM = (SQRT(RTWO) * COUP)/(P3(0)**2-P3(1)**2-P3(2)**2-P3(3)**2 - M3 * (M3 -CI
     $ * W3))
     
      PV3(3) = -DENOM
      EXTV3 = 0
      LEV3L = LEF1
      LEV3R = LEF2
      
      DO I = 1, LEF1
        V3L(I) = F1(I)
      ENDDO
     
      DO J= 1, LEF2
        V3R(J) = F2(J)
      ENDDO
      END
