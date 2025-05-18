# 📁 CSV to JSON Converter Web Application

This is a simple and user-friendly web app that allows you to convert `.csv` files into `.json` format in just a few clicks. It's ideal for developers, data analysts, and anyone who works with structured data.

---

## 🚀 About the Project

CSV (Comma-Separated Values) is a popular format for storing tabular data, but modern web services and applications often prefer **JSON (JavaScript Object Notation)**. With this tool, you can easily convert your CSV data to JSON format—no programming skills required!

### Key Features

- 👨‍💻 Simple and intuitive web interface
- 📤 Upload a CSV file and instantly convert it
- 📄 View the resulting JSON directly in the browser
- 💾 Download the converted JSON file
- ❌ Clear error messages for invalid or empty files

---

## 🔧 How to Use

1. Open the web interface.
2. Select and upload a `.csv` file from your device.
3. The app sends the file to a backend server and converts it.
4. View or download the resulting `.json` file.

---

## 💻 Technologies Used

| Technology     | Purpose                                           |
|----------------|---------------------------------------------------|
| **Streamlit**  | Builds the user interface (frontend)              |
| **Flask**      | Handles file processing and conversion (backend)  |
| **Pandas**     | Reads and transforms CSV data into JSON format    |
| **requests**   | Sends HTTP requests between frontend and backend  |
| **flask-cors** | Enables secure communication between components   |

---

## ⚙️ Getting Started

To run the app locally:

```bash
pip install -r requirements.txt
```

Start the Flask backend:

```bash
python flask_app.py
```

Then launch the Streamlit frontend:

```bash
streamlit run streamlit_app.py
```

---

## 🧪 Example Workflow

1. User uploads a CSV file via Streamlit UI
2. Streamlit sends the file to the Flask API
3. Flask processes and converts the file to JSON
4. Streamlit displays the output and offers download
---

## 💡 Development Ideas

You can extend the project with the following features:

* 🔒 Authentication (JWT or API key)
* 🧹 Data cleaning (handling missing values, formatting)
* 👀 Preview CSV content before conversion
* 📦 Docker support for deployment
* 📑 Schema validation for expected CSV structure

---

## 🏁 Conclusion

This project is a practical example of how Python web technologies like Flask and Streamlit can be combined to solve real-world problems. It simplifies the process of converting CSV data into JSON for both technical and non-technical users.

### Why Use This App?

* Easily convert CSV to JSON without writing code
* Fast and accurate conversion using the Pandas library
* Clean, user-friendly design
* Open-source and ready to customize

---

## 📄 License

This project is open-source and available under the [MIT License](https://opensource.org/licenses/MIT).

---

## 📬 Feedback & Contributions

We welcome feedback, feature suggestions, and contributions! Feel free to open an issue or submit a pull request.

