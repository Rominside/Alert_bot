# Alert_bot



## Getting started

### Шаг 1: создать в Grafana/Alerting/Contact_points Webhook contact point

### Шаг 2: выполнить в консоли сл. команды:  
при первом запуске:  
`sudo docker build -t Alert_bot .`  
`sudo docker run -p 127.0.0.1:5002:5002 --name "Alert_bot" Alert_bot`  
при последующих запусках:  
`sudo docker start Alert_bot`
