  
valor = float(raw_input())

if valor >= 0 and valor <= 400.00:
  perc1 = valor * 15/100
  print "Novo salario: %.2f" %(valor+perc1)
  print "Reajuste ganho: %.2f" %(perc1)
  print "Em percentual: 15 %"
  
elif valor >= 400.01 and valor <= 800.00:
  perc2 = valor * 12/100
  print "Novo salario: %.2f" %(valor+perc2)
  print "Reajuste ganho: %.2f" %(perc2)
  print "Em percentual: 12 %"
  
elif valor >= 800.01 and valor <= 1200.00:
  perc3 = valor * 10/100
  print "Novo salario: %.2f" %(valor +perc3)
  print "Reajuste ganho: %.2f" %(perc3)
  print "Em percentual: 10 %"
  
elif valor >= 1200.01 and valor <= 2000.00:
  perc4 = valor * 7/100
  print "Novo salario: %.2f" %(valor+perc4)
  print "Reajuste ganho: %.2f" %(perc4)
  print "Em percentual: 7 %"
  
else:
  perc5 = valor * 4/100
  print "Novo salario: %.2f" %(valor+perc5)
  print "Reajuste ganho: %.2f" %(perc5)
  print "Em percentual: 4 %"
