import pandas as pd
from deepSIP import deepSIP

# load example spectra CSV
s = pd.read_csv('example/spectra.csv')
print('Loaded spectra rows:', len(s))
# take a small subset to keep runtime short
s = s.head(3)
print(s)

# ensure filenames point to the example/spectra directory
s['filename'] = 'example/spectra/' + s['filename'].astype(str)
print('\nUsing filenames:')
print(s['filename'])

# instantiate model and predict
model = deepSIP()
preds = model.predict(s, mcnum=5, status=True)
print('\nPredictions:')
print(preds)
