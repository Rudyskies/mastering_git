# 📊 Sales Dashboard App (Streamlit)

A simple and interactive sales dashboard built using **Python + Streamlit**.

Upload your CSV sales file, visualize key metrics and trends, and download an Excel report — all in one lightweight web app.

---

## 🚀 Features

- 📁 Upload your own CSV sales file  
- 📈 Interactive charts (Bar, Pie, Line)  
- 🧾 Export Excel report (3 sheets: sales summary, daily revenue, product performance)  
- 💡 Automatic demo data if no file is uploaded  

---

## 🧰 Tech Stack

- Python 3.x  
- Streamlit  
- Pandas  
- Matplotlib  
- XlsxWriter  

---

## 📷 Screenshots

<img src="screenshots/dashboard_main.png" width="600"/>  
<img src="screenshots/upload_sidebar.png" width="300"/>  
<img src="screenshots/excel_report.png" width="600"/>

---

## 📂 Sample CSV Format

Your CSV should include the following columns:

- `id_transaksi` — unique transaction ID  
- `id_produk` — product code or name  
- `jumlah` — quantity sold  
- `tanggal` — sale date (format: YYYY-MM-DD)  

You can also use the included dummy data or adjust the code as needed.

---

## 💻 Run Locally

1. Clone this repo  
2. Install requirements:

```bash
pip install -r requirements.txt