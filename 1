# libraries
import pickle
import glob
import cv2
import os
import numpy as np
from matplotlib import pyplot as plt

# global variables
xys = [[5,11], [14,11], [23,11], [32,11], [41,11]]
width = 8
height = 10
acc = 0
model = {}
data_path = "/home/ccng/workspace/sampleCaptchas"

# to create a visualization folder
if not os.path.exists("images"):
    os.mkdir("images")

# to scan all images in a folder
for filename in sorted(glob.glob("%s/input/*.jpg"%(data_path))):
    basename = os.path.basename(filename)
    filenum = basename[5:basename.find(".")]
    gt_filename = "%s/output/output%s.txt" % (data_path, filenum)
    f = open(gt_filename, "r")
    ground_truth = f.read().strip()
    print("input filename:", basename, ", ground_truth:", ground_truth)

    # to read the original image from input folder
    img = cv2.imread(filename)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # to get each letter in an image and plot it
    fig, axs = plt.subplots(1,6)
    fig.suptitle(filename)
    axs[0].imshow(img)

    ii = 0
    pred = ''
    text = ''
    for xy in xys:
        # to extract each letter based on fixed position
        ii += 1
        ltt = img[xy[1]:xy[1]+height, xy[0]:xy[0]+width]

        # to threshold an image
        #print("before: ", ltt)
        ret, ltt = cv2.threshold(ltt, 127,255,cv2.THRESH_BINARY)
        ltt = cv2.bitwise_not(ltt)
        #print("after: ", ltt)

        # to reshape the letter into a row vector
        tmp = np.reshape(ltt, (1,80))
        #print("tmp.shape: ", tmp.shape)

        # to cross check the model dictionary and add new letter
        if ground_truth[ii-1] not in model:
            model['%s'%(ground_truth[ii-1])] = tmp

        # to visualize each letter
        axs[ii].imshow(ltt)
        axs[ii].set_title(text)

    # to save the plt figure for visual checking
    plt.savefig("images/%s.png"%(basename[:-4]))

# to do a final check of model dictionary
print("Supported letter in model: ")
for i in sorted(model.keys()):
    print(i, end=" ")
print("\nTotal letter in model: ", len(model))

# to save the model dictionary into a pickle file
with open("./model.pkl", "wb") as f:
    pickle.dump(model, f)

print("model creation completed!")
