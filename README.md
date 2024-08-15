# Synthetic Data Generator

This repository contains a Python script that generates synthetic data based on the structure and content of an existing Excel file. The generated data respects the relationships between columns, such as dates and boolean flags, to create realistic synthetic datasets.

## Overview

This project is designed to assist with the generation of synthetic data, which is especially useful for testing, development, and machine learning model training when real data is unavailable or sensitive. 
The script automatically detects column headers from a provided Excel file and generates synthetic data accordingly.

## Features

- **Automatic Header Detection**: Automatically reads and uses headers from the provided Excel file.
- **Date Relationship Handling**: Ensures logical relationships between date fields (e.g., `reg_date`, `status_date`, `audit_date`).
- **Boolean Flag Handling**: Properly handles boolean fields, ensuring they are represented as `True` or `False`.
- **Customizable Data Generation**: Allows for easy modification and extension to handle different data types and relationships.

## Getting Started

### Prerequisites

- Python 3.x
- `pandas` library
- `numpy` library

Install the required packages using pip:

```bash
pip install pandas numpy
```

### Usage

1. Place your source Excel file (`Raw.xlsx`) in the same directory as the script.
2. Run the script to generate synthetic data:

```bash
python PopulatingData.py
```

3. The generated synthetic data will be saved as `Synthetic_Data_10000.xlsx` in the same directory.


## Development

This project is currently under development. The current version generates synthetic data based on an input Excel file and handles several common data types and relationships. 
Future updates may include more advanced data handling and additional customization options.

## Contributing

Contributions are welcome! Please feel free to submit issues, feature requests, or pull requests.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---
