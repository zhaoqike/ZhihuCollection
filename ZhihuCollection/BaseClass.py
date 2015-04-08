###https://github.com/YaoZeyuan/ZhihuHelp__Python/tree/master/zhihuhelp1.7.0/codes

import re
import configparser
import os


class BaseClass(object):
    u'''
    to store often used functions
    '''

    ### global variables
    check_update_flag = False
    catch_anster_flag = False
    buffer_flag = False
    database_filename = u'./ZhihuDB.db'

    def printDict(self,data = {},key = '',prefix = ''):
        if isinstance(data,dict):
            for key in data.keys:
                self.printDict(data[key],key,prefix+'    ')
        else:
            print(prefix_str(key)+' => '+str(data))
        return

    def printCurrentDir(self):
        print(os.path.realpath('.'))
        return

    def mkdir(self,path):
        try:
            os.mkdir(path)
        except OSError:
            print('dir is already exist')
        return

    def chdir(self,path):
        try:
            os.chdir(path)
        except OSError:
            print('dir not exist,please create it')
            mkdir(path)
            os.chdir(path)
        return

class SqlClass(object):
    
    def saveToDB(self,cursor,data = {}, primaryKey = '', tableName = ''):
        replaceSql = 'replace into ' + tableName + ' ('
        placeholder = ') values ('
        varTuple = []

        for columnKey in data:
            replaceSql += columnKey+','
            placeholder +='?,'
            varTuple.append(data[columnKey])

        cursor.execute(replaceSql[:-1]+placeholder[:-1]+')',tuple(varTuple))
        return



import urllib
import urllib3
import socket
import zlib
import json

class HttpBaseClass(object):

    def getHttpContent(self,url = '',extraHeader = {},data = None,timeout = 5):
        if data == None:
            request = urllib3.request(url = url)
        else:
            request = urllib3.request(url = url,data = data)

        for headerKey in extraHeader.keys:
            request.add_header(headerKey,extraHeader[headerKey])
