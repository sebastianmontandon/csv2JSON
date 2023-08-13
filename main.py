import os
from convert import convert_csv_2_json


import_path = os.path.join(os.getcwd(), 'import files')
export_path = os.path.join(os.getcwd(), 'export files')
encode = 'UTF-8'

convert_csv_2_json(import_path, export_path, encode)
