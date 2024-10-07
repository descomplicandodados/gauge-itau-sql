# Usar a imagem base do Python
FROM python:3.10-slim

# Define o diretório de trabalho
WORKDIR /app

# Copia o requirements.txt para o contêiner
COPY requirements.txt .

# Instala as dependências
RUN pip install --no-cache-dir -r requirements.txt

# Copia o restante do código para o contêiner
COPY . .

# Comando padrão
CMD ["sh", "-c", "python load.py && python cases_sql.py"]

