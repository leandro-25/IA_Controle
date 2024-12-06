import cv2
import os
import psutil
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
from comtypes import CLSCTX_ALL
from cvzone.HandTrackingModule import HandDetector


def processoRodando(nomes_processos):

    for proc in psutil.process_iter(["pid", "name"]):
        if nomes_processos.lower() in proc.info["name"].lower():
            return True
    return False


cap = cv2.VideoCapture(0)
detector = HandDetector(detectionCon=0.7)


devices = AudioUtilities.GetSpeakers()
interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
volume = interface.QueryInterface(IAudioEndpointVolume)


paint_open = False

while True:
    ret, frame = cap.read()
    if not ret:
        break

    frame = cv2.flip(frame, 1)

    hands, frame = detector.findHands(frame)

    if hands:
        for hand in hands:

            if hand["type"] == "Left":

                lmList = hand["lmList"]

                fingers = detector.fingersUp(hand)

                num_fingers = fingers.count(1)

        if num_fingers == 1 and not paint_open and not processoRodando("mspaint"):
            print("Abrindo o Paint...")
            os.system("start mspaint")
            paint_open = True

        elif num_fingers == 4 and paint_open and processoRodando("mspaint"):
            print("Fechando o Paint...")
            os.system("taskkill /f /im mspaint.exe")
            paint_open = False

            if hand["type"] == "Right":

                lmList = hand["lmList"]

                fingers = detector.fingersUp(hand)

                num_fingers = fingers.count(1)

                if num_fingers == 0:
                    print("Nenhum dedo levantado na mão direita - Volume zero")
                    volume.SetMasterVolumeLevelScalar(0.0, None)
                elif num_fingers == 1:
                    print("Um dedo levantado na mão direita - Volume 20")
                    volume.SetMasterVolumeLevelScalar(0.2, None)
                elif num_fingers == 2:
                    print("Dois dedos levantados na mão direita - Volume 40")
                    volume.SetMasterVolumeLevelScalar(0.4, None)
                elif num_fingers == 3:
                    print("Três dedos levantados na mão direita - Volume 60")
                    volume.SetMasterVolumeLevelScalar(0.6, None)
                elif num_fingers == 4:
                    print("Quatro dedos levantados na mão direita - Volume 80")
                    volume.SetMasterVolumeLevelScalar(0.8, None)
                elif num_fingers == 5:
                    print("Todos os dedos levantados na mão direita - Volume 100")
                    volume.SetMasterVolumeLevelScalar(1.0, None)

    cv2.imshow("Detecção de Gestos", frame)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
