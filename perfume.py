class Perfume:
    # Método construtor
    def __init__(self, nome, fragrancia, volume, preco, dataFabricacao, embalagem):
        self.__nome = nome
        self.__fragrancia = fragrancia
        self.__volume = volume
        self.__preco = preco
        self.__dataFabricacao = dataFabricacao
        self.__embalagem = embalagem 
 
# NOME
    def nomeGet(self):
        return self.__nome

    def nomeSet(self, nome):
        self.__nome = nome

# FRAGRANCIA
    def fragranciaGet(self):
        return self.__fragrancia

    def fragranciaSet(self, fragrancia):
        self.__fragrancia = fragrancia

# VOLUME
    def volumeGet(self):
        return self.__volume

    def volumeSet(self, volume):
        self.__volume = valor

# PRECO
    def precoGet(self):
        return self.__preco

    def precoSet(self, preco):
        self.__preco = valor

# DATAFABRICACAO 
    def dataFabricacaoGet (self):
        return self.__dataFabricacao

    def dataFabricacaoSet (self, dataFabricacao):
        self.__dataFabricacao = dataFabricacao 

# EMBALAGEM 
    def embalagemGet (self):
        return self.__embalagem

    def emlagemSet (self, embalagem):
        self.__embalagem = embalagem

    # perfume1 = "Lovely", "rosas", 500, 55.0, "10/10/22", "redonda"
    # perfume2 = "Aurora", "lírio", 100, 60.0, "01/12/22", "reutilizável"
    # perfume3 = "Shine", "lavanda", 300, 65.0, "01/01/23", "reciclável"
    # perfume4 = "Charlotte", "gardenia", 300, 80.0, "12/01/23", "reutilizável"
    # perfume5 = "Lunna", "jasmin", 400, 73.0, "19/02/23", "vidro"