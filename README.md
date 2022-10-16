Wine Quality Web Application Deployed over Heroku
```bash
https://wine-27-project.herokuapp.com/
```
create env 

```bash
conda create -n wineq python=3.9 -y
```

activate env
```bash
conda activate wineq
```

created a req file

install the req
```bash
pip install -r requirements.txt
```


```bash
git init
```
```bash
dvc init 
```
```bash
dvc add data_given/winequality.csv
```
```bash
git add .
```
```bash
git commit -m "first commit"
```

oneliner updates  for readme

```bash
git add . && git commit -m "update Readme.md"
```
```bash
git remote add origin https://github.com/Agasthya23/dvc-practise9.git
git branch -M main
git push origin main
```

tox command -
```bash
tox
```
for rebuilding -
```bash
tox -r 
```
pytest command
```bash
pytest -v
```

setup commands -
```bash
pip install -e . 
```

build your own package commands- 
```bash
python setup.py sdist bdist_wheel
```
