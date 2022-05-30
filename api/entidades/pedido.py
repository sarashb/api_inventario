class Pedido():
    def __init__(self, data_compra):
        self.__data_compra = data_compra

    @property
    def data_compra(self):
        return self.__data_compra

    @data_compra.setter
    def data_compra(self, data_compra):
        self.__data_compra = data_compra






