import pandas as pd
import requests

df = pd.read_csv('app_game_ranking.csv', header=None)

data = df[8].values.tolist()

datadic = {eval(x)['package_name']:eval(x)['app_name'] for x in data}


payload = '\
{\
"pgmNo": "110",\
"menuNo": "471",\
"maxTa": "33.0",\
"serviceSe": "F00101",\
"selectType": "2",\
"mddlClssCd": "SFC01",\
"txtStnNm": %EA%B4%80%EC%95%85%EC%82%B0%2C%EC%84%9C%EC%9A%B8%2C%EB%B6%80%EC%82%B0%2C%EB%8C%80%EA%B5%AC%2C%EB%8C%80%EA%B5%AC(%EA%B8%B0)%2C%EA%B0%95%ED%99%94%2C%EB%B0%B1%EB%A0%B9%EB%8F%84%2C%EC%9D%B8%EC%B2%9C%2C%EA%B4%91%EC%A3%BC%2C%EB%8C%80%EC%A0%84%2C%EC%9A%B8%EC%82%B0%2C%EB%8F%99%EB%91%90%EC%B2%9C%2C%EC%88%98%EC%9B%90%2C%EC%96%91%ED%8F%89%2C%EC%9D%B4%EC%B2%9C%2C%ED%8C%8C%EC%A3%BC%2C%EA%B0%95%EB%A6%89%2C%EB%8C%80%EA%B4%80%EB%A0%B9%2C%EB%8F%99%ED%95%B4%2C%EB%B6%81%EA%B0%95%EB%A6%89%2C%EB%B6%81%EC%B6%98%EC%B2%9C%2C%EC%82%BC%EC%B2%99%2C%EC%86%8D%EC%B4%88%2C%EC%98%81%EC%9B%94%2C%EC%9B%90%EC%A3%BC%2C%EC%9D%B8%EC%A0%9C%2C%EC%A0%95%EC%84%A0%EA%B5%B0%2C%EC%B2%A0%EC%9B%90%2C%EC%B6%98%EC%B2%9C%2C%ED%83%9C%EB%B0%B1%2C%ED%99%8D%EC%B2%9C%2C%EB%B3%B4%EC%9D%80%2C%EC%A0%9C%EC%B2%9C%2C%EC%B2%AD%EC%A3%BC%2C%EC%B6%94%ED%92%8D%EB%A0%B9%2C%EC%B6%A9%EC%A3%BC%2C%EA%B8%88%EC%82%B0%2C%EB%B3%B4%EB%A0%B9%2C%EB%B6%80%EC%97%AC%2C%EC%84%9C%EC%82%B0%2C%EC%B2%9C%EC%95%88%2C%ED%99%8D%EC%84%B1%2C%EA%B3%A0%EC%B0%BD%2C%EA%B3%A0%EC%B0%BD%EA%B5%B0%2C%EA%B5%B0%EC%82%B0%2C%EB%82%A8%EC%9B%90%2C%EB%B6%80%EC%95%88%2C%EC%88%9C%EC%B0%BD%EA%B5%B0%2C%EC%9E%84%EC%8B%A4%2C%EC%9E%A5%EC%88%98%2C%EC%A0%84%EC%A3%BC%2C%EC%A0%95%EC%9D%8D%2C%EA%B0%95%EC%A7%84%EA%B5%B0%2C%EA%B3%A0%ED%9D%A5%2C%EA%B4%91%EC%96%91%EC%8B%9C%2C%EB%AA%A9%ED%8F%AC%2C%EB%AC%B4%EC%95%88%2C%EB%B3%B4%EC%84%B1%EA%B5%B0%2C%EC%88%9C%EC%B2%9C%2C%EC%97%AC%EC%88%98%2C%EC%98%81%EA%B4%91%EA%B5%B0%2C%EC%99%84%EB%8F%84%2C%EC%9E%A5%ED%9D%A5%2C%EC%A3%BC%EC%95%94%2C%EC%A7%84%EB%8F%84(%EC%B2%A8%EC%B0%B0%EC%82%B0)%2C%EC%A7%84%EB%8F%84%EA%B5%B0%2C%ED%95%B4%EB%82%A8%2C%ED%9D%91%EC%82%B0%EB%8F%84%2C%EA%B2%BD%EC%A3%BC%EC%8B%9C%2C%EA%B5%AC%EB%AF%B8%2C%EB%AC%B8%EA%B2%BD%2C%EB%B4%89%ED%99%94%2C%EC%83%81%EC%A3%BC%2C%EC%95%88%EB%8F%99%2C%EC%98%81%EB%8D%95%2C%EC%98%81%EC%A3%BC%2C%EC%98%81%EC%B2%9C%2C%EC%9A%B8%EB%A6%89%EB%8F%84%2C%EC%9A%B8%EC%A7%84%2C%EC%9D%98%EC%84%B1%2C%EC%B2%AD%EC%86%A1%EA%B5%B0%2C%ED%8F%AC%ED%95%AD%2C%EA%B1%B0%EC%A0%9C%2C%EA%B1%B0%EC%B0%BD%2C%EA%B9%80%ED%95%B4%EC%8B%9C%2C%EB%82%A8%ED%95%B4%2C%EB%B0%80%EC%96%91%2C%EB%B6%81%EC%B0%BD%EC%9B%90%2C%EC%82%B0%EC%B2%AD%2C%EC%96%91%EC%82%B0%EC%8B%9C%2C%EC%9D%98%EB%A0%B9%EA%B5%B0%2C%EC%A7%84%EC%A3%BC%2C%EC%B0%BD%EC%9B%90%2C%ED%86%B5%EC%98%81%2C%ED%95%A8%EC%96%91%EA%B5%B0%2C%ED%95%A9%EC%B2%9C%2C%EA%B3%A0%EC%82%B0%2C%EC%84%9C%EA%B7%80%ED%8F%AC%2C%EC%84%B1%EC%82%B0%2C%EC%84%B1%EC%82%B0%2C%EC%84%B1%EC%82%B0%ED%8F%AC%2C%EC%A0%9C%EC%A3%BC%2C%EC%84%B8%EC%A2%85",\
"schStnId": "116%2C108%2C159%2C143%2C176%2C201%2C102%2C112%2C156%2C133%2C152%2C98%2C119%2C202%2C203%2C99%2C105%2C100%2C106%2C104%2C93%2C214%2C90%2C121%2C114%2C211%2C217%2C95%2C101%2C216%2C212%2C226%2C221%2C131%2C135%2C127%2C238%2C235%2C236%2C129%2C232%2C177%2C172%2C251%2C140%2C247%2C243%2C254%2C244%2C248%2C146%2C245%2C259%2C262%2C266%2C165%2C164%2C258%2C174%2C168%2C252%2C170%2C260%2C256%2C175%2C268%2C261%2C169%2C283%2C279%2C273%2C271%2C137%2C136%2C277%2C272%2C281%2C115%2C130%2C278%2C276%2C138%2C294%2C284%2C253%2C295%2C288%2C255%2C289%2C257%2C263%2C192%2C155%2C162%2C264%2C285%2C185%2C189%2C188%2C187%2C265%2C184%2C239",\
"startDt": "20220721"\
}\
'

payload2 = "fileType=&pgmNo=110&menuNo=471&pageIndex=&maxTa=33.0&stnGroupSns=&serviceSe=F00101&selectType=2&mddlClssCd=SFC01&txtStnNm=%EA%B4%80%EC%95%85%EC%82%B0%2C%EC%84%9C%EC%9A%B8%2C%EB%B6%80%EC%82%B0%2C%EB%8C%80%EA%B5%AC%2C%EB%8C%80%EA%B5%AC(%EA%B8%B0)%2C%EA%B0%95%ED%99%94%2C%EB%B0%B1%EB%A0%B9%EB%8F%84%2C%EC%9D%B8%EC%B2%9C%2C%EA%B4%91%EC%A3%BC%2C%EB%8C%80%EC%A0%84%2C%EC%9A%B8%EC%82%B0%2C%EB%8F%99%EB%91%90%EC%B2%9C%2C%EC%88%98%EC%9B%90%2C%EC%96%91%ED%8F%89%2C%EC%9D%B4%EC%B2%9C%2C%ED%8C%8C%EC%A3%BC%2C%EA%B0%95%EB%A6%89%2C%EB%8C%80%EA%B4%80%EB%A0%B9%2C%EB%8F%99%ED%95%B4%2C%EB%B6%81%EA%B0%95%EB%A6%89%2C%EB%B6%81%EC%B6%98%EC%B2%9C%2C%EC%82%BC%EC%B2%99%2C%EC%86%8D%EC%B4%88%2C%EC%98%81%EC%9B%94%2C%EC%9B%90%EC%A3%BC%2C%EC%9D%B8%EC%A0%9C%2C%EC%A0%95%EC%84%A0%EA%B5%B0%2C%EC%B2%A0%EC%9B%90%2C%EC%B6%98%EC%B2%9C%2C%ED%83%9C%EB%B0%B1%2C%ED%99%8D%EC%B2%9C%2C%EB%B3%B4%EC%9D%80%2C%EC%A0%9C%EC%B2%9C%2C%EC%B2%AD%EC%A3%BC%2C%EC%B6%94%ED%92%8D%EB%A0%B9%2C%EC%B6%A9%EC%A3%BC%2C%EA%B8%88%EC%82%B0%2C%EB%B3%B4%EB%A0%B9%2C%EB%B6%80%EC%97%AC%2C%EC%84%9C%EC%82%B0%2C%EC%B2%9C%EC%95%88%2C%ED%99%8D%EC%84%B1%2C%EA%B3%A0%EC%B0%BD%2C%EA%B3%A0%EC%B0%BD%EA%B5%B0%2C%EA%B5%B0%EC%82%B0%2C%EB%82%A8%EC%9B%90%2C%EB%B6%80%EC%95%88%2C%EC%88%9C%EC%B0%BD%EA%B5%B0%2C%EC%9E%84%EC%8B%A4%2C%EC%9E%A5%EC%88%98%2C%EC%A0%84%EC%A3%BC%2C%EC%A0%95%EC%9D%8D%2C%EA%B0%95%EC%A7%84%EA%B5%B0%2C%EA%B3%A0%ED%9D%A5%2C%EA%B4%91%EC%96%91%EC%8B%9C%2C%EB%AA%A9%ED%8F%AC%2C%EB%AC%B4%EC%95%88%2C%EB%B3%B4%EC%84%B1%EA%B5%B0%2C%EC%88%9C%EC%B2%9C%2C%EC%97%AC%EC%88%98%2C%EC%98%81%EA%B4%91%EA%B5%B0%2C%EC%99%84%EB%8F%84%2C%EC%9E%A5%ED%9D%A5%2C%EC%A3%BC%EC%95%94%2C%EC%A7%84%EB%8F%84(%EC%B2%A8%EC%B0%B0%EC%82%B0)%2C%EC%A7%84%EB%8F%84%EA%B5%B0%2C%ED%95%B4%EB%82%A8%2C%ED%9D%91%EC%82%B0%EB%8F%84%2C%EA%B2%BD%EC%A3%BC%EC%8B%9C%2C%EA%B5%AC%EB%AF%B8%2C%EB%AC%B8%EA%B2%BD%2C%EB%B4%89%ED%99%94%2C%EC%83%81%EC%A3%BC%2C%EC%95%88%EB%8F%99%2C%EC%98%81%EB%8D%95%2C%EC%98%81%EC%A3%BC%2C%EC%98%81%EC%B2%9C%2C%EC%9A%B8%EB%A6%89%EB%8F%84%2C%EC%9A%B8%EC%A7%84%2C%EC%9D%98%EC%84%B1%2C%EC%B2%AD%EC%86%A1%EA%B5%B0%2C%ED%8F%AC%ED%95%AD%2C%EA%B1%B0%EC%A0%9C%2C%EA%B1%B0%EC%B0%BD%2C%EA%B9%80%ED%95%B4%EC%8B%9C%2C%EB%82%A8%ED%95%B4%2C%EB%B0%80%EC%96%91%2C%EB%B6%81%EC%B0%BD%EC%9B%90%2C%EC%82%B0%EC%B2%AD%2C%EC%96%91%EC%82%B0%EC%8B%9C%2C%EC%9D%98%EB%A0%B9%EA%B5%B0%2C%EC%A7%84%EC%A3%BC%2C%EC%B0%BD%EC%9B%90%2C%ED%86%B5%EC%98%81%2C%ED%95%A8%EC%96%91%EA%B5%B0%2C%ED%95%A9%EC%B2%9C%2C%EA%B3%A0%EC%82%B0%2C%EC%84%9C%EA%B7%80%ED%8F%AC%2C%EC%84%B1%EC%82%B0%2C%EC%84%B1%EC%82%B0%2C%EC%84%B1%EC%82%B0%ED%8F%AC%2C%EC%A0%9C%EC%A3%BC%2C%EC%84%B8%EC%A2%85&schStnId=116%2C108%2C159%2C143%2C176%2C201%2C102%2C112%2C156%2C133%2C152%2C98%2C119%2C202%2C203%2C99%2C105%2C100%2C106%2C104%2C93%2C214%2C90%2C121%2C114%2C211%2C217%2C95%2C101%2C216%2C212%2C226%2C221%2C131%2C135%2C127%2C238%2C235%2C236%2C129%2C232%2C177%2C172%2C251%2C140%2C247%2C243%2C254%2C244%2C248%2C146%2C245%2C259%2C262%2C266%2C165%2C164%2C258%2C174%2C168%2C252%2C170%2C260%2C256%2C175%2C268%2C261%2C169%2C283%2C279%2C273%2C271%2C137%2C136%2C277%2C272%2C281%2C115%2C130%2C278%2C276%2C138%2C294%2C284%2C253%2C295%2C288%2C255%2C289%2C257%2C263%2C192%2C155%2C162%2C264%2C285%2C185%2C189%2C188%2C187%2C265%2C184%2C239&startDt=20220721"

payload_ex="fileType=&pgmNo=110&menuNo=471&pageIndex=&maxTa=33.0&stnGroupSns=&serviceSe=F00101&selectType=2&mddlClssCd=SFC01&txtStnNm=%EC%84%9C%EC%9A%B8%2C%EB%B6%80%EC%82%B0&schStnId=108%2C159&startDt=20220722"


headers = {'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.63 Mobile Safari/537.36', 
           'Content-type':'application/x-www-form-urlencoded; charset=UTF-8', 
           'origin':'https://data.kma.go.kr'
           }
url = 'https://data.kma.go.kr/climate/ehum/selectEhumChartAjax.do'

# payload ='{"data_ym":"2206","bjd_code":false,"industry":false,"min_sales":false,"max_sales":false,"min_salary":false,"max_salary":false,"min_prsn":false,"max_prsn":false,"min_prsn_ratio":false,"max_prsn_ratio":false,"only_good_cmpn":false,"sort":"SALES_VALUE","order":"DESC","page":2,"size":10}'


# request 접속
def bs(url,payload):
    #10번 시도
    for i in range(3):
        # time.sleep(0.5)
        # try:
        response = requests.post(url,headers=headers, data=payload)
        # print(payload['packageName'],' - try :', i)
        return response.json()

        # except:
        #     continue
        
    return False




he = bs(url,payload_ex)

df = pd.DataFrame(he['data'])
print(df)
            
print('완료')

