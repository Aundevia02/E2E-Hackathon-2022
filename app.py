from flask import Flask, render_template, request, redirect, url_for
from flask_googlemaps import GoogleMaps
from flask_googlemaps import Map

app = Flask(__name__, template_folder="html")

GoogleMaps(app, key="AIzaSyDXc9W874xRGVHWAtpeBcKokoa4VVYeBC8")

@app.route("/landing")
@app.route("/")
def searchid():
    return render_template("landing_page.html")

@app.route("/map",methods = ['POST'])
def mapredir():
    # validate input data
    userid = request.form['userid']
    # validate(id)
    # getData(id)
    return redirect(url_for('mapview', id=userid))

@app.route("/map/<id>")
def mapview(id):
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
    print(id)
    return render_template('map_display.html', userid=id, mymap=mymap, sndmap=sndmap)

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

