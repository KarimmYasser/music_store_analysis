# Music Store Analysis

This project analyzes sales and customer data for a small online music store using Python and pandas. The goal is to generate key business insights to inform marketing and product decisions.

## Project Structure

- `music_store_report.py`: Main analysis script. Loads, cleans, and analyzes the data, then prints business metrics.
- `explaination.ipynb`: Step-by-step notebook with code, explanations, and results for each analysis task.
- `music store data/`: Contains CSV files for customers, invoices, invoice lines, genres, tracks, and other related data.
- `.gitignore`: Excludes data files, virtual environments, and other non-source artifacts from version control.

## Analysis Workflow

1. **Data Ingestion**: Load CSV files into pandas DataFrames.
2. **Data Cleaning**: Standardize column names to snake_case and fix ID fields for consistency.
3. **Data Integration**: Merge tables to create a unified view, resolving column name conflicts.
4. **Business Insights**:
   - Country with the most customers
   - Top-spending customer
   - Revenue by music genre
   - Average transaction value per customer
   - Total revenue per year

## How to Run

1. Install Python 3.8+ and `pandas`.
2. Place all CSV files in the `music store data/` directory.
3. Run the analysis script:
   ```bash
   python music_store_report.py
   ```
4. Or open `explaination.ipynb` in Jupyter/VS Code for an interactive walkthrough.

## Requirements

- Python 3.8+
- pandas

## License

This project is for educational and internal business use only.
