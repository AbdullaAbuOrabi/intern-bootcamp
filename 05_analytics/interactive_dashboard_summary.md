# Day 4 — Building an Interactive Dashboard

## Task Overview

The purpose of this task was to build an interactive business analytics dashboard using Streamlit and Plotly.

The dashboard allows users to explore sales performance without changing Python code.

## What I Built

I created a Streamlit dashboard with:

- Category filter
- City filter
- Date-range filter
- KPI cards
- Revenue-over-time line chart
- Revenue-by-category bar chart
- Quantity-versus-total-price scatter plot

The dashboard automatically updates whenever the user changes a filter.

## KPIs Included

The dashboard displays:

- Total revenue
- Total orders
- Average order value
- Items sold
- Payment success rate

## Tools Used

- Python
- Pandas
- Streamlit
- Plotly Express
- Parquet datasets

## What I Learned

I learned how to:

- Combine multiple datasets into one analytics table.
- Convert text columns into usable date values.
- Connect dashboard filters to backend calculations.
- Recalculate KPIs using filtered data.
- Create interactive Plotly charts.
- Use Streamlit caching to improve performance.
- Handle filter combinations that return no records.
- Test dashboard responsiveness and automatic refresh behavior.

## Deliverables

- `analytics_dashboard.py`
- Dashboard screenshots in `reports/figures/`
- Supporting processed datasets in `data/processed/`