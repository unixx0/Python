class A:
    def __init__(self, adata):
        self.yyyy= adata 



class B(A):
    def __init__(self, adata, bdata):
        super(). __init__( adata)
        self.bdata= bdata

    def __str__(self):
        return(f"A data= {self.yyyy}, B data= {self.bdata}")
    

b= B(5, 6)
print(b)
print(b.yyyy)