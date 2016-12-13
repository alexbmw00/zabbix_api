# zabbix_api

# Run createHost
```
python createHost.py -c 'hostname' -i 'host ip' -p 'host port(default is 10050)'
```
For example:
```
python createHost.py -c 'srv-test-test1' -i '127.0.0.1' -p '10058'
```

# Run linkTemplate
```
python linkTemplate.py -l 'template name' -H 'host name'
```
For example:
```
python linkTemplate.py -l 'Template_Linux' -H 'srv-test-test'
```
