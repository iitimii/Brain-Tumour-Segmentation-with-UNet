from fastapi import FastAPI, File, UploadFile
from fastapi.responses import FileResponse
from typing import List
import os
import shutil
import nibabel as nib
import numpy as np
from inference import predict_vol, model  # Import your predict_vol and model function from the inference module

app = FastAPI()

# Function to perform inference using your model
def perform_inference(flair_file, t1ce_file):
    # Create temporary directories if they don't exist
    if not os.path.exists("temp"):
        os.makedirs("temp")

    flair_input_path = "temp/flair.nii"
    t1ce_input_path = "temp/t1ce.nii"

    # Save the uploaded Nifti files to temporary directories
    with open(flair_input_path, "wb") as flair_file_object:
        shutil.copyfileobj(flair_file.file, flair_file_object)

    with open(t1ce_input_path, "wb") as t1ce_file_object:
        shutil.copyfileobj(t1ce_file.file, t1ce_file_object)

    # Load the Nifti files and perform inference
    flair = nib.load(flair_input_path).get_fdata()
    t1ce = nib.load(t1ce_input_path).get_fdata()
    result = predict_vol(flair, t1ce, model)  # Assuming model is defined somewhere

    # Convert the NumPy array result to a Nifti file
    result_image = nib.Nifti1Image(result, affine=np.eye(4))

    # Save the result Nifti file
    result_file_path = "temp/result.nii"
    nib.save(result_image, result_file_path)

    return result_file_path  # Return the path to the result Nifti file

@app.post("/upload/")
async def upload_files(flair: UploadFile, t1ce: UploadFile):
    result_file_path = perform_inference(flair, t1ce)

    # Return the result file with appropriate headers for download
    return FileResponse(
        result_file_path,
        headers={
            "Content-Disposition": f"attachment; filename=result.nii"
        },
        media_type='application/octet-stream'
    )

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=8000)
