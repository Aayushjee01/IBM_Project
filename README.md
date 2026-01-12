# AI-Based Career Recommendation & Skill Gap Analysis System

An intelligent system that uses AI and machine learning to recommend career paths based on user skills and provides detailed skill gap analysis with personalized learning paths.

## 🚀 Features

- **AI-Powered Career Recommendations**: Uses TF-IDF vectorization and cosine similarity to match user skills with career profiles
- **Skill Gap Analysis**: Identifies matched and missing skills for each recommended career
- **Personalized Learning Paths**: Provides customized learning resources and time estimates for skill development
- **Interactive Web Interface**: User-friendly Streamlit-based interface
- **Real-time Analysis**: Instant recommendations and detailed insights

## 📋 Requirements

- Python 3.8 or higher
- See `requirements.txt` for package dependencies

## 🛠️ Installation

1. Clone or download this repository
2. Install dependencies:
```bash
pip install -r requirements.txt
```

## 💻 Usage

Run the Streamlit application:
```bash
streamlit run career_recommendation_system.py
```

The application will open in your default web browser at `http://localhost:8501`

## 📖 How to Use

1. Enter your skills in the sidebar (comma-separated or one per line)
2. Optionally select from common skills
3. Click "Analyze Career Options"
4. Review personalized career recommendations
5. Explore skill gap analysis for each career
6. Access learning paths for missing skills

## 🏗️ System Architecture

- **Frontend**: Streamlit web interface
- **Backend**: Python-based recommendation engine
- **AI/ML**: TF-IDF vectorization, cosine similarity, skill matching algorithms
- **Data**: Career database with skills, salary ranges, and growth information

## 🎯 Core Components

1. **CareerRecommendationEngine**: Main recommendation engine class
2. **Skill Gap Analysis**: Analyzes user skills vs. career requirements
3. **Learning Path Generator**: Creates personalized skill development paths
4. **Career Database**: Comprehensive database of career profiles

## 📊 Technologies Used

- Python
- Streamlit
- Scikit-learn
- Pandas
- NumPy
- TF-IDF Vectorization
- Cosine Similarity

## 🚀 Deployment

This application is ready to deploy! See [DEPLOYMENT.md](DEPLOYMENT.md) for detailed deployment instructions.

### Quick Deploy Options:

1. **Streamlit Cloud (Recommended - Free & Easy)**
   - Push code to GitHub
   - Visit https://share.streamlit.io/
   - Connect repository and deploy

2. **Railway** (For private repos)
3. **Render** (Simple deployment)
4. **Heroku** (Established platform)

⚠️ **Note:** Vercel is NOT compatible with Streamlit applications. Use the platforms mentioned above.

See [DEPLOYMENT.md](DEPLOYMENT.md) for complete deployment guide.

## 🔮 Future Enhancements

- Integration with job market APIs
- User profile persistence
- Advanced ML models (neural networks)
- Resume parsing capabilities
- Integration with online learning platforms
- Career progression tracking
- Salary prediction models

## 📝 License

This project is created for educational purposes.

## 👥 Contributors

Created as part of IBM AI Project.