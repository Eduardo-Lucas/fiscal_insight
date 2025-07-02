
````markdown
# 📊 Fiscal Insight

**Fiscal Insight** is a Django-based platform designed to streamline the upload, analysis, and classification of Brazilian electronic invoices (NF-e). It enables companies to automatically extract fiscal data from XML/PDF files, validate key tax fields, and generate insightful PDF reports. The platform includes secure user login, company association, and a dashboard to manage and monitor uploaded invoices.

---

## 🚀 Features

- 🔐 **User Authentication**
  - Email-based login
  - Each user is exclusively tied to one company

- 📁 **NF-e Upload**
  - Upload of XML and optional PDF files
  - Secure file storage and history tracking

- ⚙️ **Automated Parsing & Extraction**
  - Extracts CFOP, NCM, CST, ICMS, and other tax fields from XML

- 🧠 **Invoice Classification**
  - Applies basic tax rules to label invoices as:
    - `Regular`
    - `Alerta`
    - `Risco`

- 📄 **PDF Report Generation**
  - Generates downloadable reports with invoice data and classification summary

- 📊 **Dashboard**
  - Company-specific view of all uploaded NF-es
  - Status and classification overview

---

## 🧰 Tech Stack

| Layer       | Technology              |
|-------------|--------------------------|
| Backend     | Django 4+, Python 3.11+  |
| Frontend    | Bootstrap 5              |
| Database    | SQLite / PostgreSQL      |
| PDF Export  | WeasyPrint               |
| Deployment  | Render, Heroku, Docker   |

---

## 🛠️ Setup Instructions

1. **Clone the repository**  
   ```bash
   git clone https://github.com/your-org/fiscal-insight.git
   cd fiscal-insight
````

2. **Create virtual environment & install dependencies**

   ```bash
   python -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   ```

3. **Apply migrations & create superuser**

   ```bash
   python manage.py migrate
   python manage.py createsuperuser
   ```

4. **Run development server**

   ```bash
   python manage.py runserver
   ```

---

## 📸 Screenshots

> *(Add screenshots of upload form, dashboard view, and sample PDF report here)*

---

## 📦 Deployment

* Ready for deployment on platforms like **Render**, **Heroku**, or **Dockerized environments**.
* Add `.env` for environment variables such as `SECRET_KEY`, `DEBUG`, `ALLOWED_HOSTS`, etc.

---

## 📈 Roadmap

* [ ] REST API for integration
* [ ] Support for other document types (e.g., CT-e, NFC-e)
* [ ] Advanced fiscal analysis engine
* [ ] OCR for PDF invoice scanning
* [ ] Multi-tenant support for accounting firms

---

## 🤝 Contributing

Contributions are welcome! Please open an issue or submit a pull request with improvements, fixes, or new features.

---

## 📄 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

## 👨‍💼 Author

Developed by [Eduardo Lucas](mailto:eduardolucas40@gmail.com)
Senior Python Developer
