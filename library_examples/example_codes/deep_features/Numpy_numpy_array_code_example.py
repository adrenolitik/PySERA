import numpy as np
import nibabel as nib
import pysera

# Load image and mask as NumPy arrays (for example, using nibabel)
image_array = nib.load(r"image_path").get_fdata()
mask_array = nib.load(r"mask_path").get_fdata()

result = pysera.process_batch(
    image_input=image_array,
    mask_input=mask_array,
    output_path=r".\results",
    num_workers="6",
    apply_preprocessing=False,
    enable_parallelism=True,
    min_roi_volume=5,       # Discards RoIs with number of voxels below this threshold
    roi_selection_mode="per_img",
    roi_num=12,         # Number of ROIs to process
    extraction_mode="deep_feature",
    deep_learning_model="vgg16",
    report="all",
)

print(result)