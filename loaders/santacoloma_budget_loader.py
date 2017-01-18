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
            # old budget application: new programme
            '1100232012279909': '23113',
            '1100920012260217': '15120',
            '1100920012260300': '49100',
            '1100920012269900': '49100',
            '1100920012270600': '49100',
            '1100920014490100': '24100',
            '1110912024890500': '91204',
            '1200924044890300': '92400',
            '1200943014660100': '92200',
            '1200943014660300': '92200',
            '1300433012269900': '43200',
            '2000152014490300': '15000',
            '2000152017490000': '15000',
            '2000241014490100': '24100',
            '2000241014490200': '23116',
            '2000320002279913': '32609',
            '2000324054110200': '32606',
            '2000341014110100': '34000',
            '2000931004900000': '92901',
            '2700920042269980': '92401',
            '2800920112260300': '92009',
            '2900152012020100': '23105',
            '2900231052020100': '33701',
            '2900333012020100': '92400',
            '2900334062020100': '33701',
            '2900920052269900': '92020',
            '2900920052270600': '92020',
            '2900920056210000': '92019',
            '2900920162120200': '92000',
            '2900920162120400': '92000',
            '2900920162240000': '92000',
            '2900924012020100': '92400',
            '3100132002269911': '13500',
            '3100133002279903': '13301',
            '4000231082279909': '32700',
            '5000230002269900': '23100',
            '5000920112260300': '23100',
            '5021233014640000': '23110',
            '5022233022269900': '23111',
            '5022233022279909': '23111',
            '5022233024800200': '23111',
            '5023233012269900': '23112',
            '5023233012279909': '23112',
            '5024231012279909': '23102',
            '5030313022219909': '31100',
            '5030313022269900': '31100',
            '5030313022270600': '31100',
            '5031313012210600': '31101',
            '5031313012269900': '31101',
            '5031313012270600': '31101',
            '5032493012270600': '49301',
            '5032493012270600': '49302',
            '5033313032269900': '31102',
            '5033313032279909': '31102',
            '5112232012279909': '23113',
            '5120232052200100': '23109',
            '5120232052260900': '23109',
            '5120232052269900': '23109',
            '5120232052270600': '23109',
            '5120232054890100': '23109',
            '5120232054890101': '23109',
            '5200338012269900': '33000',
            '5200338012279909': '33000',
            '5209231022269900': '23107',
            '5209231022279909': '23107',
            '5210338012269900': '33802',
            '5210338012279909': '33802',
            '5210338012279910': '33802',
            '5311232012279909': '23117',
            '5411335012269900': '33402',
            '5411335012279909': '33402',
            '5411335012279910': '33402',
            '5412335012269900': '33401',
            '5412335012279909': '33401',
            '5412335012279910': '33401',
            '5413333012269900': '33302',
            '5413333012279910': '33302',
            '5415332012269900': '33210',
            '5415332012269900': '33211',
            '5415332012269900': '33212',
            '5415332012269900': '33213',
            '5415332012269900': '33214',
            '5415332012279910': '33210',
            '5415332012279910': '33211',
            '5415332012279910': '33212',
            '5415332012279910': '33213',
            '5415332012279910': '33214',
            '5416337012279910': '33403',
            '5417232032269900': '33404',
            '5417232032269900': '33405',
            '5417232032279909': '33404',
            '5417232032279909': '33405',
            '5417232032279909': '33406',
            '5417232032279909': '33407',
            '5418232042269900': '32601',
            '5419172004890300': '31100',
            '5419232014890100': '23113',
            '5419232074800200': '23106',
            '5419233014890300': '23104',
            '5419313024890300': '31101',
            '5419324034890100': '32600',
            '5419334014890300': '33400',
            '5419924044890100': '92400',
            '5419924044890300': '92400',
            '5500231032230000': '23105',
            '5500231032269900': '23105',
            '5500231032269910': '24100',
            '5500231032279909': '23104',
            '5500231032279909': '23105',
            '5500231034800100': '23105',
            '5500231034890800': '23115',
            '5514232022269900': '23118',
            '5514232022270600': '23118',
            '5514232072279909': '23118',
            '6000924042269900': '92400',
            '6100324014890100': '32602',
            '6100324022269900': '32000',
            '6100324034890100': '32603',
            '6110324022269900': '32001',
            '6110324024890600': '32604',
            '6110324024890601': '32605',
            '6120324032269900': '32607',
            '6130321014790300': '32301',
            '6140320004890100': '32302',
            '6140920152120100': '33701',
            '6210924012260900': '92402',
            '6210924012269914': '92403',
            '6210924012270600': '92402',
            '6210924044890100': '92400',
            '6212232042279909': '33701',
            '6212334062269900': '33701',
            '6212334064890100': '33701',
            '6212924042269900': '33701',
            '7110313022269900': '31103',
            '7110313022270600': '31103',
            '7110313024650000': '31103',
            '7120313042270600': '17200',
            '7120313044890100': '17200',
            '7130179012270600': '17220',
            '7140172002270600': '17230',
            '7150172002270000': '16221',
            '7150172002270600': '16221',
            '7200433012269900': '43200',
            '7200433014890100': '43300',
            '7300151006000100': '15120',
            '7300152012269900': '15000',
            '7610163012270000': '16300',
            '7610163012279911': '16302',
            '7620162022270000': '16211',
            '7630320002270000': '32300',
            '7630320002270000': '33000',
            '7630320002270000': '34000',
            '7630920152270000': '43120',
            '7630920152270000': '92000',
            '7650163032270000': '16212',
            '7660431002120100': '43120',
            '7660431002269900': '43120',
            '7700151022100300': '15110',
            '7700151022270600': '15110',
            '7800169002100100': '15300',
            '7800169002100200': '15300',
            '7800169002101100': '15300',
            '7800169002140100': '15300',
            '7800169002219900': '15300',
            '7810155002100100': '15300',
            '7810155002100300': '15300',
            '7810155002100700': '15320',
            '7810155002101600': '15300',
            '7810155002101700': '15330',
            '7851171002270000': '16000',
            '7900320002120100': '32300',
            '7900920152120100': '92000',
            '7900920152130100': '92000',
            '7900920152270600': '92000',
            '7910165002210000': '16500',
            '7910165002210000': '16501',
            '7910165002210000': '16502',
            '7910320002210000': '32300',
            '7910320002210000': '33000',
            '7910320002210000': '34000',
            '7910320002210100': '32300',
            '7910320002210100': '33000',
            '7910320002210100': '34000',
            '7910320002210200': '32300',
            '7910320002210200': '33000',
            '7910320002210200': '34000',
            '7910920152210000': '43120',
            '7910920152210000': '92000',
            '7910920152210100': '43120',
            '7910920152210100': '92000',
            '7910920152210200': '43120',
            '7910920152210200': '92000',
            '7200155006190001': '15300',
            '7400155006100000': '15300',
            '7400155006110100': '15300',
            '7400155006190001': '15300',
            '7500155006100000': '15300',
            '7500155006190001': '15300',
            '7700155002269900': '15300',
            '7800155002100500': '15300',
            '7800155006110400': '15300',
            '7810155001200100': '15300',
            '7810155001200300': '15300',
            '7810155001200600': '15300',
            '7810155001210000': '15300',
            '7810155001210100': '15300',
            '7810155001300000': '15300',
            '7810155001300200': '15300',
            '7810155001500000': '15300',
            '7810155001600000': '15300',
            '7810155001620900': '15300',
            '7810155002210400': '15300',
            '7810155002260300': '15300',
            '7810155003520000': '15300',
            '7810155006110100': '15300',
            '7810155006190001': '15300',
            '7810155006240100': '15300',
            '7830155006110100': '15300',
            '7830155006190001': '15300',
        }

        is_expense = (filename.find('gastos.csv')!=-1)
        is_actual = (filename.find('/ejecucion_')!=-1)
        if is_expense:
            ic_code = line[2]
            fc_code = line[3]
            ec_code = line[4].ljust(7, '0')  # In 2012 data, the codes are 5 digits

            # For years before 2015 we check whether we need to amend the programme code
            year = re.search('municipio/(\d+)/', filename).group(1)
            if int(year) < 2015:
                ap_code = ic_code + fc_code + ec_code
                fc_code = programme_mapping.get(ap_code, fc_code)

            # Ignore additional digits after the fifth
            ec_code = ec_code[:5]

            return {
                'is_expense': True,
                'is_actual': is_actual,
                'fc_code': fc_code,
                'ec_code': ec_code[:-2],        # First three digits (everything but last two)
                'ic_code': '000',
                'item_number': ec_code[-2:],    # Last two digits
                'description': self._spanish_titlecase(line[5]),
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
                'description': self._spanish_titlecase(line[4]),
                'amount': self._parse_amount(line[8 if is_actual else 5])
            }
