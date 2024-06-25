__author__ = "Dimitri Paal"
__organization__ = "CSBME Bielefeld"
__date__ = "25.08.2024"

from ProductionLine import ProductionLine
from ProductionOrder import ProductionOrder
from mes_utils import mes_utils


class MES:
	def __init__(self):
		# print(f"Initializing MES")
		self.__production_lines = []

	def add_production_line(self, name):
		# print(f"Adding Production Line '{name}' to MES")
		if not self.validate_production_line(name):
			self.__production_lines.append(ProductionLine(name))
		else:
			raise ValueError(f"Production Line {name} already exists")

	def create_production_order(self, production_line_name, order_number: int, product_name, quantity):
		# print(f"Creating Production Order")
		production_line = self.get_production_line(production_line_name)
		order = ProductionOrder(order_number, product_name, quantity)
		ProductionLine.add_order(production_line, order)

	def start_production_order(self, production_line_name, order_number):
		# print(f"Starting Production Order")
		production_line = self.get_production_line(production_line_name)
		order = mes_utils.get_order_by_number(production_line, order_number)
		if order:
			order.start()
		else:
			raise ValueError(
				f"Production order '{order_number}' does not exist in production line '{production_line_name}'")

	def finish_production_order(self, production_line_name, order_number):
		# print(f"Finishing Production Order")
		production_line = self.get_production_line(production_line_name)
		order = mes_utils.get_order_by_number(production_line, order_number)
		if order:
			order.finish()
		else:
			raise ValueError(
				f"Production order '{order_number}' does not exist in production line '{production_line_name}'")

	def produce_units(self, production_line_name, order_number, units):
		# print(f"Producing Units")
		production_line = self.get_production_line(production_line_name)
		order = mes_utils.get_order_by_number(production_line, order_number)
		if order:
			order.produce(units)
		else:
			raise ValueError(
				f"Production order '{order_number}' does not exist in production line '{production_line_name}'")

	def get_production_lines(self):
		# print(f"Returning Production Lines in MES")
		return self.__production_lines

	def get_production_line(self, production_line_name):
		# print(f"Returning a single Production Line")
		for production_line in self.__production_lines:
			if ProductionLine.get_production_line_name(production_line) == production_line_name:
				return production_line
			else:
				raise ValueError(f"Production line '{production_line_name}' does not exist")

	def validate_production_line(self, production_line_name):
		for production_line in self.__production_lines:
			if ProductionLine.get_production_line_name(production_line_name) == production_line_name:
				return True
			else:
				return False
