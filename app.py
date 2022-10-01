from flask import Flask, flash, render_template, request, redirect, url_for
from flask_googlemaps import GoogleMaps
from flask_googlemaps import Map
import csv
from test import to_csv

app = Flask(__name__, template_folder="html")


class CodeInfo:
    def __init__(self, code, lat, lng, type_emer):
        self.code = code
        self.lat = lat
        self.long = lng
        self.type = type_emer

    def get_code(self):
        return self.code

    def get_lat(self):
        return self.lat

    def get_lng(self):
        return self.long

    def get_type_emer(self):
        return self.type_emer
    # def __str__(self):
    #     return f"{self.lat}, {self.long}, {self.type_emer}"


def to_csv(name):
    import csv

    dict_from_csv = {}
    data = []

    with open(name, mode='r') as inp:
        reader = csv.reader(inp)
        dict_from_csv = {rows[0]: CodeInfo(rows[0], rows[1], rows[2], rows[3])
                         for rows in reader}

    return dict_from_csv


code_dict = to_csv('codes.csv')

GoogleMaps(app, key="AIzaSyDXc9W874xRGVHWAtpeBcKokoa4VVYeBC8")


@app.route("/landing")
@app.route("/")
def searchid():
    return render_template("landing_page.html")


@app.route("/map", methods=['POST'])
def mapredir():
    # validate input data
    userid = request.form['userid']
    # validate(id)

    code_info = code_dict.get(userid)

    if (code_info == None):
        return render_template("landing_page.html")
    else:
        # getData(id)
        return redirect(url_for('mapview', uid=userid))


@ app.route("/map/<uid>")
def mapview(uid):
    # get CodeInfo object from uid
    u_code_info = code_dict.get(uid)

    # creating a map in the view
    mymap = Map(
        identifier="view-side",
        lat=37.4419,
        lng=-122.1419,
        markers=[(37.4419, -122.1419)]
    )
    sndmap = Map(
        identifier="sndmap",
        lat=37.4419,
        lng=-122.1419,
        markers=[
            {
                'icon': 'http://maps.google.com/mapfiles/ms/icons/green-dot.png',
                'lat': 37.4419,
                'lng': -122.1419,
                'infobox': "<b>Hello World</b>"
            },
            {
                'icon': 'http://maps.google.com/mapfiles/ms/icons/blue-dot.png',
                'lat': 37.4300,
                'lng': -122.1400,
                'infobox': "<b>Hello World from other place</b>"
            }
        ]
    )
    # print(id)
    return render_template('map_display.html', mymap=mymap, sndmap=sndmap, userid=u_code_info.code, code_info=u_code_info)


if __name__ == "__main__":
    app.run(debug=True)


# from flask_cors import CORS
# from flask import Flask, jsonify, render_template

# from processdata import processdata

# app = Flask(__name__)
# CORS(app)
# # In this case, the URL route is 'displaylocations'.


# @app.route('/displaylocations')
# def displaylocations():
#     # Obtain the CSV data.
#     l = processdata()
#     # Forward the data to the source that called this API.
#     return jsonify(l)

# @app.route('/')
# def main():
#     return render_template('index.html')
