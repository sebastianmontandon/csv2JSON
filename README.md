# Welcome to csv2JSON converter 

This module give the chance to conver any CSV file to JSON, yo can specify encoding for csv files.

## Usage

To use this module, just need to copy the module to your proyect and then import the module in your code when you need it
```python
from convert import convert_csv_2_json

# initial parameters
import_path = os.path.join(os.getcwd(), 'import files')
export_path = os.path.join(os.getcwd(), 'export files')
encode = 'UTF-8'

# just use when need it
convert_csv_2_json(import_path, export_path, encode)
```

## Contributing

Pull requests are welcome. For major changes, please open an issue first
to discuss what you would like to change.

This is a practice proyect so, maybe have changes in the future