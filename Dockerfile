FROM python:3.8

# define enviromente variables
ENV MODEL_PATH ./model

# Add source files

RUN mkdir /app
WORKDIR /app
ADD . /app

# Install dependencies

RUN python -m pip install -r requirements.txt

# Install package

RUN python -m pip install . --upgrade

# Expose API port

EXPOSE 5000

# Start application

CMD ["panelais_models_api"]
