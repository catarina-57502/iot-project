# Projeto IoT

## Run Cloud

Start virtual machine  
Open SSL terminal  
Run:
```
node-red
```
IP
```
http://$PUBLIC_IP$:1880/
```

## DB String

```
mongodb+srv://admin:admin@iot.qwwov.mongodb.net/test
```

## Import flow

Import  
Select node-red/flow.json  
Deploy  

## Exercices

1. Both the number of charge and discharge cycles. (DONE)
2. Both the average and standard deviation of the charge and discharge time.
3. Range, average and standard deviation of the battery temperature, separately
   when charging and discharging.
4. A chart displaying two lines simultaneously on the same axis, each for a complete
   charge/discharge cycle selected by the user. The two cycles will be selected with
   reference to two distinct timestamps, hence allowing the visualization of the
   battery performance decrease between the two selected timestamps.
   
 Segunda fase:  
   a. predict the remaining battery available time (when discharging).  
   b. predict the remaining time until full charge is attained (when charging).
   
Com:  
   
Additionally, the groups must use the online data set (online_1.json and
   online_2.json) to continuously send the battery sensors data from their own local
   computer to the cloud-based MQTT broker, similarly as the mobile devices would on
   a realistic scenario.
