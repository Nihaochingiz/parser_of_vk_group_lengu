
import requests;
import time;
import csv;


def take_1000_posts():
    version = 5.131
    domain = 'lengu'
    my = 'https://api.vk.com/method/wall.get?domain=lengu&access_token=ad85f2e2ad85f2e2ad85f2e2eaadfc4afeaad85ad85f2e2ccef4d562892862eb8e1f2b1&v=5.131'
    offset = 0
    count = 100
    token = 'ad85f2e2ad85f2e2ad85f2e2eaadfc4afeaad85ad85f2e2ccef4d562892862eb8e1f2b1'
    all_posts = []
    while offset < 1000:
        response = requests.get('https://api.vk.com/method/wall.get',
                                params ={
                                        'access_token': token,
                                        'v': version,
                                        'domain': domain,
                                        'count': count,
                                        'offset': offset
                                
                        }
                        )

        data = response.json()['response']['items']

        offset += 100
        all_posts.extend(data)
        
    return all_posts


def file_writer(data):
        img_url = []
        with open('lengu.csv', 'w',encoding="utf-8") as file:
           a_pen = csv.writer(file)
           a_pen.writerow(('likes', 'body', 'url'))
           for post in data:
                try:
                    if post['attachment'][0]['type']:
                        img_url = post[0]['attachment']['photo'] ['sizes'][-1] ['url']

                    else:
                        img_url = 'pass'
               
                except:
                     pass
                a_pen.writerow((post['likes']['count'], post ['text'], img_url))
all_posts = take_1000_posts()
file_writer(all_posts)



