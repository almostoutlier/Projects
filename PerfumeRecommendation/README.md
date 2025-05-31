# Perfume Recommendation System

A Flask-based web application that provides personalized perfume recommendations based on user preferences using Natural Language Processing (NLP) and cosine similarity.

## Overview

This project implements a recommendation system that suggests perfumes to users based on their gender, preferred brand, and description inputs. The system uses TF-IDF vectorization and cosine similarity to find perfumes that best match the user's preferences. The project includes both a web application and a Jupyter notebook for data analysis and model development.

1. Landing page for the user to give input
![alt text](/PerfumeRecommendation/images%20and%20videos/Screenshot%20(77).png)

2. Results page with top 5 suggestions
![alt text](/PerfumeRecommendation/images%20and%20videos/Screenshot%20(78).png)

**Architecture Flow:**
![Architecture](/PerfumeRecommendation/images%20and%20videos/architecture.jpg)

## Features

- Gender-based filtering
- Brand-specific recommendations
- Text-based similarity matching using TF-IDF
- Top 5 perfume recommendations
- Web interface for easy interaction
- Detailed perfume information including ratings and descriptions
- Docker support for easy deployment

## Tech Stack

- **Backend Framework**: Flask
- **Data Processing**: Pandas, NumPy
- **Machine Learning**: Scikit-learn (TF-IDF Vectorizer, Cosine Similarity)
- **Frontend**: HTML/CSS
- **Containerization**: Docker
- **Development**: Jupyter Notebook

## Project Structure

```
perfume-recommender/
├── app.py                  # Main Flask application
├── Dockerfile             # Docker configuration
├── main.ipynb            # Jupyter notebook for data analysis
├── templates/             
│   ├── index.html         # Home page template
│   └── results.html       # Results page template
├── fra_cleaned.csv        # Dataset file
├── requirements.txt       # Project dependencies
└── README.md             # Project documentation
```

## Installation

### Local Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/perfume-recommender.git
cd perfume-recommender
```

2. Create and activate a virtual environment (optional but recommended):
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install required packages:
```bash
pip install -r requirements.txt
```

### Docker Installation

1. Build the Docker image:
```bash
docker build -t perfume-recommender .
```

2. Run the Docker container:
```bash
docker run -p 80:80 perfume-recommender
```

## Usage

### Running the Web Application

#### Local Development
1. Start the Flask application:
```bash
python app.py
```

2. Open a web browser and navigate to `http://localhost:80`

#### Using Docker
1. After running the Docker container, access the application at `http://localhost:80`

### Using the Application

1. Enter your preferences:
   - Select gender
   - (Optional) Enter preferred brand
   - Describe your preferred fragrance notes or characteristics

2. Click "Submit" to get personalized recommendations

### Jupyter Notebook

The `main.ipynb` notebook contains:
- Data exploration and analysis
- Model development process
- Feature engineering steps
- Performance evaluation

To run the notebook:
1. Ensure Jupyter is installed: `pip install jupyter`
2. Launch Jupyter: `jupyter notebook`
3. Open `main.ipynb`


## Docker Configuration

The included Dockerfile:
- Uses Python 3.11 as the base image
- Sets up the working directory
- Installs dependencies
- Copies necessary files
- Exposes port 80
- Runs the Flask application

## Data Processing

The system processes perfume data through several steps:
1. Data cleaning and preprocessing
2. Text vectorization using TF-IDF
3. Similarity calculation using cosine similarity
4. Filtering based on user preferences

## Contributing

1. Fork the repository
2. Create a new branch (`git checkout -b feature/improvement`)
3. Make changes and commit (`git commit -am 'Add new feature'`)
4. Push to the branch (`git push origin feature/improvement`)
5. Create a Pull Request

## License

[![MIT License](https://img.shields.io/badge/License-MIT-green.svg)](https://choosealicense.com/licenses/mit/)
