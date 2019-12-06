import numpy as np

#=========================GIVEN=========================
D = 80. ; d = 14. ;  pitch = 32. ; Lf = 280. #[mm]
P = 612.5  #[N]
G = 78000. #[MPa]
#=======================================================

def TAUnDE(D,d,pitch,Lf,P):
    T = P*D/2 ; C = D/d ; G = 78000
    Tau = (8*D*P)/(np.pi*(d**3))*(((4*C-1)/(4*C-4))+(0.615/C))
    Na = Lf/pitch
    delta = (8*Na*(D**3)*P)/(G*(d**4))
    return Tau,delta

def TAUnDEbyP(P):
    #=========================GIVEN=========================
    D = 80. ; d = 14. ;  pitch = 32. ; Lf = 280.    #[mm] 
    G = 78000.    #[MPa]
    #=======================================================
    C = D/d ; T = P*D/2 ; G = 78000
    Tau = (8*D*P)/(np.pi*(d**3))*(((4*C-1)/(4*C-4))+(0.615/C))
    Na = Lf/pitch
    delta = (8*Na*(D**3)*P)/(G*(d**4))
    return Tau,delta

def TAUnDEbyDnd(D,d):
    #=========================GIVEN=========================
    pitch = 32. ; Lf = 280.    #[mm] ;
    P = 612.5    #[N]
    G = 78000.   #[MPa]
    #=======================================================
    C = D/d ; T = P*D/2.
    Tau = ((8.*D*P)/(np.pi*(d**3.)))*(((4.*C-1.)/(4.*C-4.))+(0.615/C))
    Na = Lf/pitch
    delta = (8.*Na*(D**3.)*P)/(G*(d**4.))
    return Tau,delta

def Safety(P,D,d):
    C = D/d
    Tau_y = 1000 ; Tau_e = 392    #인강강도, 항복강도
    Tau_m = (8*D*P)/(np.pi*(d**3))*(((4*C-1)/(4*C-4))+(0.615/C))
    Safety = (Tau_m)/Tau_y
    return 1/Safety