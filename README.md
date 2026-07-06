# Willkommen bei GitIntro

Das hier ist eine kleine Einführung in [Git](https://git-scm.com/). Was ihr hier seht, ist bereits ein sogenanntes [Repository](https://git-scm.com/book/en/v2/Git-Basics-Working-with-Remotes), kurz 'Repo' genannt.

## Git installieren

Geht dafür auf die Seite [Git](https://git-scm.com/downloads) und installiert Git.

## Ein Repo Klonen

Um ein Repo herunterzuladen, genannt klonen, könnt ihr den folgenden Befehl in eurer Kommandozeile ausführen:

```bash
git clone https://git.schulth.net/leoschultheiss/GitIntro.git
```

## Euer erster Commit

Bearbeitet die Datei [main.py](main.py) nach eurem Belieben. Z.B. könnt ihr einen Kommentar hinzufügen, oder die Ausgabe ändern.

Seht euch an, welche Dateien geändert wurden:

```bash
git status
```

Um die Änderungen zu speichern, müsst ihr diese zuerst mit dem Befehl `git add` zur sogenannten Staging Area hinzufügen. Danach könnt ihr die Änderungen mit dem Befehl `git commit` speichern.

```bash
git add main.py
git commit -m "Euer Kommentar hier"
```

Mit `git log` könnt ihr dann euren Commit anschauen.