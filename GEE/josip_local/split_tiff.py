
## Razbijanje velikog file-a na manje fileove:
import os, gdal
import os.path as osp
import subprocess
import shutil
 
input_folder = '/home/josip/gee/content/tmp_data'
input_filename = '3.1_VEG_FAPAR_PROBA-V_D.tif'
input_fn = osp.join(input_folder, input_filename)
 
out_folder = '/home/josip/gee/content/tmp_data/3.1_VEG_FAPAR_PROBA-V_D'

gdal_options=["COMPRESS=DEFLATE","PREDICTOR=2","NUM_THREADS=ALL_CPUS","BIGTIFF=YES","TILED=YES","BLOCKXSIZE=512","BLOCKYSIZE=512"]
gdal_config=["GDAL_DISABLE_READDIR_ON_OPEN TRUE","GDAL_CACHEMAX 5000"]
#%%
def run_cmd(cmd):
    #print("COMMAND: {}".format(' '.join(cmd)))
    cp = subprocess.run(cmd, universal_newlines=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    print(cp.stdout)

fsize = osp.getsize(input_fn)
# check if size is too big

ds = gdal.Open(input_fn)
band = ds.GetRasterBand(1)
xsize = band.XSize
ysize = band.YSize

# calculate tile_size_x and tile_size_y
tile_size_x = xsize//2
tile_size_y = ysize//2
 
if osp.exists(out_folder):
        shutil.rmtree(out_folder)
os.mkdir(out_folder)
 
for i in range(0, xsize, tile_size_x):
    for j in range(0, ysize, tile_size_y):
        cmd = ['gdal_translate', input_fn, osp.join(out_folder, str(i) + "_" + str(j) + ".tif")]
        cmd.extend(["-srcwin", "{},{},{},{}".format(i,j,tile_size_x,tile_size_y)])
        for opt in gdal_options:
                cmd.extend(['-co', opt])
        for opt in gdal_config:
                cmd.extend(['--config']+opt.split(" "))
        #com_string = "gdal_translate -of GTIFF -srcwin " + str(i)+ ", " + str(j) + ", " + str(tile_size_x) + ", " + str(tile_size_y) + " " + str(input_fn) + " " + osp.join(out_folder, str(i) + "_" + str(j) + ".tif")
        #os.system(com_string)
        run_cmd(cmd)