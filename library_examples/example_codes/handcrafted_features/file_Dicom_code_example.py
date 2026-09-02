import pysera

result = pysera.process_batch(
    image_input="image_path",
    mask_input="mask_path",

    output_path="./results",

    feature_value_mode="APPROXIMATE_VALUE",
    categories="diag, morph",
    aggregation_lesion=True,
    # extraction_mode="handcrafted_feature",

    temporary_files_path="./tmp",                  ###### for rt-struct cases to save lesion files in Disk not in Ram
)

print(f"processing_time: {result['processing_time']}")