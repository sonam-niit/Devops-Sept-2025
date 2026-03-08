# App monitoring using Prometheus and Grafana with docker compose

- create app.py (python-code)
- create requirements.txt (for dependency)
- create docker file to build image for Python Project
- create prometheus.yml for configuration
- create docker-compose.yml file 

*Here its using Prometheus image, grafana image to start containers*

```bash
docker-compose up -d --build

docker-compose logs
# if all servers running
```

- access localhost:9090 (prometheus)
- access localhost:5000 (python app) - refresh multiple time
- in prometheus query:
    + http_requests_total (you can see no of req)
- access localhost:3000 (grafana app)
    + access: admin / admin
    + add datasource: prometheus: use service name to connect with pometheus not localhost:
        - http://prometheus:9090
    + test
- create dashboard:
    + panel name (traffic trend)
    + query: rate(http_requests_total[1m])

*fi you are getting error 3000 port is busy as grafana server is already running*
- sudo service grafana-server stop

- again do docker-compose up -d

- to down all services just do:
    + docker compose down 