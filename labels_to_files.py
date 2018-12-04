import numpy as np
import pandas as pd
import re
from PIL import Image
import os, sys


#import all test images
image_folder = "openlabeling/images"
image_files = [f for f in os.listdir(image_folder) if os.path.isfile(os.path.join(image_folder, f))]

#create dataframe
df = pd.DataFrame(columns = ['dead','y','x','height','width','image']) 

#import all test images
txt_folder = "openlabeling/bbox_txt"
txt_files = [f for f in os.listdir(txt_folder) if os.path.isfile(os.path.join(txt_folder, f))]

print("Working with {0} images".format(len(image_files)))

#read multiple txt file into df
frames = []
for i in range(len(txt_files)):
    #read single txt files into df
    file_data = pd.read_csv(txt_folder + "/" + txt_files[i], sep = ' ', header = None, names = ['dead','y','x','height','width','image'])

    #append dataframe with current file name
    img_file = re.sub('.txt$','.jpg',txt_files[i])
    file_data['image']="openlabeling/images/"+img_file
    frames.append(file_data)

# concatenate list of all frames into one    
result = pd.concat(frames, ignore_index=True)
print(type(result), " ", result.shape)

#convert corner points back to pixel values
cols= ['x','y','width','height']
result[cols] *=1500
result[cols]=result[cols].astype(int)

yeast_list = []

for i in range(len(result)):
    #bring in single image and convert to np array
    img = Image.open(result.loc[i,'image'])
    a = np.asarray(img)
    #some bounding boxes are too close to edge to be 80x80
    #select area with yeast cell
    b = a[int(result.loc[i,'x']-40):int(result.loc[i,'x']+40),
          int(result.loc[i,'y']-40):int(result.loc[i,'y']+40),
          0]
    
    #outpust to show it's still working
    yeast_list.append(b)
    if (i%20==0):
        print("working on ",i," of ",len(result))
        
#convet np arrays to images for each cell
for i in range(len(result)):
    try :
        cell_status = ""
        if result.loc[i,'dead']==0:
            cell_status = "alive"
        else :
            cell_status = "dead"
        test_cell = Image.fromarray(yeast_list[i])
        test_cell.save("yeast_cell_data/yeast_cells/"+cell_status+"/"+cell_status+str(i)+".jpg")
    except :
        print("deleted ",i," too close to image edge")