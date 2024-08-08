# Usa a imagem base do Python
FROM python:3.8

# Define o diretório de trabalho dentro do contêiner
WORKDIR /code

# Copia o arquivo requirements.txt para o diretório de trabalho
COPY requirements.txt .

# Atualiza o pip e instala as dependências do projeto
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Copia todo o código fonte para o diretório de trabalho
COPY . .

# Expondo a porta 8000, onde o Django vai rodar
EXPOSE 8000

# Comando para executar o servidor do Django
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

ENV DEBUG=1
ENV SECRET_KEY=your_secret_key
ENV DATABASE_URL=sqlite:///db.sqlite3
