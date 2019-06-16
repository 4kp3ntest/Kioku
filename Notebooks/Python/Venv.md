# virtual env
python -m venv testerix
### python2.7
virtualenv -p / usr / bin / python2 .7 -- clear venv_Host
source /venv/bin/activate

#create kernel for jupyter (venv needs to be active!)
pip install ipykernel
python -m ipykernel install --user --name=VenvName

#INSTALL 
pip install pip-autoremove

