import numpy as np
import nrrd
import pysera

# Load NRRD files using pynrrd
image_array, image_header = nrrd.read(r"image_path").astype(np.float32)
mask_array, mask_header = nrrd.read(r"mask_path")

#  as NumPy arrays
image_array = image_array.astype(np.float32)
mask_array = mask_array.astype(np.float32)

result = pysera.process_batch(
    image_input=image_array,
    mask_input=mask_array,
    output_path=r".\results",
    num_workers="4",
    enable_parallelism=False,
    categories="diag, morph",
    bin_size=25,        # Determines number of intensity levels
    roi_num=1,
    roi_selection_mode="per_region",
    min_roi_volume=10,
    apply_preprocessing=False,
    feature_value_mode="APPROXIMATE_VALUE",
    aggregation_lesion=True,  
    IBSI_based_parameters={
        "radiomics_DataType": "MRI",
        "radiomics_DiscType": "FBN",
        "radiomics_isScale": 1
    },      # Advanced config parameters for IBSI
    report="all"        # Level of logging - Default: 'all'
)

print(result)