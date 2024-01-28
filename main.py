import requests
from bs4 import BeautifulSoup as bs
from datetime import datetime

def getNumberOnly(string: str) -> int:
    numbers: [str] = [word for word in string if word.isdigit()]
    number: str = ''.join(numbers)
    return int(number)

def getInnerTextByCssSelector(soup: bs, selector: str) -> str:
    tags = soup.select(selector)
    firstTag = tags[0]
    firstTagStr: str = firstTag.text
    return firstTagStr

def getCurrentAccount(url) -> str:
    return url.split('/')[-1]
    
def getStatusDict(id: str, total: str, active: str, fault: str, recovery: str) -> dict:
    now = datetime.now()
    currentTimestamp = now.strftime('%Y-%m-%d %H:%M:%S')
    return {'id': id, 'total': total, 'active': active, 'fault': fault, 'recovery': recovery, 'timestamp': currentTimestamp}
    
# check if is there's any fault by address url.
def checkMining(url: str) -> None:
    htmlOfurl = requests.get(url).text
    soup = bs(htmlOfurl, 'lxml')
    
    now = datetime.now()
    
    currentAccount = getCurrentAccount(url)
    
    totalStr = getInnerTextByCssSelector(soup, '.text-xs.text-gray-800.text-right > span:first-child')
    numOfTotal = getNumberOnly(totalStr)
    
    activeStr = getInnerTextByCssSelector(soup, '.text-green-600')
    numOfActive = getNumberOnly(activeStr)
    
    faultStr = getInnerTextByCssSelector(soup, '.text-red-700')
    numOfFault = getNumberOnly(faultStr)
    
    recoveryStr = getInnerTextByCssSelector(soup, '.text-yellow-500')
    numOfRecovery = getNumberOnly(recoveryStr)
    
    print(getStatusDict(currentAccount, numOfTotal, numOfActive, numOfFault, numOfRecovery))
    
    
    # if numOfFaults > 0:
    #     print(f'Fault 발생: {numOfFaults}개의 Fault가 발생했습니다 - 계정 {currentAccount}.')
    # elif numOfFaults == 0:
    #     print(f'정상(Fault 없음): 계정 {currentAccount}는 정상 작동 중입니다.')
    
checkMining('https://filfox.info/ko/address/f033025')