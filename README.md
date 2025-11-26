# Measles Surveillance Dashboard

This repository contains an interactive measles surveillance dashboard for England, built using the DIY Disease Tracking Dashboard Kit framework.

## Dashboard Features

The **Dashboard.ipynb** notebook provides:

- **Time Series Visualization**: Interactive line chart showing weekly measles cases with:
  - Date range selection (IntRangeSlider)
  - Moving average smoothing (IntSlider: 1-12 weeks)
  - Trend line overlay (Checkbox)
  - Linear/logarithmic scale toggle (Dropdown)

- **Age Distribution Analysis**: Stacked bar chart displaying cases by age group with:
  - Year/period filter (Dropdown)
  - Monthly/Quarterly/Yearly aggregation (Dropdown)
  - Age group selection (SelectMultiple)

- **API Integration**: Single integrated button to download current UKHSA data and refresh all graphs

- **Offline Capability**: Pre-loaded JSON data ensures dashboard works without API access

## Data Files

- `measles_weekly.json` - Weekly case counts (200 weeks)
- `measles_age.json` - Age-stratified data (8 age groups)
- `measles_regional.json` - Regional breakdown (9 regions)

## Running the Dashboard

1. Open `Dashboard.ipynb` in JupyterHub or Jupyter Notebook
2. Run all cells (Kernel → Restart & Run All)
3. Use interactive widgets to explore the data
4. Click "Refresh Data" to update from UKHSA API (when available)

## Technical Implementation

- **Data Wrangling**: Pandas DataFrames with proper date indexing
- **Visualization**: Matplotlib with customizable plots
- **Interactivity**: iPywidgets for controls (sliders, dropdowns, checkboxes)
- **API Access**: Requests library with rate limiting

---

# DIY Disease Tracking Dashboard Kit

Build and deploy your own Disease Tracker Dashboard using iPywidgets, Voila and Binders. Based on UK Government [data](https://ukhsa-dashboard.data.gov.uk/) published by the UK Health Security Agency ([UKHSA](https://www.gov.uk/government/organisations/uk-health-security-agency)).

Click here to launch this repository as a Binder: [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/fsmeraldi/diy-covid19dash/main)

Click [here](https://mybinder.org/v2/gh/fsmeraldi/diy-covid19dash/main?urlpath=%2Fvoila%2Frender%2FDashboard.ipynb) to render the dashboard template (```Dasboard.ipynb```) with Voila; this is where you will assemble your dashboard after going through the other notebooks.

**(C) 2020,2024 Fabrizio Smeraldi** ([f.smeraldi@qmul.ac.uk](mailto:f.smeraldi@qmul.ac.uk) - [web](http://www.eecs.qmul.ac.uk/~fabri/)). This repository is released under the [GNU GPLv3.0 or later](https://www.gnu.org/licenses/).
