### Ubuntu 16.04

```
we need python 3.5.2 minimum
sudo apt-get install build-essential python3-dev python3-venv libpq-dev libev-dev postgresql-9.5-postgis-2.2 binutils libproj-dev gdal-bin
```

### Python Virtualenv

```
python3 -m venv venv
source venv/bin/activate
pip install -r requirements-dev.txt 
```

### Activate Workspace python3

```
source venv/bin/activate
```
