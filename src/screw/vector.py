class Vectors:
    """
    The class vector has:
    An attribute, that requires a n quantity of elements.
    Has multiple operator overwritten and owm functions that will let to calculate.
    The function len() on this object will tell the vector's dimension
    The vector can be accessed by [], has also can be set with this operator and a value, such has
    V[0]=8
    Also, can be iterable, so a loop will pass through all elements of the vector.
    As a representation by default
    the operator +, will be applied to two vectors objects to sum both vectors.
    The operator *, will make
    """
    #add values at your vector
    def __init__(self,*v):
        """
        Constructor for the Vectors class.
        It requires an n quantity of elements
        """
        if len(v)==1 and isinstance(v[0],(list,tuple)):
            self.v=list(v[0])
        else:
            self.v=list(v)
        if isinstance(v[0],(set)):
            print("It is not recommendable use sets")
    #Enables the len function for the object
    def __len__(self):
        return len(self.v)
    #enables the funciton to obtain values due an index
    def __getitem__(self,index):
        return self.v[index]
    #sets a value due an item
    def __setitem__(self,index,value):
        self.v[index]=value
    #enables the ability to be iterable
    def __iter__(self):
        return iter(self.v)
    #the defalut representation of a vector
    def __repr__(self):
        return f"Vector({', '.join(str(c) for c in self.v)})"
    #define the sum
    def __add__(self,other):
        if isinstance(other,Vectors):
            if (len(other)!=len(self.v)):
                raise ValueError("Vector must be at the same length")
            sumed=[self.v[i]+other.v[i] for i in range(len(self.v))]
            return Vectors(*sumed)
        return NotImplemented
    def __radd__(self,other):
        if other==0:
            return self
        return self.__add__(other)            
    def __sub__(self,other):
        if isinstance(other,Vectors):
            if (len(other.v)!=len(self.v)):
                raise ValueError("Vector must be at the same length")
            subs=[self.v[i]-other.v[i] for i in range(len(self.v))]
            return Vectors(*subs)
        return NotImplemented
    def __rsub__(self,other):
            
        if other==0:
            return Vectors(*[-x for x in self.v])
        return self.__sub__(other)
    def UnitaryVector(self):
        """
        The calculation of the unitary vector it goes with itself
        """
        denominator=sum([u**2 for u in self.v])
        return [(1/(denominator)**(1/2))*u for u in self.v]
    def DirectionalVector(self,v1):
        """
        You require another vector
        """
        if isinstance(v1,Vectors):
            if (len(v1.v)==len(self.v)):
                denominator=sum([(v1.v[u]-self.v[u])**2 for u in range(len(self.v))])
                numerator=v1-self
                return [(1/(denominator)**(1/2))*(u) for u in numerator]
    def DotProd(self,v1,v2):
        if isinstance(v1,Vectors) and isinstance(v2,Vectors):
            if(len(v1.v)!=len(v2.v)):
                raise ValueError("Vectors must be at the same length")
            mult=sum([v2.v[i]*v1.v[i] for i in range(len(v1.v))])
            return mult
        return NotImplemented
    def __xor__(self,other):
        if isinstance(other,Vectors):
            if(len(other.v)!=3 or len(self.v)!=3):
                raise ValueError("Vectors must be 3-dimension")

            return Vectors(
                self.v[1]*other.v[2]-self.v[2]*other.v[1],
                self.v[2]*other.v[0]-self.v[0]*other.v[2],
                self.v[0]*other.v[1]-self.v[1]*other.v[0]
            ) 
        return NotImplemented
    def __mul__(self,scalar):
        if (isinstance(scalar,(int,float))) :
            return Vectors(*[scalar*i for i in self.v])
        elif isinstance(scalar,Vectors):
            return self.DotProd(self,scalar)
        return NotImplemented
    def __rmul__(self,scalar):
        return self.__mul__(scalar)



    #equality
    def __eq__(self, v1):
        if not isinstance(v1,Vectors):
            return NotImplemented
        return self.v==v1.v
    def __neq__(self, v1):
        if not isinstance(v1,Vectors):
            return NotImplemented
        return not self.v==v1.v


    #So at this point I have to put other class, called PLÜCKER COORDINATES

#First, I must understand the Plucker coordinates.
#Therefore, check the functions described on maple
