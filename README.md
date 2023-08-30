# Alert_bot

##### Шаг 1: создать в Grafana/Alerting/Contact_points Webhook contact point  

![Image alt](https://gitlab.angarasecurity.ru/r.karpov/alert_bot/-/blob/main/docs/checkpoint.jpeg)


##### Шаг 2: выполнить в консоли сл. команды:  
при первом запуске:    
```no-highlight
docker build -t alert_bot .
```
```no-highlight
docker run -p 127.0.0.1:5002:5002 --name "alert_bot" alert_bot
``` 
при последующих запусках:  
```no-highlight
docker start Alert_bot
```
