#!coding: utf-8

import xlwt, xlrd
import xlwt.Worksheet

from tmm_tools import CWorksheet

wb = xlrd.open_workbook("app_id单个集群包含多个机型统计列表_1.xls")
sh = wb.sheet_by_index(0)
values = sh.col_values(0)
print(type(values))
print(values)



wb_2 = xlwt.Workbook()
sh_2 = wb_2.add_sheet("one")
CWorksheet.write_row(sh_2, 1, 0, values)
wb_2.save("test-out.xls")
