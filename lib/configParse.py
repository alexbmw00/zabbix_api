#!/usr/bin/python

import ConfigParser
import base64

class configParse:
    def __init__(self, conFile):
        self.conFile = conFile
        self.config = ConfigParser.ConfigParser()
        self.config.read(self.conFile)

    def parse(self):
        try:
            self.zabbix_url = self.config.get('zabbix', 'zabbix_url')
        except:
            self.zabbix_url = 'https://zabbix-qa.service.chinanetcloud.com/api_jsonrpc.php'

        try:
            self.zabbix_user = self.config.get('zabbix', 'zabbix_user')
        except:
            self.zabbix_user = 'zabbix'

        try:
           self.zabbix_passwd = base64.b64decode(self.config.get('zabbix', 'zabbix_passwd'))
        except:
            self.zabbix_passwd = 'zabbix'
