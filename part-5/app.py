"""
Part 5: Mini Project - Personal Website with Flask
===================================================
A complete personal website using everything learned in Parts 1-4.

How to Run:
1. Make sure venv is activated
2. Run: python app.py
3. Open browser: http://localhost:5000
"""

from flask import Flask, render_template

app = Flask(__name__)

# =============================================================================
# YOUR DATA - Customize this section with your own information!
# =============================================================================

PERSONAL_INFO = {
    'name': 'Anurag Patil',
    'title': 'Web Developer,AI Engineer',
    'bio': 'A passionate developer learning Flask and web development.',
    'email': 'anuragpatil060@gmail.com',
    'github': 'https://github.com/DarkNetNinja',
    'linkedin': 'https://linkedin.com/in/yourusername',
}

SKILLS = [
    {'name': 'Python', 'level': 80},
    {'name': 'HTML/CSS', 'level': 75},
    {'name': 'Flask', 'level': 60},
    {'name': 'C++', 'level': 50},
    {'name': 'SQL', 'level': 45},
]

PROJECTS = [
    {'id': 1, 'name': 'Portfolio', 'description': 'A Flask-powered personal portfolio website.', 'tech': ['Python', 'Flask', 'HTML', 'CSS'], 'status': 'Completed'},
    {'id': 2, 'name': 'Recommendation Engine', 'description': 'A simple movie recommender', 'tech': ['Python', 'Flask', 'SQLite'], 'status': 'Completed'},
    {'id': 3, 'name': 'receipt Generator', 'description': 'Generate a receipt after after shopping.', 'tech': ['Python', 'Flask', 'API'], 'status': 'In Progress'},
    {'id': 4, 'name': 'tic tac toe game', 'description': 'simple web tic tac toe game.', 'tech': ['Python', 'Flask',], 'status': 'Planned'}
    
]
blog_posts = [
    {'id': 1, 'title': 'My First Post', 'content': 'Hello world! This is my start.'},
    {'id': 2, 'title': 'Flask is Cool', 'content': 'I am learning about routes and templates.'},
    {'id': 3, 'title': 'Life Update', 'content': 'Just coding and drinking coffee.'}
]



# =============================================================================
# ROUTES
# =============================================================================

@app.route('/')
def home():
    return render_template('index.html', info=PERSONAL_INFO)


@app.route('/about')
def about():
    return render_template('about.html', info=PERSONAL_INFO, skills=SKILLS)


@app.route('/projects')
def projects():
    return render_template('projects.html', info=PERSONAL_INFO, projects=PROJECTS)


@app.route('/project/<int:project_id>')  # Dynamic route for individual project
def project_detail(project_id):
    project = None
    for p in PROJECTS:
        if p['id'] == project_id:
            project = p
            break
    return render_template('project_detail.html', info=PERSONAL_INFO, project=project, project_id=project_id)


@app.route('/contact')
def contact():
    return render_template('contact.html', info=PERSONAL_INFO)

blog_posts = [
    {'id': 1, 'title': 'My First Post', 'content': 'Hello world! This is my start.'},
    {'id': 2, 'title': 'Flask is Cool', 'content': 'I am learning about routes and templates.'},
    {'id': 3, 'title': 'Life Update', 'content': 'Just coding and drinking coffee.'}
]

# --- 2. The Route ---
@app.route('/blog')
def blog():
    # Pass the list of posts to the template
    
        return render_template('blog.html', posts=blog_posts)

@app.route('/skill/<skill_name>')
def skill(skill_name):
    found_skill = next((s for s in SKILLS if s['name'].lower() == skill_name.lower()),None)
    related_projects = []
    for project in PROJECTS:
        tech_stack = [t.lower() for t in project['tech']]

        if skill_name.lower() in tech_stack:
            related_projects.append(project)

    
    if found_skill:
        return render_template('skills.html',skill = found_skill,projects = related_projects)
    else:
        return "<h1>Skill not found!</h1>",404

if __name__ == '__main__':
    app.run(debug=True)


# =============================================================================
# PROJECT STRUCTURE:
# =============================================================================
#
# part-5/
# ├── app.py              <- You are here
# ├── static/
# │   └── style.css       <- CSS styles
# └── templates/
#     ├── base.html       <- Base template (inherited by all pages)
#     ├── index.html      <- Home page
#     ├── about.html      <- About page
#     ├── projects.html   <- Projects list
#     ├── project_detail.html <- Single project view
#     └── contact.html    <- Contact page
#
# =============================================================================

# =============================================================================
# EXERCISES:
# =============================================================================
#
# Exercise 5.1: Personalize your website
#   - Update PERSONAL_INFO with your real information
#   - Add your actual skills and projects
#
# Exercise 5.2: Add a new page
#   - Create a /blog route
#   - Add blog posts data structure
#   - Create blog.html template
#
# Exercise 5.3: Enhance the styling
#   - Modify static/style.css
#   - Add your own color scheme
#   - Make it responsive for mobile
#
# Exercise 5.4: Add more dynamic features
#   - Create a /skill/<skill_name> route
#   - Show projects that use that skill
#
# =============================================================================
