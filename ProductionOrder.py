__author__ = "Dimitri Paal"
__organization__ = "CSBME Bielefeld"
__date__ = "25.08.2024"

class ProductionOrder:
	def __init__(self, order_number, product_name, quantity):
		self.__order_number = order_number
		self.__product_name = product_name
		self.__quantity = quantity
		self.__status = "created"
		self.__produced_units = 0

	def get_order_number(self):
		# print(f"Returning Order Number")
		return self.__order_number

	def start(self):
		# print(f"-- Starting Production --")
		self.__status = "started"

	def finish(self):
		# print(f"Finishing Order")
		self.__status = "finished"

	def produce(self, units):
		if self.__quantity - self.__produced_units < units:
			raise ValueError(f"Units > Remaining")
		# print(f"Producing Order")
		self.__status = "producing"
		i = 0
		while i < units:
			i += 1
			self.__produced_units += 1

	def get_production_progress(self):
		# print(f"Returning Production Progress")
		return round((self.__produced_units / self.__quantity) * 100, 2)

	def __str__(self):
		progress = self.get_production_progress()
		return (
			f"Order Number: {self.__order_number}, "
			f"Product: {self.__product_name}, "
			f"Quantity: {self.__quantity}, "
			f"Produced Units: {self.__produced_units}, "
			f"Status: {self.__status}, "
			f"Progress: {progress}%"
		)
