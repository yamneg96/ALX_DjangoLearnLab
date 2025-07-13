# 📚 Alx Django Learn Lab

Welcome to the **Alx Django Learn Lab**! 🚀  
This repository is your hands-on playground for mastering Django, the powerful Python web framework. Whether you're a beginner or brushing up on your skills, this lab is packed with practical exercises and clear documentation.

---

## 🗂️ Project Structure

```plaintext
Alx_DjangoLearnLab/
│
├── Introduction_to_Django/
│   ├── bookshelf/           # 📖 Django app: Bookshelf CRUD
│   │   ├── __init__.py
│   │   ├── admin.py
│   │   ├── apps.py
│   │   ├── migrations/
│   │   │   └── __init__.py
│   │   ├── models.py
│   │   ├── tests.py
│   │   └── views.py
│   ├── LibraryProject/      # 🏛️ Main Django project
│   │   ├── __init__.py
│   │   ├── asgi.py
│   │   ├── settings.py
│   │   ├── urls.py
│   │   └── wsgi.py
│   ├── manage.py            # ⚙️ Django management script
│   ├── create.md            # 📝 Guide: Creating records
│   ├── retrieve.md          # 📝 Guide: Retrieving records
│   ├── update.md            # 📝 Guide: Updating records
│   ├── delete.md            # 📝 Guide: Deleting records
│   └── CRUD_operations.md   # 📝 Overview: CRUD in Django
│
└── README.md                # 📄 This file!
```

---

## 🚦 Getting Started

1. **Clone the repository**  
   ```bash
   git clone <repo-url>
   cd Alx_DjangoLearnLab/Introduction_to_Django
   ```

2. **Install dependencies**  
   Make sure you have Python 3.8+ and Django installed:
   ```bash
   pip install django
   ```

3. **Run migrations**  
   ```bash
   python manage.py migrate
   ```

4. **Start the development server**  
   ```bash
   python manage.py runserver
   ```

5. **Explore the app!**  
   Visit [http://127.0.0.1:8000/](http://127.0.0.1:8000/) in your browser.

---

## 🛠️ Features

- 📖 **Bookshelf App**: Practice CRUD (Create, Read, Update, Delete) operations
- 🏗️ **Modular Structure**: Easy to navigate and extend
- 📝 **Step-by-step Guides**: Markdown files for each CRUD operation
- 💡 **Beginner Friendly**: Clear comments and documentation

---

## 🤝 Contributing

Pull requests are welcome!  
Feel free to fork the repo and submit improvements, bug fixes, or new exercises.

---

Happy coding! 🎉  
*— YN from ALX*