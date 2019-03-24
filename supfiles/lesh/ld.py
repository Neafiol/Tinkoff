import json

import cv2
import requests
import vk,os
import os.path
from tqdm import tqdm
import argparse

# wget "ur" -O dataset.rar
# unrar x dataset.rar
# https://tech.yandex.ru/disk/poligon/#!//v1/disk/resources/GetResourceUploadLink

parser = argparse.ArgumentParser()

parser.add_argument('-c', dest="count", default=10, type=int)
parser.add_argument('-o', dest="owner_id", default=-1, type=int)
parser.add_argument('-a', dest="album_id", default=-1, type=int)
parser.add_argument('-g', dest="group", default=-1, type=int)
parser.add_argument('-rs', dest=["path",'final_wide'],action='resize', default=-1, type=int)

args = parser.parse_args()
session = vk.AuthSession('6861498', '+79775766448', 'hersones17', scope='wall, messages')
vk_api = vk.API(session)

#
def resize(path,final_wide):
    filenames = []
    for root, dirs, files in os.walk(path):
        for file in files:
            if file.endswith('.jpg') or file.endswith('.JPG'):
                filenames.append(os.path.join(root, file))

    images = []
    for filename in tqdm(filenames):
        image = cv2.imread(filename)

        r = float(final_wide) / image.shape[1]
        dim = (final_wide, int(image.shape[0] * r))
        # уменьшаем изображение до подготовленных размеров
        resized = cv2.resize(image, dim, interpolation=cv2.INTER_AREA)
        # cv2.imshow("Resize image", resized)
        cv2.waitKey(0)
        cv2.imwrite(filename, resized)

def loadfromal(owner_id,album_id,count,foldname='albom'):
    urls = vk_api.photos.get(owner_id=owner_id,album_id=album_id,count=count,version=5.92)
    # print(urls[0])
    if(foldname==""):
        foldname='noname'
    try:
        if(not os.path.exists(foldname) ):
            os.mkdir(foldname)
    except:
        return
    for u in tqdm(urls):
        p = requests.get(u["src_big"])
        out = open(foldname+'/'+str(u['pid'])+".jpg", "wb")
        out.write(p.content)
        out.close()

if(args.group!=-1):
    alboms=(vk_api.photos.getAlbums(owner_id=args.group,version=5.92))
    for a in alboms:
        try:
            loadfromal(args.group,a['aid'],a['size'],a['description'])
        except:
            print('error')

    exit(0)

if(args.owner_id==-1):
    print("You need add owner id of groupe ` -o -43264 `")
    exit(0)
if(args.album_id==-1):
    print("You need add album id ` -a 787264 `")
    exit(0)
loadfromal(owner_id=args.owner_id,album_id=args.album_id,count=args.count)

