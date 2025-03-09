from .PluckerScrew import  PluckerScrew
class MatrixScrew(PluckerScrew):
    def __init__(self,i):
        self.i=i
        self.matrix=[[] for _ in range(i)]
    def __setitem__(self, index,screw):
        if index>=self.i:
            raise ValueError(f"Columna fuera de rango{self.i-1}")
        self.matrix[index]=screw
    def __len__(self):
        return len(self.matrix)
    #enables the funciton to obtain values due an index
    def __getitem__(self,index):
        return self.matrix[index]
    def __repr__(self):
        return "\n".join([str(col) for col in self.matrix])
    def __iter__(self):
        return iter(self.matrix)
    @classmethod
    def reciproco(self,max_index,screw,matrx_screw):
        sum=0
        for k in range(max_index):
            sum+=PluckerScrew.KleinColineality(screw,matrx_screw[k])
        return sum
