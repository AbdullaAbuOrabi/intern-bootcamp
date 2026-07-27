# Logging and Monitoring Summary

## Overview

This task improved the e-commerce ETL pipeline by adding structured logging, runtime measurement, performance profiling, optimization, and error notification.

The pipeline now records important information about each execution and makes it easier to identify slow stages or failures.

## Structured Logging

A reusable logger was created in `logger_config.py`.

The logger includes:

- Timestamps
- Log levels such as INFO, WARNING, and ERROR
- Logger name
- Pipeline task details
- Console output
- File-based logging
- Log rotation

The main pipeline writes logs to:

`logs/pipeline.log`

The scheduler writes logs to:

`logs/pipeline_run.log`

## Performance Monitoring

Python's `time.perf_counter()` was used to measure the runtime of:

- Extract
- Transform
- Load
- Complete pipeline

A baseline performance test produced these results:

| Stage | Duration |
|---|---:|
| Extract | 0.0516 seconds |
| Transform | 0.0804 seconds |
| Load | 0.2106 seconds |
| Total | 0.3426 seconds |

The load stage was the slowest because it writes multiple Parquet files to disk.

## Profiling

Python's `cProfile` was used to inspect the pipeline runtime.

The profiled execution showed that part of the total runtime came from loading Python libraries and importing modules. The actual ETL execution was much faster than the full profiler runtime.

## Transformation Optimization

The original transformation always copied every DataFrame and removed duplicates.

The optimized version avoids unnecessary copies and only removes duplicates when duplicate rows exist.

The original and optimized transformations were tested five times.

| Version | Average Transform Time |
|---|---:|
| Before optimization | 0.011049 seconds |
| After optimization | 0.005739 seconds |

The optimized transformation was approximately 48.06% faster.

The comparison results were saved in:

`performance_results.csv`

The visual comparison was saved as:

`performance_comparison.png`

## Error Handling and Notification

The pipeline uses a try-except block to handle failures safely.

When an error occurs, the pipeline:

- Records the error in the log
- Includes the full traceback
- Shows a console alert
- Stops execution instead of continuing with incomplete data

The scheduler also retries failed pipeline runs before reporting final failure.

## Conclusion

The ETL pipeline is now easier to monitor, troubleshoot, and optimize. Structured logs provide clear execution details, performance measurements identify slow stages, and the optimized transformation reduces processing time. Error handling and notification also make the pipeline safer and more reliable.