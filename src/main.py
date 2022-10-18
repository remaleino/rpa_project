import requests, sys, argparse

# Download .csv file
def download_csv_file(url):
    pass



# convert .csv to excel


# data analyysi


# robot framework


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Description of your program')
    parser.add_argument('-start','--start-date', help='Description for foo argument', required=True)
    parser.add_argument('-end','--end-date', help='Description for bar argument', required=False)
    parser.add_argument('-s','--supervisor', help='Description for bar argument', required=False)
    args = vars(parser.parse_args())

    start_date = args['start_date']
    end_date = args['end_date']
    supervisor = args['supervisor']

    print(start_date)
    print(end_date)
    print(supervisor)