import pysera

result = pysera.process_batch(
    image_input="image_path",
    mask_input="mask_path",
    output_path="./results",
    roi_selection_mode="per_region",
    extraction_mode="deep_feature",
)


print(f"Success: {result['success']}")
print(f"Output path: {result['output_path']}")