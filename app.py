import rawpy
import imageio
import glob, os

path = os.getcwd()
os.chdir(path)
for file in glob.glob("*.CR2"):
    print(file)
    pathPhoto = path+'/'+file
    raw = rawpy.imread(pathPhoto)
    rgb = raw.postprocess(use_auto_wb=True)
    imageio.imsave(file+'.png', rgb)
