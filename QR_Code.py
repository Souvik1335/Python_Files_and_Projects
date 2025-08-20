import cv2
import qrcode

# Step 1: Generate QR code
data = "https://copilot.microsoft.com/chats/bSLNsx8oH11KQFXj1aLP7"
qr = qrcode.make(data)
qr.save("MyQr.png")

# Step 2: Read QR code with OpenCV
img = cv2.imread("MyQr.png")
detector = cv2.QRCodeDetector()

decoded_data, points, _ = detector.detectAndDecode(img)

if decoded_data:
    print("Decoded Data:", decoded_data)
else:
    print("No QR code detected.")
