from flask import Flask, request, jsonify
from flask_cors import CORS
import pandas as pd
import io

app = Flask(__name__)
CORS(app)

@app.route('/convert', methods=['POST'])
def convert_csv_to_json():
    try:
        if 'file' not in request.files:
            return jsonify({"error": "No file uploaded"}), 400
        
        file = request.files['file']
        if file.filename == '':
            return jsonify({"error": "Invalid file"}), 400

        csv_data = io.StringIO(file.stream.read().decode('utf-8-sig'))  
        
        df = pd.read_csv(csv_data)
        json_list = df.to_dict(orient='records')  # Python list/dict
        return jsonify({"json": json_list})  # Correctly serialized 
    
    except pd.errors.EmptyDataError:
        return jsonify({"error": "CSV file is empty"}), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == '__main__':
    import os
    port = int(os.environ.get("PORT", 5000))  
    app.run(host='0.0.0.0', port=port)




