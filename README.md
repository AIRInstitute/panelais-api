# Panelais Models API

API for serving models developed for Panelais.


## Install requirements

```bash
sudo apt update
sudo apt install python3 python3-pip nodejs npm -y
sudo npm install -g pm2
```

## Run application

For running directly the application in a "raw" way:

```bash
sudo python3 -m pip install pip --upgrade
sudo python3 -m pip install . --upgrade
sudo panelais_models_api
```

## Deploy application

### Raw deployment

Application can be launched with the launch script:

```bash
sudo bash launch.sh
```

Note: if the script `launch.sh` doesn't works, you can use `launch2.sh` instead.

### PM2 deployment

Application can be launched in background as a production service with PM2 tool:

```bash
sudo pm2 start pm2.json
```

### Docker deployment

Application can be also deployed with docker. For that purpose, first build and push the application:

```bash
docker build . -t <your dockerhub user>/panelais-api
docker push <your dockerhub user>/panelais-api
```

Then in the enviroment where application must be deplolyed, pull changes and deploy:

```bash
docker pull <your dockerhub user>/panelais-api
docker run -p 5000:<your-published-port> <your dockerhub user>/panelais-api
```

## Automatic Deployment

There is a GitHub Actions automatic CI deployment located in `.github/workflows/docker-deploy`. This one, builds the docker image on each push into main branch, and pushes it to dockerhub. For using this deployment, is neccesary to define a repository secret called `DOCKERHUB_TOKEN`, with the personal dockerhub token.

## Integration

For make easier the integration, the API deploys a swagger interface. Also in the repository there is a postman collection in `integration/panelais-models-api-api.postman_collection.json`, which you can generate the request with for any language included in the postman client.

## Disclaimer

Component developed by Francisco Pinto-Santos (@Gandalfran on GitHub) on 2023. For manteinance and bug reports please contact the developer at franpintosantos@air-institute.com.
Copyright BISITE 2023. All rights reserved. See license for details.
