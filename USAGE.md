# Usage

Quick examples to run the helper scripts included in this repo.

Run the small example (first 3 spectra):

```powershell
& .venv\Scripts\python.exe run_example.py
```

Run full predictions on `example/spectra.csv` (adjust `mcnum` for accuracy):

```powershell
& .venv\Scripts\python.exe run_full_predictions.py 200
```

Output files are written to the `example/` directory as `predictions_mc{mcnum}.csv`.
