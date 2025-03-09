from .screw import Screw
from .vector import Vectors
class PluckerScrew(Screw):
    def __init__(self, u,p,paso,type_screw="P"):
        self.u= u if isinstance(u,Vectors) else Vectors(*u)
        self.type_screw=type_screw
        self.p=p if isinstance(p,Vectors) else Vectors(*p)
        self.paso=paso
        if type_screw=="P":
            super().__init__(Vectors(0,0,0),self.u)
        elif type_screw=="R":
            V1=(self.p^self.u)+(self.paso*self.u)
            super().__init__(self.u,V1)