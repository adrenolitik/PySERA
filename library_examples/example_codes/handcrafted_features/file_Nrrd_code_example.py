import pysera

result = pysera.process_batch(
    image_input="image_path",
    mask_input="mask_path",

    output_path="./results",

    dimensions="2d,3d",
    
    bin_size=25,
    roi_num=1,
    roi_selection_mode="per_region",
    min_roi_volume=10,
    feature_value_mode="REAL_VALUE",
    IBSI_based_parameters={
        "radiomics_DataType": "MRI",
        "radiomics_DiscType": "FBN",
        "radiomics_isScale": 1
    },
    report="all"
)

print(result)