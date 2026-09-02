import pysera

result = pysera.process_batch(
    image_input="image_path",
    mask_input="mask_path",

    output_path="./results",          #### result path

    min_roi_volume=10,       
    roi_selection_mode="per_region",  #### roi selection mode (per_region / per_img)

    roi_num=1,                        #### number of roi must be selected to process
    
    extraction_mode="deep_feature",
    deep_learning_model="densenet121",

    apply_preprocessing=True,
)

print(result)