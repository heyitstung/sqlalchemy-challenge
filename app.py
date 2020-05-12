from sqlalchemy import create_engine
from sqlachemy.ext.declarative import declarative_base
from sqlalchemy.ext.automap import automap_base
from flask import Flask, jsonify

engine = create_engine("sqlite:///hawaii.sqlite")

Base = automap_base()

Measurement = Base.classes.measurement
Station = Base.classes.station

app = Flask(__name__)

@app.route("/")
def main():
     return (
        f"Available Routes:<br/>"
        f"/api/precipitation<br/>"
        f"/api/stations<br/>"
        f"/api/tobs<br/>"
        f"/api/<start><br/>"
        f"/api/<start>/<end>"
    )


session.measurements = [func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs), func.count(Measurement.tobs))]

return measurement