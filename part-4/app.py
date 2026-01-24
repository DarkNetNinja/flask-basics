"""
Part 4: Dynamic Routes - URL Parameters
========================================
How to Run:
1. Make sure venv is activated
2. Run: python app.py
3. Try different URLs like /user/YourName or /post/123
"""

from flask import Flask, render_template, url_for

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/user/<username>')  # <username> captures any text from URL, visit: /user/Alice, /user/Bob
def user_profile(username):
    return render_template('user.html', username=username)


@app.route('/post/<int:post_id>')  # <int:post_id> captures only integers, /post/abc returns 404
def show_post(post_id):
    posts = {  # Simulated post data (in real apps, this comes from a database)
        1: {'title': 'Getting Started with Flask', 'content': 'Flask is a micro-framework...'},
        2: {'title': 'Understanding Routes', 'content': 'Routes map URLs to functions...'},
        3: {'title': 'Working with Templates', 'content': 'Jinja2 makes HTML dynamic...'},
    }
    post = posts.get(post_id)  # Get the post or None if not found
    return render_template('post.html', post_id=post_id, post=post)


@app.route('/user/<username>/post/<int:post_id>')  # Multiple dynamic segments, visit: /user/Alice/post/1
def user_post(username, post_id):
    return render_template('user_post.html', username=username, post_id=post_id)


@app.route('/about/')  # Trailing slash means both /about and /about/ work
def about():
    return render_template('about.html')


@app.route('/links')  # Demonstrates url_for() - generates URLs dynamically (better than hardcoding!)
def show_links():
    links = {
        'home': url_for('home'),
        'about': url_for('about'),
        'user_alice': url_for('user_profile', username='Alice'),
        'user_bob': url_for('user_profile', username='Bob'),
        'post_1': url_for('show_post', post_id=1),
        'post_2': url_for('show_post', post_id=2),
    }
    return render_template('links.html', links=links)

@app.route('/product/<int:product_id>')
def product_details(product_id):
    products = {
        
        1: {'name': 'Gaming Laptop', 'price': 1200},
        2: {'name': 'Mechanical Keyboard', 'price': 100},
        3: {'name': 'Wireless Mouse', 'price': 40}
    }

    product = products.get(product_id)

    return render_template('product.html',product = product,product_id = product_id)

@app.route('/category/<category_name>/product/<int:product_id>')
def category_product_details(category_name,product_id):
    products = {
        
        1: {'name': 'Gaming Laptop', 'price': 1200},
        2: {'name': 'Mechanical Keyboard', 'price': 100},
        3: {'name': 'Wireless Mouse', 'price': 40}
    }
    product = products.get(product_id)

    if product:
        return render_template('category_product.html', category=category_name, product=product)
    else:
        return "<h1>Product Not Found</h1>", 404
    
@app.route('/add/<float:num1>/<float:num2>')
def add_num(num1,num2):
    result = num1 + num2
    return render_template('calculator.html',n1= num1,n2 = num2,total = result)

@app.route('/files/<path:file_path>')
def show_file(file_path):
    return f"<h1>You are accesing the file: {file_path}</h1>"

@app.route('/convert/<float:amount>/from/<currency_from>/to/<currency_to>')
def converter(amount,currency_from,currency_to):
    rates = {
        'USD': 1.0,
        'EUR': 0.85,
        'GBP': 0.75,
        'INR': 83.0
    }

    if currency_from not in rates or currency_to not in rates:
        return "<h1>Error: Currency not supported</h1>",400
    
    val_in_usd = amount/rates[currency_from]
    converted_amount = val_in_usd * rates[currency_to]

    final_amount = round(converted_amount,2)

    return f"<h1>{amount} {currency_from}"

@app.route('/search/<query>')
def search(query):
    return f"<h1>Search results for: {query}</h1>"

if __name__ == '__main__':
    app.run(debug=True)


# =============================================================================
# URL PARAMETER TYPES:
# =============================================================================
#
# <variable>         - String (default), accepts any text without slashes
# <int:variable>     - Integer, accepts only positive integers
# <float:variable>   - Float, accepts floating point numbers
# <path:variable>    - String, but also accepts slashes
# <uuid:variable>    - UUID strings
#
# =============================================================================

# =============================================================================
# EXERCISES:
# =============================================================================
#
# Exercise 4.1: Create a product page
#   - Add route /product/<int:product_id>
#   - Create a products dictionary with id, name, price
#   - Display product details or "Not Found" message
#
# Exercise 4.2: Category and product route
#   - Add route /category/<category_name>/product/<int:product_id>
#   - Display both the category and product information
#
# Exercise 4.3: Search route
#   - Add route /search/<query>
#   - Display "Search results for: [query]"
#   - Bonus: Add a simple search form that redirects to this route
#
# =============================================================================
