import sys
from utils import apply_SCRN, measure_length


def main(path: str) -> None:

    image_root = path # path of the folder containing images
    
    infos = apply_SCRN(image_root) # dictionnary like => {i : {path of segmented image, original size of the image, preprocessed image } }
    
    lengths = {}
    
    for i in infos.keys(): # for each segmented image, we compute the total length of the gun
        lengths[i] = measure_length(infos[i])
        

        
if __name__ == "__main__":
    main(sys.argv[1])