import nibabel as nib
import numpy as np
import pysera

 # Load as NumPy arrays
image_array = nib.load(r"image_path").get_fdata().astype(np.float32)
mask_array = nib.load(r"mask_path").get_fdata().astype(np.float32)



result = pysera.process_batch(
    image_input=image_array,
    mask_input=mask_array,
    output_path=r".\results",
)

print(f"Success: {result['success']}")