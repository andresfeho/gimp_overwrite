import gimpfu
import glob

def overwrite (folder):
    for fname in glob.glob(folder):
        img = pdb.gimp_file_load(fname, fname)
        display = gimp.Display(img)
        filename = pdb.gimp_image_get_filename(img)
        layer = pdb.gimp_image_merge_visible_layers(img, (0))
        pdb.file_tiff_save(img, pdb.gimp_image_get_active_drawable( img ), filename, filename, (1))
        pdb.gimp_display_delete(display)

overwrite ('C:/path/to/file/**/*.tif')
