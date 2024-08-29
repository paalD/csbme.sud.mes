__author__ = "Dimitri Paal"
__organization__ = "CSBME Bielefeld"
__date__ = "25.08.2024"

class ProductionLine:
	def __init__(self, name):
		# print(f"Creating Production Line with name: '{name}'")
		self.__production_line_name = name
		self.__orders = []

	def add_order(self, order):
		# print(f"Adding Production Order: {order}\nto Production Line: '{self.get_production_line_name()}'")
		self.__orders.append(order)

	def get_production_line_name(self):
		# print(f"Returning Production Line Name")
		return self.__production_line_name

	def get_orders(self):
		# print(f"Returning Production Orders from: '{self.get_production_line_name()}'")
		return self.__orders

	def __str__(self):
		orders_str = ", ".join(map(str, self.__orders))  # Liste der Aufträge als String
		return f"Produktionslinie: {self.__production_line_name}, Aufträge: [{orders_str}]"


