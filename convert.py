import json
import csv
import os
from rich import print

def convert_csv_2_json(input_path, output_path, encoding):
    """ This function obtain 3 parameters,
            input_path:     Path where do you need to put you .csv files to convert
            output_path:    Path where do you need to export converted files
            encoding:       Encode tipe(example, UTF-8)

        Console return:
            Welcome menssage,
            List of all files converted
            Final message with exported files path
    """
    list_of_files = os.listdir(input_path)
    print(f'\nWelcome to csv2json\n')
    for file in list_of_files:
        file_name = str(file).replace('.csv', '')
        file_path = input_path +'\\'+ file
        with open(file_path, 'r', encoding=encoding) as file:
            with open(output_path +"\\"+ file_name +".json", "w",encoding=encoding,) as write_json:
                render = csv.DictReader(file, delimiter=";", doublequote=True)
                json.dump(list(render), write_json,indent = 4, ensure_ascii=False, sort_keys=True)
        print(f'Convertion to {file_name}, finished OK!')
    print(f'\nFind your files on {os.path.join(os.getcwd(), "export files")}\n')