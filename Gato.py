"""
Clase Gato.
:author: Jaime Rabasco Ronda.
"""


class Gato:
    """
    Clase Gato.
    :author: Óscar Martín-Castaño Carrillo.
    """

    def __init__(self):
        """
        Constructor Gato.

        :param: Miau
        """
        self.maulla = 'Miau'

    def maulla(self):
        """
        Imprime el maullido del gato

        :return:
        """
        print(self.maulla)


g = Gato()
g.maulla()
