from Core import NetWork
from Core.URLs import WebUrl
from Core.NetWork import visit
from Core.NetWork import VisitorWays
import requests

def WebUrlPostTest():
    weburl = WebUrl.WebUrlBuilder().addHost("https://yz.chsi.com.cn/zsml/queryAction.do").build()
    res = {}
    res['ssdm'] = ''
    res['dwmc'] = ''
    res['mldm'] = "01"
    res['mlmc'] = ''
    res['yjxkdm'] = "0101"
    res['zymc'] = ''

    header = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.183 Safari/537.36',
        'Cookie': 'JSESSIONID=013DAE2815E6FE159B4DA440DF470A2D; zg_did=%7B%22did%22%3A%20%22175a325eff2ba-0fbf63495c84d7-230346d-144000-175a325eff35f5%22%7D; _ga=GA1.3.1289928378.1604759974; zg_14e129856fe4458eb91a735923550aa6=%7B%22sid%22%3A%201604759973881%2C%22updated%22%3A%201604759977136%2C%22info%22%3A%201604759973891%2C%22superProperty%22%3A%20%22%7B%7D%22%2C%22platform%22%3A%20%22%7B%7D%22%2C%22utm%22%3A%20%22%7B%7D%22%2C%22referrerDomain%22%3A%20%22www.baidu.com%22%2C%22landHref%22%3A%20%22https%3A%2F%2Fwww.chsi.com.cn%2F%22%7D; zg_0d76434d9bb94abfaa16e1d5a3d82b52=%7B%22sid%22%3A%201604759977544%2C%22updated%22%3A%201604759995845%2C%22info%22%3A%201604759977546%2C%22superProperty%22%3A%20%22%7B%7D%22%2C%22platform%22%3A%20%22%7B%7D%22%2C%22utm%22%3A%20%22%7B%7D%22%2C%22referrerDomain%22%3A%20%22www.chsi.com.cn%22%2C%22landHref%22%3A%20%22https%3A%2F%2Fmy.chsi.com.cn%2Farchive%2Findex.jsp%22%7D; acw_tc=2760828e16104374395925239e629adfe364bf9e5b40d9315a100d8f19fb5a; JSESSIONID=059E1FDF24699EA6FC8E1A7E078C91AC; XSRF-CCKTOKEN=8acf6963fb2cb86e9b83193b6317036e; CHSICC_CLIENTFLAGYZ=b3f23705f49aa1f0153b27a2a1b49236; _gid=GA1.3.1966964760.1610437443; CHSICC_CLIENTFLAGZSML=d8c16c2f542f3f0f2eb1a9a0fc30c2bb; zg_adfb574f9c54457db21741353c3b0aa7=%7B%22sid%22%3A%201610437442868%2C%22updated%22%3A%201610438643810%2C%22info%22%3A%201610437442871%2C%22superProperty%22%3A%20%22%7B%7D%22%2C%22platform%22%3A%20%22%7B%7D%22%2C%22utm%22%3A%20%22%7B%7D%22%2C%22referrerDomain%22%3A%20%22www.baidu.com%22%2C%22landHref%22%3A%20%22https%3A%2F%2Fyz.chsi.com.cn%2F%22%7D'
    }

    res = visit(weburl,VisitorWays.POST,res,header)
    # print(res.encoding,res.apparent_encoding)
    res.encoding = res.apparent_encoding
    # print(res.text)
    return res

if __name__ == '__main__':
    # res = NetWork.visit(WebUrl("https://shanghairanking.cn/api/pub/v1/bcsr/rank?"),NetWork.VisitorWays.GET,{'target_yr':'2020',"subj_code":0},dict())
    # print(res.text)
    WebUrlPostTest()