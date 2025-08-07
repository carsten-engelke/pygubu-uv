# Anleitung: Pygubu-App mit `uv` erstellen, bauen, testen und veröffentlichen

Diese Schritt-für-Schritt-Anleitung zeigt, wie du eine neue Pygubu-App mit dem Tool [`uv`](https://github.com/astral-sh/uv) aufsetzt.  
Wir verwenden **ausschließlich** die von dir genannten `uv`-Befehle (`init`, `build`, `publish`, `run`).  
**uv pip** wird an keiner Stelle verwendet.

## Voraussetzungen

- Python 3.8+ installiert
- [`uv`](https://github.com/astral-sh/uv) installiert (`pipx install uv`)
- Account auf [TestPyPI](https://test.pypi.org/account/register/)

---

## 1. Neues Projekt anlegen

Erstelle ein neues Verzeichnis und initialisiere das Paket:

```sh
mkdir meine_pygubu_app
cd meine_pygubu_app
uv init --package
```

Folge dem Assistenten und gib die gewünschten Metadaten ein (z.B. Name, Beschreibung, etc.).

---

## 2. Pygubu als Abhängigkeit hinzufügen

Bearbeite die Datei `pyproject.toml` und füge bei `[project]` unter `dependencies` `pygubu` mittels `uv` hinzu:

```sh
uv add pygubu
```

---

## 3. Beispiel-Code für eine einfache Pygubu-App

Erstelle im Projektverzeichnis eine ui-Datei mit dem `pygubu-designer`, z.B. `src/meine_pygubu_app/meine_pygubu_app.ui`.
Lege den Modulnamen fest (er wird später mit `ui` ergänzt die GUI-Klasse enthalten,z.B. `meine_pygubu_app`. Vergebe einen beliebigen Projektnamen und eine Beschreibung und lege den Klassennamen für fur GUI fest, z.B. `MeineApp`). Erstelle die die Applikation durch Click auf `Code generieren` und benenne die Python-Datei mit dem Modulnamen in `__main__.py` um (`meine_pygubu_app.py` -> `__main__.py`). 

**Achtung:** Passe deinen Code an, sodass es eine Funktion `main()` gibt, z.B.:

```python
def main():
    app = ExampleApp()
    app.run()

if __name__ == "__main__":
    main()
```

---

## 4. Script-Entry-Point festlegen

Ändere den Script-Entry-Poitn in deiner `pyproject.toml` unter `[project.scripts]`:

```toml
[project.scripts]
meine-pygubu-app = "meine_pygubu_app.__main__:main"
```

Du kannst den Inhalt der `__init__.py` löschen, da er nicht mehr benötigt wird.


---

## 5. Die App testen

Starte die App direkt mit:

```sh
uv run meine-pygubu-app
```

---

## 6. Paket bauen

Erstelle ein Build-Artefakt (Wheel und sdist):

```sh
uv build
# Die Dateien findest du im Verzeichnis dist/
```

---

## 7. Auf TestPyPI veröffentlichen

Veröffentliche das Paket auf TestPyPI:

```sh
uv publish --repository testpypi
```

Beim ersten Mal wirst du nach deinen [TestPyPI](https://test.pypi.org/account/register/)-Zugangsdaten gefragt.

---

## 8. Hinweise

- Du kannst das Paket nun von TestPyPI installieren (auf einem anderen System oder in einer frischen Umgebung).
- Für die Veröffentlichung auf dem echten PyPI entferne einfach das `--repository testpypi` beim `uv publish`.

---

## Quellen

- [uv Dokumentation](https://github.com/astral-sh/uv)
- [Pygubu Projekt](https://github.com/alejandroautalan/pygubu)
- [TestPyPI](https://test.pypi.org/)
