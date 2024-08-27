
# Streamlit dependencies
import streamlit as st
import joblib,os
# Set the page title and icon
st.set_page_config(page_title="Kamogelo's Portfolio", page_icon="computer", layout="wide")

# Add custom CSS to style the app
st.markdown("""
    <style>
    /* Set the background color of the app */
    body {
        background-color: #f0f0f0; /* Light grey background */
    }
    
    /* Set the color and font size for titles and headers */
    .title {
        color: #333; /* Dark grey text */
    }
    .css-18e3th9 {
        color: #333; /* Text color for headers */
    }

    /* Set the color and border for the sidebar */
    .css-1d391kg {
        background-color: #e0e0e0; /* Slightly darker grey for sidebar */
        border-right: 1px solid #ccc; /* Light grey border */
    }

    /* Style the main content area */
    .css-1q8dd3e {
        background-color: #ffffff; /* White background for content */
        padding: 20px;
    }
    </style>
""", unsafe_allow_html=True)

# Data dependencies
import pandas as pd




# The main function where we will build the actual app
def main():
    # Add FontAwesome CDN link
    st.markdown(
    """
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0-beta3/css/all.min.css">
    """,
    unsafe_allow_html=True)

    # Add custom CSS for a lighter grey theme
    st.markdown("""
    <style>
        /* Set background color for the main container */
        .reportview-container {
            background-color: #f5f5f5; /* Very light grey background */
            color: #000000; /* Black text color */
        }

        /* Set background color for main content area */
        .main {
            background-color: #f5f5f5; /* Very light grey background */
        }

        /* Set color for headers */
        h1, h2, h3, h4, h5, h6 {
            color: #333333; /* Dark grey color for headers */
        }

        /* Set color for subheaders */
        .css-1b1r11w { /* Adjust this selector if necessary */
            color: #666666; /* Medium grey color for subheaders */
        }

        /* Set color for regular text */
        .css-18e3th9, .css-1v0mbdj, .css-1u7w7k7, .css-ffh4ll { /* Adjust these selectors if necessary */
            color: #000000; /* Black color for text */
        }

        /* Customize button styles */
        .stButton > button {
            background-color: #dddddd;
            color: #000000;
            border: 1px solid #cccccc;
            padding: 10px 20px;
            border-radius: 5px;
        }

        .stButton > button:hover {
            background-color: #cccccc;
        }

        /* Customize other interactive elements */
        .css-1v0mbdj a { /* Adjust this selector if necessary */
            color: #1e90ff; /* Example link color */
        }

        /* Customize sidebar styles */
        .css-1d391kg { /* Adjust this selector if necessary */
            background-color: #e0e0e0; /* Slightly darker grey for sidebar */
            color: #000000;
        }

        .css-1d391kg .css-18e3th9 {
            color: #000000;
        }
    </style>
    """, unsafe_allow_html=True)




    
    # Create a sidebar with navigation options
    st.sidebar.title("Navigation")
    options = ["Home", "About Me", "Projects", "Contact"]
    selected_option = st.sidebar.selectbox("Select a page:", options)
    
    


    

    # Build out the home page
    if selected_option == "Home":
        
        # Add a professional profile picture
        st.image("https://img.freepik.com/premium-photo/graph_1197721-106702.jpg?w=740", width=350)
        st.title("Hi!,I'm Kamogelo")
        st.subheader("Data Scientist | Machine Learning Enthusiast")
        # Brief Introduction with text styling
        st.write("""
    **Data Scientist** with a robust foundation in Python programming, machine learning, and data analysis, complemented by hands-on experience in developing predictive models and classification systems. My academic background in Environmental Sciences with Chemistry and Geography from North West University, combined with specialized training from Explore AI Academy, has equipped me with the skills to tackle complex data challenges effectively.
    """)
        # Key Skills
        st.markdown("### Core Competencies")
        st.markdown("""
        - **Machine Learning:** Skilled in developing predictive models and classification systems.
        - **Data Analysis:** Expertise in regression analysis, feature engineering, and statistical modeling.
        - **Natural Language Processing (NLP):** Proficient in text processing and classification tasks.
        - **Technical Proficiency:** Python, scikit-learn, pandas, NLTK.
        """)
        
        # Value Proposition
        st.write("""
        I am dedicated to using data to solve complex problems and help organizations make data-driven decisions. My analytical mindset, combined with a deep understanding of data science methodologies, allows me to deliver high-impact solutions that drive business value.
""")
        
        # Add a call-to-action or a quote to inspire or engage visitors
        st.markdown(
    """
    <div style="background-color:#f0f0f0;padding:10px;border-radius:5px;margin-top:20px;">
        <p style="font-size:18px;text-align:center;font-style:italic;">“The best way to predict the future is to invent it.” — Alan Kay</p>
    </div>
    """,
    unsafe_allow_html=True
)
        
        

        
        

        

    # Build out the About page
    elif selected_option == "About Me":
        st.title("About Me")
        # Add a professional profile picture
        st.image("portfolio.jpeg",width=200)
        st.write("""


    I'm a dedicated Data Scientist with a deep passion for unraveling the complexities of data to drive innovation and efficiency. My journey into data science began with a fascination for how data can be leveraged to solve real-world problems, leading me to explore various methodologies and tools that have shaped my career.
    """)
        st.subheader("My Passion")
        st.write("""
    What drives me is the challenge of transforming raw data into meaningful insights that can significantly impact decision-making processes. I thrive on exploring new data science techniques, experimenting with different models, and continuously learning to refine my skills. My enthusiasm for data science is not just about working with numbers, but about the stories and solutions that data can uncover.
    """)
        st.subheader("Skills and Expertise")
        st.markdown("""
        <style>
        .skills-container {
            display: flex;
            flex-wrap: wrap;
            justify-content: center;
            margin-top: 20px;
        }
        .skill-item {
            margin: 10px;
            text-align: center;
        }
        .skill-item i {
            font-size: 24px;
            display: block;
        }
        .skill-item span {
            display: block;
            margin-top: 5px;
        }
        </style>
        <div class="skills-container">
            <div class="skill-item">
                <i class="fas fa-code"></i>
                <span>Python</span>
            </div>
            <div class="skill-item">
                <i class="fab fa-js-square"></i>
                <span>JavaScript</span>
            </div>
            <div class="skill-item">
                <i class="fab fa-html5"></i>
                <span>HTML5</span>
            </div>
            <div class="skill-item">
                <i class="fab fa-css3-alt"></i>
                <span>CSS</span>
            </div>
            <div class="skill-item">
                <i class="fas fa-chart-line"></i>
                <span>Regression Analysis</span>
            </div>
            <div class="skill-item">
                <i class="fas fa-language"></i>
                <span>NLP</span>
            </div>
            <div class="skill-item">
                <i class="fas fa-calculator"></i>
                <span>Statistical Modeling</span>
            </div>
            <div class="skill-item">
                <i class="fas fa-cogs"></i>
                <span>scikit-learn</span>
            </div>
            <div class="skill-item">
                <i class="fas fa-database"></i>
                <span>pandas</span>
            </div>
            <div class="skill-item">
                <i class="fas fa-tachometer-alt"></i>
                <span>PowerBI</span>
            </div>
            <div class="skill-item">
                <i class="fas fa-server"></i>
                <span>MySQL</span>
            </div>
            <div class="skill-item">
                <i class="fas fa-globe"></i>
                <span>ArcGIS Pro</span>
            </div>
            <div class="skill-item">
                <i class="fas fa-comments"></i>
                <span>Effective Communication</span>
            </div>
            <div class="skill-item">
                <i class="fas fa-users"></i>
                <span>Team Leadership</span>
            </div>
            <div class="skill-item">
                <i class="fas fa-presentation"></i>
                <span>Presentation Skills</span>
            </div>
        </div>
        """, unsafe_allow_html=True)


        
        st.subheader("Education")
        st.markdown("""
        <style>
        .education-container {
            display: flex;
            flex-direction: column;
            align-items: center;
            margin-top: 20px;
        }
        .education-item {
            display: flex;
            align-items: center;
            margin: 10px;
            text-align: center;
        }
        .education-item img {
            height: 40px;
            margin-right: 10px;
        }
        .education-item div {
            display: flex;
            flex-direction: column;
            justify-content: center;
        }
        </style>

        <div class="education-container">
            <div class="education-item">
                <img src=https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQdM_gXMqMhW48YXpcWM4OZ5wCG2uT4EWmTKg&s alt="Explore AI Academy Logo" />  
                <div>
                    <strong>Explore AI Academy</strong><br />
                    Data Science<br />
                    - Specialized in advanced data science techniques and methodologies.
                </div>
            </div>
            <div class="education-item">
                <img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSTQa-wC2-6b6dHstqnvpTLgfC0b4aZUpjkrw&s" alt="North West University Logo" />  
                <div>
                    <strong>North West University</strong><br />
                    BSc in Environmental Sciences with Chemistry and Geography<br />
                    - Developed a strong foundation in scientific methods and data analysis through interdisciplinary studies.
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)
        
        st.subheader("Experience")
        st.markdown("""
        <style>
        .experience-container {
        display: flex;
        flex-direction: column;
        align-items: center;
        margin-top: 20px;
    }
    .experience-item {
    display: flex;
    align-items: center;
    margin: 10px;
    text-align: center;
    }
    .experience-item img {
    height: 40px;
    margin-right: 10px;
    }
    .experience-item div {
    display: flex;
    flex-direction: column;
    justify-content: center;
   }
   </style>
   <div class="experience-container">
   <div class="experience-item">
   <img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRhNZ-oA857LBER7nEhPzLXCmLyIfHwbhRV4w&s" alt="Sand Technologies Logo" />
   <div>
   <strong>Sand Technologies</strong><br />
   Data Science Intern(August 2024 - Present)<br />
   - Engaging in all data science tasks, utilizing a wide range of tools and techniques commonly used in the field.
   </div>
   </div>
   </div>
""", unsafe_allow_html=True)
        st.subheader("Looking Ahead")
        st.write("""
        I am eager to collaborate with forward-thinking teams and contribute to innovative projects that push the boundaries of data science and AI. My goal is to apply my skills and knowledge to make a meaningful impact and drive organizational success through data-driven decision-making.
        """)
        
        
        pass

        

    # Build out the projects page
    elif selected_option == "Projects":
        # Define the project_box function
        def project_box(image_path, title, role, institution, objective, techniques, results, github_link, app_link=None, button_key=None):
           st.image(image_path, use_column_width=True)
           st.subheader(title)
           st.write(f"**Role:** {role}")
           st.write(f"**Academic Institution:** {institution}")
           st.write(f"**Objective:** {objective}")
           st.write(f"**Techniques Used:** {techniques}")
           st.write(f"**Results:** {results}")
           if app_link:
               st.write(f"[Check out the deployed app]({app_link})")
           if st.button("View Project", key=button_key):
               st.write(f"[View on GitHub]({github_link})")
            
        
    
        st.title("Projects")
        # Project 1: Predicting CO2 Emissions from the Agri-food Sector
        col1, col2 = st.columns(2)
        with col1:
            project_box("https://media.istockphoto.com/id/1304758575/photo/reduction-of-the-amount-of-co2-emissions-concept-image-with-co2-icon-text-and-tree-shape-in.jpg?s=612x612&w=0&k=20&c=OO0Jl_EhAuRUPQSCqpxcKEr4CFQ_WNJ-J68w8IG0JbY=",
                        "Predicting CO2 Emissions from the Agri-food Sector", 
                        "Team Leader, Data Scientist", 
                        "Explore AI Academy", 
                        "Developed predictive models to forecast CO2 emissions from agricultural activities and identify key emission sources.", 
                        "Regression analysis, feature engineering, Python (scikit-learn, pandas).", 
                        "Developed three regression models and provided actionable insights for reducing emissions and recommendations for sustainable agricultural practices.", 
                        
                        "https://github.com/01Kamo/Predicting-CO2-Emissions.git",
                        button_key="co2_project_button")

        # Project 2: News Classification System
        with col2:
            project_box("https://media.istockphoto.com/id/1368872054/vector/online-news-search-and-reading-news-updates-news-websites-information-on-newspapers-public.jpg?s=612x612&w=0&k=20&c=lnqRsfz6XqoOSHNMXCazLduB5RELyp9e-M0UoKQq4jY=",
                        "News Classification System", 
                        "Team Leader, Data Scientist", 
                        "Explore AI Academy", 
                        "Built a machine learning-based news classification system to categorize articles for a news outlet.", 
                        "Natural Language Processing (NLP), classification algorithms (SVM, Naive Bayes, etc), Python (NLTK, scikit-learn).", 
                        "Deployed three models that enhanced editorial workflow by automating article categorization. Actionable Insights: Streamlined editorial processes, improving efficiency and content management.",
                        "https://github.com/01Kamo/News-Classification-System.git",
                        app_link="https://my-app-repo-jwrthtc8pflncqykhvkthd.streamlit.app/",
                        button_key="news_project_button")
            # Project 3: Anime Recommender System
        col3, col4 = st.columns(2)
        with col3:
            project_box("https://i.pinimg.com/originals/d3/14/d7/d314d775cac76cee6dbf27931b5fee9a.png",
                        "Anime Recommender System",
                        "Team Leader, Data Scientist", 
                        "Explore AI Academy", 
                        "Developed a highly accurate and user-centric recommender system that provides fans with relevant and engaging anime recommendations.", 
                        "Collaborative filtering, content-based filtering, Python (scikit-learn, pandas, Streamlit).", 
                        "Designed and evaluated the system using Root Mean Square Error (RMSE) to ensure high accuracy and user satisfaction.", 
                        "https://github.com/01Kamo/Anime-Recommender-System.git",
                        button_key="anime_project_button")
    # Build out the contact page
    elif selected_option == "Contact":
            
        st.title("Contact Me")
        st.write("""
    **I’d love to hear from you!** Whether you have questions, opportunities, or just want to connect, feel free to reach out using the contact details below. I'm always open to discussing exciting projects, collaborations, or any other opportunities.
    """)
    # Display contact details with icons
        st.subheader("Contact Details")
    # Phone Numbers
        st.write("**Phone Numbers:**")
        col1, col2 = st.columns(2)
        with col1:
            st.write("📞 +27 64 786 4621")
            # Email
        st.write("**Email: KamoNkwana64@gmail.com**")
        email = "KamoNkwana64@gmail.com"
        if st.button("Send me an email"):
            st.markdown(f"[Send me an email](mailto:{email})")

        
        # LinkedIn
        st.write("**LinkedIn: Kamogelo Nkwana**")
        linkedin_url = "https://www.linkedin.com/in/kamogelo-nkwana-a2b505236"
        if st.button("Visit my LinkedIn Profile"):
            st.markdown(f"[My LinkedIn Profile]({linkedin_url})")
        


                    



            
            

            
            
        
            
            
                
                        
            
        
        


            




    
    
    




       
    

            
   
        

	

		

# Required to let Streamlit instantiate our web app.  
if __name__ == '__main__':
	main()