# A = Complejo(2,1)
# B = Complejo(5,6)
# A+B → 7.0+7.0i
# A-B → -3.0-5.0i
# A*B → 4.00+17.00i
# A/B → 0.26-0.11i
# Mod(A) → 2.24+0.00i
# Mod(B) → 7.81+0.00i
#NOTA: NO puede utilizar el método nativo complex()

class Complejos:
    def __init__(self,real,imaginario) -> None:
        self.real = real
        self.imaginario = imaginario
    
    def __add__(self, segundo_complejo):
        parte_real = self.real+ segundo_complejo.real
        parte_imaginaria = self.imaginario+ segundo_complejo.imaginario

        return Complejos(parte_real,parte_imaginaria)
    
    def __sub__(self, segundo_complejo):
        parte_real = self.real - segundo_complejo.real
        parte_imaginaria = self.imaginario - segundo_complejo.imaginario

        return Complejos(parte_real,parte_imaginaria)

    def __mul__(self, segundo_complejo):
        parte_real = (self.real * segundo_complejo.real) - (self.imaginario * segundo_complejo.imaginario)
        parte_imaginaria =  (self.real* segundo_complejo.imaginario) + (self.imaginario * segundo_complejo.real) 

        return Complejos(parte_real,parte_imaginaria)

    def __truediv__ (self, segundo_complejo):
        denominador =  segundo_complejo.real**2 + segundo_complejo.imaginario**2
        parte_real = ((self.real * segundo_complejo.real) + (self.imaginario * segundo_complejo.imaginario))/denominador
        parte_imaginaria =  ((self.imaginario * segundo_complejo.real) - (self.real* segundo_complejo.imaginario)) / denominador

        return Complejos(parte_real,parte_imaginaria)
    
    def Mod(self):

        return (self.real**2 + self.imaginario ** 2)**(1/2)


    def __repr__(self) -> str:
        
        if self.imaginario > 0 :
            return f' {float(self.real)}+{float(self.imaginario)}i'            
        return f' {float(self.real)}{float(self.imaginario)}i'

A = Complejos(2,1)
B = Complejos(5,6)
print(A)
print(B)
print(A+B)
print(A-B)
print(A*B)
print(A/B)
print(A.Mod())
print(B.Mod())
