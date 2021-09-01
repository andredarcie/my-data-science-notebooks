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
        print("pessoa: " + str(e) + ' - ' + str(t))

    if len(objetoADetectados) > 0:
        cv2.imwrite(imagem.replace(".jpg", "_objetoa.jpg"), img)

    cv2.waitKey(0)