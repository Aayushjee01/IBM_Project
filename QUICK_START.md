# Quick Start Guide

## Getting Started

### Prerequisites
- Python 3.8 or higher
- pip (Python package installer)

### Installation Steps

1. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

2. **Run the Application**
   ```bash
   streamlit run career_recommendation_system.py
   ```

3. **Access the Application**
   - The application will automatically open in your default web browser
   - Default URL: http://localhost:8501

### Using the System

1. **Enter Your Skills**
   - Use the sidebar to enter your skills
   - You can type skills (comma-separated) or select from common skills
   - Examples: "Python, Machine Learning, SQL" or select from the dropdown

2. **Analyze Career Options**
   - Click the "Analyze Career Options" button
   - Wait for the system to process (usually <2 seconds)

3. **Review Recommendations**
   - View your top 5 career matches
   - Check match percentages
   - Expand each career to see details

4. **Explore Skill Gap Analysis**
   - See which skills you have (matched)
   - Identify skills you need to learn (missing)
   - Review match percentages

5. **Access Learning Paths**
   - Click on learning path sections
   - View recommended resources
   - Check time estimates for skill development

## Project Structure

```
Ibm Project/
├── career_recommendation_system.py  # Main application file
├── requirements.txt                 # Python dependencies
├── README.md                        # Project documentation
├── LEAN_CANVAS.md                   # Business model canvas
├── CONCEPT_NOTES.md                 # Detailed concept documentation
├── PRESENTATION.md                  # Presentation slides (markdown)
├── PRESENTATION_OUTLINE.txt         # Presentation outline
└── QUICK_START.md                   # This file
```

## Key Features to Try

1. **Test with Different Skill Sets**
   - Try technical skills: Python, Java, SQL, AWS
   - Try soft skills: Communication, Leadership, Analytics
   - Try mixed skills: Python, Communication, Leadership

2. **Compare Careers**
   - Note the different match percentages
   - Review skill gaps for each career
   - See how learning paths differ

3. **Explore Learning Paths**
   - Check time estimates
   - Review recommended resources
   - Plan your skill development

## Troubleshooting

### Issue: Package Installation Errors
**Solution:** Make sure you have Python 3.8+ and pip is up to date
```bash
python --version
pip install --upgrade pip
```

### Issue: Streamlit Not Found
**Solution:** Install streamlit explicitly
```bash
pip install streamlit
```

### Issue: Port Already in Use
**Solution:** Streamlit will try another port automatically, or specify one:
```bash
streamlit run career_recommendation_system.py --server.port 8502
```

## Next Steps

1. **Customize Careers**: Edit the `CAREER_DATABASE` in the Python file to add more careers
2. **Enhance Learning Paths**: Update the `get_learning_path` method with more resources
3. **Add Features**: Implement user profiles, save recommendations, etc.
4. **Deploy**: Consider deploying to Streamlit Cloud or other platforms

## Support

For questions or issues:
- Review the README.md for detailed documentation
- Check CONCEPT_NOTES.md for system architecture details
- Review PRESENTATION.md for overview and features