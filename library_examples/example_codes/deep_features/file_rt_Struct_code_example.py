import pysera

result = pysera.process_batch(
    image_input=r"Final_Clone\PySERA\library_examples\Data\RT-STRUCT\CT",
    mask_input=r"Final_Clone\PySERA\library_examples\Data\RT-STRUCT\RT Struct",
    output_path=r"C:\Users\AsemaN\Desktop\PySERA_Videos\results",
    roi_num=5,
    extraction_mode="deep_feature",
    deep_learning_model="resnet50",

    aggregation_lesion=True,           #### To aggregation of some features
)
print(result) 