# Odporúčaná štruktúra pre modulárnu Flask aplikáciu

Jasné, rád pomôžem. Optimálna štruktúra pre modulárnu Flask aplikáciu sa zvyčajne opiera o koncept **Blueprints** a vzor **Application Factory**. Tento prístup umožňuje rozdeliť aplikáciu na menšie, znovupoužiteľné komponenty.

## Odporúčaná štruktúra súborov

Toto je ideálna štruktúra pre stredne veľkú až veľkú aplikáciu:

```
/my_project/
├── .venv/                  # Virtuálne prostredie
├── app/                    # Hlavný balíček aplikácie
│   ├── __init__.py         # Application Factory (funkcia create_app)
│   │
│   ├── auth/               # Prvý Blueprint (napr. pre autentifikáciu)
│   │   ├── __init__.py     # Definuje Blueprint
│   │   ├── routes.py       # Cesty (routes) pre tento Blueprint
│   │   ├── forms.py        # Formuláre špecifické pre auth
│   │   └── templates/      # Šablóny špecifické pre tento Blueprint
│   │       └── auth/
│   │           ├── login.html
│   │           └── register.html
│   │
│   ├── products/           # Druhý Blueprint (napr. pre produkty)
│   │   ├── __init__.py
│   │   ├── routes.py
│   │   ├── models.py       # Modely špecifické pre produkty
│   │   └── templates/
│   │       └── products/
│   │           └── list.html
│   │
│   ├── static/             # Globálne statické súbory (CSS, JS, obrázky)
│   │   ├── css/
│   │   └── js/
│   │
│   ├── templates/          # Globálne šablóny
│   │   ├── base.html
│   │   └── 404.html
│   │
│   ├── extensions.py       # Inicializácia rozšírení (napr. SQLAlchemy, LoginManager)
│   └── models.py           # Globálne dátové modely (npr. User)
│
├── instance/               # Konfigurácia a súbory, ktoré nemajú byť v Git-e
│   └── config.py           # Napr. produkčné kľúče, pripojenie k databáze
│
├── tests/                  # Testy pre aplikáciu
│   ├── __init__.py
│   └── test_basic.py
│
├── run.py                  # Spúšťací skript aplikácie
├── config.py               # Hlavný konfiguračný súbor (triedy pre Dev, Prod, Test)
├── pyproject.toml          # Definuje projekt a závislosti (pre nástroje ako Poetry alebo UV)
├── uv.lock                 # (alebo requirements.txt) Zoznam závislostí
└── .env                    # Premenné prostredia (napr. FLASK_APP, FLASK_DEBUG)
```

---

## Vysvetlenie kľúčových častí

### 1. `app/__init__.py` (Application Factory)
*   Toto je srdce vašej aplikácie. Namiesto globálneho objektu `app = Flask(__name__)` tu vytvoríte funkciu `create_app()`.
*   **Prečo je to dôležité?**
    *   **Zabraňuje cirkulárnym importom:** Rozšírenia a Blueprints sa môžu bezpečne importovať a registrovať.
    *   **Uľahčuje testovanie:** Pre každý test môžete vytvoriť novú inštanciu aplikácie s inou konfiguráciou.
*   **Príklad `create_app()`:**
    ```python
    from flask import Flask
    from .extensions import db, login_manager
    from .auth.routes import auth_bp
    from .products.routes import products_bp
    from config import Config

    def create_app(config_class=Config):
        app = Flask(__name__)
        app.config.from_object(config_class)
        app.config.from_pyfile('../instance/config.py', silent=True)

        # Inicializácia rozšírení
        db.init_app(app)
        login_manager.init_app(app)

        # Registrácia Blueprints
        app.register_blueprint(auth_bp, url_prefix='/auth')
        app.register_blueprint(products_bp, url_prefix='/products')

        return app
    ```

### 2. `app/auth/` (Príklad Blueprintu)
*   Blueprint je ako mini-aplikácia v rámci vašej hlavnej aplikácie.
*   Má vlastné cesty (`routes.py`), šablóny (`templates/auth/`) a logiku.
*   To vám umožní zapuzdriť jednu konkrétnu funkčnosť (napr. všetko, čo sa týka používateľov a prihlasovania) na jedno miesto. Ak ju nebudete potrebovať, jednoducho ju odregistrujete v `create_app()`.

### 3. `run.py` (Spúšťací skript)
*   Tento súbor je veľmi jednoduchý. Importuje `create_app` a spustí aplikáciu.
*   **Príklad:**
    ```python
    from app import create_app

    app = create_app()

    if __name__ == '__main__':
        app.run(debug=True)
    ```

### 4. `config.py`
*   Definujte rôzne konfiguračné triedy pre rôzne prostredia (vývoj, produkcia, testovanie).
*   **Príklad:**
    ```python
    import os

    class Config:
        SECRET_KEY = os.environ.get('SECRET_KEY') or 'a-very-secret-key'
        SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///app.db'
        # ... ďalšie nastavenia

    class DevelopmentConfig(Config):
        DEBUG = True

    class ProductionConfig(Config):
        DEBUG = False
    ```

### 5. `instance/` adresár
*   Flask ho automaticky rozpozná. Ukladajte sem citlivé konfiguračné súbory alebo databázový súbor (napr. `app.db` pre SQLite), ktoré by nemali byť súčasťou Git repozitára. Nezabudnite pridať `instance/` do `.gitignore`.

## Výhody tejto štruktúry

*   **Modularita:** Každá hlavná funkcia aplikácie je oddelená vo vlastnom Blueprinte.
*   **Škálovateľnosť:** Je veľmi jednoduché pridať novú sekciu do aplikácie vytvorením nového Blueprintu.
*   **Udržiavateľnosť:** Kód je organizovaný logicky, čo uľahčuje jeho hľadanie, opravu a vylepšovanie.
*   **Testovateľnosť:** Vzor Application Factory je kľúčový pre písanie spoľahlivých testov.
