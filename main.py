from flask import Flask, jsonify
from flask.globals import request
from flask_cors import CORS
from datetime import datetime
import json
import collection as collection
import tensorflow as tf



app = Flask(__name__)
app.config['SECRET_KEY'] = 'abc12345'

CORS(app, resources={r'/api/*' : {'origins' : '*'}})



@app.route('/api/v1/predict', methods=['POST'])
def prediction():
    try:
        data = request.form["trans_data"]
        to_json = json.loads(data)
        fc_prop = collection.Collection.color_properties(to_json['first_color'])
        sc_prop = collection.Collection.color_properties(to_json['second_color'])


        fc_rgb = fc_prop['rgb']
        sc_rgb = sc_prop['rgb']

        fc_hex = fc_prop['hex']
        sc_hex = sc_prop['hex']

        normalize_fc_rgb = [float(fcr) / 255.0 for fcr in fc_rgb]
        normalize_sc_rgb = [float(scr) / 255.0 for scr in sc_rgb]

        color_pair = to_json['first_color'] + '_' + to_json['second_color']

        inputData = [[normalize_fc_rgb, normalize_sc_rgb]]

        # model = tf.keras.models.load_model('C:/Personal File/code/sample-project/api-prediksi-warna-batik/model_simple_rnn/model_prediksi_warna.h5')
        model = tf.keras.models.load_model('./model_simple_rnn/model_prediksi_warna.h5')

        real_hex_mix = collection.Collection.mixed_color_hex(color_pair)

        prediction = model.predict(inputData)

        # print(prediction)
        getPrediction = [prediction[0][0], prediction[0][1], prediction[0][2]]

        getPrediction = [int(val * 255.0) for val in getPrediction]


        # print(getPrediction)

        convertToHex = collection.Conversion.rgb_to_hex(getPrediction[0], getPrediction[1], getPrediction[2])
        

        result = {
            'msg' : 'prediction process complete',
            'data' : {
                'first_color_hex' : fc_hex,
                'second_color_hex' : sc_hex,
                'predicted_mix_color' : convertToHex,
                'real_mix_color' :  real_hex_mix
            },
            'status' : 200
        }

        return jsonify({'result' : result}), 200
    
    except:
        return jsonify({'msg' : 'prediction timeout'}), 400

if __name__ == '__main__':
    app.debug = True
    app.run()
