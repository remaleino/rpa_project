import  csv, os, requests
from pathlib import Path
from RPA.Excel.Files import Files


class CreateExcel():
    def __init__(self, url, supervisor):
        self.lib = Files()
        self.url = url
        self.supervisor = supervisor
        # reports dest_folder
        self.reports_folder = os.path.join(Path.cwd(), 'reports')
        if not os.path.isdir(self.reports_folder):
            os.mkdir(self.reports_folder)
        self.csv_file_name = "csvReport.csv"

    def download_csv_file(self):
        file_path = os.path.join(self.reports_folder, self.csv_file_name)
        r = requests.get(self.url, stream=True)
        if r.ok:
            with open(file_path, 'wb') as f:
                for chunk in r.iter_content(chunk_size=1024 * 8):
                    if chunk:
                        f.write(chunk)
                        f.flush()
                        os.fsync(f.fileno())
        else:
            print("Download failed")

    def get_data_from_csv(self):
        csv_file_path = os.path.join(self.reports_folder, self.csv_file_name)
        with open(csv_file_path, 'r') as csvFile:
            dict_reader = csv.DictReader(csvFile)
            data = list(dict_reader)
        #Return raw csv data dictionary
        return data

    def csv_to_json_converter(self):
        pass
        #TO JSON-file
        #json_file_name = "jsonReport.json"
        #json_file_path = os.path.join(dest_folder, json_file_name)
        #with open(json_file_path, 'w', encoding='utf-8') as jsonf:
        #    jsonf.write(json.dumps(data, indent=4))

    def convert_dict_to_json(self):
        pass

    def iterate_over_csv_dict(self, data):
        filtered_dict = []
        for dict in data:
            for value in dict.values():
                if value == self.supervisor:
                    filtered_dict.append(dict)
        return sorted(filtered_dict, key=lambda d: d['project_name'])

    def create_excel_file(self, data):
        path_to_excel = os.path.join(self.reports_folder,  "timesheet.xlsx")
        if not os.path.isfile(path_to_excel):
            self.lib.create_workbook()
            self.lib.save_workbook(path_to_excel)
        self.lib.open_workbook(path=path_to_excel)

        header = ["worktime_duration","date","project_name","task_name","on_call","overtime","invoice_note","first_name","last_name","supervisor","contract_type"]
        row_number = 1
        cell_header = 1
        for r in header:
            self.lib.set_cell_value(row_number, cell_header, r)
            row = 2
            for d in data:
                for key, value in d.items():
                    if key == r:
                        self.lib.set_cell_value(row, cell_header, value)
                        row += 1
            cell_header += 1
        self.lib.save_workbook(path_to_excel)

    # def filter_excel(lib :Files, path_to_excel):
    #     active = lib.set_active_worksheet(path_to_excel)
    #     print(active)
    #     table = active.read_worksheet_as_table(path_to_excel)
    #     print(table)
