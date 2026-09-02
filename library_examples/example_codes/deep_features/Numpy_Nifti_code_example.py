import numpy as np
import nibabel as nib
import pysera

# Load image and mask as NumPy arrays 
image_array = nib.load(r"image_path").get_fdata()
mask_array = nib.load(r"mask_path").get_fdata()

result = pysera.process_batch(
    image_input=image_array,
    mask_input=mask_array,
    output_path=r".\results",
    num_workers="4",        # Number of CPU cores engaged with the process
    enable_parallelism=True,    # Enables parallel processing - Default: True
    min_roi_volume=10,
    roi_selection_mode="per_region",
    roi_num=1,
    extraction_mode="deep_feature",
    deep_learning_model="densenet121",
    apply_preprocessing=True,
)

print(result)