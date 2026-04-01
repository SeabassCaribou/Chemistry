#Equilibrium
#Python program designed to solve Chemical Equilibrium problems that will fit on a TI-84 plus CE Python
import math
def p():
	input('--OK--')
def kckp(d):
	if d==1: print('Kp=Kc*(RT)^Dn')
	else: print('Kc=Kp/(RT)^Dn')
	K=float(input('K:'))
	T=float(input('Temp C:'))
	N=float(input('Dn prod-rct:'))
	T=T+273.15
	R=0.08206*T
	if d==1: print('Kp='+str(K*R**N))
	else: print('Kc='+str(K/R**N))
	p()
def ice():
	print('ICE: aA+bB->cC+dD')
	print('(0 if no species)')
	K=float(input('K:'))
	a=float(input('coeff A:'))
	E=float(input('[A]0:'))
	b=float(input('coeff B:'))
	F=float(input('[B]0:'))
	c=float(input('coeff C:'))
	G=float(input('[C]0:'))
	d=float(input('coeff D:'))
	H=float(input('[D]0:'))
	lo=0.0
	hi=0.9999
	if a>0 and E>0: hi=min(hi,E/a*0.9999)
	if b>0 and F>0: hi=min(hi,F/b*0.9999)
	for i in range(100):
		m=(lo+hi)/2.0
		Ae=E-a*m; Be=F-b*m
		Ce=G+c*m; De=H+d*m
		nu=1.0; de=1.0
		if c>0: nu=nu*Ce**c
		if d>0: nu=nu*De**d
		if a>0 and Ae>0: de=de*Ae**a
		if b>0 and Be>0: de=de*Be**b
		Q=nu/de
		if Q<K: lo=m
		else: hi=m
	x=(lo+hi)/2.0
	print('x='+str(x))
	print('[A]='+str(E-a*x))
	print('[B]='+str(F-b*x))
	print('[C]='+str(G+c*x))
	print('[D]='+str(H+d*x))
	p()
def combk():
	print('K_tot=K1^m1*K2^m2')
	print('neg mult=reverse')
	n=int(input('Num rxns:'))
	K=1.0
	for i in range(n):
		a=float(input('K:'))
		b=float(input('mult:'))
		K=K*a**b
	print('K='+str(K))
	p()
def keq():
	print('K from eq conc/P')
	a=float(input('coeff A:')); Ae=float(input('[A]eq:'))
	b=float(input('coeff B:')); Be=float(input('[B]eq:'))
	c=float(input('coeff C:')); Ce=float(input('[C]eq:'))
	d=float(input('coeff D:')); De=float(input('[D]eq:'))
	nu=1.0; de=1.0
	if c>0: nu=nu*Ce**c
	if d>0: nu=nu*De**d
	if a>0: de=de*Ae**a
	if b>0: de=de*Be**b
	print('K='+str(nu/de))
	p()
def knt():
	print('K at new T')
	K1=float(input('K1:'))
	T1=float(input('T1 C:'))
	H=float(input('DH kJ/mol:'))
	T2=float(input('T2 C:'))
	T1=T1+273.15; T2=T2+273.15
	L=math.log(K1)-(H*1000/8.314)*(1/T2-1/T1)
	print('K2='+str(math.exp(L)))
	p()
def qvk():
	print('Q vs K')
	K=float(input('K:'))
	a=float(input('coeff A:')); Ac=float(input('[A]:'))
	b=float(input('coeff B:')); Bc=float(input('[B]:'))
	c=float(input('coeff C:')); Cc=float(input('[C]:'))
	d=float(input('coeff D:')); Dc=float(input('[D]:'))
	nu=1.0; de=1.0
	if c>0: nu=nu*Cc**c
	if d>0: nu=nu*Dc**d
	if a>0: de=de*Ac**a
	if b>0: de=de*Bc**b
	Q=nu/de
	print('Q='+str(Q))
	print('K='+str(K))
	if Q<K: print('Q<K: forward')
	elif Q>K: print('Q>K: reverse')
	else: print('Equilibrium')
	p()
r=True
while r:
	print('=EQUILIBRIUM=')
	print('1:Kc to Kp')
	print('2:Kp to Kc')
	print('3:ICE table')
	print('4:Combine K')
	print('5:K from eq conc')
	print('6:K at new temp')
	print('7:Q vs K')
	print('0:Quit')
	c=int(input('Choice:'))
	if c==0: r=False
	elif c==1: kckp(1)
	elif c==2: kckp(2)
	elif c==3: ice()
	elif c==4: combk()
	elif c==5: keq()
	elif c==6: knt()
	elif c==7: qvk()
	else: print('Invalid')
