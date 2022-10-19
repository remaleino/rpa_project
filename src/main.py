import requests, argparse, csv, json, urllib, os, robot.api.logger as logger
from robot.libraries.BuiltIn import BuiltIn
#import robot.api.logger as logger

def download_csv_file(url: str, dest_folder:str, file_name: str):
    if not os.path.exists(dest_folder):
        os.makedirs(dest_folder)
    file_path = os.path.join(dest_folder, file_name)
    r = requests.get(url, stream=True)
    if r.ok:
        with open(file_path, 'wb') as f:
             for chunk in r.iter_content(chunk_size=1024 * 8):
                if chunk:
                    f.write(chunk)
                    f.flush()
                    os.fsync(f.fileno())
    else:
        print("Download failed")

def csv_to_json_converter():
    url = "https://backendforrobot.herokuapp.com/api/schedule"
    dest_folder = "reports"
    csv_file_name = "csvReport.csv"
    json_file_name = "jsonReport.json"
    csv_file_path = os.path.join(dest_folder, csv_file_name)
    json_file_path = os.path.join(dest_folder, json_file_name)
    download_csv_file(url, dest_folder, csv_file_name)
    data = {}
    with open(csv_file_path, 'r') as csvFile:
        dict_reader = csv.DictReader(csvFile)
        l = list(dict_reader)
        data = l
    #Return dictionary
    return(data)
    #TO JSON-file
    #with open(json_file_path, 'w', encoding='utf-8') as jsonf:
    #    jsonf.write(json.dumps(data, indent=4))

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