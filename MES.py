import ProductionLine

class MES:
	def __init__(self):

	def add_production_line(self, name):
		self.__production_line = ProductionLine.ProductionLine(name)

	def create_production_order(self, production_line_name, order_number: int, product_name, quantity):

		if not production_line:
			raise ValueError(f"Production line '{production_line_name}' does not exist")
		order = ProductionOrder(order_number, product_name, quantity)
		production_line.add_order(order)

	def start_production_order(self, production_line_name, order_number):
		production_line = self.get_production_line(production_line_name)
		if not production_line:
			raise ValueError(f"Production line '{production_line_name}' does not exist")
		order = mes_utils.get_order_by_number(production_line, order_number)
		if order:
			order.start()
		else:
			raise ValueError(
				f"Production order '{order_number}' does not exist in production line '{production_line_name}'")

	def finish_production_order(self, production_line_name, order_number):
		production_line = self.get_production_line(production_line_name)
		if not production_line:
			raise ValueError(f"Production line '{production_line_name}' does not exist")
		order = mes_utils.get_order_by_number(production_line, order_number)
		if order:
			order.finish()
		else:
			raise ValueError(
				f"Production order '{order_number}' does not exist in production line '{production_line_name}'")

	def produce_units(self, production_line_name, order_number, units):
		production_line = self.get_production_line(production_line_name)
		if not production_line:
			raise ValueError(f"Production line '{production_line_name}' does not exist")
		order = mes_utils.get_order_by_number(production_line, order_number)
		if order:
			order.produce(units)
		else:
			raise ValueError(
				f"Production order '{order_number}' does not exist in production line '{production_line_name}'")

	def get_production_lines(self):

	def get_production_line(self, name):
