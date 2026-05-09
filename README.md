# 📝 Flask Blog

> **Python · Flask · SQLite · Jinja2**  
> Prosta aplikacja blogowa z systemem logowania, tworzeniem postów i panelem administratora.

---

## 📋 Opis projektu

Aplikacja webowa zbudowana w mikro-frameworku **Flask**, umożliwiająca rejestrację i logowanie użytkowników, publikowanie postów oraz moderację treści przez administratora. Dane przechowywane są w lekkiej bazie **SQLite**.

---

## ✨ Funkcjonalności

### 📰 Blog
- Wyświetlanie wszystkich postów na stronie głównej
- Tworzenie nowych postów (tytuł + treść) przez zalogowanych użytkowników

### 🔐 Autoryzacja
- Rejestracja nowego konta z walidacją danych
- Logowanie i wylogowanie
- Hasła hashowane przez **Werkzeug** (`generate_password_hash`)
- Sesja użytkownika przechowująca ID i rolę

### 🛠️ Panel administratora (`/admin`)
- Podgląd listy wszystkich użytkowników i postów
- Usuwanie użytkowników (z wyjątkiem adminów)
- Usuwanie dowolnych postów

---

## 🗂️ Struktura projektu

```
app/
├── __init__.py        # Fabryka aplikacji Flask
├── db.py              # Połączenie z SQLite, inicjalizacja bazy
├── auth.py            # Blueprint: rejestracja, logowanie, wylogowanie
├── blog.py            # Blueprint: lista postów, tworzenie posta
├── admin.py           # Blueprint: panel admina
├── schema.sql         # Schemat bazy danych
└── templates/
    ├── base.html
    ├── auth/
    │   ├── login.html
    │   └── register.html
    ├── blog/
    │   ├── index.html
    │   └── create.html
    └── admin/
        └── dashboard.html
```

---

## 🗄️ Schemat bazy danych

```sql
user (id, username, password, is_admin)
post (id, author_id → user.id, title, body)
```

---

## 🛠️ Stack technologiczny

| Technologia | Zastosowanie |
|-------------|-------------|
| **Python 3** | Język backendu |
| **Flask** | Mikro-framework webowy |
| **SQLite** | Baza danych |
| **Jinja2** | Silnik szablonów HTML |
| **Werkzeug** | Hashowanie haseł |

---

## 🚀 Instalacja i uruchomienie

### Wymagania
- Python >= 3.8

### Kroki

```bash
# 1. Sklonuj repozytorium
git clone https://github.com/[twoj-login]/flask-blog.git
cd flask-blog

# 2. Utwórz i aktywuj środowisko wirtualne
python -m venv venv
source venv/bin/activate        # Linux/macOS
venv\Scripts\activate           # Windows

# 3. Zainstaluj zależności
pip install flask werkzeug

# 4. Zainicjalizuj bazę danych
flask --app app init-db

# 5. Uruchom serwer deweloperski
flask --app app run
```

Aplikacja będzie dostępna pod adresem `http://localhost:5000`.

---

## 🔗 Endpointy

| Metoda | URL | Opis |
|--------|-----|------|
| GET | `/` | Lista postów |
| GET/POST | `/create` | Tworzenie posta |
| GET/POST | `/auth/register` | Rejestracja |
| GET/POST | `/auth/login` | Logowanie |
| GET | `/auth/logout` | Wylogowanie |
| GET | `/admin/` | Panel administratora |
| POST | `/admin/delete_user/<id>` | Usunięcie użytkownika |
| POST | `/admin/delete_post/<id>` | Usunięcie posta |

---

## 👤 Autor

**[Imię i Nazwisko]**  
[Opcjonalnie: link do profilu GitHub]  
[Rok]
