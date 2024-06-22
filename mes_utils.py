class mes_utils:

	@staticmethod
	def get_order_by_number(production_line, order_number):
		# print(f"Returning Order by Number")
		order_list = production_line.get_orders()
		for order in order_list:
			if order.get_order_number() == order_number:
				return order
		raise ValueError(
			f"Production order '{order_number}' does not exist in production line "
			f"'{production_line.get_production_line_name()}'")

	@staticmethod
	def calculate_production_progress(order):
		#  print(f"Calculating Production Progress")
		return order.get_production_progress()
