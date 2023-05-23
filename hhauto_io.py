import aiohttp
import asyncio
import re

async def send_req(item)
    async with aiohttp.ClientSession() as session
        check = await session.post('https://hh.ru/applicant/vacancy_response/popup', data={"incomplete": False, "vacancy_id":int(item[0]), "resume_hash": f"{item[1]}","ignore_postponed": True, "_xsrf":f"{item[2]}", "letter": f"{item[3]}", "lux": True, "withoutTest": "no", "hhtmFromLabel": "undefined", "hhtmSourceLabel": "undefined"})
        
        print(check.status, item[0])
        if check.status != 200:
            response_json = await check.json()
            if response_json['error'] == 'negotiations-limit-exceeded':
                return False

async def main()
    n = 0
    
    cookies = "Вставь сюда свои куки"

    if cookies == "Вставь сюда свои куки":
        raise Exception("Ты забыл вставить сюда свои куки")
    
    if cookies == Вставь сюда свои куки
        raise Exception(Ты забыл вставить сюда свои куки)
    
    req.headers = {"Host": "hh.ru", "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.1 Safari/605.1.15", "Cookie": f"""{cookies}"""}

    """Здесь нам нужно вставить хеш резюме. Оно находиться в разделе https://hh.ru/applicant/resumes . Дальше ты должен перейти в одно из своих резюме и скопировать хеш после ссылки . Как пример https://hh.ru/resume/8376c225ff0b671c9b0039ed1f5850384c3570 . Тут нам нужно забрать 8376c225ff0b671c9b0039ed1f5850384c3570 и вставить в поле ниже"""
   
    resume_hash = "хеш резюме"

    if resume_hash == "хеш резюме":
        raise Exception("Ты забыл вставить сюда своё резюме")
    
    xsrf_token = re.search(_xsrf=(.);, cookies).group(1)
    
    """Ниже вставляем свое общее письмо."""

    letter = "Вставь сюда свое письмо"

    if letter == "Вставь сюда свое письмо":
        raise Exception("Ты забыл вставить сюда своё письмо")

    """Создание запроса для поиска вакансий: https://hh.ru/search/vacancy?text=автоматизация+python&salary=&schedule=remote&ored_clusters=true&enable_snippets=true"""

    search_link = "Вставь сюда свой поисковый запрос"

    if search_link == "Вставь сюда свой поисковый запрос":
        raise Exception("Ты забыл вставить сюда свой запрос")
    
    async with aiohttp.ClientSession(headers=headers) as session
        pool = []
        while True
            data = await session.get(f{search_link}&page={n})
            data_text = await data.text()
            links = re.findall('https://hh.ru/vacancy/(\d*)?', data_text, re.DOTALL)
            send_dict = []
            for link in links
                send_dict.append((link, resume_hash, xsrf_token, letter))
            if links == []
                break
            tasks = [send_req(item) for item in send_dict]
            check = await asyncio.gather(tasks)
            if False in check
                break
            n += 1
    
    await asyncio.gather(pool)

if __name__ == __main__
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
    loop.close()
