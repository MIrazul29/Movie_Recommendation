# Movie_Recommendation
This is a web application for recommending movies based on user preferences. It uses collaborative filtering to suggest movies that are similar to the ones a user has liked in the past. The website has a simple and intuitive user interface that allows users to create an account, rate movies, and get personalized recommendations.
![image](https://user-images.githubusercontent.com/81968951/225115452-c6749718-8560-4634-be62-352d168a19c1.png)

# Installation
To install and run this web application on your local machine, follow these steps:

1. Clone this repository to your local machine using git clone.
2. Install the required dependencies using pip install -r requirements.txt.
3. Create a new database and run the migrations using python manage.py migrate.
4. Load the sample movie data using python manage.py loaddata movies.json.
5. Start the web application using python manage.py runserver.
Usage
6. To use the web application, simply open a web browser and navigate to the URL where the application is hosted (http://localhost:8000/ by default). You will be prompted to create a new account or log in if you already have one.

Once you are logged in, you can rate movies by giving them a score from 1 to 5 stars. Based on your ratings, the application will recommend movies that you might like. You can view your personalized recommendations by clicking the "Recommendations" link in the navigation bar.

# Development
This web application was built using FLASK and Python. The front-end uses HTML, CSS, and JavaScript. If you would like to contribute to the development of this project, you can follow these steps:

1. Fork this repository to your own GitHub account.
2. Clone the forked repository to your local machine using git clone.
3. Create a new branch for your changes using git checkout -b feature/your-feature-name.
4. Make your changes and commit them to your branch using git commit -m "Your commit message".
5. Push your changes to your forked repository using git push origin feature/your-feature-name.
6. Open a pull request to merge your changes into the original repository.

 Authors:
 ```
Khondoker Mirazul Mumenin
```
