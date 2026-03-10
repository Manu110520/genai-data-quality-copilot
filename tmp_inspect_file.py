path = 'data/sample.xlsx'
with open(path, 'rb') as f:
    h = f.read(512)

print('First 64 bytes (hex):', h[:64].hex())
print('First 64 bytes (repr):', repr(h[:64]))
try:
    print('Text preview:', h.decode('utf-8', errors='replace')[:300])
except Exception as e:
    print('Decode error:', e)
