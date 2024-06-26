# Author: Muhammed Elyamani
# Date: 03/02/2023
# GitHub: https://github.com/WikiGenius

from utils.draw_boxes import draw_count_people, draw_analyse_faces
from utils.preprocess import preprocess, resize 
from utils.render import create_rounded_img
from utils.style_app import StyleApp
from utils.preprocess_face import preprocess_face
from utils.age_gender import predict_age_gender
from utils.process_image import Process
import random
random.seed(0)


