#!/usr/bin/python
# -*- coding: utf-8 -*-

from src.QcloudApi.modules.base import Base
import time
class Wenzhi(Base):
    requestHost = 'wenzhi.api.qcloud.com'

def main():
    action = 'TextKeywords'
    config = {
        'Region': 'gz',
        'secretId': '你的secretId',
        'secretKey': '你的secretKey',
        'method': 'get'
    }
    params = {
        'Action' : 'TextKeywords',
        'Nonce' : 345122,
        'Region' : 'sz',
        'SecretId' : '你的secretId',
        'Timestamp' : time.time(),
        'title': '今天市场指数沪深300大跌5%',
        'content': '今天市场指数沪深300大跌5%',
        'channel':'CHnews_news_finance'
    }
    service = Wenzhi(config)
    print(service.call(action, params))

if (__name__ == '__main__'):
    main()
