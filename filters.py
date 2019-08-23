from PIL import Image

# Define your load_img() function here.
#       Parameters: The name of the file to be opened (string)
#       Returns: The image object with the opened file.
def load_img(file):
    im = Image.open(file)
    return im
    #C:\Users\GWC2019\Desktop\TestFolder
    #"Capture.jpg"

# Define your show_img() function here.
#       Parameters: The image object to display.
#       Returns: nothing.
def show_img(im):
    im.show()

# Define your save_img() function here.
#       Parameters: The image object to save, the name to save the file as (string)
#       Returns: nothing.
def save_img(im, file):
    im.save(file,)
    show_img(im)

# Define your obamicon() function here.
#       Parameters: The image object to apply the filter to.
#       Returns: A New Image object with the filter applied.

#def obamicon():
#    .

def main():
    pic = input("Tell me your image name (with a .filetype behind it) ")
    load_img(pic)
    show_img(im)
    save_img()


if __name__ == "__main__":
    main()
