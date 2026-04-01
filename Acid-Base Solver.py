import math
def p():
	input('--OK--')
def phs():
	print('Strong acid/base')
	t=int(input('1:acid 2:base:'))
	C=float(input('Conc M:'))
	if t==1:
		print('pH='+str(round(-math.log10(C),4)))
	else:
		pOH=-math.log10(C)
		print('pH='+str(round(14-pOH,4)))
	p()
def phwa():
	print('Weak acid HA')
	K=float(input('Ka:'))
	C=float(input('[HA] M:'))
	x=(-K+math.sqrt(K**2+4*K*C))/2
	pH=-math.log10(x)
	print('[H+]='+str(x))
	print('pH='+str(round(pH,4)))
	print('% diss='+str(round(x/C*100,2)))
	p()
def phwb():
	print('Weak base B')
	K=float(input('Kb:'))
	C=float(input('[B] M:'))
	x=(-K+math.sqrt(K**2+4*K*C))/2
	pOH=-math.log10(x)
	print('[OH-]='+str(x))
	print('pH='+str(round(14-pOH,4)))
	p()
def kapH():
	print('Ka from pH')
	C=float(input('[HA] M:'))
	pH=float(input('pH:'))
	H=10**(-pH)
	print('Ka='+str(H**2/(C-H)))
	p()
def kbpH():
	print('Kb from pH')
	C=float(input('[B] M:'))
	pH=float(input('pH:'))
	OH=10**(pH-14)
	print('Kb='+str(OH**2/(C-OH)))
	p()
def kakb():
	t=int(input('1:Ka->Kb 2:Kb->Ka:'))
	if t==1:
		K=float(input('Ka:'))
		print('Kb='+str(1e-14/K))
	else:
		K=float(input('Kb:'))
		print('Ka='+str(1e-14/K))
	p()
def hh():
	print('Henderson-Hasselbalch')
	t=int(input('1:pH 2:ratio 3:molHCl:'))
	K=float(input('Ka:'))
	pKa=-math.log10(K)
	if t==1:
		A=float(input('[A-]:'))
		H=float(input('[HA]:'))
		print('pH='+str(round(pKa+math.log10(A/H),4)))
	elif t==2:
		pH=float(input('Target pH:'))
		print('[A-]/[HA]='+str(round(10**(pH-pKa),4)))
	else:
		V=float(input('Vol L:'))
		M=float(input('Molarity salt:'))
		pH=float(input('Target pH:'))
		N=M*V
		R=10**(pH-pKa)
		print('mol HCl='+str(round(N/(1+R),6)))
	p()
def titr():
	print('Titration any point')
	t=int(input('1:WkAc+StrBs 2:WkBs+StrAc:'))
	if t==1:
		K=float(input('Ka:'))
		pKa=-math.log10(K)
		Ca=float(input('[acid] M:'))
		Va=float(input('Vol acid mL:'))
		Cb=float(input('[base] M:'))
		Vb=float(input('Vol base mL:'))
		na=Ca*Va; nb=Cb*Vb
		if Vb==0:
			x=(-K+math.sqrt(K**2+4*K*Ca))/2
			print('pH='+str(round(-math.log10(x),4)))
		elif nb<na:
			print('Buffer')
			print('pH='+str(round(pKa+math.log10(nb/(na-nb)),4)))
		elif nb>na:
			OH=(nb-na)/1000/(Va+Vb)*1000
			print('Past eq pt')
			print('pH='+str(round(14+math.log10(OH),4)))
		else:
			Vt=(Va+Vb)/1000
			S=na/1000/Vt
			OH=math.sqrt(1e-14/K*S)
			print('Equiv pt')
			print('pH='+str(round(14+math.log10(OH),4)))
	else:
		K=float(input('Kb:'))
		pKb=-math.log10(K)
		Cb=float(input('[base] M:'))
		Vb=float(input('Vol base mL:'))
		Ca=float(input('[acid] M:'))
		Va=float(input('Vol acid mL:'))
		nb=Cb*Vb; na=Ca*Va
		if Va==0:
			x=(-K+math.sqrt(K**2+4*K*Cb))/2
			print('pH='+str(round(14+math.log10(x),4)))
		elif na<nb:
			print('Buffer')
			print('pH='+str(round(14-pKb-math.log10(na/(nb-na)),4)))
		elif na>nb:
			H=(na-nb)/1000/(Va+Vb)*1000
			print('Past eq pt')
			print('pH='+str(round(-math.log10(H),4)))
		else:
			Vt=(Va+Vb)/1000
			S=nb/1000/Vt
			H=math.sqrt(1e-14/K*S)
			print('Equiv pt')
			print('pH='+str(round(-math.log10(H),4)))
	p()
def misc():
	print('1:Polyprotic base')
	print('2:Dilute strong acid')
	print('3:% dissoc->pH')
	print('4:Sol at fixed pH')
	c=int(input('Choice:'))
	if c==1:
		C=float(input('Molarity M:'))
		N=float(input('OH- per unit:'))
		OH=C*N
		print('pH='+str(round(14+math.log10(OH),4)))
	elif c==2:
		C=float(input('[acid] M:'))
		H=(C+math.sqrt(C**2+4e-14))/2
		print('pH='+str(round(-math.log10(H),4)))
	elif c==3:
		C=float(input('[acid/base] M:'))
		P=float(input('% dissoc:'))
		x=C*P/100
		t=int(input('1:acid 2:base:'))
		if t==1: print('pH='+str(round(-math.log10(x),4)))
		else: print('pH='+str(round(14+math.log10(x),4)))
	elif c==4:
		K=float(input('Ksp:'))
		N=float(input('n OH- per form:'))
		pH=float(input('pH:'))
		OH=10**(pH-14)
		print('s='+str(K/OH**N))
	p()
r=True
while r:
	print('=ACIDS & BASES=')
	print('1:pH strong')
	print('2:pH weak acid')
	print('3:pH weak base')
	print('4:Ka from pH')
	print('5:Kb from pH')
	print('6:Ka/Kb convert')
	print('7:Henderson-Hass')
	print('8:Titration')
	print('9:Misc(poly/dil/pct/sol)')
	print('0:Quit')
	c=int(input('Choice:'))
	if c==0: r=False
	elif c==1: phs()
	elif c==2: phwa()
	elif c==3: phwb()
	elif c==4: kapH()
	elif c==5: kbpH()
	elif c==6: kakb()
	elif c==7: hh()
	elif c==8: titr()
	elif c==9: misc()
	else: print('Invalid')
