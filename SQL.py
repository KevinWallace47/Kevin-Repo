from importlib.metadata import metadata

from sqlalchemy import Column, Integer, String, ForeignKey, Sequence, create_engine, text, MetaData, inspect
from sqlalchemy.dialects.mysql import DOUBLE
from sqlalchemy.orm import sessionmaker, relationship, declarative_base

engine = create_engine('sqlite:///FiveYearWeather.db')

#Initialized the database, also connects you to database
Session = sessionmaker(bind=engine)
session = Session()

Base = declarative_base()

#Base.metadata.drop_all(engine)


#C4 creating a table in SQLite through SQLAlchemy with all listed instance variables
class WeatherData(Base):
    __tablename__ = 'WeatherData'
    id = Column(Integer, Sequence('user_id_seq'), primary_key=True)
    lat = Column(DOUBLE)
    long = Column(DOUBLE)
    month = Column(Integer)
    day = Column(Integer)
    Year = Column(String)
    avg_temp = Column(DOUBLE)
    min_temp = Column(DOUBLE)
    max_temp = Column(DOUBLE)
    avg_wind = Column(DOUBLE)
    min_wind = Column(DOUBLE)
    max_wind = Column(DOUBLE)
    sum_prec = Column(DOUBLE)
    min_prec = Column(DOUBLE)
    max_prec = Column(DOUBLE)

    #Constructor for the class
    def __init__(self, lat, long, month, day, year, avg_temp, min_temp, max_temp, avg_wind, min_wind, max_wind,
                 sum_prec, min_prec, max_prec):
        # Float
        self.lat = lat
        # Float
        self.long = long
        # Int
        self.month = month
        # Int
        self.day = day
        # String
        self.year = '2021 - 2025'
        # Float
        self.avg_temp = avg_temp
        # Float
        self.min_temp = min_temp
        # Float
        self.max_temp = max_temp
        # Float
        self.avg_wind = avg_wind
        # Float
        self.min_wind = min_wind
        # Float
        self.max_wind = max_wind
        # Float
        self.sum_prec = sum_prec
        # Float
        self.min_prec = min_prec
        # Float
        self.max_prec = max_prec
#Update database function, used to insert data into the database
Base.metadata.create_all(engine)
def update_database(
        og_WeatherData
):
    #Inputting SQL weather data class based off the data from the OG weather data.
    new_entry = WeatherData(**vars(og_WeatherData))
    #Adds data to the database
    session.add(new_entry)
    session.commit()

    #prints each row in the database everytime you update database
    with engine.connect() as conn:
        year_update = conn.execute(text("UPDATE WeatherData SET Year = '2021 - 2025'"))
        result = conn.execute(text("SELECT * FROM WeatherData"))
        for row in result:
            print(row)
#Views the tables
def view_tables(

):
    inspector = inspect(engine)
    tables = inspector.get_table_names()
    print(tables)
    return (len(tables))
