      SUBROUTINE LLV1_2(F1,LEF1,PF1,MOF1,V3,PV3,MO3L,MO3R,NEXTERNAL,
     & MSQR,MANG,COUP,M2,W2,MOF2,F2,PF2,LEF2)
      IMPLICIT NONE
      COMPLEX*16 CI
      PARAMETER (CI=(0D0,1D0))
      DOUBLE PRECISION RTWO
      PARAMETER (RTWO=2.0D0)
      INTEGER NEXTERNAL,I,J
C     EB: Length of F1 and F2.
      INTEGER LEF1,LEF2
C     EB: Left external mothers of F1 and F2.
      INTEGER MOF1(*),MOF2(*)
C     EB: Left and right external mothers of V3.
      INTEGER MO3L(*),MO3R(*)
      COMPLEX*16 COUP
C     EB: Vectors carrying innerproducts from previous vertices
C         for the fermions and the boson.
      COMPLEX*16 F1(*),F2(*),V3(*)
C     EB: Complex, 2-component version of 
C         momentum of F1, F2, and V3.
C     EB: PV3(3) gives the innerproduct 
C         for the polarisation factor of V3. 
      COMPLEX*16 PF1(*),PF2(*),PV3(*)
C     EB: Real version of F2 momentum.
      REAL*8 P2(0:3)
C     EB: Matrices containing all innerproducts for the process.
C         MSQR contains the square innerproducts.
C         MANG contains the angle innerproducts.
      COMPLEX*16, DIMENSION(NEXTERNAL,NEXTERNAL) :: MSQR
      COMPLEX*16, DIMENSION(NEXTERNAL,NEXTERNAL) :: MANG
      REAL*8 M2
      REAL*8 W2
      COMPLEX*16 DENOM
      COMPLEX*16 SUMF1
      
      PF2(1) = +PF1(1)+PV3(1)
      PF2(2) = +PF1(2)+PV3(2)
      P2(0) = -DBLE(PF2(1))
      P2(1) = -DBLE(PF2(2))
      P2(2) = -DIMAG(PF2(2))
      P2(3) = -DIMAG(PF2(1))
      DENOM = COUP/(P2(0)**2-P2(1)**2-P2(2)**2-P2(3)**2)
      SUMF1 = 0
      
C     EB: if F1 is internal.
      IF (LEF1.GT.0) THEN
        LEF2=LEF1+1
        DO I = 1,LEF1
          SUMF1 = SUMF1 + F1(I)*MSQR(ABS(MOF1(I)),ABS(MO3L(1)))
        ENDDO
C     EB: else F1 is external.
      ELSE
        LEF2=LEF1+2
        SUMF1 = MSQR(ABS(MOF1(1)),ABS(MO3L(1)))
      ENDIF

      DO J = 1, LEF2
C       EB: if external mother of F2 is final.
        IF (MOF2(J).GT.0) THEN
         F2(J) = DENOM*CI*(DSQRT(RTWO)/PV3(3))*SUMF1*MANG(ABS(MO3R(1)),ABS(MOF2(J)))
        ENDIF
C       EB: if external mother of F2 is initial.
        IF (MOF2(J).LT.0) THEN
         F2(J) = -DENOM*CI*(DSQRT(RTWO)/PV3(3))*SUMF1*MANG(ABS(MO3R(1)),ABS(MOF2(J)))
        ENDIF        
      ENDDO 
      END
