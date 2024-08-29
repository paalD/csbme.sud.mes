__author__ = "Oussama Abdellaoui"
__organization__ = "CSBME Bielefeld"
__date__ = "29.08.2024"

from MES import MES


class Input:
    @staticmethod
    def start_input(mes: MES):
        while True:
            print('Auswahl:')
            print('1 für Liste der Produktionslinien')
            print('2 für neue Produktionslinie anlegen')
            choice = input()

            match choice:
                case '1':
                    production_lines = mes.get_production_lines()
                    for line in production_lines:
                        print(line.get)
                case '2':
                    print('Benenne die neue Produktionslinie:')
                    line_name = input()
                    mes.add_production_line(line_name)
                case _:
                    print('Ungültige Auswahl, bitte versuche es erneut.')

