re# ProtectedHaven
Website linked with a QR code used for foreigners in Ulsan, Korea to report crimes easier. Mostly women in international marriages

## How to run the development site

- Install Postgresql (if you don't have it installed already)
- run 'createdb protected_haven' to create a database
- run 'python3 -m venv venv' to create a virtual environment 
- run 'source venv/Scripts/activate' to acivate the virtual environment
  (On Windows, run the above on bash or run the alternative 'venv/Scripts/activate.ps1')
- run 'pip install -r requirements.txt' to install all dependencies
- run 'export FLASK_ENV=development' to put Flask in development mode
- run 'python3 seed.py' to generate and input data to our new database
- run 'flask run' to start the server
