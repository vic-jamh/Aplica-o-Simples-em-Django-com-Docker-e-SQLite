# Usar a imagem base oficial do Python
FROM python:3.12

# Definir o diretório de trabalho no contêiner
WORKDIR /tarefas

# Copiar os arquivos de requisitos e instalá-los
COPY requirements.txt /tarefas/
RUN pip install --no-cache-dir -r requirements.txt

# Copiar o restante dos arquivos do projeto para o contêiner
COPY . /tarefas/

# Expor a porta padrão do Django
EXPOSE 8000

# Comando para iniciar o servidor de desenvolvimento do Django
CMD ["python", "manage.py", "runserver", "127.0.0.1:8000"]