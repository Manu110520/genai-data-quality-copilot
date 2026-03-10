import pandas as pd
import sys

path = "data/sample.xlsx"
engines = ['openpyxl','xlrd','pyxlsb']
for eng in engines:
    try:
        print('Trying', eng)
        df = pd.read_excel(path, engine=eng)
        print('OK', eng, 'shape', df.shape)
        sys.exit(0)
    except Exception as e:
        print('Error', eng, ':', type(e).__name__, str(e))

print('All attempts failed')
sys.exit(2)
