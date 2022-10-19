from RPA.Excel.Files import Files
from RPA.Tables import Tables
import os
from pathlib import Path

class Orders:
    def get_orders(self, excel):
        files = Files()
        workbook = files.open_workbook(excel)
        rows = workbook.read_worksheet(header=True)
        
        tables = Tables()
        table = tables.create_table(rows)
        tables.filter_empty_rows(table)
        

        #orders = []
        #for row in table:
        #    first_name, last_name = row["Name"].split()
        #    order = {
        #        "item": row["Item"],
        #        "zip": int(row["Zip"]),
        #        "first_name": first_name,
        #        "last_name": last_name
        #    }
        #    orders.append(order)
#
        #return orders

if __name__ == "__main__":
    work_path = os.path.join(Path.cwd(), "src")
    path_to_excel = os.path.join(work_path,  "timesheet.xlsx")
    
    orders = Orders()

    orders.get_orders(path_to_excel)