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
    num_workers="4",
    enable_parallelism=True,
    categories="glcm, glrlm, glszm",
    dimensions="3d",
    bin_size=25,
    roi_num=1,
    roi_selection_mode="per_region",
    min_roi_volume=10,
    apply_preprocessing=True,
    feature_value_mode="REAL_VALUE",
    IBSI_based_parameters={
        "radiomics_DataType": "CT",
        "radiomics_DiscType": "FBN",
        "radiomics_isScale": 1
    },
    report="info"
)

print(result)    