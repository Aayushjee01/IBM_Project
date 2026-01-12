"""
AI-Based Career Recommendation & Skill Gap Analysis System
Main application file using Streamlit for the web interface
"""

import streamlit as st
import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from typing import List, Dict, Tuple

# Set page config
st.set_page_config(
    page_title="AI Career Recommendation System",
    page_icon="🚀",
    layout="wide"
)

# Sample career database with skills required
CAREER_DATABASE = {
    "Data Scientist": {
        "skills": ["Python", "Machine Learning", "Statistics", "SQL", "Data Visualization", "Deep Learning", "NLP"],
        "description": "Analyze complex data to extract insights and build predictive models",
        "salary_range": "$90,000 - $150,000",
        "growth": "High",
        "experience_level": "2-5 years"
    },
    "Software Engineer": {
        "skills": ["Python", "Java", "JavaScript", "System Design", "Databases", "Cloud Computing", "Git"],
        "description": "Design, develop, and maintain software applications",
        "salary_range": "$80,000 - $140,000",
        "growth": "Very High",
        "experience_level": "0-5 years"
    },
    "Product Manager": {
        "skills": ["Product Strategy", "Market Research", "Agile", "Communication", "Analytics", "Leadership", "UX"],
        "description": "Lead product development from concept to launch",
        "salary_range": "$100,000 - $160,000",
        "growth": "High",
        "experience_level": "3-7 years"
    },
    "DevOps Engineer": {
        "skills": ["Docker", "Kubernetes", "AWS", "CI/CD", "Linux", "Scripting", "Monitoring"],
        "description": "Bridge development and operations for efficient software delivery",
        "salary_range": "$95,000 - $145,000",
        "growth": "Very High",
        "experience_level": "2-5 years"
    },
    "UX Designer": {
        "skills": ["Figma", "User Research", "Prototyping", "Design Thinking", "HTML/CSS", "Wireframing", "Usability Testing"],
        "description": "Create intuitive and user-friendly digital experiences",
        "salary_range": "$70,000 - $120,000",
        "growth": "High",
        "experience_level": "1-4 years"
    },
    "Cloud Architect": {
        "skills": ["AWS", "Azure", "GCP", "Cloud Security", "Architecture", "Infrastructure", "Kubernetes"],
        "description": "Design and manage cloud infrastructure solutions",
        "salary_range": "$110,000 - $170,000",
        "growth": "Very High",
        "experience_level": "5-10 years"
    },
    "AI Engineer": {
        "skills": ["Python", "TensorFlow", "PyTorch", "MLOps", "Deep Learning", "Computer Vision", "NLP"],
        "description": "Build and deploy AI/ML models at scale",
        "salary_range": "$100,000 - $160,000",
        "growth": "Very High",
        "experience_level": "2-5 years"
    },
    "Business Analyst": {
        "skills": ["SQL", "Excel", "Data Analysis", "Requirements Gathering", "Stakeholder Management", "Power BI", "Documentation"],
        "description": "Analyze business processes and recommend data-driven solutions",
        "salary_range": "$65,000 - $110,000",
        "growth": "Medium",
        "experience_level": "1-4 years"
    },
    "Cybersecurity Specialist": {
        "skills": ["Network Security", "Ethical Hacking", "SIEM", "Compliance", "Risk Assessment", "Penetration Testing", "Firewalls"],
        "description": "Protect organizations from cyber threats and vulnerabilities",
        "salary_range": "$85,000 - $140,000",
        "growth": "Very High",
        "experience_level": "2-5 years"
    },
    "Data Engineer": {
        "skills": ["Python", "SQL", "ETL", "Big Data", "Spark", "Hadoop", "Data Warehousing"],
        "description": "Build and maintain data pipelines and infrastructure",
        "salary_range": "$90,000 - $145,000",
        "growth": "Very High",
        "experience_level": "2-5 years"
    }
}

class CareerRecommendationEngine:
    """AI-based career recommendation engine with skill gap analysis"""
    
    def __init__(self, career_database: Dict):
        self.career_database = career_database
        self.vectorizer = TfidfVectorizer()
        self._build_model()
    
    def _build_model(self):
        """Build TF-IDF model for skill matching"""
        career_texts = []
        for career, info in self.career_database.items():
            skills_text = " ".join(info["skills"])
            career_texts.append(skills_text)
        
        self.skill_matrix = self.vectorizer.fit_transform(career_texts)
        self.career_names = list(self.career_database.keys())
    
    def analyze_skill_gap(self, user_skills: List[str], target_career: str) -> Dict:
        """Analyze gap between user skills and target career requirements"""
        if target_career not in self.career_database:
            return {}
        
        required_skills = set(self.career_database[target_career]["skills"])
        user_skills_set = set([s.lower().strip() for s in user_skills])
        required_skills_lower = set([s.lower() for s in required_skills])
        
        # Calculate matched and missing skills
        matched_skills = []
        missing_skills = []
        
        for skill in required_skills:
            skill_lower = skill.lower()
            if skill_lower in user_skills_set:
                matched_skills.append(skill)
            else:
                # Check for partial matches
                matched = False
                for user_skill in user_skills_set:
                    if user_skill in skill_lower or skill_lower in user_skill:
                        matched_skills.append(skill)
                        matched = True
                        break
                if not matched:
                    missing_skills.append(skill)
        
        match_percentage = (len(matched_skills) / len(required_skills)) * 100 if required_skills else 0
        
        return {
            "matched_skills": matched_skills,
            "missing_skills": missing_skills,
            "match_percentage": match_percentage,
            "total_required": len(required_skills),
            "total_matched": len(matched_skills)
        }
    
    def recommend_careers(self, user_skills: List[str], top_n: int = 5) -> List[Tuple[str, float, Dict]]:
        """Recommend careers based on user skills using cosine similarity"""
        user_skills_text = " ".join(user_skills)
        user_vector = self.vectorizer.transform([user_skills_text])
        
        # Calculate similarity scores
        similarities = cosine_similarity(user_vector, self.skill_matrix)[0]
        
        # Get top recommendations
        top_indices = np.argsort(similarities)[::-1][:top_n]
        
        recommendations = []
        for idx in top_indices:
            career_name = self.career_names[idx]
            similarity_score = similarities[idx] * 100
            gap_analysis = self.analyze_skill_gap(user_skills, career_name)
            
            recommendations.append((
                career_name,
                similarity_score,
                gap_analysis,
                self.career_database[career_name]
            ))
        
        return recommendations
    
    def get_learning_path(self, missing_skills: List[str], career: str) -> Dict:
        """Generate learning path recommendations for missing skills"""
        skill_priority = {
            "Python": {"level": "Beginner-Intermediate", "resources": ["Python.org", "Real Python", "Codecademy"], "time": "2-3 months"},
            "Machine Learning": {"level": "Intermediate-Advanced", "resources": ["Coursera ML Course", "Fast.ai", "Kaggle"], "time": "3-4 months"},
            "SQL": {"level": "Beginner", "resources": ["SQLBolt", "Mode Analytics", "LeetCode"], "time": "1-2 months"},
            "Cloud Computing": {"level": "Intermediate", "resources": ["AWS Training", "Cloud Academy", "A Cloud Guru"], "time": "2-3 months"},
            "Data Visualization": {"level": "Beginner-Intermediate", "resources": ["Tableau Public", "DataCamp", "Storytelling with Data"], "time": "1-2 months"}
        }
        
        learning_path = []
        for skill in missing_skills:
            if skill in skill_priority:
                learning_path.append({
                    "skill": skill,
                    **skill_priority[skill]
                })
            else:
                learning_path.append({
                    "skill": skill,
                    "level": "Intermediate",
                    "resources": ["Online Courses", "Documentation", "Practice Projects"],
                    "time": "2-3 months"
                })
        
        return {
            "career": career,
            "skills_to_learn": learning_path,
            "estimated_time": f"{len(missing_skills) * 2}-{len(missing_skills) * 3} months"
        }

def main():
    st.title("🚀 AI-Based Career Recommendation & Skill Gap Analysis System")
    st.markdown("### Discover your ideal career path and identify skills to develop")
    
    # Initialize session state
    if 'recommendations' not in st.session_state:
        st.session_state.recommendations = None
    if 'engine' not in st.session_state:
        st.session_state.engine = CareerRecommendationEngine(CAREER_DATABASE)
    
    # Sidebar for user input
    with st.sidebar:
        st.header("📝 Your Profile")
        st.markdown("---")
        
        # User information
        user_name = st.text_input("Your Name", placeholder="Enter your name")
        current_role = st.text_input("Current Role (Optional)", placeholder="e.g., Student, Developer")
        
        st.markdown("### Your Skills")
        st.markdown("Enter your skills (comma-separated or one per line)")
        
        skills_input = st.text_area(
            "Skills",
            height=200,
            placeholder="Python, Machine Learning, SQL, Communication, Leadership..."
        )
        
        # Parse skills
        if skills_input:
            user_skills = [skill.strip() for skill in skills_input.replace('\n', ',').split(',') if skill.strip()]
        else:
            user_skills = []
        
        # Quick skill selection
        st.markdown("**Or select from common skills:**")
        common_skills = ["Python", "Java", "JavaScript", "SQL", "Machine Learning", "AWS", "Docker", "Git", "Communication", "Leadership"]
        selected_common = st.multiselect("Common Skills", common_skills)
        user_skills = list(set(user_skills + selected_common))
        
        st.markdown("---")
        analyze_button = st.button("🔍 Analyze Career Options", type="primary", use_container_width=True)
    
    # Main content area
    if analyze_button and user_skills:
        with st.spinner("Analyzing your profile and generating recommendations..."):
            recommendations = st.session_state.engine.recommend_careers(user_skills, top_n=5)
            st.session_state.recommendations = recommendations
        
        if st.session_state.recommendations:
            st.success(f"Found {len(st.session_state.recommendations)} career matches for you!")
            
            # Display recommendations
            st.header("🎯 Recommended Careers")
            
            for idx, (career_name, score, gap_analysis, career_info) in enumerate(st.session_state.recommendations, 1):
                with st.expander(f"#{idx} {career_name} - {score:.1f}% Match", expanded=(idx == 1)):
                    col1, col2 = st.columns([2, 1])
                    
                    with col1:
                        st.markdown(f"**Description:** {career_info['description']}")
                        st.markdown(f"**Salary Range:** {career_info['salary_range']}")
                        st.markdown(f"**Growth Potential:** {career_info['growth']}")
                        st.markdown(f"**Experience Level:** {career_info['experience_level']}")
                    
                    with col2:
                        # Progress bar for match percentage
                        st.metric("Match Score", f"{gap_analysis['match_percentage']:.1f}%")
                        progress_value = gap_analysis['match_percentage'] / 100
                        st.progress(progress_value)
                    
                    # Skill gap analysis
                    st.markdown("#### 📊 Skill Gap Analysis")
                    
                    col3, col4 = st.columns(2)
                    
                    with col3:
                        st.markdown("**✅ Matched Skills**")
                        if gap_analysis['matched_skills']:
                            for skill in gap_analysis['matched_skills']:
                                st.success(f"✓ {skill}")
                        else:
                            st.info("No skills matched yet")
                    
                    with col4:
                        st.markdown("**❌ Missing Skills**")
                        if gap_analysis['missing_skills']:
                            for skill in gap_analysis['missing_skills']:
                                st.error(f"✗ {skill}")
                        else:
                            st.success("All required skills matched!")
                    
                    # Learning path
                    if gap_analysis['missing_skills']:
                        st.markdown("#### 📚 Recommended Learning Path")
                        learning_path = st.session_state.engine.get_learning_path(
                            gap_analysis['missing_skills'],
                            career_name
                        )
                        
                        for skill_info in learning_path['skills_to_learn'][:5]:  # Show top 5
                            with st.expander(f"Learn: {skill_info['skill']}"):
                                st.markdown(f"**Level:** {skill_info.get('level', 'Intermediate')}")
                                st.markdown(f"**Time Required:** {skill_info.get('time', '2-3 months')}")
                                st.markdown("**Resources:**")
                                for resource in skill_info.get('resources', []):
                                    st.markdown(f"- {resource}")
                    
                    st.markdown("---")
    
    elif analyze_button and not user_skills:
        st.warning("⚠️ Please enter at least one skill to get career recommendations.")
    
    else:
        # Welcome screen
        st.markdown("""
        ### Welcome to the AI Career Recommendation System! 👋
        
        This intelligent system helps you:
        
        - 🎯 **Discover** career paths that match your skills
        - 📊 **Analyze** the gap between your current skills and career requirements
        - 📚 **Get** personalized learning paths to bridge skill gaps
        - 💡 **Make** informed career decisions with AI-powered insights
        
        #### How it works:
        1. Enter your skills in the sidebar
        2. Click "Analyze Career Options"
        3. Review your personalized career recommendations
        4. Explore skill gap analysis and learning paths
        
        #### Features:
        - **AI-Powered Matching**: Uses advanced NLP and similarity algorithms
        - **Comprehensive Analysis**: Detailed skill gap identification
        - **Personalized Learning**: Customized learning paths for each career
        - **Real-time Insights**: Instant recommendations and analysis
        """)
        
        # Display sample careers
        st.markdown("### 💼 Available Career Profiles")
        career_cols = st.columns(3)
        careers_list = list(CAREER_DATABASE.keys())
        
        for idx, career in enumerate(careers_list):
            col_idx = idx % 3
            with career_cols[col_idx]:
                with st.container():
                    st.markdown(f"**{career}**")
                    st.caption(CAREER_DATABASE[career]['description'][:80] + "...")
                    st.markdown(f"*Growth: {CAREER_DATABASE[career]['growth']}*")

if __name__ == "__main__":
    main()