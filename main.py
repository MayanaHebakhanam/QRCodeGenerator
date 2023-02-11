#It is a QR Code generator that is written in pure python
import pyqrcode
#To access png module in python
import png
from pyqrcode import QRCode

str="www.geeksforgeeks.org"
#Creating a QRCode, returns a QRCode object
url=pyqrcode.create(str)
url.png("myqr.png",scale=7)