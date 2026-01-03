# Books-Recommender-Engine

A Machine Learning based Books Recommender System that suggests books based on user interests using Collaborative Filtering (Nearest Neighbors algorithm). This project includes a complete pipeline from data ingestion to a Streamlit web application for the user interface.

## Features

- **Data Ingestion**: Automatically downloads and extracts the dataset.
- **Data Validation**: Validates the dataset schema and quality.
- **Data Transformation**: Prepares the data for the model (creating pivot tables, sparse matrices).
- **Model Training**: Trains a Nearest Neighbors model to find similar books.
- **Web Application**: A user-friendly interface built with Streamlit to browse and get recommendations.
- **Modular Codebase**: Organized into components, pipelines, and configuration for maintainability.

## Tech Stack

- **Python**: Primary programming language.
- **Scikit-learn**: For the Nearest Neighbors algorithm.
- **Pandas & NumPy**: For data manipulation and analysis.
- **Streamlit**: For the web application interface.
- **PyYAML**: For configuration management.

## Installation

1.  **Clone the repository:**

    ```bash
    git clone https://github.com/seneshMH/Books-Recommender-Engine.git
    cd Books-Recommender-Engine
    ```

2.  **Create and activate a virtual environment (optional but recommended):**

    ```bash
    python -m venv venv
    # Windows
    .\venv\Scripts\activate
    # Linux/Mac
    source venv/bin/activate
    ```

3.  **Install dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

    _Note: Ensure you have the required packages installed (numpy, pandas, pyyaml, scikit-learn, streamlit)._

## Usage

### 1. Run the Training Pipeline

Before running the app, you need to process the data and train the model.

```bash
python main.py
```

This command will:

- Download the dataset.
- Validate and transform the data.
- Train the model and save the artifacts (model and data) in the `artifacts/` directory.

### 2. Run the Web Application

Once the model is trained, launch the Streamlit app:

```bash
streamlit run app.py
```

The application will open in your default web browser. You can select a book from the dropdown to see recommendations.

## Configuration

The project configuration is located in `config/config.yaml`. You can modify paths, dataset URLs, and model parameters there.

## License

This project is licensed under the MIT License.
