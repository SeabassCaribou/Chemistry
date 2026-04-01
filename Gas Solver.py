import math
def p():
	input('--OK--')
def ig():
	print('PV=nRT (0=unknown)')
	P=float(input('P atm:'))
	V=float(input('V L:'))
	N=float(input('n mol:'))
	T=float(input('T C:'))
	T=T+273.15
	R=0.08206
	if P==0: print('P='+str(round(N*R*T/V,4))+'atm')
	elif V==0: print('V='+str(round(N*R*T/P,4))+'L')
	elif N==0: print('n='+str(round(P*V/(R*T),6))+'mol')
	else: print('T='+str(round(P*V/(N*R),2))+'K')
	p()
def wk():
	c=int(input('1:w=-PDV 2:w=-DnRT:'))
	if c==1:
		P=float(input('P atm:'))
		A=float(input('V1 L:'))
		B=float(input('V2 L:'))
		w=-P*(B-A)*101.325
		print('w='+str(round(w,2))+'J')
	else:
		Dn=float(input('Dn gas:'))
		T=float(input('Temp C:'))+273.15
		w=-Dn*8.314*T
		print('w='+str(round(w,2))+'J')
	if w>0: print('Work ON system')
	else: print('Work BY system')
	p()
def grh():
	print('r1/r2=sqrt(M2/M1)')
	c=int(input('1:ratio 2:find M:'))
	if c==1:
		A=float(input('M1:'))
		B=float(input('M2:'))
		print('r1/r2='+str(round(math.sqrt(B/A),4)))
	else:
		M=float(input('Known M:'))
		R=float(input('r1/r2:'))
		print('M='+str(round(M*R**2,4)))
	p()
def sol():
	c=int(input('1:Ksp->s 2:CommonIon 3:s->Ksp 4:Simult:'))
	if c==1:
		K=float(input('Ksp:'))
		x=float(input('coeff cat:'))
		y=float(input('coeff an:'))
		print('s='+str((K/(x**x*y**y))**(1/(x+y))))
	elif c==2:
		K=float(input('Ksp:'))
		x=float(input('coeff cat:'))
		y=float(input('coeff an:'))
		t=int(input('1:cat 2:an shared:'))
		C=float(input('Common ion M:'))
		lo=0.0; hi=(K)**(1/(x+y))*10
		for i in range(100):
			m=(lo+hi)/2.0
			if t==2: Q=(x*m)**x*(y*m+C)**y
			else: Q=(x*m+C)**x*(y*m)**y
			if Q<K: lo=m
			else: hi=m
		print('s='+str((lo+hi)/2))
	elif c==3:
		s=float(input('s mol/L:'))
		x=float(input('coeff cat:'))
		y=float(input('coeff an:'))
		print('Ksp='+str((x*s)**x*(y*s)**y))
	else:
		print('Both 1:1 salts')
		A=float(input('Ksp1:'))
		B=float(input('Ksp2:'))
		R=A/B
		s2=math.sqrt(B/(R+1))
		s1=R*s2
		C=s1+s2
		print('s1='+str(s1))
		print('s2='+str(s2))
		print('shared='+str(C))
	p()
r=True
while r:
	print('=GASES & SOLUBILITY=')
	print('1:Ideal gas PV=nRT')
	print('2:Work')
	print('3:DE=q+w')
	print('4:DH=DE+DnRT')
	print('5:Graham effusion')
	print('6:Solubility')
	print('0:Quit')
	c=int(input('Choice:'))
	if c==0: r=False
	elif c==1: ig()
	elif c==2: wk()
	elif c==3:
		q=float(input('q J:'))
		w=float(input('w J:'))
		print('DE='+str(round(q+w,2))+'J')
		p()
	elif c==4:
		E=float(input('DE kJ:'))
		Dn=float(input('Dn gas:'))
		T=float(input('Temp C:'))+273.15
		print('DH='+str(round(E+Dn*8.314*T/1000,4))+'kJ')
		p()
	elif c==5: grh()
	elif c==6: sol()
	else: print('Invalid')
