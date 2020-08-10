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

overwrite ('D:/massive_agents/agents_improvements/assets/01-R2R_Agent_MD_and_Zbrush_files/new_female/new_color_maps/**/*.tif')
