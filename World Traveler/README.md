# OverView --
 
World Traveler Web App is to focus on practicing developing controllers. (Home, City, Traveler)

## Objectives --

- Add an MVC controller to a web application.
- Write actions in an MVC controller that respond to user operations.
- Add custom routes to a web application. 
- Write action filters that run code for multiple actions.

## Controller Notes:

### MVC Quick Overview

1. Controller: (A class containing actions (public methods))
   1) Responsible for processing a web request by interacting with the model, then pass the result to the view.
   2) MVC apps use the URL Routing to find which controller and action to handle the request.

2. Model: (Sometimes referred to as the "Domain")
   1) Business Layer, including data objects, app logic, and business rules.
   2) Examples: Product, User, Photo ...

3. View:
   Uses the data retrieved from the controller to produce HTML/ other output to get sent back to the browser.

### Writing Controllers and Actions

1. Responding to User Requests

Web Browser --request--> Controller Object Instantiated --> *Action Method Selected* --model object--> View --HTML/o*--> Browser.

** A Model Binder determines the values passed to action as parameters.
** The action often creates a new instance of a model class.

2. Writing Controller Actions

Actions returns objects that implement the IActionResult interface.
	Ex. View() --> Create and Return a ViewResult object(inherits from the ActionResult class that implements the IAction Interface).
Action Result Return Types:
	1) ViewResult -- Corresponding View() template, which will generate the output sent to the browser.
	2) ContentResult -- Returns text(plain, XML, Comma-Seperated Table...) to the browser
	3) RedirectToActionResult -- Returns HTTP302 response to the browser, causing the browser to send the request to another method.
	4) RedirectToRouteResult -- Redirect the browser to another route, which can be passed in the RedirectToRouteResult class's constructor.
	5) StatusCodeResult -- Returns an action result w/ a specific HTTP response status code and description.

3. Using Parameters

Model Binders locate parameters in a 1) Posted Form
				     2) Routing Values
				     3) Query String
				     4) Posted Files
An action is called if the name and type of a parameter from the request matches the declared parameter declared in the action method.
* <Behind the Scenes> The model binder uses the RouteData Property -- Contains 'Value' Property and Encapsulate info about the route.


4. ViewBag & ViewData --> Pass Info to Views; ~~ Dictionary

ViewBag.Title = "Title";		ViewData["Title"] = "Title";
<p> Title is: @ViewBag.Title </p>	<p> Title is: @ViewData["Title"] </p>

** Note that the calling methods for ViewBag and ViewData may be mix-matched.

### Configuring Routes

1. ASP.NET Core Routing Engine

   1) Routing determines which controller and action should be called to handle a request.
   2) Routing Decides what Parameters to be passed to an action.
   3) A route is a RULE. Routes are Configurable: Centrally in the Startup.cs &/| Locally by using Attributes.
   4) Routeing can link URLs and content more effectively.

2. Search Engine Optimization

3. Configuring Routes by Using Convention-Based Routing

4. Using Routes to Pass Parameters

5. COnfiguring Routes by using Attributes

### Writing Action Filters

1. Action Filters Overview

2. Create and Use Action Filters

### Common Issue and Troubleshooting Tip

1. Issue: Navigate to an existing action though get an HTTP 404 Not Found Error. --> A Configuration-Based Route never took effect.
2. Troubleshooting tip: Verify that the routes are configured correctly in the MVC app.
		    	Ensure to Add Configuration-Based Routes in the correct ORDER.
			Generally speaking, the most specific routes should be added FIRST and the lease specific should be added LAST.
