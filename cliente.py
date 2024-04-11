
class Cliente:
    def __init__(self, nome):
        self.__nome = nome

    @property
    def nome(self):
        print("chamando o @propety nome()")
        return self.__nome.title()

    @nome.setter
    def nome(self, nome):
        print("chamando o setter nome()")
        self.__nome = nome