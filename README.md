# ProtectedHaven
Website linked with a QR code used for foreigners in Ulsan, Korea to report crimes easier. Mostly women in international marriages

## How to run the development site

- Install Postgresql (if you don't have it installed already)
- create a 'protected_haven' database
- run 'python3 -m venv venv' to create a virtual environment
- run 'source venv/Scripts/activate' to acivate the virtual environment
- run 'pip install -r requirements.txt' to install all dependencies
- run 'export FLASK_ENV=development' to put Flask in development mode
- run 'py seed.py'
- run 'flask run' to start the server