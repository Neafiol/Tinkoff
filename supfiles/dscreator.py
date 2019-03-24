import json

import cv2
import requests
import vk,os
import os.path
from tqdm import tqdm
import argparse
from config import *

# wget "ur" -O dataset.rar
# unrar x dataset.rar
# https://tech.yandex.ru/disk/poligon/#!//v1/disk/resources/GetResourceUploadLink


session = vk.AuthSession('686148', vklog, vkpas, scope='wall, messages')
vk_api = vk.API(session)

#
def resize(path,final_wide):

    filenames = []
    for root, dirs, files in os.walk(path):
        for file in files:
            if file.endswith('.jpg') or file.endswith('.JPG'):
                filenames.append(os.path.join(root, file))

    for filename in tqdm(filenames):
        try:
            image = cv2.imread(filename)

            r = float(final_wide) / image.shape[1]
            dim = (final_wide, int(image.shape[0] * r))
            # уменьшаем изображение до подготовленных размеров
            resized = cv2.resize(image, dim, interpolation=cv2.INTER_AREA)
            # cv2.imshow("Resize image", resized)
            cv2.waitKey(0)
            cv2.imwrite(filename, resized)
        except:
            pass
def trans(path1,path2,lim):
    from random import sample

    filenames = []
    if(os.path.exists(path1)):
        os.mkdir(path2)
    for root, dirs, files in os.walk(path1):
        for file in files:
            if file.endswith('.jpg') or file.endswith('.JPG'):
                filenames.append(os.path.join(root, file))

    filenames= sample(filenames, min(lim,len(filenames)))
    for i,filename in tqdm(enumerate(filenames)):
        os.rename(filename,path2+"\\"+str(i)+'.jpg')


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

parser = argparse.ArgumentParser()

parser.add_argument('-c', "--count", default=10, type=int)
parser.add_argument('-o', "--owner_id", type=int)
parser.add_argument('-a', "--album_id", type=int)
parser.add_argument('-g', "--group", type=int)
parser.add_argument('-rs','--resize',nargs=2 )
parser.add_argument('-tr','--trans',nargs=3 )


args = parser.parse_args()


if(args.group):
    alboms=(vk_api.photos.getAlbums(owner_id=args.group,version=5.92))
    for a in alboms:
        try:
            loadfromal(args.group,a['aid'],a['size'],a['description'])
        except:
            print('error')

    exit(0)
if(args.resize):
    resize(args.resize[0],int(args.resize[1]))

if(args.album_id and args.owner_id):
    loadfromal(owner_id=args.owner_id,album_id=args.album_id,count=args.count)
if(args.trans):
    trans(args.trans[0],args.trans[1],int(args.trans[2]))

