# portable-python-code-generator

Using [Daoguang/PyCodeGPT](https://github.com/microsoft/PyCodeGPT) to run Python code generator offline. Uses CPU instead of GPU.

Created working example from [issue](https://github.com/microsoft/PyCodeGPT/issues/8)

## Getting Started

Guide made using Windows 11.

### Requirements

- Python version 3.7-3.9 (PyTorch limits)

### Venv

Refresher on Python virtual environment.

```powershell
python -m venv venv # Create virtual environment
.\venv\Scripts\activate # Activate virtual environment
deactivate # Deactivate virtual environment
```

## Running the application

```powershell
python -m pip install -r requirements.txt # Install dependencies if not installed yet
python main.py # Downloads PyTorch model if not downloaded yet and runs the app/script
```
