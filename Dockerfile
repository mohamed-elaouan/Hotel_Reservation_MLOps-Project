FROM python:slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

WORKDIR /app
# libgomp1 : it requirement for LightGBM dependency 
RUN apt-get update && apt_get install -y --no-install-recommends \
    libgomp1 \  
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

COPY . .

RUN pip install --no-cache-dir -e .

RUN python pipeline/training_pipeline.py

# Expose the port that Flask will run on
EXPOSE 5000 

# Command to run the app
CMD ["python", "application.py"]