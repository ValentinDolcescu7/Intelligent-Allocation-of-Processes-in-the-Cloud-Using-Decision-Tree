# Proiect de Alocare a Muncitorilor

Acest proiect este destinat alocării muncitorilor utilizând un model de clasificare a arborilor de decizie. Proiectul include diverse scripturi Python pentru pregătirea datelor, antrenarea modelului și simularea alocării muncitorilor.

## Cuprins

- [Despre Proiect](#despre-proiect)
- [Structura Proiectului](#structura-proiectului)
- [Cum să Rulezi Proiectul](#cum-să-rulezi-proiectul)
- [Detalii Tehnice](#detalii-tehnice)
- [Contribuții](#contribuții)

## Despre Proiect

Acest proiect utilizează un set de date pentru a antrena un model de clasificare, care prezice muncitorul alocat pe baza caracteristicilor unei sarcini. Proiectul include, de asemenea, o simulare vizuală a alocării sarcinilor folosind matplotlib.

## Structura Proiectului

- `Cloud/`
  - Conține scripturi și datele CSV pentru pregătirea și antrenarea modelului.

- `Edges/`
  - Contine scripturi si datele CSV pentru evaluarea și testarea modelului.

- `myvenv/`
  - Mediu virtual pentru instalarea dependințelor proiectului.

- `generate_dataset/`
  - Scripturi pentru generarea și manipularea seturilor de date.

- `__pycache__/`
  - Cache Python generat automat.

- `workers/`
  - Scripturi pentru gestionarea muncitorilor și alocarea sarcinilor.

- `allocated_worker_model.joblib`
  - Modelul antrenat salvat în format Joblib.

## Cum să Rulezi Proiectul

1. **Configurarea Mediului de Dezvoltare**

   - Asigură-te că ai Python 3.x instalat.
   - Clonează acest repository:
     ```sh
     git clone [link către repository]
     ```
   - Navighează în directorul proiectului:
     ```sh
     cd [nume-proiect]
     ```
   - Creează un mediu virtual și activează-l:
     ```sh
     python -m venv myvenv
     source myvenv/bin/activate # pentru Unix
     myvenv\Scripts\activate # pentru Windows
     ```
   - Instalează dependențele necesare:
     ```sh
     pip install -r requirements.txt
     ```

2. **Antrenarea Modelului**

   - Rulează scriptul `train.py` pentru a antrena modelul:
     ```sh
     python Cloud/train.py
     ```

3. **Simularea Alocării Sarcinilor**

   - Rulează scriptul `Master.py` pentru a simula alocarea sarcinilor:
     ```sh
     python Master.py
     ```

## Detalii Tehnice

- **Librării Utilizate**:
  - `pandas`: pentru manipularea datelor.
  - `scikit-learn`: pentru antrenarea și evaluarea modelului.
  - `matplotlib`: pentru vizualizarea grafică a simulării.
  - `joblib`: pentru salvarea și încărcarea modelului antrenat.

- **Structura Datelor**:
  - Fișierele CSV conțin datele utilizate pentru antrenarea și testarea modelului.
  - Scripturile Python manipulează aceste date și implementează logica de antrenare și predicție.

## Contribuții

Oricine este bine venit să contribuie la acest proiect. Te rugăm să urmezi pașii de mai jos pentru a contribui:

1. Fork acest repository.
2. Creează o nouă ramură (`git checkout -b feature/nou-feature`).
3. Fă commit modificărilor tale (`git commit -m 'Adaugă un nou feature'`).
4. Trimite modificările tale (`git push origin feature/nou-feature`).
5. Deschide un Pull Request.

