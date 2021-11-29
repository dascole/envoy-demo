FROM python:3
WORKDIR .
COPY requirements.txt .
COPY *.py ./
RUN pip install --no-cache-dir -r requirements.txt
EXPOSE 7771

CMD ["python", "main.py"]
