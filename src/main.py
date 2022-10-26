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
    supervisor = supervisor.replace("/", " ")
    leikki_url = f"https://backendforrobot.herokuapp.com/api/schedule{start_date}{end_date}"
    print(leikki_url)

    url = "https://backendforrobot.herokuapp.com/api/schedule"
    
    create_excel = CreateExcel(url, supervisor)
    create_excel.download_csv_file()
    data_from_csv = create_excel.get_data_from_csv()
    filtered_data_dict = create_excel.iterate_over_csv_dict(data_from_csv)
    print(filtered_data_dict)
    create_excel.create_excel_file(filtered_data_dict)

    # change workhours cells into integer
    create_excel.change_excel()

