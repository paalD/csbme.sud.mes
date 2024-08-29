from Input import Input
from MES import MES
from mes_utils import mes_utils

import time

# Erstelle eine MES-Instanz
mes = MES()

#Input.start_input(mes)

# Füge eine Produktionslinie hinzu
mes.add_production_line("Produktionslinie 1")

# Erstelle eine Bestellung
mes.create_production_order("Produktionslinie 1", 1001, "Produkt 1", 100)

# Starte den Produktionsauftrag
mes.start_production_order("Produktionslinie 1", 1001)

# Produziere Einheiten für einen Auftrag
mes.produce_units("Produktionslinie 1", 1001, 50)

# Beende den Produktionsauftrag
mes.finish_production_order("Produktionslinie 1", 1001)

# Berechne die Produktionseffizienz des Produktionsauftrags
# order = mes_utils.get_order_by_number(mes.production_lines["Produktionslinie 2"], 1001)
order = mes_utils.get_order_by_number(mes.get_production_line("Produktionslinie 1"), 1001)
efficiency = mes_utils.calculate_production_progress(order)

print(f"Der Produktionsfortschritt des Auftrags ist {efficiency}%.")

production_lines = mes.get_production_lines()
for line in production_lines:
    print(line)
