      SUBROUTINE %(proc_prefix)sSMATRIXHEL(P,HEL,ANS)
      IMPLICIT NONE
C
C CONSTANT
C
      INTEGER    NEXTERNAL
      PARAMETER (NEXTERNAL=%(nexternal)d)
      INTEGER                 NCOMB         
      PARAMETER (             NCOMB=%(ncomb)d)
CF2PY INTENT(OUT) :: ANS                                                                                                                                                                                     
CF2PY INTENT(IN) :: HEL                                                                                                                                                                                    
CF2PY INTENT(IN) :: P(0:3,NEXTERNAL)  

C  
C ARGUMENTS 
C  
      REAL*8 P(0:3,NEXTERNAL),ANS
	  INTEGER HEL
C
C GLOBAL VARIABLES
C
      INTEGER USERHEL
	  COMMON/%(proc_prefix)sHELUSERCHOICE/USERHEL
C ----------
C BEGIN CODE
C ----------
      USERHEL=HEL
	  CALL %(proc_prefix)sSMATRIX(P,ANS)
	  USERHEL=-1

	  END

      SUBROUTINE %(proc_prefix)sSMATRIX(P,ANS)
C  
%(info_lines)s
C 
C MadGraph5_aMC@NLO StandAlone Version
C 
C Returns amplitude squared summed/avg over colors
c and helicities
c for the point in phase space P(0:3,NEXTERNAL)
C  
%(process_lines)s
C  
      IMPLICIT NONE
C  
C CONSTANTS
C  
      INTEGER    NEXTERNAL
      PARAMETER (NEXTERNAL=%(nexternal)d)
	  INTEGER    NINITIAL 
      PARAMETER (NINITIAL=%(nincoming)d)
      INTEGER NPOLENTRIES
      PARAMETER (NPOLENTRIES=(NEXTERNAL+1)*6)
      INTEGER                 NCOMB         
      PARAMETER (             NCOMB=%(ncomb)d)
	  INTEGER HELAVGFACTOR
	  PARAMETER (HELAVGFACTOR=%(hel_avg_factor)d)
C  
C ARGUMENTS 
C  
      REAL*8 P(0:3,NEXTERNAL),ANS
CF2PY INTENT(OUT) :: ANS
CF2PY INTENT(IN) :: P(0:3,NEXTERNAL)
C  
C LOCAL VARIABLES 
C  
      INTEGER NHEL(NEXTERNAL,NCOMB),NTRY
C  put in common block to expose this variable to python interface
      COMMON/%(proc_prefix)sPROCESS_NHEL/NHEL 
      REAL*8 T
      REAL*8 %(proc_prefix)sMATRIX
      INTEGER IHEL,IDEN, I, J
C     For a 1>N process, them BEAMTWO_HELAVGFACTOR would be set to 1.
      INTEGER BEAMS_HELAVGFACTOR(2)
	  DATA (BEAMS_HELAVGFACTOR(I),I=1,2)/%(beamone_helavgfactor)d,%(beamtwo_helavgfactor)d/
      INTEGER JC(NEXTERNAL)
      LOGICAL GOODHEL(NCOMB)
      DATA NTRY/0/
      DATA GOODHEL/NCOMB*.FALSE./

C
C GLOBAL VARIABLES
C
      INTEGER USERHEL
	  COMMON/%(proc_prefix)sHELUSERCHOICE/USERHEL
	  DATA USERHEL/-1/	  
      LOGICAL HELRESET
      common/%(proc_prefix)shelreset/HELRESET
      data HELRESET/.true./
      
%(helicity_lines)s
%(den_factor_line)s

	  INTEGER POLARIZATIONS(0:NEXTERNAL,0:5)
      COMMON/%(proc_prefix)sBORN_BEAM_POL/POLARIZATIONS
      DATA ((POLARIZATIONS(I,J),I=0,NEXTERNAL),J=0,5)/NPOLENTRIES*-1/

C
C     FUNCTIONS
C
      LOGICAL %(proc_prefix)sIS_BORN_HEL_SELECTED

c----------
c   Check if helreset mode is on
c---------
if (HELRESET) then
   NTRY = 0
   do i=1,NCOMB
      GOODHEL(I) = .false.
   enddo
   HELRESET = .false.
endif

C ----------
C BEGIN CODE
C ----------
      IF(USERHEL.EQ.-1) NTRY=NTRY+1
      DO IHEL=1,NEXTERNAL
         JC(IHEL) = +1
      ENDDO
C     When spin-2 particles are involved, the Helicity filtering is dangerous for the 2->1 topology.
C     This is because depending on the MC setup the initial PS points have back-to-back initial states
C     for which some of the spin-2 helicity configurations are zero. But they are no longer zero
C     if the point is boosted on the z-axis. Remember that HELAS helicity amplitudes are no longer
C     lorentz invariant with expternal spin-2 particles (only the helicity sum is).
C     For this reason, we simply remove the filterin when there is only three external particles.
      IF (NEXTERNAL.LE.3) THEN
        DO IHEL=1,NCOMB
		  GOODHEL(IHEL)=.TRUE.
		ENDDO
	  ENDIF
      ANS = 0D0
          DO IHEL=1,NCOMB
	         IF (USERHEL.EQ.-1.OR.USERHEL.EQ.IHEL) THEN		  
                IF (GOODHEL(IHEL) .OR. NTRY .LT. 20.OR.USERHEL.NE.-1) THEN
				    IF(NTRY.GE.2.AND.POLARIZATIONS(0,0).ne.-1.and.(.not.%(proc_prefix)sIS_BORN_HEL_SELECTED(IHEL))) THEN
                        CYCLE
                    ENDIF
                    T=%(proc_prefix)sMATRIX(P ,NHEL(1,IHEL),JC(1))
                    IF(POLARIZATIONS(0,0).eq.-1.or.%(proc_prefix)sIS_BORN_HEL_SELECTED(IHEL)) THEN
                        ANS=ANS+T
                    ENDIF
				    IF (T .NE. 0D0 .AND. .NOT.    GOODHEL(IHEL)) THEN
                        GOODHEL(IHEL)=.TRUE.
                    ENDIF
                ENDIF
		     ENDIF
          ENDDO
      ANS=ANS/DBLE(IDEN)
	  IF(USERHEL.NE.-1) THEN
          ANS=ANS*HELAVGFACTOR	  
	  ELSE
		DO J=1,NINITIAL
		  IF (POLARIZATIONS(J,0).ne.-1) THEN
            ANS=ANS*BEAMS_HELAVGFACTOR(J)
            ANS=ANS/POLARIZATIONS(J,0)
		  ENDIF
		ENDDO
	  ENDIF
c AW: remove this later
      OPEN(1, FILE = '/home/adam/Special_gluons/MadCAFE/bin/testdata.txt', STATUS = 'old', ACTION = 'write', POSITION = 'append') 
      WRITE(1,*) ANS
	  END
      
      
      
      REAL*8 FUNCTION %(proc_prefix)sMATRIX(P,NHEL,IC)
C  
%(info_lines)s
C
C Returns amplitude squared -- no average over initial state/symmetry factor
c for the point with external lines W(0:6,NEXTERNAL)
C  
%(process_lines)s
C  
      IMPLICIT NONE
C  
C CONSTANTS
C  
      INTEGER    NGRAPHS
      PARAMETER (NGRAPHS=%(ngraphs)d) 
      INTEGER    NEXTERNAL
      PARAMETER (NEXTERNAL=%(nexternal)d)
      INTEGER    NWAVEFUNCS, NCOLOR
      PARAMETER (NWAVEFUNCS=%(nwavefuncs)d, NCOLOR=%(ncolor)d) 
      REAL*8     ZERO
      PARAMETER (ZERO=0D0)
      COMPLEX*16 IMAG1
      PARAMETER (IMAG1=(0D0,1D0))
C  
C ARGUMENTS 
C  
      REAL*8 P(0:3,NEXTERNAL)
      REAL*8 PB(0:3,NEXTERNAL)
      INTEGER NHEL(NEXTERNAL), IC(NEXTERNAL)
C  
C LOCAL VARIABLES 
C  
      INTEGER I,J,ZEROVAMPS,ZEROLRAMPS,TOTAMPS,ZEROWFS,TOTWFS,HELASLOOP,AMPLOOP,WFLOOP
      COMPLEX*16 ZTEMP
      REAL*8 CF(NCOLOR,NCOLOR)
c AW: 15/06/2023 adding ref vector manually
      REAL*8 REFVEC1(0:3),REFVEC2(0:3)
      COMPLEX*16 AMP(NGRAPHS), JAMP(NCOLOR), TMP_JAMP(%(nb_temp_jamp)i)
      COMPLEX*16 W(20,NWAVEFUNCS)
      COMPLEX*16 DUM0,DUM1
      DATA DUM0, DUM1/(0d0, 0d0), (1d0, 0d0)/
C  
C GLOBAL VARIABLES
C  
      include 'coupl.inc'
%(global_variable)s
      ZEROVAMPS = 0
      ZEROLRAMPS = 0
      TOTAMPS = 0
      ZEROWFS = 0
      TOTWFS = 0

C  
C COLOR DATA
C
%(color_data_lines)s
C ----------
C BEGIN CODE
C ----------
       PB = P
C       REFVEC1(0) = 500
C       REFVEC1(1) = -110.92428444383279
C       REFVEC1(2) = -444.83078948812141
C       REFVEC1(3) = 199.55292993087872
C       REFVEC2(0) = 500
C       REFVEC2(1) = 110.92428444383278
C       REFVEC2(2) = 444.83078948812135
C       REFVEC2(3) = -199.55292993087878
C       DO HELASLOOP = 1,1    
       open(2, FILE = '/home/adam/Special_gluons/MadCAFE/bin/testzeros.txt', STATUS = 'old', POSITION= 'append', ACTION= 'write')
       WRITE(2,*) NHEL
%(helas_calls)s
       
C       ENDDO

       
C      OPEN(1, FILE = '/home/adam/Special_gluons/MadCAFE/bin/amps.txt', STATUS = 'old', ACTION = 'write', POSITION = 'append')
       DO AMPLOOP = 1,NGRAPHS
         WRITE(*,*) AMPLOOP, ABS(AMP(AMPLOOP))   
       ENDDO       
      
       OPEN(1, FILE = '/home/adam/Special_gluons/MadCAFE/bin/zeroamps.txt', STATUS = 'old', ACTION = 'write', POSITION = 'append')
       DO AMPLOOP = 1,NGRAPHS
         IF (ABS(AMP(AMPLOOP)).le.1E-15) THEN
            WRITE(1,*) AMPLOOP, NHEL
         ENDIF
       ENDDO
       OPEN(1, FILE = '/home/adam/Special_gluons/MadCAFE/bin/zerowfs.txt', STATUS = 'old', ACTION = 'write', POSITION = 'append')
       DO WFLOOP = 1,NWAVEFUNCS
         IF (ABS(W(3,WFLOOP)).LE.1E-18.AND.ABS(W(4,WFLOOP)).LE.1E-18.AND.ABS(W(5,WFLOOP)).LE.1E-18.AND.ABS(W(6,WFLOOP)).LE.1E-18) THEN 
            WRITE(1,*) WFLOOP, NHEL
         ENDIF
       ENDDO
%(jamp_lines)s
C      WRITE(*,*) 'ZERO V AMPS = ' ,ZEROVAMPS
C      WRITE(*,*) 'ZERO LRV AMPS = ' ,ZEROLRAMPS
C      WRITE(*,*) 'TOTAMPS = ' ,TOTAMPS
C      WRITE(*,*) 'ZEROWFS = ' ,ZEROWFS
C      WRITE(*,*) 'TOTWFS = ' ,TOTWFS

      %(proc_prefix)sMATRIX = 0.D0 
      DO I = 1, NCOLOR
          ZTEMP = (0.D0,0.D0)
          DO J = 1, NCOLOR
              ZTEMP = ZTEMP + CF(J,I)*JAMP(J)
          ENDDO
          %(proc_prefix)sMATRIX = %(proc_prefix)sMATRIX+ZTEMP*DCONJG(JAMP(I))
      ENDDO
%(amp2_lines)s
      END

      SUBROUTINE %(proc_prefix)sGET_value(P, ALPHAS, NHEL ,ANS)
      IMPLICIT NONE   
C
C CONSTANT
C
      INTEGER    NEXTERNAL
      PARAMETER (NEXTERNAL=%(nexternal)d)
C  
C ARGUMENTS 
C  
      REAL*8 P(0:3,NEXTERNAL),ANS
      INTEGER NHEL
      DOUBLE PRECISION ALPHAS 
      real*8 pi     
CF2PY INTENT(OUT) :: ANS  
CF2PY INTENT(IN) :: NHEL   
CF2PY INTENT(IN) :: P(0:3,NEXTERNAL) 
CF2PY INTENT(IN) :: ALPHAS
C     ROUTINE FOR F2PY to read the benchmark point.    
C     the include file with the values of the parameters and masses 
      include "coupl.inc"
      
      pi = 3.141592653589793d0
      G = 2* DSQRT(ALPHAS*pi)
      call UPDATE_AS_PARAM()
      if (NHEL.ne.0) then
        CALL %(proc_prefix)sSMATRIXHEL(P, NHEL, ANS)
      else
        CALL %(proc_prefix)sSMATRIX(P, ANS)
      endif
      return 
      end

      SUBROUTINE %(proc_prefix)sINITIALISEMODEL(PATH)
C     ROUTINE FOR F2PY to read the benchmark point.    
      IMPLICIT NONE   
      CHARACTER*512 PATH
CF2PY INTENT(IN) :: PATH 
      call setpara(PATH)  !first call to setup the paramaters    
      return 
      end      

      LOGICAL FUNCTION %(proc_prefix)sIS_BORN_HEL_SELECTED(HELID)
      IMPLICIT NONE
C     
C     CONSTANTS
C     
      INTEGER    NEXTERNAL
      PARAMETER (NEXTERNAL=%(nexternal)d)
      INTEGER    NCOMB
      PARAMETER (NCOMB=%(ncomb)d)
C
C     ARGUMENTS
C
      INTEGER HELID
C
C     LOCALS
C
      INTEGER I,J
      LOGICAL FOUNDIT
C
C     GLOBALS
C
      INTEGER HELC(NEXTERNAL,NCOMB)
      COMMON/%(proc_prefix)sPROCESS_NHEL/HELC

      INTEGER POLARIZATIONS(0:NEXTERNAL,0:5)
      COMMON/%(proc_prefix)sBORN_BEAM_POL/POLARIZATIONS
C     ----------
C     BEGIN CODE
C     ----------
      
      %(proc_prefix)sIS_BORN_HEL_SELECTED = .True.
      if (POLARIZATIONS(0,0).eq.-1) THEN
        RETURN
      ENDIF

      DO I=1,NEXTERNAL
        IF (POLARIZATIONS(I,0).eq.-1) THEN
          CYCLE
        ENDIF
        FOUNDIT = .FALSE.
        DO J=1,POLARIZATIONS(I,0)
          IF (HELC(I,HELID).eq.POLARIZATIONS(I,J)) THEN
            FOUNDIT = .True.
            EXIT
          ENDIF
        ENDDO
        IF(.not.FOUNDIT) THEN
          %(proc_prefix)sIS_BORN_HEL_SELECTED = .False.
          RETURN
        ENDIF
      ENDDO

      RETURN
      END
