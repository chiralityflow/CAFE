      SUBROUTINE LRV1_0(F1,LEF1,PF1,MOF1,F2,LEF2,PF2,MOF2,V3,PV3,MO3L,MO3R,NEXTERNAL,
     & MSQR,MANG,COUP,VERTEX)      
      IMPLICIT NONE
      COMPLEX*16 CI
      PARAMETER (CI=(0D0,1D0))
      DOUBLE PRECISION RTWO
      PARAMETER (RTWO=2.0D0)
      INTEGER NEXTERNAL,I,J
C     EB: Length of F1 and F2
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
C     EB: Matrices containing all innerproducts for the process.
C         MSQR contains the square innerproducts.
C         MANG contains the angle innerproducts.
      COMPLEX*16, DIMENSION(NEXTERNAL,NEXTERNAL) :: MSQR
      COMPLEX*16, DIMENSION(NEXTERNAL,NEXTERNAL) :: MANG
      COMPLEX*16 SUMF1
      COMPLEX*16 SUMF2
      COMPLEX*16 VERTEX
      
      SUMF1 = 0
      SUMF2 = 0
      
C     EB: if F1 is internal.
      IF (LEF1.GT.0) THEN
        DO I = 1, LEF1
          SUMF1 = SUMF1 + F1(I)*MSQR(ABS(MOF1(I)),ABS(MO3L(1)))
        ENDDO
C     EB: else F1 is external.
      ELSE
        SUMF1 = MSQR(ABS(MOF1(1)),ABS(MO3L(1)))
      ENDIF
      
C     EB: if F2 is internal.
      IF (LEF2.GT.0) THEN
        DO J = 1, LEF2
          SUMF2 = SUMF2 + F2(J)*MANG(ABS(MO3R(1)),ABS(MOF2(J)))
        ENDDO
C     EB: else F2 is external.
      ELSE
        SUMF2 = MANG(ABS(MO3R(1)),ABS(MOF2(1)))       
      ENDIF
      
      VERTEX = -COUP * (DSQRT(RTWO)/PV3(3)) * SUMF1 * SUMF2 
      END
