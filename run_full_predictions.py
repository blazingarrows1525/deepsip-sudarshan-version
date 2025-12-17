import sys
import pandas as pd
from deepSIP import deepSIP

def main():
    mcnum = int(sys.argv[1]) if len(sys.argv) > 1 else 50
    outname = f"example/predictions_mc{mcnum}.csv"

    s = pd.read_csv('example/spectra.csv')
    print('Loaded spectra rows:', len(s))

    # ensure filenames point to the example/spectra directory
    s['filename'] = 'example/spectra/' + s['filename'].astype(str)

    # run predictions
    model = deepSIP()
    preds = model.predict(s, mcnum=mcnum, status=True)
    print('\nSaving predictions to', outname)
    preds.to_csv(outname, index=False)
    print('Done')

if __name__ == '__main__':
    main()
