import requests, argparse, csv, json, os, robot.api.logger as logger
from robot.libraries.BuiltIn import BuiltIn
#import robot.api.logger as logger



# Download .csv file
def download_csv_file(url):
    pass

def convert_csv_file_to_json(csv):
    pass

def iterate_over_json(json):
    pass

# convert .csv to excel


# data analyysi


# robot framework


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
        logger.warn("You are missing the supervisor!")
    
    url = ''