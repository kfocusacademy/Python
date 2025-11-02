# DataScience

DataScience starter folder

## What this contains
- `requirements.txt` — common Data Science Python libraries to install in a virtualenv.
- `example_analysis.py` — small self-contained script that loads the Iris dataset, prints basic info, and writes a scatter plot to `DataScience/iris_scatter.png`.

## Quick start (PowerShell)
```powershell
cd 'c:\Ravi\Python\python'
python -m venv .venv
.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install -r DataScience\requirements.txt
# Run the example script
python DataScience\example_analysis.py
```

## Notes
- The `requirements.txt` pins minimal versions to be reasonably modern; adjust as needed for your environment.
- The example script writes an image file to `DataScience/iris_scatter.png`. If running in an environment without a display, the script uses a non-interactive matplotlib backend.
- To use Jupyter, run `jupyter lab` or `jupyter notebook` after activating the venv.
