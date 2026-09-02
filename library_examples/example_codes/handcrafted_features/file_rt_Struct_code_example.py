import pysera

result = pysera.process_batch(
    image_input=r"Final_Clone\PySERA\library_examples\Data\RT-STRUCT\CT",
    mask_input=r"Final_Clone\PySERA\library_examples\Data\RT-STRUCT\RT Struct\1.dcm",
    output_path=r"C:\Users\AsemaN\Desktop\PySERA_Videos\results",
    categories="gldzm, ngldm", 
    dimensions="3d, 2_5d",  
) 

print(result)