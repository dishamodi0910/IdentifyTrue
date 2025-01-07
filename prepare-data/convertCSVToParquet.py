import dask.dataframe as dd

def convert_large_csv_to_single_parquet_dask(csv_file_path, parquet_output_path):
    df = dd.read_csv(
        csv_file_path,
        dtype="object",  
        assume_missing=True,  
        blocksize=25e6  
    )
    
    df = df.repartition(npartitions=10)  
    
    df.to_parquet(parquet_output_path, engine="pyarrow", compression="snappy", write_metadata_file=False)
    print(f"Data successfully converted and saved to {parquet_output_path}")

convert_large_csv_to_single_parquet_dask(
    "/home/dishamodi0910/DEV/true-identify/keystroke_dataset/keystroke_data.csv",
    "/home/dishamodi0910/DEV/true-identify/keystroke_dataset/keystroke_data.parquet"
)
