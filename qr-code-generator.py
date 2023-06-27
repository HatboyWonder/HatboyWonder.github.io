import qrcode
import qrcode.image.svg
from qrcode.image.styles.moduledrawers.pil import RoundedModuleDrawer

qr = qrcode.make(
    'https://hatboywonder.github.io/', 
    image_factory = qrcode.image.svg.SvgImage
)

qr.save('qrcode.svg')