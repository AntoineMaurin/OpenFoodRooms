from database.database_populating import DatabasePopulating
from API.data_from_api import DataFromApi

setup = DatabasePopulating()
data = DataFromApi()

setup.create_tables()

# Receives data from API and adds it in database
data.request()
