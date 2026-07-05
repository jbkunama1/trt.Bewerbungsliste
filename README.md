
# trt.Bewerbungsliste (Panels + Flask + SQLite)

![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)
![Docker](https://img.shields.io/badge/docker-ready-blue)
![Flask](https://img.shields.io/badge/backend-Flask%2FSQLite-green)

Zentrale Bewerbungs-Linkliste im Panel-Design, mit Flask-Backend und SQLite-Datenbank. Alle Nutzer:innen im LAN sehen dieselbe Liste (Jobs, Studium, FSJ etc.).

## Features

- Panel-Design mit Statistik-Karten, Dark-/Light-Theme (unverändert aus der ursprünglichen Version).
- Formularfelder: Stelle/Studiengang, Bewerbungslink, Notizen (z. B. "angeschrieben am 05.07.26"), Art der Bewerbung, Rückmeldung.
- Checkbox zum Markieren als erledigt.
- Zentrale Speicherung in SQLite über eine Flask-REST-API – kein localStorage mehr.
- "Erledigte entfernen"-Button löscht alle abgehakten Einträge zentral.

## Projektstruktur

```text
trt.Bewerbungsliste_flask_panels/
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

### 1. GitHub-Repository

```bash
cd trt.Bewerbungsliste_flask_panels
git init
git remote add origin https://github.com/<dein-user>/trt.Bewerbungsliste_flask_panels.git
git add .
git commit -m "Initial commit: Panels-Frontend + Flask + SQLite (fetch-basiert)"
git branch -M main
git push -u origin main
```

### 2. Installation auf dem Docker-Host

```bash
git clone https://github.com/<dein-user>/trt.Bewerbungsliste_flask_panels.git
cd trt.Bewerbungsliste_flask_panels
sudo mkdir -p /opt/trt.Bewerbungsliste_panels/data
docker compose up -d
```

Zugriff im LAN über: `http://<docker-host>:8090`

### 3. Persistenz

Die SQLite-Datenbank liegt im Volume `/opt/trt.Bewerbungsliste_panels/data` (Host) und bleibt bei Container-Neustarts erhalten. Alle Benutzer:innen im LAN sehen dieselben Einträge, unabhängig von Browser oder Gerät.

## Lizenz

MIT License – frei nutzbar und anpassbar im schulischen Kontext.
