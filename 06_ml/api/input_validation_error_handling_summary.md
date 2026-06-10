# Input Validation and Error Handling Summary

## Task Overview

This task improved the FastAPI machine learning API by adding strict input validation, output validation, error handling, and logging. The API was already able to receive input data and return predictions from the trained model. In this task, the API was improved so it can reject invalid requests, return clear error messages, and save logs for successful predictions and handled errors.

## Files Updated

* `06_ml/api/serve_model.py`
* `06_ml/api/api_logs.txt`
* `06_ml/api/input_validation_error_handling_summary.md`

## What Was Implemented

* Added a Pydantic input model called `PredictionInput`.
* Added strict input validation using `extra = "forbid"`.
* Created a Pydantic output model called `PredictionOutput`.
* Connected the output model to the `/predict` endpoint using `response_model=PredictionOutput`.
* Added a validation error handler using `RequestValidationError`.
* Added a general exception handler for unexpected errors.
* Added logging using Python’s built-in `logging` library.
* Configured the API to write logs into `api_logs.txt`.

## Tests Performed

The API was tested using the FastAPI Swagger documentation page:

`http://127.0.0.1:8000/docs`

The following test cases were performed:

1. Correct input

   * The API returned a successful prediction with status code `200`.

2. Missing field

   * One required field was removed from the request.
   * The API returned a validation error with status code `422`.

3. Extra wrong field

   * An extra field called `wrong_field` was added to the request.
   * The API rejected the request because extra inputs are not permitted.

4. Wrong data type

   * A text value was sent instead of a number.
   * The API returned a validation error explaining that the input should be a valid number.

## Results

The API successfully handled both valid and invalid requests. Valid input returned a prediction successfully, while invalid input was rejected before reaching the model. The `api_logs.txt` file recorded the successful prediction and the handled validation errors.

## Lessons Learned

In this task, I learned how Pydantic is used with FastAPI to validate incoming JSON requests. I learned how to define clear input and output schemas, reject extra fields, and handle missing or incorrect data types. I also learned how exception handlers improve the API by returning cleaner error messages. Finally, I learned how logging helps developers track successful predictions and errors for debugging and monitoring.
