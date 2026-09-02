import pysera

result = pysera.process_batch(
    image_input="image_path",
    mask_input="mask_path",
    output_path="./output_results",
    extraction_mode="deep_feature",
)

print(f"--- processing_time ---: {result['processing_time']}")
print(f"--- logs ---: {result['logs']}")