#!/usr/bin/env python
#coding=utf-8

import requests
import json
from .models import Secs

def crawl_secs():
	url = ('http://app.jg.eastmoney.com/Economy_Copy/GetAllBondTrade.do?'
		'STR_MARKET=沪深合计&type=1')
	headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.81 Safari/537.36 OPR/45.0.2552.812'}
	r = requests.get(url,headers=headers)

	ranks = json.loads(r.text)

	for rank in ranks:
		sec_id = int(rank['STR_SECODE'])
		sec_name = rank['STR_SECNAME']
		gqj_data = rank['GQJ_data']
		gqj_rank = int(rank['GQJ_rank'])
		Secs.objects.update_or_create(sec_id=sec_id, sec_name=sec_name, gqj_data=gqj_data,gqj_rank=gqj_rank)
