# Use uma imagem base oficial do Python
FROM python:3.9-slim

# Define o diretório de trabalho dentro do container
WORKDIR /app

# Copia o arquivo requirements.txt para o diretório de trabalho
COPY requirements.txt .

# Instala as dependências especificadas no requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copia todos os arquivos do diretório atual (onde está o Dockerfile) para o diretório de trabalho no container
COPY . .

# Exponha a porta que a aplicação vai rodar (ajuste conforme necessário)
EXPOSE 5000

# Define o comando padrão para rodar a aplicação (ajuste conforme necessário)
CMD ["python", "app.py"]
