FROM python:3.12-alpine
WORKDIR /app
# demo only: a deliberately old, vulnerable dependency to show the Shipyard SBOM gate
RUN pip install --no-cache-dir "Django==2.2.0" "PyYAML==5.3"
COPY app.py .
EXPOSE 8080
CMD ["python", "app.py"]
