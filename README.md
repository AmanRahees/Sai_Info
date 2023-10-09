## Getting Started
To get started you can simply clone this project repository and install the dependencies.

Clone the Sai_Info repository using git:
```python
git clone https://github.com/AmanRahees/Sai_Info.git
cd Sai_Info
```

Create a virtual environment to install dependencies in and activate it:
```python
python3 -m venv env
source env/bin/activate
```

Then install the dependencies:
```python
(env) pip install -r r.txt
```

Once ```pip``` has finished downloading the dependencies:
```python
cd expose
python3 manage.py makemigrations
python3 manage.py migrate
python3 manage.py runserver
```
