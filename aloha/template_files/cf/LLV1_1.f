      SUBROUTINE LLV1_1(F2,LEF2,PF2,MOF2,V3,PV3,MO3L,MO3R,NEXTERNAL,
     & MSQR,MANG,COUP,M1,W1,MOF1,F1,PF1,LEF1)
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
C     EB: Real version of F1 momentum.
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
      
      PF1(1) = +PF2(1)+PV3(1)
      PF1(2) = +PF2(2)+PV3(2)
      P1(0) = -DBLE(PF1(1))
      P1(1) = -DBLE(PF1(2))
      P1(2) = -DIMAG(PF1(2))
      P1(3) = -DIMAG(PF1(1))
      DENOM = COUP/(P1(0)**2-P1(1)**2-P1(2)**2-P1(3)**2)
      SUMF2 = 0
      
C     EB: if F2 is internal.
      IF (LEF2.GT.0) THEN
        LEF1=LEF2+1
        DO I = 1,LEF2
          SUMF2 = SUMF2 + F2(I)*MSQR(ABS(MOF2(I)),ABS(MO3L(1)))
        ENDDO
C     EB: else F2 is external.
      ELSE
        LEF1=LEF2+2
        SUMF2 = MSQR(ABS(MOF2(1)),ABS(MO3L(1)))
      ENDIF
      
      DO J = 1, LEF1
C       EB: if external mother of F1 is final. 
        IF (MOF1(J).GT.0) THEN
         F1(J) = -DENOM*CI*(DSQRT(RTWO)/PV3(3))*SUMF2*MANG(ABS(MO3R(1)),ABS(MOF1(J)))
        ENDIF
C       EB: if external mother of F1 is initial. 
        IF (MOF1(J).LT.0) THEN
         F1(J) = DENOM*CI*(DSQRT(RTWO)/PV3(3))*SUMF2*MANG(ABS(MO3R(1)),ABS(MOF1(J)))
        ENDIF 
      ENDDO 
      END
      
      SUBROUTINE LLV1I_1(F2,LEF2,PF2,MOF2,V3L,LEV3L,PV3,MO3L,MO3R,V3R,LEV3R,
     & NEXTERNAL,MSQR,MANG,COUP,M1,W1,MOF1,F1,PF1,LEF1)
      IMPLICIT NONE
      COMPLEX*16 CI
      PARAMETER (CI=(0D0,1D0))
      DOUBLE PRECISION RTWO
      PARAMETER (RTWO=2.0D0)
      INTEGER NEXTERNAL,I,J,K,L
C     EB: Length of F1, F2, V3L, and V3R
      INTEGER LEF1,LEF2,LEV3L,LEV3R
C     EB: Left external mothers of F1 and F2.
      INTEGER MOF1(*),MOF2(*)
C     EB: Left and right external mothers of V3.
      INTEGER MO3L(*),MO3R(*)
      COMPLEX*16 COUP
C     EB: Vectors carrying innerproducts from previous vertices
C         for the fermions and the boson.
C     EB: V3L has the left-handed part and V3R the right-handed.
      COMPLEX*16 F1(*),F2(*),V3L(*),V3R(*)
C     EB: Complex, 2-component version of 
C         momentum of F1, F2, and V3.
C     EB: PV3(3) keeps the DENOM from previous vertex.
      COMPLEX*16 PF1(*),PF2(*),PV3(*)
C     EB: Real version of F1 momentum.
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
     
      PF1(1) = +PF2(1)+PV3(1)
      PF1(2) = +PF2(2)+PV3(2)
      P1(0) = -DBLE(PF1(1))
      P1(1) = -DBLE(PF1(2))
      P1(2) = -DIMAG(PF1(2))
      P1(3) = -DIMAG(PF1(1))
      DENOM = COUP/(P1(0)**2-P1(1)**2-P1(2)**2-P1(3)**2)
      SUMF2 = 0
      
C     EB: if F2 is internal.
      IF (LEF2.GT.0) THEN
        LEF1=LEF2+LEV3L+LEV3R  
        IF (LEV3L.GT.0) THEN
          DO I = 1, LEF2
            DO J = 1, LEV3L
              SUMF2 = SUMF2 + F2(I)*V3L(J)*MSQR(ABS(MOF2(I)),ABS(MO3L(J)))
            ENDDO
          ENDDO
        ELSE
          LEF1 = LEF1+1
          DO I = 1, LEF2
            SUMF2 = SUMF2 + F2(I)*MSQR(ABS(MOF2(I)),ABS(MO3L(1)))
          ENDDO
        ENDIF    
C     EB: else F2 is external.
      ELSE
        LEF1=1+LEV3L+LEV3R
        IF (LEV3L.GT.0) THEN
          DO J = 1, LEV3L
            SUMF2 = SUMF2 + V3L(J)*MSQR(ABS(MOF2(1)),ABS(MO3L(J)))
          ENDDO
        ELSE
          LEF1 = LEF1+1
          SUMF2 = MSQR(ABS(MOF2(1)),ABS(MO3L(1)))
        ENDIF
      ENDIF
      
      IF (LEV3R.GT.0) THEN
        DO K = 1, LEF1
          F1(K) = 0
C         EB: if external mother of F1 is final.
          IF (MOF1(K).GT.0) THEN
            DO L = 1, LEV3R
              F1(K) = F1(K) - DENOM*CI*PV3(3)*SUMF2*V3R(L)*
     & MANG(ABS(MO3R(L)),ABS(MOF1(K)))
            ENDDO
          ENDIF
        
C         EB: if external mother of F1 is initial. 
          IF (MOF1(K).LT.0) THEN
            DO L = 1, LEV3R
              F1(K) = F1(K) + DENOM*CI*PV3(3)*SUMF2*V3R(L)*
     & MANG(ABS(MO3R(L)),ABS(MOF1(K)))
            ENDDO
          ENDIF 
        ENDDO 
      ELSE
        LEF1 = LEF1+1
        DO K = 1, LEF1
          IF (MOF1(K).GT.0) THEN
            F1(K) = -DENOM*DSQRT(RTWO)*CI*PV3(3)*SUMF2*MANG(ABS(MO3R(1)),ABS(MOF1(K)))
          ELSE
            F1(K) = DENOM*DSQRT(RTWO)*CI*PV3(3)*SUMF2*MANG(ABS(MO3R(1)),ABS(MOF1(K)))
          ENDIF
        ENDDO
      ENDIF
      END 
