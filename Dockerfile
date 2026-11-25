# Mesma versao do Python do .venv (3.12), imagem enxuta.
FROM python:3.12-slim

ENV PYTHONDONTWRITEBYTECODE=1 PYTHONUNBUFFERED=1

# Usuario sem privilegio de administrador.
RUN useradd --create-home --uid 1001 app
WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# O .dockerignore deixa de fora o .env, o .venv, o .git, rascunhos e a apresentacao.
COPY --chown=app:app . .
USER app

# O Cloud Run entrega a porta em PORT; 8080 so vale para rodar o contêiner na maquina.
CMD ["sh", "-c", "exec streamlit run app.py --server.port=${PORT:-8080}"]
