# 📚 Django Library Management System

This is a Django web application that allows administrators to manage an online library system, including **Authors**, **Books**, and **Borrow Records**. It also supports **pagination** and **exporting data to Excel**.

---

## 🚀 Features

- Add / View / Paginate:
  - Authors
  - Books
  - Borrow Records
- Form validation (e.g., email domain for authors)
- Export all data to Excel (separate sheets for Authors, Books, and Borrow Records)
- Class-based views used throughout
- Clean and responsive Bootstrap-based UI

---

## 📂 Project Structure

libraryProject/
│
├── libraryapp/
│   ├── templates/
│   │   └── libraryapp/
│   │       ├── base.html
│   │       ├── add_author.html
│   │       ├── add_book.html
│   │       ├── add_borrowrecord.html
│   │       ├── author_list.html
│   │       ├── book_list.html
│   │       ├── borrowrecord_list.html
│   │       └── pagination.html
│   ├── forms.py
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   └── utils.py
├── libraryProject/
│   ├── settings.py
│   └── urls.py
├── manage.py
└── requirements.txt



---

## 🔧 Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/Pooja123-meshram/libraryProject.git
cd libraryProject

2. Create a virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

3. Install dependencies
pip install -r requirements.txt

4. Apply migrations
python manage.py makemigrations
python manage.py migrate

5. Create superuser (optional)
python manage.py createsuperuser

6. Run the server
python manage.py runserver
Open in browser: http://127.0.0.1:8000

📦 Requirements
Django

openpyxl (for Excel export)

Bootstrap (via CDN)

Install openpyxl:

pip install openpyxl
 
 
