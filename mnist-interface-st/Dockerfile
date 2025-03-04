# Utiliser une image Python comme base
FROM python:3.9

# Définir le répertoire de travail
WORKDIR /app

# Copier les fichiers de l'application
COPY . /app

# Installer les dépendances
RUN pip install --no-cache-dir -r requirements.txt

# Exposer le port 5001 pour Streamlit
EXPOSE 5001

# Commande pour exécuter l'application Streamlit
CMD ["streamlit", "run", "mnist_st.py", "--server.port=5001", "--server.address=0.0.0.0"]
