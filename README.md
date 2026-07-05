
# trt.Bewerbungsliste (Panels + Flask + SQLite)

![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)
![Docker](https://img.shields.io/badge/docker-ready-blue)
![Flask](https://img.shields.io/badge/backend-Flask%2FSQLite-green)

Zentrale Bewerbungs-Linkliste im Panel-Design, mit Flask-Backend und SQLite-Datenbank. Alle Nutzer:innen im LAN sehen dieselbe Liste (Jobs, Studium, FSJ etc.).

Repository: [jbkunama1/trt.Bewerbungsliste](https://github.com/jbkunama1/trt.Bewerbungsliste)

## Features

- Panel-Design mit Statistik-Karten, Dark-/Light-Theme.
- Formularfelder: Stelle/Studiengang, Bewerbungslink, Notizen (z. B. "angeschrieben am 05.07.26"), Art der Bewerbung, Rückmeldung.
- Checkbox zum Markieren als erledigt.
- Zentrale Speicherung in SQLite über eine Flask-REST-API.
- "Erledigte entfernen"-Button löscht alle abgehakten Einträge zentral.

## Projektstruktur

```text
trt.Bewerbungsliste/
├─ Dockerfile           # Baut ein eigenes Image mit app.py + static
├─ app.py               # Flask-App mit SQLite-Backend & API
├─ docker-compose.yml   # Docker-Stack (baut Image, Port 8090 -> Flask 5000)
├─ static/
│  └─ index.html        # Frontend im Panel-Design, per fetch() an Flask/SQLite angebunden
└─ LICENSE              # MIT-Lizenz
```

## API-Endpunkte

- `GET /api/applications` – alle Bewerbungen laden.
- `POST /api/applications` – neue Bewerbung anlegen (title, url, description, type, feedback).
- `PUT /api/applications/<id>` – Felder aktualisieren, z. B. `done`.
- `DELETE /api/applications/<id>` – Eintrag löschen.

## Installation und Deployment

### 1. Repository klonen oder pushen

Falls du dieses Projekt lokal neu aufsetzt und in das bestehende Repository pushen möchtest:

```bash
cd trt.Bewerbungsliste
git init
git remote add origin https://github.com/jbkunama1/trt.Bewerbungsliste.git
git add .
git commit -m "Initial commit: Panels-Frontend + Flask + SQLite (Dockerfile-basiert)"
git branch -M main
git push -u origin main
```

Falls das Repository bereits existiert und du es nur aktualisierst:

```bash
git clone https://github.com/jbkunama1/trt.Bewerbungsliste.git
cd trt.Bewerbungsliste
# Dateien aus diesem Paket hinein kopieren/überschreiben
git add .
git commit -m "Fix: Dockerfile statt Bind-Mount fuer app.py (behebt __main__-Fehler)"
git push
```

### 2. Deployment als Stack in Portainer

Diese App wird über ein eigenes **Dockerfile** gebaut, nicht mehr per Bind-Mount des Codes. Das behebt den Fehler `can't find '__main__' module in '/app/app.py'`, der auftritt, wenn Docker eine fehlende Datei versehentlich als leeres Verzeichnis mountet.

1. In Portainer im Menü auf **Stacks → Add stack** gehen.
2. Einen Namen vergeben, z. B. `trt-bewerbungsliste`.
3. Bei **Build method** die Option **Repository** auswählen und folgende Angaben machen:
   - **Repository URL**: `https://github.com/jbkunama1/trt.Bewerbungsliste.git`
   - **Repository reference**: `refs/heads/main`
   - **Compose path**: `docker-compose.yml`
4. Unter **Environment variables** sind keine zusätzlichen Variablen nötig.
5. Auf **Deploy the stack** klicken.

Portainer klont das Repository, baut das Image gemäß `Dockerfile` und startet den Container gemäß `docker-compose.yml`.

**Wichtig:** Vor dem ersten Deploy muss auf dem Docker-Host das Datenverzeichnis für die SQLite-Datenbank existieren:

```bash
sudo mkdir -p /opt/trt.Bewerbungsliste/data
```

Dieses Verzeichnis wird als Volume in den Container gemountet, damit die Datenbank bei Neustarts und Updates des Stacks erhalten bleibt.

### 3. Stack aktualisieren

Wenn im Repository neue Commits vorhanden sind (z. B. nach `git push`):

1. In Portainer den Stack `trt-bewerbungsliste` öffnen.
2. Auf **Pull and redeploy** (bzw. **Update the stack**) klicken. Dabei wird das Image aus dem `Dockerfile` neu gebaut.

### 4. Fehlerbehebung: `can't find '__main__' module in '/app/app.py'`

Dieser Fehler trat auf, weil `app.py` per Bind-Mount eingehängt wurde und Docker die Datei nicht fand, wodurch stattdessen ein leeres Verzeichnis `/app/app.py` erstellt wurde. Die aktuelle Version behebt das, indem `app.py` und `static/` direkt im `Dockerfile` ins Image kopiert werden (`COPY app.py /app/app.py`, `COPY static /app/static`) – kein Bind-Mount des Codes mehr nötig.

Nach dem Update in Portainer unbedingt **Update the stack** mit aktivierter Option **Re-pull image and redeploy** bzw. **Rebuild** ausführen, damit das neue Image tatsächlich gebaut wird.

### 5. Zugriff im LAN

Nach erfolgreichem Deploy ist die App erreichbar unter:

```
http://<docker-host>:8090
```

Alle Benutzer:innen im LAN sehen dieselbe zentrale Liste, da alle über dieselbe Flask-API auf die gemeinsame SQLite-Datenbank zugreifen.

## Lizenz

MIT License – frei nutzbar und anpassbar im schulischen Kontext.
