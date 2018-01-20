import urllib.request
from bs4 import BeautifulSoup
from db_helper import insert_event

def _get_html(url):
    req = urllib.request.Request(url)
    response = urllib.request.urlopen(req)
    html = response.read()
    soup = BeautifulSoup(html, "lxml")
    return soup

def find_all_contetns_on_page(url, page_num):
    url = url + page_num
    soup = _get_html(url)
    all_contents = soup.find_all("div", attrs={"class": "content-box-general"})
    return all_contents

#Extract details of each new coins from div contents
def extract_coin_detail(content):
    # ローカルのhtmlを直接開くとき
    h5 = content.find_all("h5")
    details = {}
    details["date"] = h5[0].strong.text.strip()
    details["coin_name"] = h5[1].text.strip()
    details["title"] = h5[2].text.strip()
    details["added_date"] = content.find("p", attrs={"class": "added-date"}).text.replace("[Added", "").replace("]","").strip()
    details["desc"] = content.find("p", attrs={"class": "description"}).text.strip()

    evidences = content.find_all("a", attrs={"class": "btn btn-w btn-xs btn-round"})
    proof_url = evidences[0].get("href")
    try:
        details["proof_url"] = "http://coinmarketcal.com/" + proof_url
    except:
        details["proof_url"] = ""
        print("No proof_url")

    try:
        details["source_url"] = evidences[1].get("href")
    except:
        print("No soucer url")
        details["source_url"] = ""
    details["validation_votes"] = content.find("span", attrs={"class": "votes"}).text
    details["validation_percentage"] = content.find("div", attrs={"class": "progress-bar pb-dark"}).get("aria-valuenow")

    return details

if __name__ == '__main__':
    page_num = 1
    url = 'http://coinmarketcal.com/?form%5Bmonth%5D=&form%5Byear%5D=&form%5Bsort_by%5D=created_desc&form%5Bsubmit%5D=&page='
    contents = find_all_contetns_on_page(url, str(page_num))
    for content in contents:
        values = extract_coin_detail(content)
        print(values)
        insert_event("./coin_alert.db", "coinalerts", values)
        print(res)
        total += 1
