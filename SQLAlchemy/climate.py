

from flask import Flask, json, jsonify
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
from sqlalchemy import inspect

engine = create_engine("sqlite:///Resources/hawaii.sqlite")

Base = automap_base()
Base.prepare(engine, reflect=True)

Measurement = Base.classes.measurement
Station = Base.classes.station
session = Session(engine)

app = Flask(__name__)

@app.route('/')
def home():
    return (f"Enter Available Route Endpoints.  Where dates are required, modify date selection as desired: <br><br/>"
        f"1.   2017 Dates and Temperature Dictionary:   <br/>"
        f"   /api/v1.0/precipitation/ <br><br/>" 
        f"2.   JSON list of Weather Stations:    <br/>"
        f" /api/v1.0/stations/ <br><br/>" 
        f"3.    2017 JSON list of Temperature Observations:  <br/>"
        f" /api/v1.0/tobs/ <br><br/>"
        f"For the following, enter date as form 'yyyy' or 'yyyy-mm' or 'yyyy-mm-dd' for BEST RESULTS! <br><br/>"
        f"4.    Stats Combined Stations. Enter Start date:  <br/>"
        f" /api/v1.0/2016-01-01/ <br><br/>" 
        f"5.    Stats Combined Stations. Enter Start & End Date:  <br/>"
        f" /api/v1.0/2016-01-01/2016-12-31/ <br><br/>"
    
@app.route('/api/v1.0/precipitation/')
def precipitation():
    prcp_results = session.query(Measurement.date, Measurement.tobs)\
    .filter(Measurement.date >= '2017-01-01').all()
    p_dict = dict(prcp_results)
    print()
    print("Results for Precipitation")
    return jsonify(p_dict) 

@app.route('/api/v1.0/stations/')
def stations():
    station_list = session.query(Station.station)\
    .order_by(Station.station).all() 
    print()
    print("Station List:")   
    for row in station_list:
        print (row[0])
    return jsonify(station_list)

@app.route('/api/v1.0/tobs/')
def tobs():
    temp_obs = session.query(Measurement.tobs)\
    .order_by(Measurement.date).all()
    print()
    print("Temperature for All Stations")
    return jsonify(temp_obs)

@app.route('/api/v1.0/<start>/')
def combined_start_stats(start):
    q = session.query(Station.id,
                  Station.station,
                  func.min(Measurement.tobs),
                  func.max(Measurement.tobs),
                  func.avg(Measurement.tobs))\
                  .filter(Measurement.station == Station.station)\
                  .filter(Measurement.date >= start).all()                  
    print()
    print("Query Temps Combined Stations with Start ({start}) Date")
    for row in q:
        print()
        print(row)
    return jsonify(q)


@app.route('/api/v1.0/<start>/<end>/')
def combined_start_end_stats(start,end):
    q = session.query(Station.id,
                  Station.station,
                  func.min(Measurement.tobs),
                  func.max(Measurement.tobs),
                  func.avg(Measurement.tobs))\
                  .filter(Measurement.station == Station.station)\
                  .filter(Measurement.date <= end)\
                  .filter(Measurement.date >= start).all()
    print()
    print(f"Query Temps Combined Stations with Start ({start}) and End ({end}) Date")
    for row in q:
        print()
        print(row)
    return jsonify(q)

