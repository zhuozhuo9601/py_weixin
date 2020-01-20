import requests

url = "http://hops.hoolai.com/turnover/special_operation/"
# y_list = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12']
# y_list = ['02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12']
# y_list = ['04', '05', '06', '07', '08', '09', '10', '11', '12']
# y_list = ['01', '02', '03', '04', '05', '06', '07', '08', '09']
# y_list = ['01', '02', '03', '04', '05', '06', '07']
# y_list = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10']
# y_list = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11']
# y_list = ['01', '02', '03', '04', '05', '06', '07', '11', '12']
# y_list = ['06', '07', '08', '09', '10', '11', '12']
# y_list = ['03', '04', '05', '06', '07', '08', '09', '10', '11']
# y_list = ['02', '03', '05', '06', '10', '12']
# y_list = ['09', '10', '11', '12']
y_list = ['11', '12']
for i in y_list:
    data = {'oper_type': 'oper_syn',
            'year_months': '2019-{0}'.format(i),
            'mul_id': '1845'}
    headers = {
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Connection': 'keep-alive',
        'Content-Length': '49',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'Cookie': 'sessionid=qmkczchigldsfa6wbzjvn62z3o8xip4k',
        'Host': 'hops.hoolai.com',
        'Origin': 'http://hops.hoolai.com',
        'Referer': 'http://hops.hoolai.com/turnover/multipleinfo/',
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36',
        'X-Requested-With': 'XMLHttpRequest'
    }
    res = requests.post(url=url, data=data, headers=headers, verify=False)
    print(res.text)
