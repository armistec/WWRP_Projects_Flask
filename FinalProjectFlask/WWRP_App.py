from flask import Flask, render_template, request, redirect, url_for, flash
import pickle
import pandas as pd
import shapely, shapely.geometry, fiona, fiona.crs, pandas, folium, geopandas

app = Flask(__name__)

#Homepage
@app.route('/')
def index():
	res = 'WWRP Project Map'
	return render_template("profile.html" , output1=res)

#Submit user form, store data for predict
@app.route('/ProgramType', methods=['POST'])
def ProgramType():
	
	# Store inputs from form
	p=request.form['program']

	# Unpickle dataframe - currently stored locally
	df = pd.read_pickle("C:\\Users\\CorrineArmistead\\Desktop\\PickleWWRP_FlaskTest.pk1")

	if p == 'local parks':
		points = df[df['program']=='local parks']
	if p == 'state parks':
		points = df[df['program']=='state parks']
	if p == 'habitat restoration':
		points = df[df['program']=='habitat restoration']

	locations = points[['lat', 'long']]
	locationlist = locations.values.tolist()

	map1 = folium.Map(location=[47, -120], zoom_start=6)

	for point in range(0, len(locationlist)):
	    folium.Marker(locationlist[point]).add_to(map1)

	map1.save('C:\\Users\\CorrineArmistead\\Desktop\\FinalProjectFlask\\templates\\map.html')

	return render_template('index.html')

	##if p == 'state parks':
		##display state parks points
	##if p == 'habitat restoration':
		##Display habitat projects

if __name__ == "__main__":
	app.run(debug=True)