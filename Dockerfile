FROM python:3.10

# Mise à jour des paquets pip
RUN pip install --upgrade pip
RUN mkdir /comptes-bancaires

WORKDIR /comptes-bancaires

# Ajout des fichiers dans le conteneurs
ADD . /comptes-bancaires

#Ajout requirements.txt et installation des dépendances python
RUN pip install --trusted-host pypi.python.org -r requirements.txt
CMD [ "/comptes-bancaires/src/main.py" ]

ENTRYPOINT [ "python" ]