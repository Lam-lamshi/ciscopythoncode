import random
import urllib.request

def download_web_image(url):
    name=random.randrange(1,1000)
    fullname= str(name) + ".jpg"
    urllib.request.urlretrieve(url,fullname)

download_web_image("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQlodTiS9FXRXCy66Un1Rx31DMtUxi9KGQcgQ&usqp=CAU")