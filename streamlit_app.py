import streamlit as st
import requests
import json

st.title("CSV to JSON Converter")

with st.expander("📚 Project Details"):
    st.markdown("""
    **🌐 Project Description**
    
    This application is a 🚀 modern tool that converts CSV files to JSON format. 
    It uses a ⚙️ two-tier architecture with Flask API in the backend.

    **🛠 Technical Details**
    
    - Backend: Flask (🐍 Python Web Framework)
    - Frontend: Streamlit (📊 Data Application Interface)
    - Data Conversion: Pandas 📈 library
    - CORS Management: flask-cors 🌐

    **⚙️ How It Works?**
    
    1. 📤 User uploads a CSV file
    2. 🔄 Streamlit sends the file to Flask API
    3. 🧠 Flask converts CSV to JSON using Pandas
    4. 📥 Result is displayed and available for download

    **⚠️ Important Notes**
    - 🔌 Ensure the API server is running
    - 📄 CSV files must be in UTF-8 format
    - 🐢 Conversion time may increase for large files (100MB+)
    - 🔒 Be cautious with sensitive data during conversion
    """)

uploaded_file = st.file_uploader("Upload CSV file", type="csv")

if uploaded_file is not None:
    try:
        response = requests.post(
            'https://csv-to-json-converter-backend.onrender.com/convert',
            files={'file': (uploaded_file.name, uploaded_file, 'text/csv')}
        )
        
        if response.status_code == 200:
            json_data = response.json().get('json')  # This is a Python list/dict
    
    # Display JSON
            st.json(json_data)
    
    # Convert to JSON string for downloading
            json_str = json.dumps(json_data, indent=2)

            st.download_button(
                label="Save JSON",
                data=json_str,  # Pass the string, not the list/dict
                file_name=uploaded_file.name.replace(".csv", ".json"),
                mime="application/json"
            )
                    
        else:
            st.error(f"Error: {response.json().get('error', 'Unknown error')}")
    
    except requests.exceptions.ConnectionError:
        st.error("API server is not running. Please start Flask first.")
    except Exception as e:
        st.error(f"Unexpected error: {e}")
