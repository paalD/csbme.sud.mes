class ProductionOrder:
	def __init__(self, order_number, product_name, quantity):
		self.__order_number = order_number
		self.__product_name = product_name
		self.__quantity = quantity
		self.__status = "created"
		self.__produced_units = 0

	def get_order_number(self):
		return self.__order_number

	def start(self):
		self.__produced_units += 1

	def finish(self):
		self.__status = "finished"

	def produce(self, units):
		i = 0
		while i < self.__quantity:
			self.start()

	def get_production_efficiency(self):
		return round((self.__produced_units / self.__quantity) * 100, 2)
