from .vector import Vectors
class Screw(Vectors):
    def __init__(self,w,v):
        if isinstance(w, (int, float)):
            raise TypeError("Error: No se permite un número único como entrada en `w`.")
        if isinstance(w, (set, dict)):
            raise TypeError("Advertencia: `w` no puede ser un conjunto (set) o diccionario (dict). Usa una lista o tupla.")
        if not isinstance(w, (list, tuple)) and len(w) != 3:
            raise ValueError("Error: `w` debe ser una lista o tupla de exactamente 3 elementos.")

        # Validación de `v`
        if isinstance(v, (int, float)):
            raise TypeError("Error: No se permite un número único como entrada en `v`.")
        if isinstance(v, (set, dict)):
            raise TypeError("Advertencia: `v` no puede ser un conjunto (set) o diccionario (dict). Usa una lista o tupla.")
        if not isinstance(v, (list, tuple)) and len(v) != 3:
            raise ValueError("Error: `v` debe ser una lista o tupla de exactamente 3 elementos.")

        self.w= w if isinstance(w,Vectors) else Vectors(*w)
        self.v= v if isinstance(v,Vectors) else Vectors(*v)
        
    def getW(self):
        return self.w
    def getV(self):
        return self.v
    def LieBracket(self,S1,S2):
        if isinstance(S1,Screw) and isinstance(S2,Screw):
            return Screw(
                S1.w^S2.w,
                (S1.w^S2.v)-(S2.w^S1.v)
            )   
        return NotImplemented
    def __add__(self,other):
        if isinstance(other,Screw):
            return Screw(
                self.w+other.w,
                self.v+other.v
            )
        return NotImplemented
    def __sub__(self,other):
        if isinstance(other,Screw):
            return Screw(
                self.w-other.w,
                self.v-other.v
            )
        return NotImplemented
    def __repr__(self):
        return f"Screw=[W={self.w} V={self.v}]"
    def __mul__(self,scalar):
        if (isinstance(scalar,(int,float))) :
            return Screw(scalar*self.w,scalar*self.v)
        elif isinstance(scalar,Vectors):
            return self.LieBracket(self,scalar)
        return NotImplemented
    def __rmul__(self,scalar):
        return self.__mul__(scalar)
    @classmethod
    def KillingColineality(self,S1,S2):
        if isinstance(S1,Screw) and isinstance(S2,Screw):
            return S1.w*S2.w
    @classmethod
    def KleinColineality(self,S1,S2):
        if isinstance(S1,Screw) and isinstance(S2,Screw):
            return S1.w*S2.v+S2.w*S1.v