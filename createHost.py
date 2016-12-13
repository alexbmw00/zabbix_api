# -*- encoding: utf-8 -*-
import sys
import argparse
from zabbix.api import ZabbixAPI
from lib.configParse import configParse

config_file = './conf/zabbix_api.conf'

def getTemplateID(templateName=None):
    try:
        templateID = zapi.get_id('template', templateName)
        return templateID
    except:
        print "Error: No templateid found on template %s" % templateName
        sys.exit(1)

def createHost(hostName=None, hostIP='127.0.0.1', hostPort='10050', groupID=None, templateID=None):
    data = {
        'host': hostName,
        'interfaces': [{
            'type': 1,
            'main': 1,
            'useip': 1,
            'ip': hostIP,
            'dns': '',
            'port': hostPort}],
        'groups': [{'groupid': groupID}],
        'templates': [{'templateid': templateID}],
        'inventory_mode': -1
    }

    try:
        result = zapi.do_request('host.create', data)
        try:
            hostID = result['result']['hostids'][0]
            print "Info: Successfully create host '%s', hostid is '%s'" % (hostName, hostID)
        except:
            print "Warning: uncorrected returned data, it may fail to create host '%s', please check your dashboard; Returned data is: '%s'" % (hostName, result)
    except Exception as e:
        print "Error: Failed to create host %s; Error Message: %s" % (hostName, e)

def main():
    global config
    global zapi
    config = configParse(config_file)
    config.parse()
    zapi = ZabbixAPI(url=config.zabbix_url, user=config.zabbix_user, password=config.zabbix_passwd)
    parser = argparse.ArgumentParser(description='Process some integers.')
    parser.add_argument('-c','--create-host', help='Provide host name if you need create host')
    parser.add_argument('-p','--host-port', default='10050', help='Provide host port if you need create host')
    parser.add_argument('-i','--host-ip', help='Provide host ip if you need create host')
    args = parser.parse_args()
    if args.create_host:
        createHost(hostName=args.create_host, hostIP=args.host_ip, hostPort=args.host_port, groupID='347',
                   templateID='10068')
    else:
        print "Warning: Check your parameters!"
        sys.exit(1)

if __name__ == '__main__':
    main()
