from PIL import ImageFont, ImageDraw, Image  
import numpy as np
import os
import cv2
import random
import pickle
from sys import argv


VISUALIZE = False
def generate_sample(num_samples,save_dir):
    if(os.path.isdir(save_dir)):
        pass
    else:
        os.makedirs(save_dir)
    def textsize(self, text, font=None, *args, **kwargs):
        """Get the size of a given string, in pixels."""
        if self._multiline_check(text):
            return self.multiline_textsize(text, font, *args, **kwargs)

        if font is None:
            font = self.getfont()
        return font.getsize(text)
    blanks = os.listdir(os.path.join("Blanks"))
    bible_original = open(os.path.join("data","kingjamesbible"),"r").read().split("\n")
    def reformat(bible,textlength):
        bible_reformatted = []
        for line in bible:
            split_idx = 0
            while(True):
                next_line = line[split_idx:]
                if(len(next_line)>textlength):
                    bible_reformatted.append(line[split_idx:split_idx+textlength])
                    split_idx = split_idx +textlength
                else:
                    bible_reformatted.append(next_line)
                    break
        return bible_reformatted

    alphabets = "abcdefghijklmnopqrstuvwxyz ,;"
    alphabets = alphabets + alphabets.upper()
    def split(word):
        return [char for char in word]
    alphabets = split(alphabets)

    def get_text_length(font):
        numpy_image = np.zeros((512,800))
        image = Image.fromarray(np.uint8(numpy_image))
        draw = ImageDraw.Draw(image)
        text_num = 0
        while(True):
            test_text = "".join(list(np.random.choice(alphabets,text_num)))
            size = textsize(draw,test_text,font=font)
            text_num +=1
            if(size[0]>400):
                break
        return text_num

    #Label words Plus bounding boxes
    labels = []
    from tqdm import tqdm

    for item in tqdm(os.listdir("fonts")):
        if(item.endswith(".ttf") and "Anothershabby" not in item):
            font = ImageFont.truetype(os.path.join("fonts",item), 25)                
            textlength = get_text_length(font)     
            bible = reformat(bible_original,textlength)
            lines = []
            lines_bound = []        
            for num in range(num_samples):
                #Get a range of text within the bible
                end = random.randint(22,(len(bible)-1))
                begin = end -22                            

                #===========================
                #Create Blank Canvas
                #===========================
                blank_choice = random.choice(blanks)
                bg = 255 - cv2.imread(os.path.join("Blanks",blank_choice))
            
                numpy_image = cv2.resize(bg,(512,800))
                image = Image.fromarray(np.uint8(numpy_image))
                draw = ImageDraw.Draw(image)                    
                #===========================
                #Iterate through the lines
                #===========================
                for idx in range(begin,end):                
                    #Create new image switching 18 lines.
                    #numpy_image = np.zeros((512,512))
                    l = bible[idx]
                    if(l!=""):
                        lines.append(l)
                        size = textsize(draw,l,font=font)
                        lines_bound.append([48,52+size[0],82+(idx%22)*25,83+(idx%22)*25+size[1]])
                    draw.text((50, 80+ (idx%22)*25), l, font=font)
                
                #Save Previous one
                #===========================
                img = 255 - np.array(image)
                img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
                image = Image.fromarray(np.uint8(img))
                if(VISUALIZE):
                    b = lines_bound[1]
                    #print(lines[1])
                    cv2.imshow('seg',img[b[2]:b[3],b[0]:b[1]])
                    for b in lines_bound:
                        img = cv2.rectangle(img,(b[0],b[2]),(b[1],b[3]),(255,0,0),1)
                    cv2.imshow('img',img)            
                    k= cv2.waitKey(0)
                    if(k==ord('q')):
                        cv2.destroyAllWindows()
                        exit()
                else:
                    pass
                labels.append({
                "blank":blank_choice,
                "save_name":str(begin)+item+".png",
                "begin":begin,
                "text":lines,
                "font":item,
                "bounding":lines_bound,
                "text_length":textlength
                })
                image.save(os.path.join(save_dir,str(begin)+item+".png"))  
                lines = []
                lines_bound = []
    import pickle
    if not VISUALIZE:
        filename = "labels.pkl"
        pickle.dump(labels, open(filename, 'wb'))
    return labels

if __name__=="__main__":
    try:
        num_samples = argv[1]
        if(num_samples.isdigit()):
            num_samples = int(num_samples)
        else:
            print("Invalid argument, usage:")
            print("python gen_samples.py --num_samples_per_font")
            exit()
    except Exception:
        print("sample number not specified, using default = 100")
        num_samples = 100
    save_dir = os.path.join("..","samples")
    generate_sample(num_samples,save_dir)