import requests
import re
from multiprocessing import Pool

def send_req(item):
    check = item[4].post('https://hh.ru/applicant/vacancy_response/popup', data={"incomplete": False, "vacancy_id":int(item[0]), "resume_hash": f"{item[1]}","ignore_postponed": True, "_xsrf":f"{item[2]}", "letter": f"{item[3]}", "lux": True, "withoutTest": "no", "hhtmFromLabel": "undefined", "hhtmSourceLabel": "undefined"})

    print(check.status_code, item[0])
    if check.status_code != 200:
        if check.json()['error'] == 'negotiations-limit-exceeded':
            return False


if __name__ == "__main__":
    n = 0
    req = requests.Session()
    
    cookies = "Вставь сюда свои куки"

    if cookies == "Вставь сюда свои куки":
        raise Exception("Ты забыл вставить сюда свои куки")

    req.headers = {"Host": "hh.ru", "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.1 Safari/605.1.15", "Cookie": f"""{cookies}"""}

    """Здесь нам нужно вставить хеш резюме. Оно находиться в разделе https://hh.ru/applicant/resumes . Дальше ты должен перейти в одно из своих резюме и скопировать хеш после ссылки . Как пример https://hh.ru/resume/8376c225ff0b671c9b0039ed1f5850384c3570 . Тут нам нужно забрать 8376c225ff0b671c9b0039ed1f5850384c3570 и вставить в поле ниже"""

    resume_hash = "хеш резюме"

    if resume_hash == "хеш резюме":
        raise Exception("Ты забыл вставить сюда своё резюме")

    xsrf_token = re.search("_xsrf=(.*?);", cookies).group(1)

    """Ниже вставляем свое общее письмо."""

    letter = "Вставь сюда свое письмо"

    if letter == "Вставь сюда свое письмо":
        raise Exception("Ты забыл вставить сюда своё письмо")

    """Создание запроса для поиска вакансий: https://hh.ru/search/vacancy?text=автоматизация+python&salary=&schedule=remote&ored_clusters=true&enable_snippets=true"""

    search_link = "Вставь сюда свой поисковый запрос"

    if search_link == "Вставь сюда свой поисковый запрос":
        raise Exception("Ты забыл вставить сюда свой запрос")

    pool = Pool(processes=60)

    """Если ты все сделал правильно, то ты будешь видеть в консоли такие записи
    400 76870753
    200 76613497
    400 и 200 статусы это ок.
    Если ты видишь только 403 или 404 проверь, правильно ли ты вставил куки
    """

    while True:
        data = req.get(f"{search_link}&page={n}").text
        links = re.findall('https://hh.ru/vacancy/(\d*)?', data, re.DOTALL)
        send_dict = []
        for link in links:
            send_dict.append((link, resume_hash, xsrf_token, letter, req))
        if links == []:
            break
        check = pool.map(send_req, send_dict)
        if False in check:
            break
        n += 1
    pool.close()
    pool.join()