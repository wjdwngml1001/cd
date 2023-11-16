# Create your models here.
from django.conf import settings
from django.db import models
from django.utils import timezone

class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()
    def __str__(self):
        return self.title
    
#
#import cv2
#import numpy as np
#from tensorflow.keras.applications.vgg16 import VGG16, preprocess_input, decode_predictions
#from tensorflow.keras.preprocessing import image
#from tensorflow.keras.models import load_model

# 얼굴 감지를 위한 Haar Cascade 분류기 로드
#face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# VGG16 모델 로드
#vgg_model = VGG16(weights='imagenet')

# 나이 및 감정 모델 로드
#age_model = load_model('path/to/age_model.h5')  # 예시 경로, 실제 경로로 변경해야 함
#emotion_model = load_model('path/to/emotion_model.h5')  # 예시 경로, 실제 경로로 변경해야 함

# 감정 클래스
#emotion_labels = ['Angry', 'Disgust', 'Fear', 'Happy', 'Sad', 'Surprise', 'Neutral']

# OpenCV 비디오 캡처 초기화
#cap = cv2.VideoCapture(0)

#while True:
    # 프레임 읽기
 #   ret, frame = cap.read()

    # 그레이스케일로 변환
#    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # 얼굴 감지
 #   faces = face_cascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5)

  #  for (x, y, w, h) in faces:
        # 얼굴 영역 추출
   #     face_roi = frame[y:y+h, x:x+w]

        # VGG16 입력에 맞게 전처리
    #    img = cv2.resize(face_roi, (224, 224))
    #   img = image.img_to_array(img)
     #   img = np.expand_dims(img, axis=0)
      #  img = preprocess_input(img)

        # VGG16 모델로 객체 예측
       # predictions = vgg_model.predict(img)
      #  vgg_label = decode_predictions(predictions)[0][0][1]

        # 이미지를 나이 모델에 맞게 전처리
      #  img = cv2.resize(face_roi, (48, 48))
      #  img = image.img_to_array(img)
      #  img = np.expand_dims(img, axis=0)
      #  img = preprocess_input(img)

        # 나이 모델로 예측
      #  age = age_model.predict(img)[0][0]

        # 이미지를 감정 모델에 맞게 전처리
      #  img = cv2.resize(face_roi, (48, 48))
      #  img = image.img_to_array(img)
      #  img = np.expand_dims(img, axis=0)
      #  img = preprocess_input(img)

        # 감정 모델로 예측
      #  emotion_probabilities = emotion_model.predict(img)[0]
      #  emotion_label = emotion_labels[np.argmax(emotion_probabilities)]

        # 결과 표시
      #  cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
      #  cv2.putText(frame, f'VGG: {vgg_label}, Age: {int(age)}, Emotion: {emotion_label}',
      #              (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 2)

    # 결과를 화면에 표시
 #   cv2.imshow('Face Detection', frame)

    # 'q' 키를 누르면 종료
 #   if cv2.waitKey(1) & 0xFF == ord('q'):
 #       break

# 비디오 캡처 종료
#cap.release()
#cv2.destroyAllWindows()
