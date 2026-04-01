#Python program designed to solve Thermodynamics problems that will fit on a TI-84 plus CE Python
import math
def p():
	input('--OK--')
def dg():
	print('DG=DH-T*DS')
	H=float(input('DH kJ/mol:'))
	S=float(input('DS J/mol/K:'))
	T=float(input('Temp C:'))
	T=T+273.15
	G=H-T*(S/1000)
	print('T(K)='+str(round(T,2)))
	print('DG='+str(round(G,4))+' kJ/mol')
	if G<0: print('Spontaneous')
	if G>0: print('Nonspontaneous')
	p()
def dgk():
	print('DG=-RT*ln(K)')
	K=float(input('K:'))
	T=float(input('Temp C:'))
	T=T+273.15
	G=-8.314*T*math.log(K)/1000
	print('DG='+str(round(G,4))+' kJ/mol')
	p()
def dgnew():
	print('DG=DH-T*DS at new T')
	H=float(input('DH kJ/mol:'))
	S=float(input('DS J/mol/K:'))
	T=float(input('Temp C:'))
	T=T+273.15
	G=H-T*(S/1000)
	print('DG='+str(round(G,4))+' kJ/mol')
	if G<0: print('Spontaneous')
	if G>0: print('Nonspontaneous')
	p()
def dgns():
	print('DG=DG0+RT*ln(Q)')
	G=float(input('DG0 kJ/mol:'))
	T=float(input('Temp C:'))
	Q=float(input('Q:'))
	T=T+273.15
	G=G+8.314*T*math.log(Q)/1000
	print('DG='+str(round(G,4))+' kJ/mol')
	if G<0: print('Fwd spontaneous')
	if G>0: print('Rev spontaneous')
	p()
def ds():
	print('DS=nR*ln(V2/V1)')
	print('  =nR*ln(P1/P2)')
	c=int(input('1:Vol 2:Pres:'))
	n=float(input('Moles:'))
	if c==1:
		A=float(input('V1:'))
		B=float(input('V2:'))
		D=n*8.314*math.log(B/A)
	else:
		A=float(input('P1:'))
		B=float(input('P2:'))
		D=n*8.314*math.log(A/B)
	print('DS='+str(round(D,4))+' J/K')
	p()
r=True
while r:
	print('=THERMODYNAMICS=')
	print('1:DG=DH-TDS')
	print('2:DG from K')
	print('3:DG at new T')
	print('4:DG nonstandard')
	print('5:DS isothermal')
	print('0:Quit')
	c=int(input('Choice:'))
	if c==0: r=False
	elif c==1: dg()
	elif c==2: dgk()
	elif c==3: dgnew()
	elif c==4: dgns()
	elif c==5: ds()
	else: print('Invalid')