"""
Clase Estudiante base para el Examen Convocatoria Ordinaria de la UD4
:author: Jaime Rabasco
Refactorización
Extrae una superclase con los campos
	nombre
	apellidos
	nif
"""


class Persona:
    """
    :author: Óscar Martín-Castaño Carrillo
    """

    def __init__(self, nif, nombre, apellidos):
        """
        Constructor de la clase Persona

        :param nif:
        :param nombre:
        :param apellidos:
        """
        self.__nif = nif
        self.__nombre = nombre
        self.__apellidos = apellidos


class Estudiante(Persona):
    """
    Clase Estudiante con los campos

    nif, curso, nombre, apellidos
    """
    nif = "11111111Z";
    curso = "Primaria";
    nombre = "Nombre";
    apellidos = "Apellidos";

    def __init__(self):
        pass;

    def __init__(self, nif, curso, nombre, apellidos):
        """
        Constructor de la clase Estudiante

        :param nif:
        :param curso:
        :param nombre:
        :param apellidos:
        """
        self.nif = nif;
        self.curso = curso;
        self.nombre = nombre;
        self.apellidos = apellidos;

    @property
    def nif(self):
        """
        Retorna el nif

        :return:
        """
        return self.__nif

    @nif.setter
    def nif(self, value):
        """
        Le da un valor al nif

        :param value:
        :return:
        """
        self.__nif = value

    @property
    def curso(self):
        """
        Retorna el curso

        :return:
        """
        return self.__curso

    @curso.setter
    def curso(self, value):
        """
        Le da valor al curso

        :param value:
        :return:
        """
        self.__curso = value

    @property
    def nombre(self):
        """
        Retorna el nombre

        :return:
        """
        return self.__nombre

    @nombre.setter
    def nombre(self, value: int):
        """
        Le da valor al nombre

        :param value:
        :return:
        """
        self.__nombre = value

    @property
    def apellidos(self):
        """
        Retorna los apellidos

        :return:
        """
        return self.__apellidos

    @apellidos.setter
    def apellidos(self, value):
        """
        Le da valor al apellidos
        :param value:
        :return:
        """
        self.__apellidos = value
