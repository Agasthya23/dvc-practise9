created environment
'''bash
conda create -n wine27 python=3.9 -y
'''

activate env
'''bash
conda activate wine27
'''

created requirments.txt and installed it
'''bash
pip install -r requirements.txt
'''
create template.py
write code to create directories and files

create another directory for the given data and paste the csv file
'''
mkdir data_given
'''

initialize git and dv
'''
git init
dvc init
'''

add given data to dvc to track
'''
dvc add data_given\winequality.csv
'''

'''
git add .

git commit -m "first commit"
'''

git remote add origin https://github.com/Agasthya23/dvc-practise9.git
git branch -M main
git push origin main
