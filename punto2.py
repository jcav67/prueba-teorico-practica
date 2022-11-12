

class Complejos:
    def __init__(self,real,imaginario) -> None:
        """
            constructor dela funcion
            args: 
                real->float
                imaginario->float
        """
        self.real = real
        self.imaginario = imaginario
    
    def __add__(self, segundo_complejo):
        """
            sobreescribe el metodo sumatoria de la clase
            args:
                segundo_complejo->float

            retorna:
                objeto de la clase Complejos
        """
        parte_real = self.real+ segundo_complejo.real
        parte_imaginaria = self.imaginario+ segundo_complejo.imaginario

        return Complejos(parte_real,parte_imaginaria)
    
    def __sub__(self, segundo_complejo):
        """
            sobreescribe el metodo resta de la clase
            args:
                segundo_complejo->float

            retorna:
                objeto de la clase Complejos
        """
        parte_real = self.real - segundo_complejo.real
        parte_imaginaria = self.imaginario - segundo_complejo.imaginario

        return Complejos(parte_real,parte_imaginaria)

    def __mul__(self, segundo_complejo):
        """
            sobreescribe el metodo multiplicacion de la clase
            args:
                segundo_complejo->float

            retorna:
                objeto de la clase Complejos
        """
        parte_real = (self.real * segundo_complejo.real) - (self.imaginario * segundo_complejo.imaginario)
        parte_imaginaria =  (self.real* segundo_complejo.imaginario) + (self.imaginario * segundo_complejo.real) 

        return Complejos(parte_real,parte_imaginaria)

    def __truediv__ (self, segundo_complejo):
        """
            sobreescribe el metodo division de la clase
            args:
                segundo_complejo->float

            retorna:
                objeto de la clase Complejos
        """
        denominador =  segundo_complejo.real**2 + segundo_complejo.imaginario**2
        parte_real = ((self.real * segundo_complejo.real) + (self.imaginario * segundo_complejo.imaginario))/denominador
        parte_imaginaria =  ((self.imaginario * segundo_complejo.real) - (self.real* segundo_complejo.imaginario)) / denominador

        return Complejos(parte_real,parte_imaginaria)
    
    def Mod(self):
        """
            metodo que permite halla el modulo de la division de complejos

            retorna:
                objeto de la clase Complejos
        """
        return (self.real**2 + self.imaginario ** 2)**(1/2)


    def __repr__(self) -> str:
        """
            sobreescribe el metodo de representacion de la clase        

            retorna:
                string con la representacion numericas de los complejos
        """
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
