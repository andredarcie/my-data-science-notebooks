import dlib

# Gerar os arquivos XML
# https://imglab.in/

opcoes = dlib.simple_object_detector_training_options()
opcoes.add_left_right_image_flips = True
opcoes.C = 5

# Treinamento
dlib.train_simple_object_detector("res/treinamentoimagens.xml", "res/detectorimagens.svm", opcoes)
