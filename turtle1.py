import turtle

S = []

def SM(s):  
  s1 = " ".join(s.split())
  t = s1.split()
  print t
  L = len(t)
  i = 0
  while i<L:
    if (t[i]=='f'):
      turtle.forward( S.pop() )
    elif (t[i]=='l'):
      turtle.left( S.pop() )
    
    else:
      S.append( float(t[i]) )
    i += 1


turtle.shape("turtle")

# turtle.forward(25)

SM("25   f 45 l 50 f 45 l 50 f")

turtle.exitonclick()




