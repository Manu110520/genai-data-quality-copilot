import pandas as pd
import os

df = pd.DataFrame({'customer_id':[1,2,2,3],'exposure':[10, -5, 3, 0]})
path = 'data/sample.xlsx'
df.to_excel(path, index=False)
print('Wrote', path, 'size', os.path.getsize(path))
