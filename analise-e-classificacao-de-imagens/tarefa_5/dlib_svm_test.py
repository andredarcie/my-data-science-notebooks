import os
import dlib
import cv2
import glob

# Le os detectores gerados no treinamento
detectorObjetoA = dlib.simple_object_detector("res/detectorobjetoa.svm")
detectorObjetoB = dlib.simple_object_detector("res/detectorobjetob.svm")
detectorObjetoC = dlib.simple_object_detector("res/detectorobjetoc.svm")

for imagem in glob.glob(os.path.join("imagens", "*.jpg")):
    print(imagem)
    img = cv2.imread(imagem)
    objetoADetectados = detectorObjetoA(img, 2)
    for d in objetoADetectados:
        e, t, d, b = (int(d.left())), int(d.top()), int(d.right()), int(d.bottom())
        cv2.rectangle(img, (e, t), (d, b), (255, 0, 0), 2)
        print("a: " + str(e) + ' - ' + str(t))

    if len(objetoBDetectados) > 0:
        cv2.imwrite(imagem.replace(".jpg", "_objetoa.jpg"), img)

    img = cv2.imread(imagem)
    objetoBDetectados = detectorObjetoB(img, 2)
    for d in objetoBDetectados:
        e, t, d, b = (int(d.left())), int(d.top()), int(d.right()), int(d.bottom())
        cv2.rectangle(img, (e, t), (d, b), (255, 0, 0), 2)
        print("b: " + str(e) + ' - ' + str(t))

    if len(objetoBDetectados) > 0:
        cv2.imwrite(imagem.replace(".jpg", "_objetob.jpg"), img)

    img = cv2.imread(imagem)
    objetoCDetectados = detectorObjetoC(img, 2)
    for d in objetoCDetectados:
        e, t, d, b = (int(d.left())), int(d.top()), int(d.right()), int(d.bottom())
        cv2.rectangle(img, (e, t), (d, b), (255, 0, 0), 2)
        print("c: " + str(e) + ' - ' + str(t))

    if len(objetoCDetectados) > 0:
        cv2.imwrite(imagem.replace(".jpg", "_objetoc.jpg"), img)

    cv2.waitKey(0)

cv2.destroyAllWindows()