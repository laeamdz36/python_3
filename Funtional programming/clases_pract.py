"""Practica con clases"""
import functools


class secretAgent():  # declaracion de la clase
    """Clase para creacion de agentes secretos"""

    # Class attributes
    _codeword = "Cheese"

    # definicion de pripiedad de la instancia
    def _getsecret(self):
        return self._secrets[-1] if self._secrets else None

    def _setsecret(self, value):
        self._secrets.append(self._encrypt(value))

    def _delsecret(self):
        self._secrets = []

    # Definicion de propiedad, se puede declara los argumentos con argumentos posicionales
    # en el orden que se tiene actualmente los keyword arguments
    secret = property(fget=_getsecret, fset=_setsecret, fdel=_delsecret)

    # Segunda forma de definicion de propiedades

    secret_v2 = property()

    @secret_v2.getter
    def secret_v2(self):
        return self._secrets[-1] if self._secrets else None

    @secret_v2.setter
    def secret_v2(self, value):
        self._secrets.append(self._encrypt(value))

    @secret_v2.deleter
    def secret_v2(self):
        self._secrets = []

    # finalizacion de declaracion de propiedad secret_v2

    # ultima forma de declaracion con decoradores, version mas corta, llamaremos a esta propiedad
    # v3

    @property
    def secret_v3(self):
        return self._secrets[-1] if self._secrets else None

    @secret_v3.setter
    def secret_v3(self, value):
        self._secrets.append(self._encrypt(value))

    @secret_v3.deleter
    def secret_v3(self):
        self._secrets = []

    def __init__(self, codename, age):
        self.codename = codename
        self.age = age
        self.__country = "Mexico"  # name mangled
        self.countryNameString = ""
        self._secrets = []

    def __del__(self):
        print(f"Agent {self.codename} has been desahutorizada")

    def addSecret(self, secret):
        """Metodo para agregar objetos a la lista d esecretos"""

        self._secrets.append(secret)

    def getSecrets(self):
        """Get all secrets in the list"""

        for i, secret in enumerate(self._secrets):
            print(f"Secreto {i+1} -> {secret}")

    @classmethod
    def _encrypt(cls, message, *, decrypt=False):

        code = sum(ord(c) for c in cls._codeword)
        if decrypt:
            code = -code
        return "".join(chr(ord(m) + code) for m in message)

    @classmethod  # class methode accesa a los atributos de la clase no de l ainstancia
    def inform(cls, codeword):
        cls._codeword = codeword

    @staticmethod  # No accesa
    def inquire(question):
        print("Yo no se nada")


def textStringWraps(func):
    """Decorador para encapsulacion de texto de funcion"""
    @functools.wraps(func)
    def wraps(*args, **kwargs):
        print(f"{args[0].codename}".center(50, "-"))
        result = func(*args, **kwargs)
        print("-".center(50, "-"))
        return result
    return wraps


@textStringWraps
def printObjectAttributes(inClass):
    """Funcion para impresion de atributos de la instancia"""

    print(f"Nombre de la clase: {inClass.codename}")
    print(f"-> {inClass.codename}: edad: {inClass.age}")
    print(f"Class attribute: {inClass._codeword}")
    # print(f"Class attribute: {inClass.__country}") # name mangled no funciona asi

# Main routine


mouse = secretAgent("Mouse", 30)
armadillo = secretAgent("Armadillo", 50)
perro = secretAgent("Copper", 3)
juno = secretAgent("Juno", 12)

printObjectAttributes(mouse)

print(mouse._secretAgent__country)

mouse.addSecret((10.40, 20.35))
mouse.addSecret("Segundo secreto")

armadillo.addSecret("Noche de juegos")
juno.addSecret("Hola mundo")

mouse.getSecrets()
print(mouse._codeword)

# al utilizar el metodo de la clase se modifica el atributo de la clase, que es el mismo para
# todas las instancias.
mouse.inform("Cheese is the mana")
print(f"Code word for armadillo {armadillo._codeword}")
mouse.inquire("Quien eres??")

juno.secret = "Jose Luis Peña Mendez"
print(juno.secret)
