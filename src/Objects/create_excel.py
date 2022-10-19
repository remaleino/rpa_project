import  csv, urllib,  os
from pathlib import Path
from RPA.Excel.Files import Files


class CreateExcel():
    def __init__(self, url, supervisor):
        self.lib = Files()
        self.url = url
        self.supervisor = supervisor

    def download_csv_file(self):
        urllib.request.urlretrieve(self.url, "file.csv")
        data = {}
        with open('file.csv', 'r') as csvFile:
            dict_reader = csv.DictReader(csvFile)
            l = list(dict_reader)
            data = l
        return data

    def iterate_over_csv_dict(self, data):
        filtered_dict = []
        for dict in data:
            for value in dict.values():
                if value == self.supervisor:
                    filtered_dict.append(dict)
        return filtered_dict

    def create_excel_file(self, data):
        work_path = os.path.join(Path.cwd(), "src")
        path_to_excel = os.path.join(work_path,  "timesheet.xlsx")
        if not os.path.isfile(path_to_excel):
            self.lib.create_workbook()
            self.lib.save_workbook(path_to_excel)
        self.lib.open_workbook(path=path_to_excel)

        header = ["worktime_duration","date","project_name","task_name","on_call","overtime","invoice_note","first_name","last_name","supervisor","contract_type"]
        row_number = 1
        cell_header = 1
        for r in header:
            self.lib.set_cell_value(cell_header, row_number, r)
            cell = 2
            for d in data:
                for key, value in d.items():
                    if key == r:
                        self.lib.set_cell_value(cell, row_number, value)
                        cell += 1
            row_number += 1
        self.lib.save_workbook(path_to_excel)

    # def filter_excel(lib :Files, path_to_excel):
    #     active = lib.set_active_worksheet(path_to_excel)
    #     print(active)
    #     table = active.read_worksheet_as_table(path_to_excel)
    #     print(table)
