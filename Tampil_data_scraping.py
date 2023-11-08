from bs4 import BeautifulSoup
import requests

def coba():
    try:
        content = requests.get('https://bmkg.go.id')
    except Exception:
        return None
    print(content)

    if content.status_code == 200:   
        soup = BeautifulSoup(content.text, 'html.parser')
        result = soup.find('div', {'class', 'col-md-6 col-xs-6 gempabumi-detail no-padding'})
        result = result.findChildren('li')
        print(result)
        print("\n")
        i = 0
        for res in result:
            print(i ,res)
    
    else:
        return None
    
def test1(result):
    return result

if __name__=='__main__':
    print("tampilan hasil scraping")
    result = coba()
    test1(result)

