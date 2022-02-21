FROM python:3.10

# Mise à jour des paquets pip
RUN pip install --upgrade pip
RUN mkdir /comptes-bancaires

WORKDIR /comptes-bancaires

COPY requirements.txt ./

#Ajout requirements.txt et installation des dépendances python
RUN pip install --trusted-host pypi.python.org -r requirements.txt

# Ajout des fichiers dans le conteneurs
ADD . /comptes-bancaires

CMD [ "/comptes-bancaires/src/main.py" ]

ENTRYPOINT [ "python" ]