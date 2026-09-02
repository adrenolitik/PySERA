import pysera

result = pysera.process_batch(
    image_input="./Examples/Data/NRRD_img",
    mask_input="./Examples/Data/NRRD_mask",
    output_path="./results",
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