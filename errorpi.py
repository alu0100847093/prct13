#! encoding: UTF-8
import time
import timeit
import modulo
import sys
import matplotlib.pyplot as pl

def error(nro_intervalos,nro_test,umbral):
   fallos=0
   for i in range (nro_test):
    s=modulo.aproxpi(nro_intervalos)
    error=abs(s-modulo.pi)
    if error>=umbral:
      fallos=fallos+1
    return ((fallos/nro_test)*100)
x=[]
y=[]
t_upla_p3=(0.0001,0.00001,0.000001,0.0000001,0.00000001)
t_upla_p1=(10,50,100,150,500,550,1000)
for i in range(7):
 start=time.time()
 p1=t_upla_p1[i]
 p2=5
 p3=0.1
 y=y +[p1]
 s=error(p1,p2,p3)
 print "El porcentaje de error es de: %5.3f" %s
 finish=time.time()-start
 print "El tiempo que tarda en realizarse es: %14.13f" %finish
 x=x+[finish]
print x
print y
v=[]
t=[]
for i in range(5):
 start=time.time()
 p1=5
 p2=5
 p3=t_upla_p3[i]
 v=v+[s]
 s=error(p1,p2,p3)
 print "El porcentaje de error es de: %5.3f" %s
 finish=time.time()-start
 print "El tiempo que tarda en realizarse es: %14.13f" %finish
 t=t+[p3]
print v
print t
pl.plot(y,x,'ro--')

#pl.plot(t,v,'ro')
pl.show()