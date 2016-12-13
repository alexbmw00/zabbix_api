# -*- encoding: utf-8 -*-
import sys
import argparse
from zabbix.api import ZabbixAPI
from lib.configParse import configParse

config_file = './conf/zabbix_api.conf'

def getHostID(hostName=None):
    try:
        hostid = zapi.get_id('host', hostName)
        return hostid
    except:
        print "Error: No hostid found on hostname %s" % hostName
        sys.exit(1)

def getTemplateID(templateName=None):
    try:
        templateID = zapi.get_id('template', templateName)
        return templateID
    except:
        print "Error: No templateid found on template %s" % templateName
        sys.exit(1)

def linkTemplate(hostName=None, templateName=None):
    templateID = getTemplateID(templateName)
    hostID = getHostID(hostName)
    if templateID is None or hostID is None:
        print "Error: Can not link Template '%s' on Host '%s' because no tempalteID or HostID; Returned templateid is '%s', hostid is '%s" % (
        templateName, hostName, templateID, hostID)
        sys,exit(1)

    data = {
        'hosts': [{
            'hostid': hostID
        }],
        'templates': [{
            'templateid': templateID
        }]
    }

    try:
        result = zapi.do_request('template.massadd', data)
        try:
            templateids = result['result']['templateids']
            print "Info: Successfully link template %s to host %s" % (hostName, templateName)
        except:
            print "Warning: uncorrected returned value, it may fail to link template '%s' to host '%s', returned data is '%s' please check your dashboard" % (templateName, hostName, result)
    except Exception as e:
        print "Error: Failed to link template %s to host %s; Error Message: %s" % (templateName, hostName, e)

def main():
    global config
    global zapi
    config = configParse(config_file)
    config.parse()
    zapi = ZabbixAPI(url=config.zabbix_url, user=config.zabbix_user, password=config.zabbix_passwd)
    parser = argparse.ArgumentParser(description='Process some integers.')
    parser.add_argument('-l','--link-template', help='Provide template name if you need link template')
    parser.add_argument('-H','--host-name', help='Provides hostname to link template')
    args = parser.parse_args()
    if args.link_template:
        linkTemplate(hostName=args.host_name, templateName=args.link_template)
    else:
        print "Warning: Check your parameters!"
        sys.exit(1)

if __name__ == '__main__':
    main()
