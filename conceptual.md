### Conceptual Exercise

Answer the following questions below:

- What are important differences between Python and JavaScript?

- Given a dictionary like ``{"a": 1, "b": 2}``: , list two ways you
  can try to get a missing key (like "c") *without* your programming
  crashing.

- What is a unit test?

- What is an integration test?

- What is the role of web application framework, like Flask?

- You can pass information to Flask either as a parameter in a route URL
  (like '/foods/pretzel') or using a URL query param (like
  'foods?type=pretzel'). How might you choose which one is a better fit
  for an application?

- How do you collect data from a URL placeholder parameter using Flask?

- How do you collect data from the query string using Flask?

- How do you collect data from the body of the request using Flask?

- What is a cookie and what kinds of things are they commonly used for?

- What is the session object in Flask?

- What does Flask's `jsonify()` do?


### **Answers**

- Python follows an object-oriented programming style and it's easier to read because of its clear syntax. JavaScript is primarily event-driven and is essential for developing interactive web pages.
- For a Python dictionary like **`{"a": 1, "b": 2}`**, there are a couple of ways to safely access a missing key:
    1. Use the dictionary's **`get`** method: **`value = dict.get('c', default_value)`**.
    2. Use a try/except block:
        
        ```
        pythonCopy code
        try:
          value = dict['c']
        except KeyError:
          value = default_value
        
        ```
        
- A unit test is a type of test that checks the correctness of an isolated piece of code (usually a single function or method). They are used to verify that individual units of code are working as expected.
- An integration test is a type of test that checks the interactions between different pieces of code or system components. They are used to catch bugs in the interactions between these components.
- A web application framework like Flask provides a structured way to build web applications. It provides libraries for database access, templating, routing, and session management, among others, allowing developers to focus more on application logic rather than low-level details.
- Whether to use a route URL parameter (like '/foods/pretzel') or a URL query parameter (like 'foods?type=pretzel') depends on the specific requirements of the application. If the data is essential for the resource's identity, use a route parameter. If the data is optional, or used to filter or sort resources, use a query parameter.
- To collect data from a URL placeholder parameter in Flask, you include the parameter in the route decorator and the function definition. For example:
    
    ```
    pythonCopy code
    @app.route('/foods/<food_item>')
    def get_food(food_item):
        # Now you can use food_item
    
    ```
    
- To collect data from the query string in Flask, you can use the **`request`** object's **`args`** property, which returns a dictionary of the query string parameters. For example, for 'foods?type=pretzel', you could get the type with **`request.args.get('type')`**.
- To collect data from the body of a request in Flask, you use the **`request`** object's **`get_json`** method, which parses the request body as JSON and returns a Python dictionary.
- A cookie is a small piece of data stored on the user's browser by the web server. They are commonly used for maintaining session information, tracking user's browsing activities, and storing user preferences.
- The session object in Flask is a feature that allows you to store information specific to a user from one request to the next. It is a way to remember information between HTTP requests.
- Flask's **`jsonify()`** is a function that turns Python dictionaries, arrays, strings, and other data types into a JSON-formatted response, which can then be returned by a Flask view function. This is useful when building APIs that should return JSON.