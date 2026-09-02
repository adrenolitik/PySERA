import pysera

result = pysera.process_batch(
    image_input="image_path",
    mask_input="mask_path",

    output_path="./results",

    categories="glszm, glrlm",                #### diag, morph, glcm, glrlm, glszm, ngtdm, ngldm 
    dimensions="2d",                          #### 1st, 2D, 2.5D, 3D

    bin_size=25,
    roi_num=1,
    roi_selection_mode="per_region",
    min_roi_volume=5,
    apply_preprocessing=True,

    feature_value_mode="APPROXIMATE_VALUE",    #### approximate value for some uncalculable features
    report="info"
)

print(result)