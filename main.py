import glob
import pathlib
import cv2

# Use this for pyinstaller version, place the folder onto the Desktop
# icon_file = glob.glob("./Desktop/notelove-portrait-editor/icons/*.png")
# input_images = glob.glob("./Desktop/notelove-portrait-editor/input/*.jpeg") + glob.glob("./Desktop/notelove-portrait-editor/input/*.jpg")

# testing paths
icon_file = glob.glob("./icons/*.png")
input_images = glob.glob("./input/*.jpeg") + glob.glob("./input/*.jpg")

icons = ["SKIP INSTRUMENT"]
for current_file in icon_file:
    p = pathlib.Path(current_file)
    icons.append(p.stem)

for current_file in input_images:
    print("Processing:", current_file)
    print("\n")
    print("Instrument Icons")
    for idx, x in enumerate(icons):
        print(idx, x)

    index_plus_one = int(input("Select First Instrument Icon to Add(Just type the number and press enter): "))
    if index_plus_one != 0:

        portrait = cv2.imread(current_file, cv2.IMREAD_COLOR)
        icon = cv2.imread(icon_file[index_plus_one-1], cv2.IMREAD_COLOR)

        height, width, _ = portrait.shape
        icon_resize = cv2.resize(icon, (int(height*0.2), int(height*0.2)), interpolation = cv2.INTER_CUBIC)
        icon_height, icon_width, _ = icon_resize.shape

        
        x_offset=int(width - icon_width - (width/20))
        y_offset=int(height - icon_height - (height/20))

        portrait[y_offset:y_offset+icon_resize.shape[0], x_offset:x_offset+icon_resize.shape[1]] = icon_resize

    print("\n")
    print("Instrument Icons")
    for idx, x in enumerate(icons):
        print(idx, x)

    index_plus_one = int(input("Select Second Instrument Icon to Add(Just type the number and press enter): "))
    if index_plus_one != 0:
        icon = cv2.imread(icon_file[index_plus_one-1], cv2.IMREAD_COLOR)
        icon_resize_2 = cv2.resize(icon, (int(height*0.2), int(height*0.2)), interpolation = cv2.INTER_CUBIC)

        height, width, _ = portrait.shape
        icon_height, icon_width, _ = icon_resize_2.shape
        x_offset= int(x_offset - (icon_width*1))
        y_offset=y_offset 


        portrait[y_offset:y_offset+icon_resize_2.shape[0], x_offset:x_offset+icon_resize_2.shape[1]] = icon_resize_2
    p = pathlib.Path(current_file)

    # Use this for pyinstaller version, place the folder onto the Desktop
    #cv2.imwrite("./Desktop/notelove-portrait-editor/output/"+p.name, portrait)
    
    # testing path
    cv2.imwrite("./output/"+p.name, portrait)
