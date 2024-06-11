class ProductionLine:
	def __init__(self, name):
		self.__production_line_name = name
		self.__orders = []

	def add_order(self, order):
		self.__orders.append(order)

	def get_production_line_name(self):
		return self.__production_line_name

	def get_orders(self):
		return self.__orders
