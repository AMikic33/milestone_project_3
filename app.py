import os
from flask import (
    Flask, flash, render_template, 
    redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
if os.path.exists("env.py"):
    import env


app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)

"""
Strategy with the add to favourites button:
In both, you'll need an endpoint (function).

1. When the user clicks, the endpoint will add it to the user favourites list and render to some other/same page
2. Instead of refreshing, add an event listener to the button, when clicked, POST request, the endpoint returns JSON data, e.g. {'status': 'added'}

Recipes collection
{
    _id
    category_name
    recipe_name
    author: ObjectId(User)
    is_active: True/False
    ----- favourited_by: [ObjectId(User), ..., ObjectId(User)] --> Easier to delete but harder to query
}

User collection
{
    _id
    username
    password
    ----- favourites: [ObjectIds(Recipes), ..., ObjectIds(Recipes)], --> Easier to query but harder to delete
}

Deleting Recipes:
1. Add is_active: True/False to Recipes collection and when the author deletes it, simply set is_active to False
2. Check if the Recipe exists before rendering, if not, remove it from the list
3. When the author deletes it, get all users which have that ID in their favourites and delete it from there.

-------------------
1. Add a recipe page
2. Create endpoint to save the recipe to the database with the author
3. Work on the Homepage to display all recipes
4. Work on the profile to display only user recipes and ...
5. ...add functionality to update/delete a recipe


class FoodCategories:
        main_course = "main_course"
        soups = "soups"
        desserts = "desserts"

        @staticmethod
        def all_categories():
            return [FoodCategories.main_course, FoodCategories.soups, FoodCategories.desserts]

        @staticmethod
        def category_title(category_name):
            return category_name.replace('_', ' ').title()

@app.route("/")
@app.route("/get_recipes/<category>"). --> get_recipes/desserts
def get_recipes(category):
    recipes = list(mongo.db.recipes.find({'category_name': category}))
    return render_template("recipes.html", recipes=recipes, title=FoodCategories.category_title(category))

"""


@app.route("/")
@app.route("/get_recipes")
def get_recipes():
    recipes = list(mongo.db.recipes.find())
    return render_template("recipes.html", recipes=recipes)


@app.route("/registration", methods=["GET", "POST"])
def registration():
    if request.method == "POST":
        # checking does the username exists
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            flash("User already registered")
            return redirect(url_for("registration"))

        registration = {
            "username": request.form.get("username").lower(),
            "password": generate_password_hash(request.form.get("password"))
        }
        mongo.db.users.insert_one(registration)

        # adding new user to session 
        session["user"] = request.form.get("username").lower()
        flash("Your profile is created!")
        return redirect(url_for("user_profile", username=session["user"]))
    return render_template("registration.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            if check_password_hash(
                existing_user["password"], request.form.get("password")):
                    session["user"] = request.form.get("username").lower()
                    return redirect(url_for(
                        "user_profile", username=session["user"]))
            # checking credentials, if no match, back to login page
            else:
                flash("Credentials incorrect")
                return redirect(url_for("login"))

        else:
            flash("Credentials incorrect")
            return redirect(url_for("login"))

    return render_template("login.html")


#redirecting user to their profile
@app.route("/user_profile/<username>", methods=["GET", "POST"])
def user_profile(username):
    username = mongo.db.users.find_one(
        {"username": session["user"]})["username"]

    if session["user"]:
        return render_template("user_profile.html", username=username)
    #if not his profile, directing back to login page
    return redirect(url_for("login"))

# logout function    
@app.route("/logout")
def logout():
    flash("Logout successful")
    session.pop("user")
    return redirect(url_for("login"))

# adding a new recipe
@app.route("/add_recipe", methods=["GET", "POST"])
def add_recipe():
    if request.method == "POST":
        recipe_img = request.form.get("recipe_img") or url_for('static', filename='img/auto_img.jpg')
        recipe = {
            "recipe_name": request.form.get("recipe_name"),
            "category_name": request.form.get("category_name"),
            "recipe_img": recipe_img,
            "recipe_cuisine": request.form.get("recipe_cuisine"),
            "cooking_time": request.form.get("cooking_time"),
            "serving_nr": request.form.get("serving_nr"),
            "measure": request.form.get("measure"),
            "ing_amount": request.form.get("ing_amount"),
            "recipe_ing": request.form.get("recipe_ing"),
            "recipe_description": request.form.get("recipe_description"),
            "author": session["user"]
        }
        mongo.db.recipes.insert_one(recipe)
        flash("Recipe created")
        return redirect(url_for("get_recipes"))
    categories = mongo.db.categories.find().sort("category_number", 1)
    time = mongo.db.time.find().sort("cooking_number", 1)
    servings = mongo.db.servings.find().sort("serving_nr", 1)
    measures = mongo.db.measures.find().sort("measure_number", 1)
    print(len(measures))
    return render_template("add_recipe.html", categories=categories, time=time, servings=servings, measures=measures)

# see a single recipe function 
@app.route("/single_recipe/<recipe_id>")
def single_recipe(recipe_id):
    recipe = mongo.db.recipes.find_one({'_id': ObjectId(recipe_id)})
    return render_template("single_recipe.html", recipe=recipe)


# edit recipe function
@app.route("/edit_recipe/<recipe_id>", methods=["GET", "POST"])
def edit_recipe(recipe_id):
    recipe = mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})
    return render_template("edit_recipe.html", recipe=recipe)


# delete recipe function
@app.route("/delete_recipe/<recipe_id>")
def delete_recipe(recipe_id):
    mongo.db.recipes.remove({"_id": ObjectId(recipe_id)})
    flash ("Recipe deleted")
    return redirect(url_for("get_recipes"))


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
