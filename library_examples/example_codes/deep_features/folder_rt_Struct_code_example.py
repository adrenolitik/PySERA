import pysera

result = pysera.process_batch(
    image_input=".\Examples\Data\RT-STRUCT\image",
    mask_input=".\Examples\Data\RT-STRUCT\mask",
    output_path="./results",
    roi_num=5,
    extraction_mode="deep_feature",
    deep_learning_model="resnet50",     # Backbone for feature extraction - choices: 'resnet50', 'vgg16', 'densenet121'
    aggregation_lesion=True,        # performs lesion-level feature aggregation - Default: False
)
print(f"success: {result['success']}")
print(f"processing_time: {result['processing_time']}")