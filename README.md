
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
├─ app.py               # Flask-App mit SQLite-Backend & API
├─ docker-compose.yml   # Docker-Stack (Port 8090 -> Flask 5000)
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
git commit -m "Initial commit: Panels-Frontend + Flask + SQLite (fetch-basiert)"
git branch -M main
git push -u origin main
```

Falls das Repository bereits existiert und du es nur aktualisierst:

```bash
git clone https://github.com/jbkunama1/trt.Bewerbungsliste.git
cd trt.Bewerbungsliste
# Dateien aus diesem Paket hinein kopieren/überschreiben
git add .
git commit -m "Update: Panels-Frontend + Flask + SQLite"
git push
```

### 2. Installation auf dem Docker-Host

```bash
git clone https://github.com/jbkunama1/trt.Bewerbungsliste.git
cd trt.Bewerbungsliste
sudo mkdir -p /opt/trt.Bewerbungsliste/data
docker compose up -d
```

Zugriff im LAN über: `http://<docker-host>:8090`

### 3. Persistenz

Die SQLite-Datenbank liegt im Volume `/opt/trt.Bewerbungsliste/data` (Host) und bleibt bei Container-Neustarts erhalten. Alle Benutzer:innen im LAN sehen dieselben Einträge, unabhängig von Browser oder Gerät.

## Lizenz

MIT License – frei nutzbar und anpassbar im schulischen Kontext.
