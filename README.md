# CO2 Emission Predictor

A web-based dashboard that predicts CO2 emissions from vehicles using a multiple linear regression model.

## Overview

This application uses machine learning to predict the CO2 emissions produced by cars based on their engine characteristics. Users can input vehicle parameters (engine size, cylinders, and fuel efficiency) through an interactive dashboard to get real-time CO2 emission predictions.

## Features

- **Interactive Dashboard**: User-friendly web interface for making predictions
- **Multiple Linear Regression Model**: Predicts CO2 emissions based on vehicle characteristics
- **Real-time Predictions**: Get instant CO2 emission estimates
- **Visual Analytics**: Data visualization powered by Plotly

## Prerequisites

- Python 3.6 or higher
- pip (Python package manager)

## Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd co2_emission
```

2. Create a virtual environment (recommended):
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage

To run the application locally:

```bash
python app.py
```

The application will be available at `http://127.0.0.1:8050/` by default.

### How to Use the Dashboard

1. Use the sliders to select:
   - **Number of Cylinders**: The number of cylinders in the engine
   - **Engine Size**: The displacement volume of the engine
   - **Miles Per Gallon (MPG)**: The fuel efficiency of the vehicle

2. The dashboard will instantly calculate and display the predicted CO2 emissions based on your inputs

## Data

The model is trained on the **Original Fuel Consumption Ratings dataset (2000-2014)**.

**Data Source**: [Original Fuel Consumption Ratings 2000-2014](https://lnkd.in/eiXxgvw)

## Research Paper

This project is based on a statistical analysis paper on predicting CO2 emissions using multiple regression models. See the linked paper for detailed methodology and statistical findings:

[Predicting the CO2 emission - Multiple Linear Regression model paper (PDF)](https://github.com/Saralkarki/statistical_papers/blob/master/Predicting%20CO2%20emission%20using%20multiple%20regression%20model.pdf)

## Technical Stack

- **Framework**: Dash (Python web framework for building analytical web apps)
- **Visualization**: Plotly
- **Backend**: Flask
- **Data Processing**: Pandas, NumPy
- **Deployment**: Gunicorn, Procfile configuration included

## Project Structure

```
co2_emission/
├── app.py              # Main Dash application
├── data.py             # Data loading and preprocessing
├── requirements.txt    # Python dependencies
├── Procfile           # Heroku deployment configuration
├── data/              # Data files directory
├── static/            # Static files (CSS, JavaScript, images)
└── .gitignore         # Git ignore rules
```

## Deployment

The application is configured for deployment on Heroku with the included `Procfile`.

## License

This project is open source and available under the MIT License.

## Author

Saral Karki

## Acknowledgments

- Data source: Original Fuel Consumption Ratings (2000-2014)
- Dashboard framework: Dash by Plotly
