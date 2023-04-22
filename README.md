# Restaurants for US cities Web App

This project is a basic web application that provides information about US cities and visualizes restaurant data for different cities. The app uses various programming techniques such as data caching, web scraping, SQLite, Unit Testing, Plotly, and Flask.

## Data Sources

1. **Wikipedia** - Source of the "Cities" table in the database. [Link](https://en.wikipedia.org/wiki/List_of_United_States_cities_by_population)
2. **Yelp Fusion** - Source of the "Restaurants" table in the database. [Link](https://www.yelp.com/developers/documentation/v3/business_search)

## Getting Started

### 1. Obtain Yelp Fusion API Key
1. Visit [Yelp API Authentication](https://www.yelp.com/developers/documentation/v3/authentication) and follow the instructions to create your app and get an API key.
2. Create a new Python file named `secret.py` in the same folder as `program.py` and add the following code:
```
API_KEY = '<your key>'
```  
### 2. Install required packages
```
$ pip install -r requirements.txt --user
```  

### 3. Run the web application  
```  
$ python program.py
```  
### 4. Open "http://127.0.0.1:5000/ " in a browser
