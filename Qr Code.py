import pyqrcode
import png
from pyqrcode import QRCode

address = 'https://www.chelseafc.com/en/news/latest-news'
url = pyqrcode.create(address)
url.png('Chelsea_News.png', scale=8)


