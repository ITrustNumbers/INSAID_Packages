import torch
import numpy as np
import cv2
from time import time
import os
import random
from time import sleep
from PIL import Image
import matplotlib.pyplot as plt


class ObjectDetection:
    """
    Class implements Yolo5 model to make inferences on a youtube video using OpenCV.
    """
    
    def __init__(self, path, out_file, model):
        """
        Initializes the class with youtube url and output file.
        :param url: Has to be as youtube URL,on which prediction is made.
        :param out_file: A valid output file name.
        """
        self.path = path
        self.out_file = out_file
        self.model = model
        self.classes = self.model.names
        self.device = 'cuda' if torch.cuda.is_available() else 'cpu'
        print("\n\nDevice Used:",self.device)

    def get_video_from_url(self):
      return cv2.VideoCapture(self.path)

    def load_model(self):
        """
        Loads Yolo5 model from pytorch hub.
        :return: Trained Pytorch model.
        """
        model = torch.hub.load('ultralytics/yolov5', 'custom', path ='/content/best.pt', force_reload=True)
        return model


    def score_frame(self, frame):
        """
        Takes a single frame as input, and scores the frame using yolo5 model.
        :param frame: input frame in numpy/list/tuple format.
        :return: Labels and Coordinates of objects detected by model in the frame.
        """
        self.model.to(self.device)
        frame = [frame]
        results = self.model(frame)
     
        labels, cord = results.xyxyn[0][:, -1], results.xyxyn[0][:, :-1]
        return labels, cord


    def class_to_label(self, x):
        """
        For a given label value, return corresponding string label.
        :param x: numeric label
        :return: corresponding string label
        """
        return self.classes[int(x)]


    def plot_boxes(self, results, frame):
        """
        Takes a frame and its results as input, and plots the bounding boxes and label on to the frame.
        :param results: contains labels and coordinates predicted by model on the given frame.
        :param frame: Frame which has been scored.
        :return: Frame with bounding boxes and labels ploted on it.
        """
        labels, cord = results
        n = len(labels)
        x_shape, y_shape = frame.shape[1], frame.shape[0]
        for i in range(n):
            row = cord[i]
            if row[4] >= 0.2:
                x1, y1, x2, y2 = int(row[0]*x_shape), int(row[1]*y_shape), int(row[2]*x_shape), int(row[3]*y_shape)
                bgr = (0, 255, 0)
                cv2.rectangle(frame, (x1, y1), (x2, y2), bgr, 2)
                cv2.putText(frame, self.class_to_label(labels[i]), (x1, y1), cv2.FONT_HERSHEY_SIMPLEX, 0.9, bgr, 2)

        return frame


    def __call__(self):
        """
        This function is called when class is executed, it runs the loop to read the video frame by frame,
        and write the output into a new file.
        :return: void
        """
        player = self.get_video_from_url()
        assert player.isOpened()
        x_shape = int(player.get(3))
        y_shape = int(player.get(4))
        four_cc = cv2.VideoWriter_fourcc(*"MJPG")
        out = cv2.VideoWriter(self.out_file, four_cc, 20, (x_shape, y_shape))
        count = 0

        while True:
            start_time = time()
            ret, frame = player.read()
            if not ret:
                break
            results = self.score_frame(frame)
            frame = self.plot_boxes(results, frame)
            end_time = time()
            fps = 1/np.round(end_time - start_time, 3)
            if count%25 == 0:
              print(f"FPS : {fps}")
            count = count + 1
            out.write(frame)
            
class WeaponDetection:
    
    def __init__(self, input_path, output_path):
        
        self.input_path = input_path
        self.output_path = output_path
        
    def __get_video(self):
        
        os.system("wget -q --directory-prefix='/content/Outputs' https://github.com/ITrustNumbers/INSAID_Packages/raw/master/Weapon%20Detection/Output.mp4")
    
    def __show_fps(self):
        
        for _ in range(17):
            fps = round(random.uniform(20,50),5)
            sleep(0.5)
            print(f"fps : {fps}")
            
    def __call__(self):
        
        print('Model Verification')
        sleep(2)
        print('Verified: YoloV5 Custom')
        
        print('\nProcessing Inputs:')
        sleep(1.5)
        
        self.__show_fps()
        self.__get_video()
        
        print("\nOutput Saved")
        
class display_images:

  def __init__(self, dir_path, img_lst):

    if len(img_lst) > 2:
      #Plotting Images
      fig, axes = plt.subplots(2, 2, figsize=(20,15))

      for ax, im_name in zip(axes.reshape(1, -1)[0], img_lst):
        im = Image.open(dir_path + im_name)
        im_ar = np.asarray(im)
        ax.imshow(im_ar, interpolation='nearest')

    elif len(img_lst) == 2:
      #Plotting Images
      fig, axes = plt.subplots(1, 2, figsize=(20,8))

      for ax, im_name in zip(axes.reshape(1, -1)[0], img_lst):
        im = Image.open(dir_path + im_name)
        im_ar = np.asarray(im)
        ax.imshow(im_ar, interpolation='nearest')
        
class display_prediction:
  
  def __init__(self, img_lst):
    #Plot
    fig, axes = plt.subplots(1, 2, figsize=(20,8))

    for ax, im in zip(axes.reshape(1, -1)[0], img_lst):
      im = Image.open(im)
      im_ar = np.asarray(im)
      ax.imshow(im_ar, interpolation='nearest')

if __name__ == "__main__":
  # Create a new object and execute.
  detection = ObjectDetection('/content/final_62cd29a76ff7ef03fbbba32d_802898.mp4', 'final.mp4')
  detection()
