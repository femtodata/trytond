trytond
=======

The server of Tryton.
Tryton is business software, ideal for companies of any size, easy to use,
complete and 100% Open Source.
It provides modularity, scalability and security.

Setup
-----

Install Required Packages
++++

- docker: https://docs.docker.com/engine/install/ubuntu/ (or other os)
- pyenv: https://github.com/pyenv/pyenv
  make sure that 3.8.8 is installed:
  ::
     pyenv install 3.8.8
- yarnpkg, via apt or dnf, e.g.,
  ::
     sudo apt install yarnpkg
- docker-compose, via apt or dnf, e.g.,
  ::
     sudo apt install docker-compose


Directory Prep and Clone
++++

Repos will be cloned at the same level as this one, so you might want to clone in a tryton-specific subdirectory:
::
   mkdir femtodata_tryton
   cd femtodata_tryton
   git clone git@github.com:femtodata/trytond.git

Python env setup
++++
Python version, install depdencies
::
   cd trytond

   # assuming python version needed is 3.8.8
   pyenv install 3.8.8

   # create venv
   python -m venv .venv

   # activate venv
   source .venv/bin/activate

   # install setup.py dependencies
   pip install -e .

   # install additional requirements
   pip install -r requirements.txt -r requirements_dev.txt

Tryton web client and modules
++++
- ``env_setup.py`` will clone trytond modules, the sao web client, and symlink them as needed in the trytond directory
  ::
     python -m env_setup
- ``sao`` is the web client, written in node.js. We will use `yarn` to install and run requirements, which provides better separation than ``npm``:
  ::
     cd sao
     yarn install
     yarn run grunt

     # remember to back out to trytond directory
     cd ..


Startup: docker setup, tryton admin setup
++++
- ``docker-compose.yml`` defines the postgres and pgadmin services
  ::
     docker-compose up -d
- if you want to see their logs, you can do:
  ::
     docker-compose logs -f
- trytond-admin to initialize db, set admin password (currently defined in ``trytonpass``)
  ::
     TRYTONPASSFILE=trytonpass ./bin/trytond-admin -v -c trytond.conf -d tryton --email admin@tryton --all

Run
++++
Run via ``trytond``
::
   ./bin/trytond -v -c trytond.conf

- Navigate to http://localhost:8000
- login is ``admin``, password in ``trytonpass`` file
- To restart server again, just make sure the docker containers are running, and run ``trytond`` again:
  ::
     docker-compose up -d
     ./bin/trytond -v -c trytond.conf


Pgadmin
++++
- access the pgadmin tool at http://localhost:8083 , login details in ``docker-compose.yml`` (e.g., ``admin@pgadmin.com/admin``)
- add a server with the connection details also found in ``docker-compose.yml``:
  - hostname: postgres
  - username: amplayer
  - password: amplayerdev

Reset
++++
You can reset everything by deleting the docker volume that contains the postgres db, and recreating:
::
   docker-compose down
   docker volume rm trytond_postgres
   docker-compose up -d
   TRYTONPASSFILE=trytonpass ./bin/trytond-admin -v -c trytond.conf -d tryton --email admin@tryton --all
   ./bin/trytond -v -c trytond.conf
