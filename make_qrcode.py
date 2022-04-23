import qrcode
import sys

def main(data):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=15,
        border=1
    )
    qr.add_data(data[1])
    qr.make(fit=True)
    img = qr.make_image()
    img.show()

if __name__ == '__main__':
   main(sys.argv)
