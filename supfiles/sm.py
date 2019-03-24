import os

from tqdm import tqdm
from PIL import Image


# добавим необходимый пакет с opencv
import cv2


path='test'
filenames = []
for root, dirs, files in os.walk(path):
    for file in files:
        if file.endswith('.jpg') or file.endswith('.JPG'):
            filenames.append(os.path.join(root, file))

images = []
for filename in tqdm(filenames):
    image = cv2.imread(filename)

    # Нам надо сохранить соотношение сторон
    # чтобы изображение не исказилось при уменьшении
    # для этого считаем коэф. уменьшения стороны
    final_wide = 200
    r = float(final_wide) / image.shape[1]
    dim = (final_wide, int(image.shape[0] * r))

    # уменьшаем изображение до подготовленных размеров
    resized = cv2.resize(image, dim, interpolation=cv2.INTER_AREA)
    # cv2.imshow("Resize image", resized)
    cv2.waitKey(0)
    cv2.imwrite(filename, resized)

