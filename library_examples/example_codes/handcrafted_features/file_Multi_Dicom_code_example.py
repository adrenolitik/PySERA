import pysera

result = pysera.process_batch(
    image_input="image_path",
    mask_input="mask_path",
    categories="all",
    dimensions="2_5d",
    roi_selection_mode="per_region",
    min_roi_volume=50,   
)

print(result)