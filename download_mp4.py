import json
import requests
import os
import re
download_dir=r''
headers={
    'Referer': 'https://aps-qa.bravuratechnologies.com/',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/142.0.0.0 Safari/537.36 Edg/142.0.0.0'
}

def validateTitle(title):
    rstr = r"[\/\\\:\*\?\"\<\>\|]"  # '/ \ : * ? " < > |'
    new_title = re.sub(rstr, "", title)
    return new_title


with open(file=os.path.join(download_dir,'live_link.json')) as js_file:
    js_data=dict(json.load(js_file))

date_list=list(js_data.keys())
print(date_list)
def download(data_dict:dict):
    title=data_dict['title']
    mp4_link=data_dict['mp4']
    vtt_link=data_dict['vtt']
    print(title)
    title=validateTitle(title)
    try:
        print(mp4_link)
        mp4_data=requests.get(url=mp4_link,headers=headers).content
        with open(file=os.path.join(download_dir,f'{title}.mp4'),mode='wb') as mp4_file:
            mp4_file.write(mp4_data)
        print(f'Download {title}.mp4')
    except:
        pass
    try:
        print(vtt_link)
        vtt_data=requests.get(url=vtt_link,headers=headers).content
        with open(file=os.path.join(download_dir,f'{title}.vtt'),mode='wb') as vtt_file:
            vtt_file.write(vtt_data)
        print(f'Download {title}.vtt')
    except:
        pass

if __name__ == '__main__':
    for data_dict in js_data['2025-11-21']:
        download(data_dict)


