      SUBROUTINE RLV1_0(F1,LEF1,PF1,MOF1,F2,LEF2,PF2,MOF2,V3,PV3,MO3L,MO3R,NEXTERNAL,
     & MSQR,MANG,COUP,VERTEX)      
      IMPLICIT NONE
      COMPLEX*16 CI
      PARAMETER (CI=(0D0,1D0))
      DOUBLE PRECISION RTWO
      PARAMETER (RTWO=2.0D0)
      INTEGER NEXTERNAL,I,J
C     EB: Length of F1 and F2
      INTEGER LEF1,LEF2
C     EB: Right resp. left external mothers of F1 resp. F2.
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
          SUMF1 = SUMF1 + F1(I)*MANG(ABS(MOF1(I)),ABS(MO3R(1)))
        ENDDO
C     EB: else F1 is external.
      ELSE
        SUMF1 = MANG(ABS(MOF1(1)),ABS(MO3R(1)))
      ENDIF
      
C     EB: if F2 is internal.
      IF (LEF2.GT.0) THEN
        DO J = 1, LEF2
          SUMF2 = SUMF2 + F2(J)*MSQR(ABS(MO3L(1)),ABS(MOF2(J)))
        ENDDO
C     EB: else F2 is external.
      ELSE
        SUMF2 = MSQR(ABS(MO3L(1)),ABS(MOF2(1)))       
      ENDIF
      
      VERTEX = -COUP * (DSQRT(RTWO)/PV3(3)) * SUMF1 * SUMF2 
      END
      
      SUBROUTINE RLV1I_0(F1,LEF1,PF1,MOF1,F2,
     & LEF2,PF2,MOF2,V3L,
     & LEV3L,PV3,MO3L,MO3R,V3R,LEV3R,NEXTERNAL,
     & MSQR,MANG,COUP,VERTEX)      
      IMPLICIT NONE
      COMPLEX*16 CI
      PARAMETER (CI=(0D0,1D0))
      DOUBLE PRECISION RTWO
      PARAMETER (RTWO=2.0D0)
      INTEGER NEXTERNAL,I,J,K,L
C     EB: Length of F1, F2, V3L, and V3R
      INTEGER LEF1,LEF2,LEV3L,LEV3R
C     EB: Right resp. left external mothers of F1 resp. F2.
      INTEGER MOF1(*),MOF2(*)
C     EB: Left and right external mothers of V3.
      INTEGER MO3L(*),MO3R(*)
      COMPLEX*16 COUP
C     EB: Vectors carrying innerproducts from previous vertices
C         for the fermions and the boson.
      COMPLEX*16 F1(*),F2(*),V3L(*),V3R(*)
C     EB: Complex, 2-component version of 
C         momentum of F1, F2, and V3.
C     EB: PV3(3) keeps the DENOM from previous vertex if any of
C          V3's mothers are external. Otherwise equal to 1.
      COMPLEX*16 PF1(*),PF2(*),PV3(*)
C     EB: Matrices containing all innerproducts for the process.
C         MSQR contains the square innerproducts.
C         MANG contains the angle innerproducts.
      COMPLEX*16, DIMENSION(NEXTERNAL,NEXTERNAL) :: MSQR
      COMPLEX*16, DIMENSION(NEXTERNAL,NEXTERNAL) :: MANG
      COMPLEX*16 SUMF1
      COMPLEX*16 SUMF2
      COMPLEX*16 VERTEX, PREVDENOM
      
      SUMF1 = 0
      SUMF2 = 0
      PREVDENOM = PV3(3)

c     EB: if V3 has internal mothers in right part.      
      IF (LEV3R.GT.0) THEN
C       EB: if F1 is internal.
        IF (LEF1.GT.0) THEN 
          DO I = 1, LEF1
            DO J = 1, LEV3R 
              SUMF1 = SUMF1 + F1(I)*V3R(J)*MANG(ABS(MOF1(I)),ABS(MO3R(J)))
            ENDDO
          ENDDO
C       EB: else F1 is external.
        ELSE
          DO I = 1, LEV3R
            SUMF1 = SUMF1 + V3R(I)*MANG(ABS(MOF1(1)),ABS(MO3R(I)))
          ENDDO
        ENDIF
      ELSE   
C       EB: if F1 is internal.
        IF (LEF1.GT.0) THEN
          DO I = 1, LEF1
            SUMF1 = SUMF1 + F1(I)*MANG(ABS(MOF1(I)),ABS(MO3R(1)))
          ENDDO
C       EB: else F1 is external.
        ELSE
          SUMF1 = MANG(ABS(MOF1(1)),ABS(MO3R(1)))
        ENDIF
      ENDIF

C     EB: if V3 has internal mothers in the left part.     
      IF (LEV3L.GT.0) THEN
C       EB: if F2 is internal.
        IF (LEF2.GT.0) THEN
          DO K = 1, LEF2
            DO L = 1, LEV3L
              SUMF2 = SUMF2 + F2(K)*V3L(L)*MSQR(ABS(MO3L(L)),ABS(MOF2(K)))
            ENDDO
          ENDDO  
C       EB: else F2 is external.     
        ELSE
          DO K = 1, LEV3L
            SUMF2 = SUMF2 + V3L(K)*MSQR(ABS(MO3L(K)),ABS(MOF2(1)))
          ENDDO
        ENDIF
      ELSE
C       EB: if F2 is internal.
        IF (LEF2.GT.0) THEN
          DO K = 1, LEF2
            SUMF2 = SUMF2 + F2(K)*MSQR(ABS(MO3L(1)),ABS(MOF2(K)))
          ENDDO
C       EB: else F2 is external.
        ELSE
          SUMF2 = MSQR(ABS(MO3L(1)),ABS(MOF2(1)))       
        ENDIF
      ENDIF
      
      VERTEX = -COUP * SQRT(RTWO) * PREVDENOM * SUMF1 * SUMF2
      END
