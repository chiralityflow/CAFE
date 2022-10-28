      SUBROUTINE RLV1P0_3(F1,LEF1,PF1,MOF1,F2,LEF2
     $ ,PF2,MOF2,NEXTERNAL,MSQR,MANG,COUP,M3,W3,V3L
     $ ,LEV3L,PV3,MO3L,MO3R,V3R,LEV3R)
      IMPLICIT NONE
      COMPLEX*16 CI
      PARAMETER (CI=(0D0,1D0))
      COMPLEX*16 COUP
      DOUBLE PRECISION RTWO
      PARAMETER (RTWO=2.0D0)
      INTEGER NEXTERNAL,I,J
C     EB: Length of F1, F2, V3L, and V3R
      INTEGER LEF1,LEF2,LEV3L,LEV3R
C     EB: Right resp. left external mothers of F1 resp. F2.
      INTEGER MOF1(*),MOF2(*)
C     EB: Left and right external mothers of V3.
      INTEGER MO3L(*),MO3R(*)
C     EB: Vectors carrying innerproducts from previous vertices
C         for the fermions and the boson.
C     EB: V3L has the left-handed part and V3R the right-handed.
      COMPLEX*16 F1(*),F2(*),V3L(*),V3R(*)
C     EB: Complex, 2-component version of 
C         momentum of F1, F2, and V3.
C     EB: PV3(3) used to keep the DENOM factor.
      COMPLEX*16 PF1(*),PF2(*),PV3(*)
      REAL*8 M3
      REAL*8 P3(0:3)
      REAL*8 W3
      COMPLEX*16, DIMENSION(NEXTERNAL,NEXTERNAL) :: MSQR
      COMPLEX*16, DIMENSION(NEXTERNAL,NEXTERNAL) :: MANG
      COMPLEX*16 DENOM
      
      
      PV3(1) = +PF1(1)+PF2(1)
      PV3(2) = +PF1(2)+PF2(2)
      P3(0) = -DBLE(PV3(1))
      P3(1) = -DBLE(PV3(2))
      P3(2) = -DIMAG(PV3(2))
      P3(3) = -DIMAG(PV3(1))
      DENOM = (SQRT(RTWO) * COUP)/(P3(0)**2-P3(1)**2-P3(2)**2-P3(3)**2 - M3 * (M3 -CI
     $ * W3))
     
      PV3(3) = -DENOM
      
      LEV3L = LEF2
C     EB: if F2 is internal.
      IF (LEF2.GT.0) THEN
        DO I = 1, LEF2
          V3L(I) = F2(I)
        ENDDO
      ENDIF
      
      LEV3R = LEF1
C     EB: if F1 is internal.
      IF (LEF1.GT.0) THEN
        DO J= 1, LEF1
          V3R(J) = F1(J)
        ENDDO
      ENDIF
      
      END
