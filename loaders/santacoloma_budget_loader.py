# -*- coding: UTF-8 -*-
from budget_app.models import *
from budget_app.loaders import SimpleBudgetLoader
from decimal import *
import csv
import os
import re

class SantacolomaBudgetLoader(SimpleBudgetLoader):

    def parse_item(self, filename, line):
        programme_mapping = {
            # old programme: new programme
            '1550': '1530',     # Mantenimiento
        }

        is_expense = (filename.find('gastos.csv')!=-1)
        is_actual = (filename.find('/ejecucion_')!=-1)
        if is_expense:
            # Work at the 'group of programmes' level, at least for now
            fc_code = line[3][0:3].ljust(4, '0')
            ec_code = line[4][:5]   # Ignore additional digits after the fifth

            # For years before 2015 we check whether we need to amend the programme code
            year = re.search('municipio/(\d+)/', filename).group(1)
            if int(year) < 2015:
                fc_code = programme_mapping.get(fc_code, fc_code)

            return {
                'is_expense': True,
                'is_actual': is_actual,
                'fc_code': fc_code,
                'ec_code': ec_code[:-2],        # First three digits (everything but last two)
                'ic_code': '000',
                'item_number': ec_code[-2:],    # Last two digits
                'description': line[5],
                'amount': self._parse_amount(line[9 if is_actual else 6])
            }

        else:
            ec_code = line[3][:5]   # Ignore additional digits after the fifth

            return {
                'is_expense': False,
                'is_actual': is_actual,
                'ec_code': ec_code[:3],         # First three digits
                'ic_code': '000',               # All income goes to the root node
                'item_number': ec_code[-2:],    # Last two digits
                'description': line[4],
                'amount': self._parse_amount(line[8 if is_actual else 5])
            }
