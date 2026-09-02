import pysera

result = pysera.process_batch(
    image_input="./Examples/Data/CT",       # Path to image folder
    mask_input="./Examples/Data/CT-Mask",       # Path to mask folder
    output_path="./results",
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