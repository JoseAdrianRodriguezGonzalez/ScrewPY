from screw.screw import Screw, Vectors,MatrixScrew,PluckerScrew

#v1^v2 cross
#v1*v2 dot
#2*v1 scalar
#v1+v2 sum vector
#len(v1)
#v1[0]=2
#v1[1]
#is iterable
#v1-v2
#unitary vector u
#unitary vector directional u->
#

##screw
#getW.obtains w, and getV obtains V
#S1*S2 LIe brackt
#2*s1 scalar and screw
#Killing and Klen colineality 


# Example usage:
u = Vectors(1, 0, 0)
p= Vectors(0, 1, 0)

# Normal addition uses __add__
# Using sum(), which calls __radd__ for the 0 initial value:
#S1=Screw(v1,v2)#[[1,2,3]  [4,5,6]]
#S2=Screw((1,2,3),(2,4,5)) #[[1,2,3]  [2,4,5]] 

#S3=S2+S1 #Screw=[W=Vector(2, 4, 6) V=Vector(6, 9, 11)]
#S4=S1+(S2+S3) #[[1,2,3] [4,5,6]]+[[3,6,9] [8,13,16]]=[[4,8,9][12,18,22]]

#S5=2*S1
#print(Screw.KillingColineality(S1,S2)) 
#print(Screw.KleinColineality(S1,S2))
#print(v1.UnitaryVector())
#print(v1.DirectionalVector(v2))


#PluckerScrew
screw_R=PluckerScrew(u,p,2,"R")
screw_P=PluckerScrew(u,p,2,"P")
print(screw_R)
print(screw_P)
m=MatrixScrew(2)
m[0]=screw_R
m[1]=screw_P
print(Screw.KleinColineality(Screw([0,1,2],[2,5,7]),screw_R))
print(MatrixScrew.reciproco(len(m),Screw([0,1,2],[2,5,7]),m))