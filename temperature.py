from flask import Flask, jsonify, request
app = Flask(__name__)

temperature = [

	{
		"TEMP_ID" : "A001",
		"DATE" : "October 4, 2022",
		"TEMPERATURE" : "36.5 Degree Celsius"
	}
]

@app.route ('/temperature', methods=['GET'])
def getTemperature():
    return jsonify(temperature)


@app.route ('/temperature', methods= ['POST'])
def addTemperature():
	temperature = request.get_json()
	temperature.append(temperature)
	return{'id': len(temperature)},200

@app.route('/movies/<int:index>' , methods= ['DELETE'])
def deleteTemperature(index):
	temperature.pop(index)
	return 'Record was deleted', 200

if __name__ == '__main__' :
    app.run()
