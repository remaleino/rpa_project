import  csv, urllib,  os, requests
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

    # Raymond changes
    # def download_csv_file(url: str, dest_folder:str, file_name: str):
    #     if not os.path.exists(dest_folder):
    #         os.makedirs(dest_folder)
    #     file_path = os.path.join(dest_folder, file_name)
    #     r = requests.get(url, stream=True)
    #     if r.ok:
    #         with open(file_path, 'wb') as f:
    #             for chunk in r.iter_content(chunk_size=1024 * 8):
    #                 if chunk:
    #                     f.write(chunk)
    #                     f.flush()
    #                     os.fsync(f.fileno())
    #     else:
    #         print("Download failed")

    # Raymond changes
    # def csv_to_json_converter(self):
    #     dest_folder = "reports"
    #     csv_file_name = "csvReport.csv"
    #     json_file_name = "jsonReport.json"
    #     csv_file_path = os.path.join(dest_folder, csv_file_name)
    #     json_file_path = os.path.join(dest_folder, json_file_name)
    #     self.download_csv_file(self.url, dest_folder, csv_file_name)
    #     data = {}
    #     with open(csv_file_path, 'r') as csvFile:
    #         dict_reader = csv.DictReader(csvFile)
    #         l = list(dict_reader)
    #         data = l
    #     #Return dictionary
    #     return(data)
    #     #TO JSON-file
    #     #with open(json_file_path, 'w', encoding='utf-8') as jsonf:
    #     #    jsonf.write(json.dumps(data, indent=4))

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
