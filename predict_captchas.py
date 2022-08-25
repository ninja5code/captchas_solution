import pickle
import cv2
import os
import numpy as np

class Captcha(object):
    def __init__(self):

        # to load the model
        self.model = ''
        with open("./model.pkl", "rb") as f:
            self.model = pickle.load(f)

        # to define the class variable
        self.xys = [[5,11], [14,11], [23,11], [32,11], [41,11]]
        self.width = 8
        self.height = 10            

    def __call__(self, im_path, save_path):
        """
        Algo for inference
        args:
            im_path: .jpg image path to load and to infer
            save_path: output file path to save the one-line outcome
        """

        # to load the image
        img = cv2.imread(im_path)

        # to make a prediction
        pred = self.inference(img)
        print("predicted text: ", pred)

        # to save the result into a file
        with open(save_path, "w") as f:
            f.write(pred)

    def inference(self, img):
        """
        Inference function
        args:
            img: input to the model
        """

        # to convert a BGR image into grayscale
        img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        # to segment the image and predict each letter
        ii = 0
        pred = ''
        text = ''
        for xy in self.xys:
            ii += 1
            ltt = img[xy[1]:xy[1]+self.height, xy[0]:xy[0]+self.width]
    
            # to threshold an image
            #print(ltt)
            ret, ltt = cv2.threshold(ltt, 127,255,cv2.THRESH_BINARY)
            ltt = cv2.bitwise_not(ltt)
            #print(ltt)
    
            # to reshape the letter into a row vector
            tmp = np.reshape(ltt, (1,80))
            #print(tmp.shape)
    
            # to predict the letter
            for key, value in self.model.items():
                arr = tmp - value
                sum1 = np.sum(arr)
                if sum1 == 0:
                    text = key
                    break
    
            # to concate all letters into a text
            pred = pred + text
        
        return pred

if __name__ == "__main__":
    
    # to set the local variable
    im_path = "/home/ccng/workspace/sampleCaptchas/input/input19.jpg"
    save_path = "./result.txt"

    # to create an instance of Captchas class
    obj = Captcha()

    # to call the model inference
    obj(im_path, save_path)

    


