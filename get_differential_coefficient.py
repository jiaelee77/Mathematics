from sympy import symbols, Limit, Derivative, sin, log

x,a,h=symbols('x,a,h')
fx=3*x**2-4*x+1
plug_a_in_fx=fx.subs({x:a}) # plug a in fx
plug_ah_in_fx=fx.subs({x:a+h}) #plug a+h in fx

#get diffenrential coeff.
lim=Limit((plug_ah_in_fx-plug_a_in_fx)/h,h,0).doit() #get limit
derv=Derivative(fx,x).doit()

print (lim)
print(derv)

#get polynomial derivative
d=Derivative(fx, x)
d.doit().subs({x:2})
print(d)
#get various derivative
print(Derivative(1/x, x).doit())
print(Derivative(sin(x), x).doit())
print(Derivative(a ** x, x).doit())
print(Derivative(log(x), x).doit())
