# Import the dependencies.
# import datetime as dt
import numpy as np
import pandas as pd 
import json
from sqlalchemy import create_engine, text, inspect
from flask import Flask, render_template, redirect


#################################################
# Flask Setup
#################################################
app = Flask(__name__)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0
#################################################
# Database Setup
#################################################
engine = create_engine("sqlite:///data/Map_data.sqlite")

# Route to render index.html template using data from Mongo
@app.route("/")
def home():
    # Return template and data
    return render_template("index.html")

@app.route("/about_us")
def about_us():
    # Return template and data
    return render_template("about_us.html")

@app.route("/dashboard")
def plotly():
    # Return template and data
    return render_template("dashboard.html")



@app.route("/df_profile")
def df_profile():
    # Return template and data
    return render_template("df_profile.html")

##########################################################################

@app.route("/api/v1.0/country_count")
def country_count():
    """Get country"""
    query = text(f"""
                SELECT
                    Country,
                    count(Country) as num_country
                FROM
                    Map_data
                
                group by
                   Country;
            """)

    df = pd.read_sql(query, engine)
#     # df.info()
#     # df2 = df.volcano_name.value_counts().reset_index()
#     # df2.columns = ["volcano_name", "counts"]

    data = json.loads(df.to_json(orient="records"))
#     # data2 = json.loads(df2.to_json(orient="records"))

#     # return({"raw_data": data, "volcanoes": data2})
    return data
###############################################################

@app.route("/api/v1.0/country__region")
def country_region():
    """Get country_region"""
    query = text(f"""
                SELECT
                    Region,
                    Country,
                    count(*) as country_count
                FROM
                    Map_data
                
                group by
                   Country, Region;
            """)

    df = pd.read_sql(query, engine)
#     # df.info()
#     # df2 = df.volcano_name.value_counts().reset_index()
#     # df2.columns = ["volcano_name", "counts"]

    data = json.loads(df.to_json(orient="records"))
#     # data2 = json.loads(df2.to_json(orient="records"))

#     # return({"raw_data": data, "volcanoes": data2})
    return data
#######################################################################
@app.route("/api/v1.0/episode__show")
def episode__show():
    """Get episode__show , shows in each region"""
    query = text(f"""
                SELECT
                    Episode,
                    Country,
                    Region,
                    Show,
                    Season,
                    COUNT(DISTINCT show) as shows_in_region
                FROM
                    Map_data
                
                group by
                   Country, Episode
                AND Show
                AND Season;
                
            """)

    df = pd.read_sql(query, engine)
#     # df.info()
#     # df2 = df.volcano_name.value_counts().reset_index()
#     # df2.columns = ["volcano_name", "counts"]

    data = json.loads(df.to_json(orient="records"))
#     # data2 = json.loads(df2.to_json(orient="records"))

#     # return({"raw_data": data, "volcanoes": data2})
    return data
####################################################################
@app.route("/api/v1.0/show_count")
def show_count():
    """Get show"""
    query = text(f"""
                SELECT
                    Show,
                    count(Show) as num_show
                FROM
                    Map_data
                
                group by
                   Show;
            """)

    df = pd.read_sql(query, engine)
    # df.info()
    # df2 = df.Show.value_counts().reset_index()
    # df2.columns = ["volcano_name", "counts"]

    data1 = json.loads(df.to_json(orient="records"))
    # data2 = json.loads(df2.to_json(orient="records"))

    # return({"raw_data": data, "volcanoes": data2})
    return data1

###########################################################################
@app.route("/api/v1.0/region_count")
def region_count():
    """Get Region"""
    query = text(f"""
                SELECT
                    Region,
                    count(Region) as num_region
                FROM
                    Map_data
                
                group by
                   Region;
            """)

    df = pd.read_sql(query, engine)
    # df.info()
    # df2 = df.volcano_name.value_counts().reset_index()
    # df2.columns = ["volcano_name", "counts"]

    data2 = json.loads(df.to_json(orient="records"))
    # data2 = json.loads(df2.to_json(orient="records"))

    # return({"raw_data": data, "volcanoes": data2})
    return data2
##########################################################################
@app.route("/api/v1.0/city_count")
def city_count():
    """Get Region"""
    query = text(f"""
                SELECT
                    City,
                    count(City) as num_city
                FROM
                    Map_data
                
                group by
                   City;
            """)

    df = pd.read_sql(query, engine)
    # df.info()
    # df2 = df.volcano_name.value_counts().reset_index()
    # df2.columns = ["volcano_name", "counts"]

    data3 = json.loads(df.to_json(orient="records"))
    # data2 = json.loads(df2.to_json(orient="records"))

    # return({"raw_data": data, "volcanoes": data2})
    return data3

######################################################################
@app.route("/api/v1.0/map_data")
def map_data():
    """Get Region"""
    query = text(f"""
                SELECT
                    *
                FROM
                    Map_data
                
                
            """)

    df = pd.read_sql(query, engine)
    # df.info()
    # df2 = df.volcano_name.value_counts().reset_index()
    # df2.columns = ["volcano_name", "counts"]

    data3 = json.loads(df.to_json(orient="records"))
    # data2 = json.loads(df2.to_json(orient="records"))

    # return({"raw_data": data, "volcanoes": data2})
    return data3


#######################################################################
@app.route("/api/v1.0/dashboard_data/<show>")
def dashboard_data(show):
    """Get show"""
    if show != "All":
        query = text(f"""
                    SELECT
                        *
                    FROM
                        Map_data
                    WHERE
                    Show = "{show}";
                """)
    else:
        query = text(f"""
            SELECT
                *
            FROM
                Map_data;
        """)

    df = pd.read_sql(query, engine)
    
    df2 = df.Season.value_counts().reset_index()
    df2.columns = ["season", "counts"]

    df3 = df.Region.value_counts().reset_index()
    df3.columns = ["region", "counts"]

    data = json.loads(df.to_json(orient="records"))
    data2 = json.loads(df2.to_json(orient="records"))
    data3 = json.loads(df3.to_json(orient="records"))

    return({"raw_data": data, "seasons": data2, "regions": data3})
    
##########################################################################

@app.after_request
def add_header(r):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also to cache the rendered page for 10 minutes.
    """
    r.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    r.headers["Cache-Control"] = "no-cache, no-store, must-revalidate, public, max-age=0"
    r.headers["Pragma"] = "no-cache"
    r.headers["Expires"] = "0"
    return r

#main
if __name__ == "__main__":
    app.run(debug=True)
