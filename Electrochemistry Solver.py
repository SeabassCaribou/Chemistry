import math
def p():
	input('--OK--')
def ecl():
	ec=float(input('E cathode V:'))
	ea=float(input('E anode V:'))
	E=ec-ea
	print('Ecell='+str(round(E,4))+'V')
	if E>0: print('Spontaneous')
	else: print('Nonspontaneous')
	p()
def dge():
	n=float(input('n mol e-:'))
	E=float(input('Ecell V:'))
	G=-n*96485*E
	print('DG='+str(round(G/1000,4))+' kJ')
	p()
def nrnst():
	E0=float(input('E0 V:'))
	n=float(input('n mol e-:'))
	Q=float(input('Q:'))
	T=float(input('Temp C:'))+273.15
	E=E0-(8.314*T/(n*96485))*math.log(Q)
	print('E='+str(round(E,6))+'V')
	p()
def cc():
	print('Concentration cell')
	n=float(input('n mol e-:'))
	A=float(input('[cathode] M:'))
	B=float(input('[anode] M:'))
	T=float(input('Temp C:'))+273.15
	Q=B/A
	E=-(8.314*T/(n*96485))*math.log(Q)
	print('Ecell='+str(round(E,6))+'V')
	p()
def elys(mode):
	if mode==1:
		I=float(input('Current A:'))
		t=float(input('Time hr:'))
		ne=float(input('e- per ion:'))
		M=float(input('Molar mass:'))
		me=I*t*3600/96485
		print('mass='+str(round(me/ne*M,4))+'g')
	elif mode==2:
		m=float(input('Target mass g:'))
		t=float(input('Time hr:'))
		ne=float(input('e- per ion:'))
		M=float(input('Molar mass:'))
		me=(m/M)*ne
		print('I='+str(round(me*96485/(t*3600),4))+'A')
	elif mode==3:
		m=float(input('Target mass g:'))
		I=float(input('Current A:'))
		ne=float(input('e- per ion:'))
		M=float(input('Molar mass:'))
		me=(m/M)*ne
		ts=me*96485/I
		print('t='+str(round(ts,2))+'s='+str(round(ts/3600,4))+'hr')
	elif mode==4:
		m=float(input('Mass g:'))
		t=float(input('Time min:'))
		I=float(input('Current A:'))
		M=float(input('Molar mass:'))
		me=I*t*60/96485
		print('charge='+str(round(me/(m/M),1))+'+')
	elif mode==5:
		m=float(input('Mass g:'))
		t=float(input('Time hr:'))
		ne=float(input('e- per ion:'))
		M=float(input('Molar mass:'))
		me=I*t*3600/96485 if False else (m/M)*ne
		print('MM='+str(round(m/((float(input('I A:'))*t*3600/96485)/ne),2)))
	p()
def mmass():
	I=float(input('Current A:'))
	t=float(input('Time hr:'))
	ne=float(input('e- per ion:'))
	m=float(input('Mass g:'))
	me=I*t*3600/96485
	print('MM='+str(round(m/(me/ne),2))+' g/mol')
	p()
def dgke():
	n=float(input('n mol e-:'))
	T=float(input('Temp C:'))+273.15
	c=int(input('1:DG 2:K 3:E:'))
	if c==1:
		G=float(input('DG kJ:'))*1000
		print('E='+str(round(-G/(n*96485),4))+'V')
		print('K='+str(math.exp(-G/(8.314*T))))
	elif c==2:
		K=float(input('K:'))
		G=-8.314*T*math.log(K)
		print('DG='+str(round(G/1000,4))+'kJ')
		print('E='+str(round(-G/(n*96485),4))+'V')
	else:
		E=float(input('E V:'))
		G=-n*96485*E
		print('DG='+str(round(G/1000,4))+'kJ')
		print('K='+str(math.exp(-G/(8.314*T))))
	p()
r=True
while r:
	print('=ELECTROCHEMISTRY=')
	print('1:Ecell')
	print('2:DG from Ecell')
	print('3:Nernst')
	print('4:Conc cell')
	print('5:Mass deposited')
	print('6:Current needed')
	print('7:Time needed')
	print('8:Molar mass')
	print('9:Ion charge')
	print('10:DG,K,E convert')
	print('0:Quit')
	c=int(input('Choice:'))
	if c==0: r=False
	elif c==1: ecl()
	elif c==2: dge()
	elif c==3: nrnst()
	elif c==4: cc()
	elif c==5: elys(1)
	elif c==6: elys(2)
	elif c==7: elys(3)
	elif c==8: mmass()
	elif c==9: elys(4)
	elif c==10: dgke()
	else: print('Invalid')
