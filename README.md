
### 
```
pyenv install 3.8.8

python -m venv .venv

source .venv/bin/activate

pip install -e .

pip install -r requirements.txt -r requirements_dev.txt

python -m env_setup

cd sao

yarn install

yarn run grunt

docker-compose up -d

TRYTONPASSFILE=trytonpass ./bin/trytond-admin -v -c trytond.conf -d tryton --email admin@tryton --all

./bin/trytond -v -c trytond.conf
```
