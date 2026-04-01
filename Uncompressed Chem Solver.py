# GENERAL CHEM SOLVER
# TI-84 Plus CE Python
import math

def pause():
    input("--ENTER--")

def menu():
    print("==CHEM SOLVER==")
    print("1:Thermodynamics")
    print("2:Equilibrium")
    print("3:Acids & Bases")
    print("4:Electrochemistry")
    print("5:Gases")
    print("6:Solubility")
    print("7:Calorimetry")
    print("8:Hess Law")
    print("0:Quit")
    return int(input("Choice:"))

# ======= THERMODYNAMICS =======

def menu_thermo():
    print("--THERMODYNAMICS--")
    print("1:DeltaG=DH-TDS")
    print("2:DeltaG from K")
    print("3:DeltaG_rxn from DGf")
    print("4:DeltaH from DeltaE")
    print("5:DeltaS isothermal")
    print("6:DeltaS from Cp")
    print("7:DeltaG non-standard")
    print("8:DeltaHvap from DeltaS")
    print("9:DG at non-std T(DH,DS)")
    print("10:DH&DS rxn from tables")
    print("11:Q vs K (rxn direct)")
    print("0:Back")
    return int(input("Choice:"))

def dG_dH_dS():
    print("DeltaG = DH - T*DS")
    dH = float(input("DeltaH kJ/mol:"))
    dS = float(input("DeltaS J/mol/K:"))
    T_C = float(input("Temp C:"))
    T = T_C + 273.15
    dG = dH - T * (dS / 1000)
    print("T(K)=" + str(round(T,2)))
    print("DeltaG=" + str(round(dG,6)) + "kJ/mol")
    if dG < 0:
        print("Spontaneous")
    elif dG > 0:
        print("Non-spontaneous")
    else:
        print("At equilibrium")
    pause()

def dG_from_K():
    print("DeltaG = -RT*ln(K)")
    K = float(input("K:"))
    T_C = float(input("Temp C:"))
    T = T_C + 273.15
    dG = -8.314 * T * math.log(K)
    print("DeltaG=" + str(round(dG,2)) + "J/mol")
    print("      =" + str(round(dG/1000,4)) + "kJ/mol")
    pause()

def dG_rxn():
    print("DG=sum(n*DGf_prod)")
    print("  -sum(n*DGf_rct)")
    np = int(input("Num products:"))
    sp = 0.0
    i = 0
    while i < np:
        dg = float(input("DGf prod" + str(i+1) + " kJ:"))
        c = float(input("coeff:"))
        sp = sp + c * dg
        i = i + 1
    nr = int(input("Num reactants:"))
    sr = 0.0
    i = 0
    while i < nr:
        dg = float(input("DGf rct" + str(i+1) + " kJ:"))
        c = float(input("coeff:"))
        sr = sr + c * dg
        i = i + 1
    print("DeltaG=" + str(round(sp-sr,4)) + "kJ/mol")
    pause()

def dH_from_dE():
    print("DH = DE + Dn*R*T")
    dE = float(input("DeltaE kJ:"))
    dn = float(input("Dn gas (p-r):"))
    T_C = float(input("Temp C:"))
    T = T_C + 273.15
    dH = dE + dn * 8.314 * T / 1000
    print("DeltaH=" + str(round(dH,4)) + "kJ")
    pause()

def dS_isothermal():
    print("DS=nR*ln(V2/V1)")
    print("  =nR*ln(P1/P2)")
    ch = int(input("1:Volume 2:Pressure:"))
    n = float(input("moles:"))
    if ch == 1:
        v1 = float(input("V1:"))
        v2 = float(input("V2:"))
        dS = n * 8.314 * math.log(v2 / v1)
    else:
        p1 = float(input("P1:"))
        p2 = float(input("P2:"))
        dS = n * 8.314 * math.log(p1 / p2)
    print("DeltaS=" + str(round(dS,4)) + "J/K")
    pause()

def dS_Cp():
    print("DS = n*Cp*ln(T2/T1)")
    n = float(input("moles:"))
    Cp = float(input("Cp J/mol/K:"))
    T1_C = float(input("T1 C:"))
    T2_C = float(input("T2 C:"))
    T1 = T1_C + 273.15
    T2 = T2_C + 273.15
    dS = n * Cp * math.log(T2 / T1)
    print("DeltaS=" + str(round(dS,4)) + "J/K")
    pause()

# ======= EQUILIBRIUM =======

def menu_equil():
    print("--EQUILIBRIUM--")
    print("1:Kc to Kp")
    print("2:Kp to Kc")
    print("3:ICE table (conc)")
    print("4:ICE table (pressure)")
    print("5:Combine K values")
    print("6:Calc K from ICE")
    print("7:DeltaG to K")
    print("8:K at new temp")
    print("0:Back")
    return int(input("Choice:"))

def kc_kp(direction):
    if direction == 1:
        print("Kp = Kc*(RT)^Dn")
        Kc = float(input("Kc:"))
    else:
        print("Kc = Kp/(RT)^Dn")
        Kc = float(input("Kp:"))
    T_C = float(input("Temp C:"))
    dn = float(input("Dn (prod-rct gas):"))
    T = T_C + 273.15
    RT = 0.08206 * T
    if direction == 1:
        print("Kp=" + str(Kc * RT**dn))
    else:
        print("Kc=" + str(Kc / RT**dn))
    pause()

def ice_table():
    print("ICE: aA+bB->cC+dD")
    print("(use 0 if no species)")
    K = float(input("K value:"))
    a = float(input("coeff A (rct):"))
    A0 = float(input("[A]0 M:"))
    b = float(input("coeff B (rct):"))
    B0 = float(input("[B]0 M:"))
    c = float(input("coeff C (prod):"))
    C0 = float(input("[C]0 M:"))
    d = float(input("coeff D (prod):"))
    D0 = float(input("[D]0 M:"))
    # bisection: find x where Q=K
    lo = 0.0
    hi = 0.9999
    if a > 0 and A0 > 0:
        hi = min(hi, A0/a * 0.9999)
    if b > 0 and B0 > 0:
        hi = min(hi, B0/b * 0.9999)
    for i in range(100):
        mid = (lo + hi) / 2.0
        Ae = A0 - a*mid
        Be = B0 - b*mid
        Ce = C0 + c*mid
        De = D0 + d*mid
        num = 1.0
        den = 1.0
        if c > 0:
            num = num * Ce**c
        if d > 0:
            num = num * De**d
        if a > 0 and Ae > 0:
            den = den * Ae**a
        if b > 0 and Be > 0:
            den = den * Be**b
        Q = num / den
        if Q < K:
            lo = mid
        else:
            hi = mid
    x = (lo + hi) / 2.0
    print("x=" + str(x))
    print("[A]=" + str(A0-a*x))
    print("[B]=" + str(B0-b*x))
    print("[C]=" + str(C0+c*x))
    print("[D]=" + str(D0+d*x))
    pause()

def dG_to_K():
    print("K = e^(-DG/RT)")
    dG = float(input("DeltaG kJ/mol:"))
    T_C = float(input("Temp C:"))
    T = T_C + 273.15
    val = -dG * 1000 / (8.314 * T)
    K = math.exp(val)
    print("K=" + str(K))
    pause()

def K_new_T():
    print("van't Hoff equation")
    print("ln(K2/K1)=-DH/R*(1/T2-1/T1)")
    K1 = float(input("K1:"))
    T1_C = float(input("T1 C:"))
    dH = float(input("DeltaH kJ/mol:"))
    T2_C = float(input("T2 C:"))
    T1 = T1_C + 273.15
    T2 = T2_C + 273.15
    lnK2 = math.log(K1) - (dH*1000/8.314)*(1/T2 - 1/T1)
    print("K2=" + str(math.exp(lnK2)))
    pause()

# ======= ACIDS & BASES =======

def menu_acid():
    print("--ACIDS & BASES--")
    print("1:pH strong acid/base")
    print("2:pH weak acid")
    print("3:pH weak base")
    print("4:Ka from pH")
    print("5:Kb from pH")
    print("6:Ka/Kb conversion")
    print("7:Henderson-Hassel")
    print("8:Titration eq pt")
    print("9:Titration any point")
    print("10:% dissoc -> pH")
    print("11:pH polyprotic base")
    print("12:pH dilute strong acid")
    print("13:Buffer mix 2 solutions")
    print("14:Solubility at fixed pH")
    print("0:Back")
    return int(input("Choice:"))

def pH_strong():
    print("Strong acid/base pH")
    t = int(input("1:acid 2:base:"))
    c = float(input("Conc M:"))
    if t == 1:
        pH = -math.log10(c)
        print("pH=" + str(round(pH,4)))
    else:
        pOH = -math.log10(c)
        pH = 14 - pOH
        print("pOH=" + str(round(pOH,4)))
        print("pH=" + str(round(pH,4)))
    pause()

def pH_weak_acid():
    print("Weak acid HA->H+A-")
    Ka = float(input("Ka:"))
    C = float(input("[HA] M:"))
    x = (-Ka + math.sqrt(Ka**2 + 4*Ka*C)) / 2
    pH = -math.log10(x)
    print("[H+]=" + str(x))
    print("pH=" + str(round(pH,4)))
    print("% diss=" + str(round(x/C*100,2)))
    pause()

def pH_weak_base():
    print("Weak base B->BH+OH-")
    Kb = float(input("Kb:"))
    C = float(input("[B] M:"))
    x = (-Kb + math.sqrt(Kb**2 + 4*Kb*C)) / 2
    pOH = -math.log10(x)
    pH = 14 - pOH
    print("[OH-]=" + str(x))
    print("pOH=" + str(round(pOH,4)))
    print("pH=" + str(round(pH,4)))
    pause()

def Ka_pH():
    print("Ka from weak acid pH")
    C = float(input("[HA] initial M:"))
    pH = float(input("pH:"))
    H = 10**(-pH)
    Ka = H**2 / (C - H)
    print("Ka=" + str(Ka))
    pause()

def Kb_pH():
    print("Kb from weak base pH")
    C = float(input("[B] initial M:"))
    pH = float(input("pH:"))
    OH = 10**(-(14-pH))
    Kb = OH**2 / (C - OH)
    print("Kb=" + str(Kb))
    pause()

def Ka_Kb_conv():
    print("Ka*Kb=Kw=1e-14")
    t = int(input("1:Ka->Kb 2:Kb->Ka:"))
    if t == 1:
        Ka = float(input("Ka:"))
        print("Kb=" + str(1e-14/Ka))
    else:
        Kb = float(input("Kb:"))
        print("Ka=" + str(1e-14/Kb))
    pause()

def henderson():
    print("Henderson-Hasselbalch")
    print("pH=pKa+log([A-]/[HA])")
    t = int(input("1:find pH 2:find ratio 3:find mol acid:"))
    Ka = float(input("Ka:"))
    pKa = -math.log10(Ka)
    if t == 1:
        A = float(input("[A-] or mol:"))
        HA = float(input("[HA] or mol:"))
        pH = pKa + math.log10(A / HA)
        print("pKa=" + str(round(pKa,4)))
        print("pH=" + str(round(pH,4)))
    elif t == 2:
        pH = float(input("Target pH:"))
        ratio = 10**(pH - pKa)
        print("pKa=" + str(round(pKa,4)))
        print("[A-]/[HA]=" + str(round(ratio,4)))
    else:
        V = float(input("Vol L:"))
        M = float(input("Molarity salt M:"))
        pH = float(input("Target pH:"))
        n_salt = M * V
        ratio = 10**(pH - pKa)
        x = n_salt / (1 + ratio)
        print("pKa=" + str(round(pKa,4)))
        print("mol HCl=" + str(round(x,6)))
    pause()

def titration_eq():
    print("Titration equiv pt")
    print("1:strong-strong pH=7")
    print("2:weak acid+strong base")
    print("3:weak base+strong acid")
    t = int(input("Type:"))
    if t == 1:
        print("pH = 7.00")
    elif t == 2:
        Ka = float(input("Ka acid:"))
        Ca = float(input("[acid] M:"))
        Va = float(input("Vol acid L:"))
        Cb = float(input("[base] M:"))
        Vb = Ca * Va / Cb
        Vtot = Va + Vb
        Cs = (Ca * Va) / Vtot
        Kb = 1e-14 / Ka
        OH = math.sqrt(Kb * Cs)
        pH = 14 - (-math.log10(OH))
        print("Vb_eq=" + str(round(Vb,4)) + "L")
        print("pH=" + str(round(pH,4)))
    else:
        Kb = float(input("Kb base:"))
        Cb = float(input("[base] M:"))
        Vb = float(input("Vol base L:"))
        Ca = float(input("[acid] M:"))
        Va = Cb * Vb / Ca
        Vtot = Vb + Va
        Cs = (Cb * Vb) / Vtot
        Ka = 1e-14 / Kb
        H = math.sqrt(Ka * Cs)
        pH = -math.log10(H)
        print("Va_eq=" + str(round(Va,4)) + "L")
        print("pH=" + str(round(pH,4)))
    pause()

# ======= ELECTROCHEMISTRY =======

def menu_electro():
    print("--ELECTROCHEMISTRY--")
    print("1:Ecell from half rxns")
    print("2:DeltaG from Ecell")
    print("3:Nernst equation")
    print("4:Concentration cell")
    print("5:Find mass deposited")
    print("6:Find current needed")
    print("7:Find time needed")
    print("8:Find molar mass")
    print("9:Find ion charge")
    print("10:DG,K,E interconvert")
    print("0:Back")
    return int(input("Choice:"))

def ecell():
    print("Ecell=Ecathode-Eanode")
    ec = float(input("E cathode V:"))
    ea = float(input("E anode V:"))
    E = ec - ea
    print("Ecell=" + str(round(E,4)) + "V")
    if E > 0:
        print("Spontaneous")
    else:
        print("Non-spontaneous")
    pause()

def dG_ecell():
    print("DeltaG = -nFE")
    n = float(input("n mol e-:"))
    E = float(input("Ecell V:"))
    F = 96485
    dG = -n * F * E
    print("DeltaG=" + str(round(dG,2)) + "J")
    print("      =" + str(round(dG/1000,4)) + "kJ")
    pause()

def nernst():
    print("E=E0-(RT/nF)*ln(Q)")
    E0 = float(input("E0 V:"))
    n = float(input("n mol e-:"))
    Q = float(input("Q reaction quotient:"))
    T_C = float(input("Temp C:"))
    T = T_C + 273.15
    E = E0 - (8.314*T/(n*96485)) * math.log(Q)
    print("E=" + str(round(E,6)) + "V")
    pause()

def electrolysis(mode):
    # mode 1=find mass, 2=find I, 3=find time
    if mode == 1:
        print("Find mass deposited")
        I = float(input("Current A:"))
        t_hr = float(input("Time hours:"))
        ne = float(input("e- per ion:"))
        MM = float(input("Molar mass g/mol:"))
        F = 96485
        mol_e = I * t_hr * 3600 / F
        mass = mol_e / ne * MM
        print("mass=" + str(round(mass,4)) + "g")
    elif mode == 2:
        print("Find current needed")
        mass = float(input("Target mass g:"))
        t_hr = float(input("Time hours:"))
        ne = float(input("e- per ion:"))
        MM = float(input("Molar mass g/mol:"))
        F = 96485
        mol_e = (mass/MM) * ne
        I = mol_e * F / (t_hr * 3600)
        print("I=" + str(round(I,4)) + "A")
    else:
        print("Find time needed")
        mass = float(input("Target mass g:"))
        I = float(input("Current A:"))
        ne = float(input("e- per ion:"))
        MM = float(input("Molar mass g/mol:"))
        F = 96485
        mol_e = (mass/MM) * ne
        t_s = mol_e * F / I
        print("t=" + str(round(t_s,2)) + "s")
        print(" =" + str(round(t_s/3600,4)) + "hr")
    pause()

# ======= GASES =======

def menu_gas():
    print("--GASES--")
    print("1:Ideal gas PV=nRT")
    print("2:Work w=-PDeltaV")
    print("3:Work w=-DeltanRT")
    print("4:DeltaE=q+w")
    print("5:DeltaH=DE+DnRT")
    print("6:Graham effusion")
    print("0:Back")
    return int(input("Choice:"))

def ideal_gas():
    print("PV=nRT (enter 0=solve)")
    P = float(input("P atm (0=?):"))
    V = float(input("V L (0=?):"))
    n = float(input("n mol (0=?):"))
    T_C = float(input("T C (0=?):"))
    R = 0.08206
    if P == 0:
        T = T_C + 273.15
        print("P=" + str(round(n*R*T/V,4)) + "atm")
    elif V == 0:
        T = T_C + 273.15
        print("V=" + str(round(n*R*T/P,4)) + "L")
    elif n == 0:
        T = T_C + 273.15
        print("n=" + str(round(P*V/(R*T),6)) + "mol")
    else:
        T = P*V/(n*R)
        print("T=" + str(round(T,2)) + "K")
        print(" =" + str(round(T-273.15,2)) + "C")
    pause()

def work_PDV():
    print("w = -P*DeltaV")
    P = float(input("P atm:"))
    V1 = float(input("V1 L:"))
    V2 = float(input("V2 L:"))
    dV = V2 - V1
    w_J = -P * dV * 101.325
    print("DV=" + str(round(dV,4)) + "L")
    print("w=" + str(round(w_J,2)) + "J")
    if w_J > 0:
        print("Work ON system")
    else:
        print("Work BY system")
    pause()

def work_Dn():
    print("w = -Dn*R*T")
    dn = float(input("Dn gas (prod-rct):"))
    T_C = float(input("Temp C:"))
    T = T_C + 273.15
    w = -dn * 8.314 * T
    print("w=" + str(round(w,2)) + "J")
    if w > 0:
        print("Work ON system")
    else:
        print("Work BY system")
    pause()

def dE_qw():
    print("DeltaE = q + w")
    q = float(input("q J:"))
    w = float(input("w J:"))
    dE = q + w
    print("DeltaE=" + str(round(dE,2)) + "J")
    print("      =" + str(round(dE/1000,4)) + "kJ")
    pause()

def dH_gas():
    print("DH = DE + Dn*R*T")
    dE = float(input("DeltaE kJ:"))
    dn = float(input("Dn gas:"))
    T_C = float(input("Temp C:"))
    T = T_C + 273.15
    dH = dE + dn * 8.314 * T / 1000
    print("DeltaH=" + str(round(dH,4)) + "kJ")
    pause()

def graham():
    print("Graham: r1/r2=sqrt(M2/M1)")
    t = int(input("1:find ratio 2:find M:"))
    if t == 1:
        M1 = float(input("M1 g/mol:"))
        M2 = float(input("M2 g/mol:"))
        ratio = math.sqrt(M2/M1)
        print("r1/r2=" + str(round(ratio,4)))
    else:
        M1 = float(input("Known M g/mol:"))
        ratio = float(input("r1/r2:"))
        print("Unknown M=" + str(round(M1*ratio**2,4)) + "g/mol")
    pause()

# ======= SOLUBILITY =======

def menu_sol():
    print("--SOLUBILITY--")
    print("1:Ksp -> molar sol")
    print("2:Common ion effect")
    print("3:Molar sol -> Ksp")
    print("4:Simultaneous equil")
    print("0:Back")
    return int(input("Choice:"))

def ksp_to_s():
    print("AxBy -> xA^m+ + yB^n-")
    Ksp = float(input("Ksp:"))
    x = float(input("coeff cation x:"))
    y = float(input("coeff anion y:"))
    # Ksp = (xs)^x * (ys)^y
    exp = x + y
    coeff = (x**x) * (y**y)
    s = (Ksp / coeff) ** (1.0/exp)
    print("s=" + str(s) + "mol/L")
    pause()

def common_ion():
    print("Common ion solubility")
    print("AxBy -> xA + yB")
    Ksp = float(input("Ksp:"))
    x = float(input("coeff cation x:"))
    y = float(input("coeff anion y:"))
    t = int(input("Common ion: 1:cation 2:anion:"))
    C0 = float(input("Common ion conc M:"))
    # bisection
    lo = 0.0
    hi = (Ksp)**(1.0/(x+y)) * 10
    for i in range(100):
        mid = (lo+hi)/2.0
        if t == 2:
            A = x*mid
            B = y*mid + C0
        else:
            A = x*mid + C0
            B = y*mid
        Q = A**x * B**y
        if Q < Ksp:
            lo = mid
        else:
            hi = mid
    s = (lo+hi)/2.0
    print("s=" + str(s) + "mol/L")
    pause()

def s_to_ksp():
    print("Molar sol -> Ksp")
    print("AxBy -> xA + yB")
    s = float(input("s mol/L:"))
    x = float(input("coeff cation x:"))
    y = float(input("coeff anion y:"))
    Ksp = (x*s)**x * (y*s)**y
    print("Ksp=" + str(Ksp))
    pause()

def simultaneous_equil():
    print("Simultaneous equilibrium")
    print("Two salts sharing one ion")
    print("e.g. BaSO4 + SrSO4")
    print("Both: AxBy -> xA + yB")
    print("-- Salt 1 --")
    Ksp1 = float(input("Ksp1:"))
    x1 = float(input("coeff cation1 x:"))
    y1 = float(input("coeff anion1 y:"))
    print("-- Salt 2 --")
    Ksp2 = float(input("Ksp2:"))
    x2 = float(input("coeff cation2 x:"))
    y2 = float(input("coeff anion2 y:"))
    print("Shared ion is:")
    t = int(input("1:anion 2:cation:"))
    # For simple 1:1 salts (most common case)
    # Ksp1 = s1 * (s1+s2)^y1  for anion shared
    # Ksp2 = s2 * (s1+s2)^y2
    # If y1=y2=1: ratio s1/s2 = Ksp1/Ksp2
    # General: use bisection on s2
    # Ksp2 = s2 * (x1*s1 + x2*s2)^y2
    # where s1 = (Ksp1 / (x1*s1+x2*s2)^y1) / x1... complex
    # For 1:1 case (covers most exam problems):
    if x1==1 and y1==1 and x2==1 and y2==1:
        # s1/s2 = Ksp1/Ksp2
        # Ksp2 = s2*(s1+s2) = s2^2*(ratio+1)
        ratio = Ksp1/Ksp2
        import math
        s2 = math.sqrt(Ksp2/(ratio+1))
        s1 = ratio*s2
        shared = s1+s2
        print("-- Results --")
        if t == 1:
            print("[cation1]=" + str(s1))
            print("[cation2]=" + str(s2))
            print("[shared anion]=" + str(shared))
        else:
            print("[anion1]=" + str(s1))
            print("[anion2]=" + str(s2))
            print("[shared cation]=" + str(shared))
        print("Check Ksp1=" + str(s1*shared))
        print("Check Ksp2=" + str(s2*shared))
    else:
        # General case: bisection on shared ion concentration
        import math
        # Let C = shared ion concentration
        # s1 = Ksp1 / C^y1 / x1  (approx, assumes x1*s1 << C for large diff)
        # s2 = Ksp2 / C^y2 / x2
        # C = x1*s1 + x2*s2 (self-consistent)
        # Solve by iteration
        C = (Ksp2)**(1.0/(x2+y2))  # initial guess
        for i in range(200):
            s1 = Ksp1 / (x1 * C**y1)
            s2 = Ksp2 / (x2 * C**y2)
            C_new = x1*s1 + x2*s2
            if abs(C_new-C) < 1e-20:
                break
            C = C_new
        print("-- Results --")
        print("[cation1]=" + str(s1))
        print("[cation2]=" + str(s2))
        print("[shared ion]=" + str(C))
        print("Check Ksp1=" + str(s1 * C**y1))
        print("Check Ksp2=" + str(s2 * C**y2))
    pause()


    print("Molar sol -> Ksp")
    print("AxBy -> xA + yB")
    s = float(input("s mol/L:"))
    x = float(input("coeff cation x:"))
    y = float(input("coeff anion y:"))
    Ksp = (x*s)**x * (y*s)**y
    print("Ksp=" + str(Ksp))
    pause()

# ======= CALORIMETRY =======

def menu_cal():
    print("--CALORIMETRY--")
    print("1:q=mcDT")
    print("2:Final temp mix")
    print("3:DH combustion")
    print("4:Limiting reagent DH")
    print("5:Multi-step q,w,DE,DH")
    print("6:DHfus from ice+water")
    print("7:Phase change process")
    print("8:% of max work")
    print("0:Back")
    return int(input("Choice:"))

def q_mcdT():
    print("q=m*c*DT")
    t = int(input("1:find q 2:find DT 3:find m:"))
    if t == 1:
        m = float(input("mass g:"))
        c = float(input("sp heat J/gK:"))
        T1 = float(input("T1 C:"))
        T2 = float(input("T2 C:"))
        q = m*c*(T2-T1)
        print("q=" + str(round(q,2)) + "J")
        print(" =" + str(round(q/1000,4)) + "kJ")
    elif t == 2:
        q = float(input("q J:"))
        m = float(input("mass g:"))
        c = float(input("sp heat J/gK:"))
        dT = q/(m*c)
        print("DT=" + str(round(dT,4)) + "C")
    else:
        q = float(input("q J:"))
        c = float(input("sp heat J/gK:"))
        dT = float(input("DT C:"))
        m = q/(c*dT)
        print("m=" + str(round(m,4)) + "g")
    pause()

def final_temp():
    print("Final temp of mix")
    print("(up to 4 substances)")
    print("Enter 0 for mass when done")
    num = 0.0
    den = 0.0
    i = 1
    running2 = True
    while i <= 4 and running2:
        m = float(input("mass" + str(i) + " g:"))
        if m == 0:
            running2 = False
        else:
            c = float(input("sp heat J/gK:"))
            T = float(input("Temp C:"))
            num = num + m*c*T
            den = den + m*c
            i = i + 1
    if den > 0:
        print("Tf=" + str(round(num/den,4)) + "C")
    pause()

def dH_combustion():
    print("DH from calorimetry")
    Ccal = float(input("Ccal J/K (or J/C):"))
    dT = float(input("DeltaT C:"))
    mol = float(input("moles burned:"))
    q_cal = Ccal * dT
    dH = -q_cal / mol / 1000
    print("q_cal=" + str(round(q_cal,2)) + "J")
    print("DH=" + str(round(dH,4)) + "kJ/mol")
    pause()

# ======= HESS =======

def hess():
    print("--HESS LAW--")
    print("neg mult = reverse rxn")
    n = int(input("Num reactions:"))
    total = 0.0
    i = 1
    while i <= n:
        dh = float(input("DH" + str(i) + " kJ:"))
        m = float(input("mult" + str(i) + ":"))
        total = total + dh * m
        i = i + 1
    print("DeltaH=" + str(round(total,4)) + "kJ")
    pause()

# ======= NEW THERMO =======

def dG_nonstandard():
    print("DeltaG=DG0+RT*ln(Q)")
    dG0 = float(input("DeltaG0 kJ/mol:"))
    T_C = float(input("Temp C:"))
    T = T_C + 273.15
    print("Enter Q (reaction quotient)")
    print("For gases use partial P")
    Q = float(input("Q:"))
    R = 8.314
    dG = dG0 + R*T*math.log(Q)/1000
    print("DeltaG=" + str(round(dG,4)) + "kJ/mol")
    if dG < 0:
        print("Spontaneous (forward)")
    elif dG > 0:
        print("Spontaneous (reverse)")
    else:
        print("At equilibrium")
    pause()

def dHvap_from_dS():
    print("A(l,T1)->A(g,T2) const P")
    print("DS_total = DS_heat_liq")
    print("  + DS_vap + DS_heat_gas")
    print("DS_vap = DH_vap/T_bp")
    dS_total = float(input("Total DS J/K/mol:"))
    T1_C = float(input("Initial T liq C:"))
    Tbp_C = float(input("Boiling pt C:"))
    T2_C = float(input("Final T gas C:"))
    Cp_l = float(input("Cp liquid J/mol/K:"))
    Cp_g = float(input("Cp gas J/mol/K:"))
    T1 = T1_C + 273.15
    Tbp = Tbp_C + 273.15
    T2 = T2_C + 273.15
    dS_liq = Cp_l * math.log(Tbp/T1)
    dS_gas = Cp_g * math.log(T2/Tbp)
    dS_vap = dS_total - dS_liq - dS_gas
    dH_vap = dS_vap * Tbp / 1000
    print("DS_liq=" + str(round(dS_liq,4)) + "J/K/mol")
    print("DS_gas=" + str(round(dS_gas,4)) + "J/K/mol")
    print("DS_vap=" + str(round(dS_vap,4)) + "J/K/mol")
    print("DHvap=" + str(round(dH_vap,4)) + "kJ/mol")
    pause()

# ======= NEW EQUILIBRIUM =======

def ice_pressure():
    print("ICE with pressures")
    print("aA+bB->cC+dD")
    print("(use 0 if no species)")
    K = float(input("Kp value:"))
    a = float(input("coeff A (rct):"))
    A0 = float(input("P_A initial atm:"))
    b = float(input("coeff B (rct):"))
    B0 = float(input("P_B initial atm:"))
    c = float(input("coeff C (prod):"))
    C0 = float(input("P_C initial atm:"))
    d = float(input("coeff D (prod):"))
    D0 = float(input("P_D initial atm:"))
    lo = 0.0
    hi = 0.9999
    if a > 0 and A0 > 0:
        hi = min(hi, A0/a*0.9999)
    if b > 0 and B0 > 0:
        hi = min(hi, B0/b*0.9999)
    for i in range(100):
        mid = (lo+hi)/2.0
        Ae = A0 - a*mid
        Be = B0 - b*mid
        Ce = C0 + c*mid
        De = D0 + d*mid
        num = 1.0
        den = 1.0
        if c > 0: num = num * Ce**c
        if d > 0: num = num * De**d
        if a > 0 and Ae > 0: den = den * Ae**a
        if b > 0 and Be > 0: den = den * Be**b
        Q = num/den
        if Q < K: lo = mid
        else: hi = mid
    x = (lo+hi)/2.0
    print("x=" + str(x) + " atm")
    print("P_A=" + str(A0-a*x))
    print("P_B=" + str(B0-b*x))
    print("P_C=" + str(C0+c*x))
    print("P_D=" + str(D0+d*x))
    pause()

def combine_K():
    print("Combine K values")
    print("K_target=K1^m1 * K2^m2...")
    print("(neg mult = reverse rxn)")
    print("(frac mult = e.g. 0.5)")
    n = int(input("Num reactions:"))
    K_total = 1.0
    i = 1
    while i <= n:
        K = float(input("K" + str(i) + ":"))
        m = float(input("mult" + str(i) + ":"))
        K_total = K_total * K**m
        i = i + 1
    print("K_combined=" + str(K_total))
    pause()

def calc_K_from_eq():
    print("Calc K from eq conc/P")
    print("aA+bB->cC+dD")
    a = float(input("coeff A:"))
    Ae = float(input("[A] or P_A eq:"))
    b = float(input("coeff B:"))
    Be = float(input("[B] or P_B eq:"))
    c = float(input("coeff C:"))
    Ce = float(input("[C] or P_C eq:"))
    d = float(input("coeff D:"))
    De = float(input("[D] or P_D eq:"))
    num = 1.0
    den = 1.0
    if c > 0: num = num * Ce**c
    if d > 0: num = num * De**d
    if a > 0: den = den * Ae**a
    if b > 0: den = den * Be**b
    K = num/den
    print("K=" + str(K))
    pause()

# ======= NEW ACIDS & BASES =======

def titration_any_point():
    print("Titration pH any point")
    print("Weak acid + strong base")
    print("OR weak base + strong acid")
    t = int(input("1:WkAcid+StrBase 2:WkBase+StrAcid:"))
    if t == 1:
        Ka = float(input("Ka weak acid:"))
        Ca = float(input("[acid] M:"))
        Va = float(input("Vol acid mL:"))
        Cb = float(input("[base] M:"))
        Vb = float(input("Vol base added mL:"))
        pKa = -math.log10(Ka)
        mol_a = Ca * Va
        mol_b = Cb * Vb
        Vb_eq = mol_a / Cb
        if Vb == 0:
            # before any base: weak acid
            x = (-Ka + math.sqrt(Ka**2 + 4*Ka*(Ca)))/2
            pH = -math.log10(x)
            print("pH=" + str(round(pH,4)))
        elif mol_b < mol_a:
            # buffer region
            mol_ha = mol_a - mol_b
            mol_conj = mol_b
            pH = pKa + math.log10(mol_conj/mol_ha)
            print("Buffer region")
            print("pH=" + str(round(pH,4)))
        elif abs(mol_b - mol_a) < 1e-9:
            # equivalence point
            Vtot = (Va + Vb)/1000
            Cs = mol_a/1000/Vtot
            Kb = 1e-14/Ka
            OH = math.sqrt(Kb*Cs)
            pH = 14 + math.log10(OH)
            print("Equiv point")
            print("pH=" + str(round(pH,4)))
        else:
            # past equivalence: excess base
            mol_excess = mol_b - mol_a
            Vtot = (Va + Vb)/1000
            OH = mol_excess/1000/Vtot
            pH = 14 + math.log10(OH)
            print("Past equiv pt")
            print("pH=" + str(round(pH,4)))
    else:
        Kb = float(input("Kb weak base:"))
        Cb = float(input("[base] M:"))
        Vb = float(input("Vol base mL:"))
        Ca = float(input("[acid] M:"))
        Va = float(input("Vol acid added mL:"))
        pKb = -math.log10(Kb)
        Ka = 1e-14/Kb
        pKa = -math.log10(Ka)
        mol_b = Cb * Vb
        mol_a = Ca * Va
        if Va == 0:
            x = (-Kb + math.sqrt(Kb**2 + 4*Kb*Cb))/2
            pOH = -math.log10(x)
            pH = 14 - pOH
            print("pH=" + str(round(pH,4)))
        elif mol_a < mol_b:
            mol_brem = mol_b - mol_a
            mol_conj = mol_a
            pOH = pKb + math.log10(mol_conj/mol_brem)
            pH = 14 - pOH
            print("Buffer region")
            print("pH=" + str(round(pH,4)))
        elif abs(mol_a - mol_b) < 1e-9:
            Vtot = (Vb + Va)/1000
            Cs = mol_b/1000/Vtot
            H = math.sqrt(Ka*Cs)
            pH = -math.log10(H)
            print("Equiv point")
            print("pH=" + str(round(pH,4)))
        else:
            mol_excess = mol_a - mol_b
            Vtot = (Vb + Va)/1000
            H = mol_excess/1000/Vtot
            pH = -math.log10(H)
            print("Past equiv pt")
            print("pH=" + str(round(pH,4)))
    pause()

def pct_dissoc_pH():
    print("% dissociation -> pH")
    C = float(input("[acid] or [base] M:"))
    pct = float(input("% dissociated:"))
    x = C * pct / 100
    t = int(input("1:acid 2:base:"))
    if t == 1:
        pH = -math.log10(x)
        Ka = x**2/(C-x)
        print("[H+]=" + str(round(x,8)))
        print("pH=" + str(round(pH,4)))
        print("Ka=" + str(round(Ka,8)))
    else:
        pOH = -math.log10(x)
        pH = 14 - pOH
        Kb = x**2/(C-x)
        print("[OH-]=" + str(round(x,8)))
        print("pH=" + str(round(pH,4)))
        print("Kb=" + str(round(Kb,8)))
    pause()

def pH_polyprotic_base():
    print("pH polyprotic strong base")
    print("e.g. Ba(OH)2 -> 2 OH-")
    C = float(input("Molarity M:"))
    n = float(input("OH- per formula unit:"))
    OH = C * n
    pOH = -math.log10(OH)
    pH = 14 - pOH
    print("[OH-]=" + str(round(OH,6)) + "M")
    print("pOH=" + str(round(pOH,4)))
    print("pH=" + str(round(pH,4)))
    pause()

def pH_dilute_strong_acid():
    print("pH dilute strong acid")
    print("Accounts for water autoion")
    print("when [H+] near 1e-7")
    C = float(input("[acid] M:"))
    # [H+]^2 - C*[H+] - Kw = 0
    Kw = 1e-14
    H = (C + math.sqrt(C**2 + 4*Kw))/2
    pH = -math.log10(H)
    print("[H+]=" + str(H))
    print("pH=" + str(round(pH,4)))
    pause()

def buffer_mix_two():
    print("Buffer from mixing 2 solns")
    print("Soln1: weak acid HA")
    print("Soln2: conjugate base A-")
    print("(or enter same Ka)")
    Ka = float(input("Ka of weak acid:"))
    pKa = -math.log10(Ka)
    C1 = float(input("[HA] soln1 M:"))
    V1 = float(input("Vol soln1 mL:"))
    C2 = float(input("[A-] soln2 M:"))
    V2 = float(input("Vol soln2 mL:"))
    mol_HA = C1 * V1
    mol_A = C2 * V2
    Vtot = V1 + V2
    pH = pKa + math.log10(mol_A/mol_HA)
    conc_HA = mol_HA/Vtot
    conc_A = mol_A/Vtot
    print("pKa=" + str(round(pKa,4)))
    print("[HA]=" + str(round(conc_HA,4)) + "M")
    print("[A-]=" + str(round(conc_A,4)) + "M")
    print("pH=" + str(round(pH,4)))
    pause()

def solubility_fixed_pH():
    print("Solubility at fixed pH")
    print("M(OH)n -> M^n+ + n OH-")
    Ksp = float(input("Ksp:"))
    n = float(input("n (OH- per formula):"))
    pH = float(input("pH of solution:"))
    OH = 10**(pH - 14)
    # Ksp = s * OH^n  where OH fixed by buffer
    s = Ksp / (OH**n)
    print("[OH-]=" + str(OH))
    print("s=" + str(s) + "mol/L")
    pause()

# ======= NEW ELECTROCHEMISTRY =======

def concentration_cell():
    print("Concentration cell")
    print("Both electrodes same metal")
    print("E=-(RT/nF)*ln(Q)")
    print("Q=[anode]/[cathode]")
    E_red = float(input("E0 reduction V:"))
    n = float(input("n mol e-:"))
    C_cat = float(input("[cathode] M:"))
    C_an = float(input("[anode] M:"))
    T_C = float(input("Temp C:"))
    T = T_C + 273.15
    R = 8.314; F = 96485
    Q = C_an/C_cat
    E = -(R*T/(n*F))*math.log(Q)
    print("Q=" + str(round(Q,6)))
    print("Ecell=" + str(round(E,6)) + "V")
    pause()

def molar_mass_electrolysis():
    print("Find molar mass by electrolysis")
    print("MCln -> M (n e- per ion)")
    I = float(input("Current A:"))
    t_hr = float(input("Time hours:"))
    n_e = float(input("e- per ion:"))
    mass = float(input("Mass deposited g:"))
    F = 96485
    t_s = t_hr * 3600
    mol_e = I * t_s / F
    mol_m = mol_e / n_e
    MM = mass / mol_m
    print("mol e-=" + str(round(mol_e,6)))
    print("mol metal=" + str(round(mol_m,6)))
    print("Molar mass=" + str(round(MM,2)) + "g/mol")
    pause()

# ======= NEW CALORIMETRY =======

def limiting_reagent_dH():
    print("DH with limiting reagent")
    print("Enter DH per mol rxn")
    print("and moles of each reactant")
    dH = float(input("DH kJ per mol rxn:"))
    n = int(input("Num reactants:"))
    ratios = []
    i = 0
    while i < n:
        mol = float(input("mol reactant" + str(i+1) + ":"))
        coeff = float(input("coeff in rxn:"))
        ratios.append(mol/coeff)
        i = i + 1
    lim = ratios[0]
    j = 1
    while j < len(ratios):
        if ratios[j] < lim:
            lim = ratios[j]
        j = j + 1
    dH_total = dH * lim
    print("Limiting mol rxn=" + str(round(lim,6)))
    print("DeltaH=" + str(round(dH_total,4)) + "kJ")
    pause()

def multistep_thermo():
    print("Multi-step q,w,DE,DH")
    print("Const pressure process")
    print("Each step: P,V1->V2")
    n_steps = int(input("Num steps:"))
    q_tot = 0.0
    w_tot = 0.0
    i = 1
    while i <= n_steps:
        print("Step " + str(i))
        P = float(input("P atm:"))
        V1 = float(input("V1 L:"))
        V2 = float(input("V2 L:"))
        q = float(input("q for step J:"))
        w = -P*(V2-V1)*101.325
        print("w" + str(i) + "=" + str(round(w,2)) + "J")
        q_tot = q_tot + q
        w_tot = w_tot + w
        i = i + 1
    dE = q_tot + w_tot
    # DH = DE + D(PV) = DE + P_final*V_final - P_init*V_init
    # For const P: DH = q_p (total heat at const P)
    print("q_total=" + str(round(q_tot,2)) + "J")
    print("w_total=" + str(round(w_tot,2)) + "J")
    print("DeltaE=" + str(round(dE,2)) + "J")
    print("DeltaH=q at const P")
    print("Enter P_i*V_i and P_f*V_f")
    PV_i = float(input("P_init*V_init L*atm:"))
    PV_f = float(input("P_final*V_final L*atm:"))
    dPV = (PV_f - PV_i)*101.325
    dH = dE + dPV
    print("DeltaH=" + str(round(dH,2)) + "J")
    pause()

def dH_fus_ice():
    print("DHfus from ice+water")
    print("Ice(0C) + Water -> mix")
    m_ice = float(input("Mass ice g:"))
    m_wat = float(input("Mass water g:"))
    T_wat = float(input("Water init temp C:"))
    T_f = float(input("Final temp C:"))
    Cp = 4.18
    # heat lost by water = heat gained by ice melting + ice warming
    q_water = m_wat * Cp * (T_wat - T_f)
    q_warm_ice = m_ice * Cp * T_f
    q_fus = q_water - q_warm_ice
    MM_water = 18.015
    mol_ice = m_ice / MM_water
    dH_fus = q_fus / mol_ice / 1000
    print("q_water=" + str(round(q_water,2)) + "J")
    print("q_warm_ice=" + str(round(q_warm_ice,2)) + "J")
    print("q_fus=" + str(round(q_fus,2)) + "J")
    print("mol ice=" + str(round(mol_ice,4)))
    print("DHfus=" + str(round(dH_fus,4)) + "kJ/mol")
    pause()

# ======= NEW THERMO (MT3) =======

def dG_at_new_T():
    print("DG at non-std T")
    print("Uses DG=DH_rxn - T*DS_rxn")
    print("Assumes DH,DS indep of T")
    dH = float(input("DH_rxn kJ/mol:"))
    dS = float(input("DS_rxn J/mol/K:"))
    T_C = float(input("Temp C:"))
    T = T_C + 273.15
    dG = dH - T*(dS/1000)
    print("T(K)=" + str(round(T,2)))
    print("DG=" + str(round(dG,2)) + "kJ/mol")
    if dG < 0:
        print("Spontaneous")
    else:
        print("Non-spontaneous")
    pause()

def dH_dS_from_tables():
    print("DH_rxn & DS_rxn from tables")
    print("DH=sum(n*DHf_prod)-sum(n*DHf_rct)")
    print("DS=sum(n*S_prod)-sum(n*S_rct)")
    np2 = int(input("Num products:"))
    sum_dH_p = 0.0
    sum_dS_p = 0.0
    i = 0
    while i < np2:
        c = float(input("coeff prod" + str(i+1) + ":"))
        dh = float(input("DHf prod" + str(i+1) + " kJ/mol:"))
        s = float(input("S prod" + str(i+1) + " J/mol/K:"))
        sum_dH_p = sum_dH_p + c*dh
        sum_dS_p = sum_dS_p + c*s
        i = i + 1
    nr2 = int(input("Num reactants:"))
    sum_dH_r = 0.0
    sum_dS_r = 0.0
    i = 0
    while i < nr2:
        c = float(input("coeff rct" + str(i+1) + ":"))
        dh = float(input("DHf rct" + str(i+1) + " kJ/mol:"))
        s = float(input("S rct" + str(i+1) + " J/mol/K:"))
        sum_dH_r = sum_dH_r + c*dh
        sum_dS_r = sum_dS_r + c*s
        i = i + 1
    dH_rxn = sum_dH_p - sum_dH_r
    dS_rxn = sum_dS_p - sum_dS_r
    print("DH_rxn=" + str(round(dH_rxn,4)) + "kJ/mol")
    print("DS_rxn=" + str(round(dS_rxn,4)) + "J/mol/K")
    print("-- Now calc DG at T --")
    T_C = float(input("Temp C (25 for std):"))
    T = T_C + 273.15
    dG = dH_rxn - T*(dS_rxn/1000)
    print("DG=" + str(round(dG,2)) + "kJ/mol")
    pause()

def Q_vs_K():
    print("Q vs K -> rxn direction")
    print("aA+bB->cC+dD")
    print("(pressures OR conc)")
    K = float(input("K value:"))
    a = float(input("coeff A:"))
    Ac = float(input("[A] or P_A:"))
    b = float(input("coeff B:"))
    Bc = float(input("[B] or P_B:"))
    c = float(input("coeff C:"))
    Cc = float(input("[C] or P_C:"))
    d = float(input("coeff D:"))
    Dc = float(input("[D] or P_D:"))
    num = 1.0
    den = 1.0
    if c > 0: num = num * Cc**c
    if d > 0: num = num * Dc**d
    if a > 0: den = den * Ac**a
    if b > 0: den = den * Bc**b
    Q = num/den
    print("Q=" + str(Q))
    print("K=" + str(K))
    if Q < K:
        print("Q<K: forward rxn")
        print("Products increase")
    elif Q > K:
        print("Q>K: reverse rxn")
        print("Reactants increase")
    else:
        print("Q=K: at equilibrium")
    pause()

# ======= NEW ELECTROCHEMISTRY (MT3) =======

def ion_charge_electrolysis():
    print("Find ion charge from electrolysis")
    I = float(input("Current A:"))
    t_min = float(input("Time minutes:"))
    mass = float(input("Mass deposited g:"))
    MM = float(input("Molar mass g/mol:"))
    F = 96485
    t_s = t_min * 60
    mol_e = I * t_s / F
    mol_m = mass / MM
    n = mol_e / mol_m
    print("mol e-=" + str(round(mol_e,4)))
    print("mol metal=" + str(round(mol_m,4)))
    print("charge=" + str(round(n,1)) + "+")
    pause()

def dG_K_E_interconvert():
    print("DG, K, E interconvert")
    print("DG=-nFE=-RT*ln(K)")
    n = float(input("n mol e-:"))
    T_C = float(input("Temp C:"))
    T = T_C + 273.15
    R = 8.314; F = 96485
    print("Enter ONE known value:")
    print("1:DG(kJ) 2:K 3:E(V)")
    ch = int(input("Which:"))
    if ch == 1:
        dG = float(input("DG kJ/mol:")) * 1000
        E = -dG/(n*F)
        K = math.exp(-dG/(R*T))
        print("E=" + str(round(E,4)) + "V")
        print("K=" + str(K))
    elif ch == 2:
        K = float(input("K:"))
        dG = -R*T*math.log(K)
        E = -dG/(n*F)
        print("DG=" + str(round(dG/1000,4)) + "kJ/mol")
        print("E=" + str(round(E,4)) + "V")
    else:
        E = float(input("E V:"))
        dG = -n*F*E
        K = math.exp(-dG/(R*T))
        print("DG=" + str(round(dG/1000,4)) + "kJ/mol")
        print("K=" + str(K))
    pause()

# ======= NEW CALORIMETRY (MT3) =======

def phase_change_process():
    print("Phase change process")
    print("Heating + phase transitions")
    print("at const pressure")
    print("(liquid->vapor only or")
    print(" solid->liq->vapor)")
    n = float(input("moles:"))
    T1_C = float(input("Initial T C:"))
    T2_C = float(input("Final T C:"))
    print("Does process include:")
    has_fus = int(input("Melting? 1:yes 0:no:"))
    has_vap = int(input("Vaporization? 1:yes 0:no:"))

    q_total = 0.0
    dS_total = 0.0

    if has_fus:
        Tfus_C = float(input("Melting pt C:"))
        Cp_s = float(input("Cp solid J/mol/K:"))
        DHfus = float(input("DHfus kJ/mol:")) * 1000
        Tfus = Tfus_C + 273.15
        # heat solid to melting pt
        dH1 = n * Cp_s * (Tfus - (T1_C+273.15))
        dS1 = n * Cp_s * math.log(Tfus/(T1_C+273.15))
        # melt
        dH2 = n * DHfus
        dS2 = n * DHfus / Tfus
        q_total = q_total + dH1 + dH2
        dS_total = dS_total + dS1 + dS2
        T_after_fus = Tfus_C
    else:
        T_after_fus = T1_C

    if has_vap:
        Tvap_C = float(input("Boiling pt C:"))
        Cp_l = float(input("Cp liquid J/mol/K:"))
        DHvap = float(input("DHvap kJ/mol:")) * 1000
        Cp_g = float(input("Cp gas J/mol/K:"))
        Tvap = Tvap_C + 273.15
        T_start_l = T_after_fus + 273.15
        # heat liquid to boiling
        if Tvap > T_start_l:
            dH3 = n * Cp_l * (Tvap - T_start_l)
            dS3 = n * Cp_l * math.log(Tvap/T_start_l)
        else:
            dH3 = 0.0; dS3 = 0.0
        # vaporize
        dH4 = n * DHvap
        dS4 = n * DHvap / Tvap
        # heat gas to final T
        T2 = T2_C + 273.15
        if T2 > Tvap:
            dH5 = n * Cp_g * (T2 - Tvap)
            dS5 = n * Cp_g * math.log(T2/Tvap)
        else:
            dH5 = 0.0; dS5 = 0.0
        q_total = q_total + dH3 + dH4 + dH5
        dS_total = dS_total + dS3 + dS4 + dS5
    else:
        # just heating liquid (or solid)
        Cp_l = float(input("Cp J/mol/K:"))
        T_s = T_after_fus + 273.15
        T2 = T2_C + 273.15
        dH3 = n * Cp_l * (T2 - T_s)
        dS3 = n * Cp_l * math.log(T2/T_s)
        q_total = q_total + dH3
        dS_total = dS_total + dS3

    # DH = q at const P
    dH_total = q_total
    # w = -P*DV; only gas expansion matters
    # At end, if gas present: DV ~ V_gas_final (liquid vol negligible)
    if has_vap:
        R = 8.314
        T2 = T2_C + 273.15
        # ideal gas: V = nRT/P, P=1atm=101325 Pa
        V_gas = n * R * T2 / 101325
        w = -101325 * V_gas  # J
    else:
        w = 0.0
    dE = dH_total + w

    print("q=DH=" + str(round(q_total/1000,2)) + "kJ")
    print("w=" + str(round(w/1000,3)) + "kJ")
    print("DE=" + str(round(dE/1000,2)) + "kJ")
    print("DS=" + str(round(dS_total,2)) + "J/K")
    pause()

def pct_max_work():
    print("% of max work (isothermal)")
    print("w_max=nRT*ln(V2/V1)")
    print("     =nRT*ln(P1/P2)")
    n = float(input("moles:"))
    T_C = float(input("Temp C:"))
    T = T_C + 273.15
    R = 8.314
    ch = int(input("1:use Vol 2:use P:"))
    if ch == 1:
        V1 = float(input("V1 L:"))
        V2 = float(input("V2 L:"))
        w_max = n * R * T * math.log(V2/V1)
    else:
        P1 = float(input("P1 atm:"))
        P2 = float(input("P2 atm:"))
        w_max = n * R * T * math.log(P1/P2)
    w_actual = float(input("Actual work done kJ:")) * 1000
    pct = w_actual / w_max * 100
    print("w_max=" + str(round(w_max/1000,4)) + "kJ")
    print("w_act=" + str(round(w_actual/1000,4)) + "kJ")
    print("% max=" + str(round(pct,1)) + "%")
    pause()

# ======= MAIN =======

running = True
while running:
    ch = menu()
    if ch == 0:
        running = False
    elif ch == 1:
        sub = menu_thermo()
        if sub == 1: dG_dH_dS()
        elif sub == 2: dG_from_K()
        elif sub == 3: dG_rxn()
        elif sub == 4: dH_from_dE()
        elif sub == 5: dS_isothermal()
        elif sub == 6: dS_Cp()
        elif sub == 7: dG_nonstandard()
        elif sub == 8: dHvap_from_dS()
        elif sub == 9: dG_at_new_T()
        elif sub == 10: dH_dS_from_tables()
        elif sub == 11: Q_vs_K()
    elif ch == 2:
        sub = menu_equil()
        if sub == 1: kc_kp(1)
        elif sub == 2: kc_kp(2)
        elif sub == 3: ice_table()
        elif sub == 4: ice_pressure()
        elif sub == 5: combine_K()
        elif sub == 6: calc_K_from_eq()
        elif sub == 7: dG_to_K()
        elif sub == 8: K_new_T()
    elif ch == 3:
        sub = menu_acid()
        if sub == 1: pH_strong()
        elif sub == 2: pH_weak_acid()
        elif sub == 3: pH_weak_base()
        elif sub == 4: Ka_pH()
        elif sub == 5: Kb_pH()
        elif sub == 6: Ka_Kb_conv()
        elif sub == 7: henderson()
        elif sub == 8: titration_eq()
        elif sub == 9: titration_any_point()
        elif sub == 10: pct_dissoc_pH()
        elif sub == 11: pH_polyprotic_base()
        elif sub == 12: pH_dilute_strong_acid()
        elif sub == 13: buffer_mix_two()
        elif sub == 14: solubility_fixed_pH()
    elif ch == 4:
        sub = menu_electro()
        if sub == 1: ecell()
        elif sub == 2: dG_ecell()
        elif sub == 3: nernst()
        elif sub == 4: concentration_cell()
        elif sub == 5: electrolysis(1)
        elif sub == 6: electrolysis(2)
        elif sub == 7: electrolysis(3)
        elif sub == 8: molar_mass_electrolysis()
        elif sub == 9: ion_charge_electrolysis()
        elif sub == 10: dG_K_E_interconvert()
    elif ch == 5:
        sub = menu_gas()
        if sub == 1: ideal_gas()
        elif sub == 2: work_PDV()
        elif sub == 3: work_Dn()
        elif sub == 4: dE_qw()
        elif sub == 5: dH_gas()
        elif sub == 6: graham()
    elif ch == 6:
        sub = menu_sol()
        if sub == 1: ksp_to_s()
        elif sub == 2: common_ion()
        elif sub == 3: s_to_ksp()
        elif sub == 4: simultaneous_equil()
    elif ch == 7:
        sub = menu_cal()
        if sub == 1: q_mcdT()
        elif sub == 2: final_temp()
        elif sub == 3: dH_combustion()
        elif sub == 4: limiting_reagent_dH()
        elif sub == 5: multistep_thermo()
        elif sub == 6: dH_fus_ice()
        elif sub == 7: phase_change_process()
        elif sub == 8: pct_max_work()
    elif ch == 8:
        hess()
    else:
        print("Invalid")
