import logging
import requests
import threading
import os



def download_gambar(url=None):
    if (url is None):
        return False
    ff = requests.get(url)
    tipe = dict()
    tipe['image/png']='png'
    tipe['image/jpg']='jpg'
    tipe['image/jpeg']='jpg'

    content_type = ff.headers['Content-Type']
    logging.warning(content_type)
    if (content_type in list(tipe.keys())):
        namafile = os.path.basename(url)
        ekstensi = tipe[content_type]
        logging.warning(f"writing {namafile}.{ekstensi}")
        fp = open(f"{namafile}.{ekstensi}","wb")
        fp.write(ff.content)
        fp.close()
    else:
        return False




if __name__=='__main__':
    # download_gambar('https://pngimage.net/wp-content/uploads/2018/06/pokemon-go-pokemon-png-6.png')
    gambar=['https://connect-prd-cdn.unity.com/p/images/82c112ad-e763-494a-b9e4-e55159d0e336_XOq7Fo.jpg',
            'https://www.freepngimg.com/download/temp/10-2-pokemon-picture.jpeg',
            'https://pngimage.net/wp-content/uploads/2018/06/pokemon-go-pokemon-png-6.png']
    threads = []
    for i in range(3):
        t = threading.Thread(target=download_gambar, args=(gambar[i],))
        threads.append(t)

    for thr in threads:
        thr.start()
