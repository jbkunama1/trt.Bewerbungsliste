
![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)
![Docker](https://img.shields.io/badge/docker-ready-blue)
![Static HTML](https://img.shields.io/badge/static-HTML%2FCSS%2FJS-lightgrey)


# trt.Bewerbungsliste

Einfache Bewerbungs-Linkliste als statische Web-App (HTML, CSS, JS) zur Dokumentation von Bewerbungen (Jobs, Studium, FSJ etc.).

Die App bietet:
- Erfassung von Stelle/Studiengang, Bewerbungslink und Notizen (z. B. "angeschrieben am 05.07.26").
- Zusatzfelder: Art der Bewerbung (E-Mail, Onlineportal, Post ...) und Rückmeldung (z. B. "Zusage am 20.07.26").
- Checkboxes zum Markieren als erledigt.
- Lokale Speicherung per `localStorage` im Browser.
- Export der Liste als CSV-Tabelle zur Weiterverarbeitung in Excel/LibreOffice/Word.

## Projektstruktur

```text
trt.Bewerbungsliste/
├─ docker-compose.yml   # Docker-Stack für Portainer / Docker
├─ html/
│  └─ index.html        # Bewerbungs-Linkliste (Web-App)
└─ README.md
```

Hinweis: Das Verzeichnis `html/` wird beim ersten Setup lokal angelegt und enthält die `index.html`.

## Lokales Setup (ohne Docker)

1. Repository klonen:
   ```bash
   git clone https://github.com/dein-user/trt.Bewerbungsliste.git
   cd trt.Bewerbungsliste
   ```
2. Datei `html/index.html` im Browser öffnen (Doppelklick oder `file://`-Pfad).

## Docker-Stack für Portainer / Docker Compose

Der Stack nutzt einen schlanken `nginx:alpine`-Container und veröffentlicht die App im LAN auf Port `8090`.

### Vorbereitung

1. Repository auf dem Docker-Host klonen:
   ```bash
   git clone https://github.com/dein-user/trt.Bewerbungsliste.git
   cd trt.Bewerbungsliste
   ```
2. Ordner `html` anlegen und die App-Datei dort ablegen:
   ```bash
   mkdir -p html
   cp index.html html/index.html
   ```

### Docker Compose (direkt auf dem Host)

```bash
# Im Projektverzeichnis
docker compose up -d
```

Die App ist anschließend unter `http://<docker-host>:8090` im LAN erreichbar.

### Portainer-Stack

1. In Portainer auf **Stacks → Add stack** gehen.
2. Als Name z. B. `trt-bewerbungsliste` wählen.
3. Inhalt von `docker-compose.yml` aus diesem Repo in das Webformular kopieren.
4. Deployen.

Auch hier ist die App unter `http://<docker-host>:8090` erreichbar.

## Hinweise zur Speicherung

- Die Bewerbungen werden pro Browser/Client im `localStorage` gespeichert.
- Bei Nutzung im LAN hat jede Person ihre eigene lokale Liste (unabhängig von anderen Clients).

## Lizenz

Dieses Projekt kann frei im schulischen Kontext genutzt, angepasst und erweitert werden.


## Installation und Deployment

### 1. GitHub-Repository

1. Auf GitHub ein neues Repository `trt.Bewerbungsliste` anlegen.
2. Lokalen Projektordner initialisieren und pushen:
   ```bash
   cd trt.Bewerbungsliste
   git init
   git remote add origin https://github.com/<dein-user>/trt.Bewerbungsliste.git
   git add .
   git commit -m "Initial commit"
   git push -u origin main
   ```

### 2. Installation auf dem Docker-Host

1. Repository auf dem Server klonen:
   ```bash
   git clone https://github.com/<dein-user>/trt.Bewerbungsliste.git
   cd trt.Bewerbungsliste
   ```
2. Hostpfad `/opt/trt.Bewerbungsliste/html` anlegen und `index.html` dorthin kopieren:
   ```bash
   sudo mkdir -p /opt/trt.Bewerbungsliste/html
   sudo cp html/index.html /opt/trt.Bewerbungsliste/html/index.html
   ```
3. Docker-Stack starten:
   ```bash
   docker compose up -d
   ```
4. Zugriff im LAN über:
   ```
   http://<docker-host>:8090
   ```

### 3. Deployment über Portainer

1. In Portainer unter **Stacks → Add stack** gehen.
2. Stack-Name z. B. `trt-bewerbungsliste` vergeben.
3. Inhalt der `docker-compose.yml` aus dem Repo in das Formular kopieren.
4. Stack deployen.
5. Sicherstellen, dass der Hostpfad `/opt/trt.Bewerbungsliste/html` existiert und `index.html` enthält (siehe Schritt 2.2 oben).



## Logo

Das Projekt enthält ein Logo `html/bewerbungsliste-logo.png`, das:
- als Favicon in der Web-App (`<link rel="icon" ...>`)
- und als Logo im Header (`<img src="bewerbungsliste-logo.png" ...>`) verwendet wird.

Bei Bedarf kannst du das Logo durch eine eigene PNG-Datei mit gleichem Namen ersetzen.
