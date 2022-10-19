import argparse, robot.api.logger as logger
from Objects.create_excel import CreateExcel


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Description of your program')
    parser.add_argument('-start','--start-date', help='Description for foo argument', required=True)
    parser.add_argument('-end','--end-date', help='Description for bar argument', required=True)
    parser.add_argument('-s','--supervisor', help='Description for bar argument', required=False)
    args = vars(parser.parse_args())
    start_date = args['start_date'] 
    end_date = args['end_date']
    supervisor = (args['supervisor'] or None)
    if supervisor == None:
        logger.error("You are missing the supervisor!")
    
    url = "https://backendforrobot.herokuapp.com/api/schedule"
    
    create_excel = CreateExcel(url, supervisor)
    data_dict = create_excel.download_csv_file()
    filtered_data_dict = create_excel.iterate_over_csv_dict(data_dict)
    create_excel.create_excel_file(filtered_data_dict)
    
    #path_to_excel = os.path.join(work_path,  "timesheet.xlsx")
    #filter_excel(lib, path_to_excel)

