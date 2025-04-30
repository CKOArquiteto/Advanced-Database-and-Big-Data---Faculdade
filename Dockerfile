# Dockerfile
FROM python:3.12.10-slim

# Diretório de trabalho
WORKDIR /app

# Copia arquivos para dentro do container
COPY app.py /app
COPY seed.py /app
COPY requirements.txt /app

# Instala dependências
RUN pip install --no-cache-dir -r requirements.txt

# Expõe a porta do Streamlit
EXPOSE 8501

# Comando para iniciar o Streamlit
CMD ["streamlit", "run", "app.py", "--server.enableCORS=false", "--server.address=0.0.0.0"]
