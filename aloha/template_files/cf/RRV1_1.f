      SUBROUTINE RRV1_1(F2,LEF2,REF2,PF2,MOF2,V3L,LEV3L,PV3,MO3L,MO3R,
     & V3R,LEV3R,EXTV3,NEXTERNAL,MSQR,MANG,COUP,M1,W1,MOF1,F1,PF1,LEF1)
C     This subroutine computes the four-momentum, inner product vector,
C     and inner product vector length of a right-handed internal fermion
C     comming from a RRV1_1 vertex, within the chirality-flow formalism.

      IMPLICIT NONE
      COMPLEX*16 CI
      PARAMETER (CI=(0D0,1D0))
      DOUBLE PRECISION RTWO
      PARAMETER (RTWO=2.0D0)
      INTEGER NEXTERNAL,I,J,K,L
C     EB: Length of F1, F2, V3L, and V3R
      INTEGER LEF1,LEF2,LEV3L,LEV3R
C     EB: Right external mothers of F1 and F2.
      INTEGER MOF1(*),MOF2(*)
C     EB: Left and right external mothers of V3.
      INTEGER MO3L(*),MO3R(*)
C     EB: Term needed to be able to treat both internal and external 
C         vector bosons with this subroutine. -1 for external vector 
C         bosons and 0 for internal vector bosons.
      INTEGER EXTV3
C     EB: Term needed to be able to treat reduced and non-reduced
C         fermions with this subroutine. 0 for non-reduced and +1
C         for reduced.
      INTEGER REF2
C     EB: Coupling constant for the vertex.
      COMPLEX*16 COUP
C     EB: Vectors carrying innerproducts from previous vertices
C         for the fermions and the boson.
C     EB: V3L has the left-handed part and V3R the right-handed.
      COMPLEX*16 F1(*),F2(*),V3L(*),V3R(*)
C     EB: Complex, 2-component version of 
C         momentum of F1, F2, and V3.
C     EB: PV3(3) keeps the DENOM from previous vertex for internal 
C          V3 and the polarization factor for external V3.
      COMPLEX*16 PF1(*),PF2(*),PV3(*)
C     EB: Real version of F2 momentum.
      REAL*8 P1(0:3)
C     EB: Matrices containing all innerproducts for the process.
C         MSQR contains the square innerproducts.
C         MANG contains the angle innerproducts.
      COMPLEX*16, DIMENSION(NEXTERNAL,NEXTERNAL) :: MSQR
      COMPLEX*16, DIMENSION(NEXTERNAL,NEXTERNAL) :: MANG
      REAL*8 M1
      REAL*8 W1
      COMPLEX*16 DENOM
      COMPLEX*16 SUMF2
      
C     EB: Calculate the four-momentum of F1.      
      PF1(1) = +PF2(1)+PV3(1)
      PF1(2) = +PF2(2)+PV3(2)
      P1(0) = -DBLE(PF1(1))
      P1(1) = -DBLE(PF1(2))
      P1(2) = -DIMAG(PF1(2))
      P1(3) = -DIMAG(PF1(1))
      
C     EB: Calculate prefactor of the vertex (coupling*fermion propagator)
      DENOM = (COUP*CI*DSQRT(RTWO))/(P1(0)**2-P1(1)**2-P1(2)**2-P1(3)**2)
      SUMF2 = 0

C     EB: Determine the lenght of F1. EXTV3 = -1 for external V3 and 
C          EXTV3 = 0 for internal V3, since only the physical parts of
C          the vector bosons contributes to the length.      
      LEF1=LEF2+REF2+LEV3L+LEV3R+EXTV3

C     EB: Contract F2 with the right-handed part of V3.      
      DO I = 1, LEF2
        DO J = 1, LEV3R
          SUMF2 = SUMF2 + F2(I)*V3R(J)*MANG(ABS(MOF2(I)),ABS(MO3R(J)))
        ENDDO
      ENDDO

C     EB: Determine vector of invariants F1. 
C     (MOF1(K)/ABS(MOF1(K))) gives sign based on initial or final
C       external mothers.
C     V3L(L)*MSQR(ABS(MO3L(L)),ABS(MOF1(K))) gives the contraction 
C     between F1 and the left-handed part of V3. 
      DO K = 1, LEF1
        F1(K) = 0
        DO L = 1, LEV3L
          F1(K) = F1(K) - (MOF1(K)/ABS(MOF1(K)))*DENOM*
     & PV3(3)*SUMF2*V3L(L)*MSQR(ABS(MO3L(L)),ABS(MOF1(K)))
        ENDDO
      ENDDO
      END 

      SUBROUTINE RRV1L_1(F2,LEF2,REF2,PF2,MOF2,V3L,LEV3L,PV3,MO3L,MO3R,
     & V3R,LEV3R,NEXTERNAL,MSQR,MANG,COUP,M1,W1,MOF1,F1,PF1,LEF1,REF1)
C     This subroutine computes the four-momentum, inner product vector,
C     and inner product vector length of a right-handed internal fermion
C     comming from a RRV1_1 vertex where the boson is external and left-
C     handed, within the chirality-flow formalism. The boson having the
C     oposite handedness means that it will not contribute to the number
C     of elements for the output fermion.

      IMPLICIT NONE
      COMPLEX*16 CI
      PARAMETER (CI=(0D0,1D0))
      DOUBLE PRECISION RTWO
      PARAMETER (RTWO=2.0D0)
      INTEGER NEXTERNAL,I,J,K,L
C     EB: Length of F1, F2, V3L, and V3R
      INTEGER LEF1,LEF2,LEV3L,LEV3R
C     EB: Right external mothers of F1 and F2.
      INTEGER MOF1(*),MOF2(*)
C     EB: Left and right external mothers of V3.
      INTEGER MO3L(*),MO3R(*)
C     EB: Term needed to be able to treat both internal and external 
C         vector bosons with this subroutine. -1 for external vector 
C         bosons and 0 for internal vector bosons.
      INTEGER EXTV3
C     EB: Term needed to be able to treat reduced and non-reduced
C         fermions with this subroutine. 0 for non-reduced and +1
C         for reduced.
      INTEGER REF1,REF2
C     EB: Coupling constant for the vertex.
      COMPLEX*16 COUP
C     EB: Vectors carrying innerproducts from previous vertices
C         for the fermions and the boson.
C     EB: V3L has the left-handed part and V3R the right-handed.
      COMPLEX*16 F1(*),F2(*),V3L(*),V3R(*)
C     EB: Complex, 2-component version of 
C         momentum of F1, F2, and V3.
C     EB: PV3(3) keeps the DENOM from previous vertex for internal 
C          V3 and the polarization factor for external V3.
      COMPLEX*16 PF1(*),PF2(*),PV3(*)
C     EB: Real version of F2 momentum.
      REAL*8 P1(0:3)
C     EB: Matrices containing all innerproducts for the process.
C         MSQR contains the square innerproducts.
C         MANG contains the angle innerproducts.
      COMPLEX*16, DIMENSION(NEXTERNAL,NEXTERNAL) :: MSQR
      COMPLEX*16, DIMENSION(NEXTERNAL,NEXTERNAL) :: MANG
      REAL*8 M1
      REAL*8 W1
      COMPLEX*16 DENOM
      COMPLEX*16 SUMF2
      
C     EB: Calculate the four-momentum of F1.      
      PF1(1) = +PF2(1)+PV3(1)
      PF1(2) = +PF2(2)+PV3(2)
      P1(0) = -DBLE(PF1(1))
      P1(1) = -DBLE(PF1(2))
      P1(2) = -DIMAG(PF1(2))
      P1(3) = -DIMAG(PF1(1))
      
C     EB: Calculate prefactor of the vertex (coupling*fermion propagator)
      DENOM = (COUP*CI*DSQRT(RTWO))/(P1(0)**2-P1(1)**2-P1(2)**2-P1(3)**2)
      SUMF2 = 0

C     EB: Determine the lenght of F1. EXTV3 = -1 for external V3 and 
C          EXTV3 = 0 for internal V3, since only the physical parts of
C          the vector bosons contributes to the length.      
      LEF1=LEF2+REF2
      REF1=1
C     EB: Contract F2 with the right-handed part of V3.      
      DO I = 1, LEF2
        DO J = 1, LEV3R
          SUMF2 = SUMF2 + F2(I)*V3R(J)*MANG(ABS(MOF2(I)),ABS(MO3R(J)))
        ENDDO
      ENDDO

C     EB: Determine vector of invariants F1. 
C     (MOF1(K)/ABS(MOF1(K))) gives sign based on initial or final
C       external mothers.
C     V3L(L)*MSQR(ABS(MO3L(L)),ABS(MOF1(K))) gives the contraction 
C     between F1 and the left-handed part of V3. 
      DO K = 1, LEF1
        F1(K) = 0
        DO L = 1, LEV3L
          F1(K) = F1(K) - (MOF1(K)/ABS(MOF1(K)))*DENOM*
     & PV3(3)*SUMF2*V3L(L)*MSQR(ABS(MO3L(L)),ABS(MOF1(K)))
        ENDDO
      ENDDO
      END     
