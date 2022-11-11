      SUBROUTINE LRV1_0(F1,LEF1,PF1,MOF1,F2,LEF2,PF2,MOF2,V3L,
     & LEV3L,PV3,MO3L,MO3R,V3R,LEV3R,NEXTERNAL,
     & MSQR,MANG,COUP,VERTEX)
C     This subroutine computes the amplitude of a diagram within the
C     chirality-flow formalism.     
      
      IMPLICIT NONE
      COMPLEX*16 CI
      PARAMETER (CI=(0D0,1D0))
      DOUBLE PRECISION RTWO
      PARAMETER (RTWO=2.0D0)
      INTEGER NEXTERNAL,I,J,K,L
C     EB: Length of F1, F2, V3L, and V3R
      INTEGER LEF1,LEF2,LEV3L,LEV3R
C     EB: Left resp. right external mothers of F1 resp. F2.
      INTEGER MOF1(*),MOF2(*)
C     EB: Left and right external mothers of V3.
      INTEGER MO3L(*),MO3R(*)
C     EB: Coupling constant for the vertex.
      COMPLEX*16 COUP
C     EB: Vectors carrying innerproducts from previous vertices
C         for the fermions and the boson.
      COMPLEX*16 F1(*),F2(*),V3L(*),V3R(*)
C     EB: Complex, 2-component version of 
C         momentum of F1, F2, and V3.
C     EB: PV3(3) keeps the DENOM from previous vertex for internal 
C          V3 and the polarization factor for external V3.
      COMPLEX*16 PF1(*),PF2(*),PV3(*)
C     EB: Matrices containing all innerproducts for the process.
C         MSQR contains the square innerproducts.
C         MANG contains the angle innerproducts.
      COMPLEX*16, DIMENSION(NEXTERNAL,NEXTERNAL) :: MSQR
      COMPLEX*16, DIMENSION(NEXTERNAL,NEXTERNAL) :: MANG
      COMPLEX*16 SUMF1
      COMPLEX*16 SUMF2
C     EB: Amplitude of the diagram.
      COMPLEX*16 VERTEX
      
      SUMF1 = 0
      SUMF2 = 0

C     EB: Contract F2 with the right-handed part of V3.
      DO J = 1, LEV3R
        DO I = 1, LEF2
          SUMF2 = SUMF2 + F2(I)*V3R(J)*MANG(ABS(MO3R(J)),ABS(MOF2(I)))
        ENDDO
      ENDDO

C     EB: Contract F1 with the left-handed part of V3.
      DO K = 1, LEF1
        DO L = 1, LEV3L
          SUMF1 = SUMF1 + F1(K)*V3L(L)*MSQR(ABS(MOF1(K)),ABS(MO3L(L)))
        ENDDO
      ENDDO  
      
C     EB: Determine the amplitude of the diagram. 
      VERTEX = -COUP * SQRT(RTWO) * PV3(3) * SUMF1 * SUMF2
      END
