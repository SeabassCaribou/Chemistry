import math
def p():
	input('--OK--')
def qmcdt():
	c=int(input('1:q 2:DT 3:m:'))
	if c==1:
		m=float(input('mass g:'))
		cp=float(input('sp heat J/gK:'))
		T1=float(input('T1 C:'))
		T2=float(input('T2 C:'))
		q=m*cp*(T2-T1)
		print('q='+str(round(q,2))+'J='+str(round(q/1000,4))+'kJ')
	elif c==2:
		q=float(input('q J:'))
		m=float(input('mass g:'))
		cp=float(input('sp heat:'))
		print('DT='+str(round(q/(m*cp),4))+'C')
	else:
		q=float(input('q J:'))
		cp=float(input('sp heat:'))
		Dt=float(input('DT C:'))
		print('m='+str(round(q/(cp*Dt),4))+'g')
	p()
def ftmp():
	print('Final temp mix')
	print('Enter 0 mass when done')
	N=0.0; D=0.0
	for i in range(4):
		m=float(input('mass g:'))
		if m==0: break
		cp=float(input('sp heat:'))
		T=float(input('temp C:'))
		N=N+m*cp*T; D=D+m*cp
	print('Tf='+str(round(N/D,4))+'C')
	p()
def hss():
	print('Hess Law')
	print('neg mult=reverse')
	n=int(input('Num rxns:'))
	T=0.0
	for i in range(n):
		H=float(input('DH kJ:'))
		M=float(input('mult:'))
		T=T+H*M
	print('DH='+str(round(T,4))+'kJ')
	p()
def comb():
	C=float(input('Ccal J/K:'))
	D=float(input('DeltaT C:'))
	N=float(input('moles:'))
	q=C*D
	print('DH='+str(round(-q/N/1000,4))+'kJ/mol')
	p()
def limrg():
	H=float(input('DH kJ/mol rxn:'))
	n=int(input('Num reactants:'))
	L=1e9
	for i in range(n):
		m=float(input('mol reactant:'))
		c=float(input('coeff:'))
		if m/c<L: L=m/c
	print('DH='+str(round(H*L,4))+'kJ')
	p()
def phch():
	print('Phase change liq->gas')
	n=float(input('moles:'))
	T1=float(input('init T C:'))+273.15
	T2=float(input('final T C:'))+273.15
	Tv=float(input('boiling pt C:'))+273.15
	Cl=float(input('Cp liq J/mol/K:'))
	Hv=float(input('DHvap kJ/mol:'))*1000
	Cg=float(input('Cp gas J/mol/K:'))
	q1=n*Cl*(Tv-T1); s1=n*Cl*math.log(Tv/T1)
	q2=n*Hv; s2=n*Hv/Tv
	q3=n*Cg*(T2-Tv); s3=n*Cg*math.log(T2/Tv)
	q=q1+q2+q3; s=s1+s2+s3
	w=-101325*(n*8.314*T2/101325)
	print('q=DH='+str(round(q/1000,2))+'kJ')
	print('w='+str(round(w/1000,3))+'kJ')
	print('DE='+str(round((q+w)/1000,2))+'kJ')
	print('DS='+str(round(s,2))+'J/K')
	p()
def ice():
	print('Ice+water DHfus')
	mi=float(input('mass ice g:'))
	mw=float(input('mass water g:'))
	Tw=float(input('water init T C:'))
	Tf=float(input('final T C:'))
	qw=mw*4.18*(Tw-Tf)
	qi=mi*4.18*Tf
	print('DHfus='+str(round((qw-qi)/(mi/18.015)/1000,4))+'kJ/mol')
	p()
r=True
while r:
	print('=CALORIMETRY & HESS=')
	print('1:q=mcDT')
	print('2:Final temp')
	print('3:Hess Law')
	print('4:DH combustion')
	print('5:Limiting reagent')
	print('6:Phase change')
	print('7:DHfus ice+water')
	print('0:Quit')
	c=int(input('Choice:'))
	if c==0: r=False
	elif c==1: qmcdt()
	elif c==2: ftmp()
	elif c==3: hss()
	elif c==4: comb()
	elif c==5: limrg()
	elif c==6: phch()
	elif c==7: ice()
	else: print('Invalid')
