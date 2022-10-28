      SUBROUTINE RRV1_2(F1,LEF1,PF1,MOF1,V3,PV3,MO3L,MO3R,NEXTERNAL,
     & MSQR,MANG,COUP,M2,W2,MOF2,F2,PF2,LEF2)
      IMPLICIT NONE
      COMPLEX*16 CI
      PARAMETER (CI=(0D0,1D0))
      DOUBLE PRECISION RTWO
      PARAMETER (RTWO=2.0D0)
      INTEGER NEXTERNAL,I,J
C     EB: Length of F1 and F2.
      INTEGER LEF1,LEF2
C     EB: Right external mothers of F1 and F2.
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
          SUMF1 = SUMF1 + F1(I)*MANG(ABS(MOF1(I)),ABS(MO3R(1)))
        ENDDO
C     EB: else F1 is external.
      ELSE
        LEF2=LEF1+2
        SUMF1 = MANG(ABS(MOF1(1)),ABS(MO3R(1)))
      ENDIF

      DO J = 1, LEF2
C       EB: if external mother of F2 is final.
        IF (MOF2(J).GT.0) THEN
         F2(J) = DENOM*CI*(DSQRT(RTWO)/PV3(3))*SUMF1*MSQR(ABS(MO3L(1)),ABS(MOF2(J)))
        ENDIF
C       EB: if external mother of F2 is initial.
        IF (MOF2(J).LT.0) THEN
         F2(J) = -DENOM*CI*(DSQRT(RTWO)/PV3(3))*SUMF1*MSQR(ABS(MO3L(1)),ABS(MOF2(J)))
        ENDIF        
      ENDDO 
      END
      
      SUBROUTINE RRV1I_2(F1,LEF1,PF1,MOF1,V3L,LEV3L,PV3,MO3L,MO3R,V3R,LEV3R,
     & NEXTERNAL,MSQR,MANG,COUP,M2,W2,MOF2,F2,PF2,LEF2)
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
      COMPLEX*16 COUP
C     EB: Vectors carrying innerproducts from previous vertices
C         for the fermions and the boson.
C     EB: V3L has the left-handed part and V3R the right-handed.
      COMPLEX*16 F1(*),F2(*),V3L(*),V3R(*)
C     EB: Complex, 2-component version of 
C         momentum of F1, F2, and V3.
C     EB: PV3(3) keeps the DENOM from previous vertex.
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
        LEF2=LEF1+LEV3L+LEV3R
        IF (LEV3R.GT.0) THEN
          DO I = 1, LEF1
            DO J = 1, LEV3R
              SUMF1 = SUMF1 + F1(I)*V3R(J)*MANG(ABS(MOF1(I)),ABS(MO3R(J)))
            ENDDO
          ENDDO
        ELSE
          LEF2 = LEF2+1
          DO I = 1, LEF1
            SUMF1 = SUMF1 + F1(I)*MANG(ABS(MOF1(I)),ABS(MO3R(1)))
          ENDDO
        ENDIF 
C     EB: else F1 is external.
      ELSE
        LEF2=1+LEV3L+LEV3R
        IF (LEV3R.GT.0) THEN
          DO J = 1, LEV3R
            SUMF1 = SUMF1 + V3R(J)*MANG(ABS(MOF1(1)),ABS(MO3R(J)))
          ENDDO
        ELSE
          LEF2 = LEF2+1
          SUMF1 = MANG(ABS(MOF1(1)),ABS(MO3R(1)))
        ENDIF
      ENDIF
      
      IF (LEV3L.GT.0) THEN
        DO K = 1, LEF2
          F2(K) = 0
C         EB: if external mother of F2 is final.
          IF (MOF2(K).GT.0) THEN
            DO L = 1, LEV3L
              F2(K) = F2(K) + DENOM*CI*PV3(3)*SUMF1*V3L(L)*
     & MSQR(ABS(MO3L(L)),ABS(MOF2(K)))
            ENDDO
          ENDIF
        
C         EB: if external mother of F1 is initial. 
          IF (MOF2(K).LT.0) THEN
            DO L = 1, LEV3L
              F2(K) = F2(K) - DENOM*CI*PV3(3)*SUMF1*V3L(L)*
     & MSQR(ABS(MO3L(L)),ABS(MOF2(K)))
            ENDDO
          ENDIF 
        ENDDO 
      ELSE
        LEF2 = LEF2+1
        DO K = 1, LEF2
          IF (MOF2(K).GT.0) THEN
            F2(K) = DENOM*DSQRT(RTWO)*CI*PV3(3)*SUMF1*MSQR(ABS(MO3L(1)),ABS(MOF2(K)))
          ELSE
            F2(K) = -DENOM*DSQRT(RTWO)*CI*PV3(3)*SUMF1*MSQR(ABS(MO3L(1)),ABS(MOF2(K)))
          ENDIF
        ENDDO
      ENDIF
      END 
      
      
      
