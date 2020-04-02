# OverView --
 
World Traveler Web App is to focus on practicing developing controllers. (Home, City, Traveler)

## Objectives --

- Add an MVC controller to a web application.
- Write actions in an MVC controller that respond to user operations.
- Add custom routes to a web application. 
- Write action filters that run code for multiple actions.

## Controller Notes:

### MVC Quick Overview -- Convention over Configuration

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

\** A Model Binder determines the values passed to action as parameters.
\** The action often creates a new instance of a model class.

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

Model Binders locate parameters in a 
  1) Posted Form
  2) Routing Values
  3) Query String
  4) Posted Files

An action is called if the name and type of a parameter from the request matches the declared parameter declared in the action method.
\* <Behind the Scenes> The model binder uses the RouteData Property -- Contains 'Value' Property and Encapsulate info about the route.

4. ViewBag & ViewData --> Pass Info to Views; ~~ Dictionary

ViewBag.Title = "Title";		ViewData["Title"] = "Title";
<p> Title is: @ViewBag.Title </p>	<p> Title is: @ViewData["Title"] </p>

\** Note that the calling methods for ViewBag and ViewData may be mix-matched.

### Configuring Routes

1. ASP.NET Core Routing Engine
   1) Routing governs the way URLs correspond to controllers and actions.
   	      NOT operate on the protocol, server, domain, or URL port#, 
	      But it does operate only on the directories and file name in the relative URL.
   2) Routing determines which controller and action should be called to handle a request.
   3) Routing Decides what Parameters to be passed to an action.
   4) A route is a RULE. Routes are Configurable: Centrally in the Startup.cs &| Locally by using Attributes.
   5) Routeing can link URLs and content more effectively.
   6) app.UseMvcWithDefaultRoute(); -- Adds MVC to the IApplicationBuilder request execution pipeline
                                       with a default route named default and the template: {controller=Home}/{action=Index}/{id?}.

2. Search Engine Optimization (SEO)
   1) Use a meaningful title element in the head section of the HTML. 
   2) Use accurate meta name="keywords" tag in the head element to include keywords that describe the content of the page 
   3) Use accurate meta name="description" tag in the head element to include a sentence that describes the content of the page
   4) Choose a domain name that includes keywords
   5) Use keywords in the h1, h2, h3 heading elements
   6) Ensure that URLs do not include Globally Unique Identifiers (GUIDs) or long query text 

3. Configuring Routes by Using Convention-Based Routing
   1) Use Convention-Based Routing by Defining routes in Startup.cs Configure Method.
   2) Convention-Based Routes may contain following properties: name, template, defaults, constraints, and dataTokens
   3) Example: app.UseMvc(routes =>
               {
	          routes.MapRoute(
		     name: "myRoute", // Assigns name to a route, NOT involved in Matching/Request Forwarding.
		     template: "{controller}/{action}/{param}", // URL pattern to determine if the route should be used.
		     defaults: new { controller = "Some", action = "ShowParam" },
		     constraints: new { param = "[0-9]+" },
		     dataTokens: new { locale = "en-US" });  // Specify the data tokens for the route, Containing a name and a value.
	       });
   4) If 404 errors received for every request (regardless of the relative URL), Check the ROUTES CONFIGURED in the app.
   5) Routes are evaluated in the order in which they are added.
   6) To fix a route to a single controller, apecify a value for the controller variable in the default property.
   
4. Using Routes to Pass Parameters
   1) Access the segment variables' values by 2 means: using the RouteData.Values collection / model binding  to pass values to action parameters.
   2) Example: - string id = (string)RouteData.Values["id"];   return Content("id: " + id); // Use RouteData.Values collection.
               - public IActionResult Print(string id) { }  // Use Model Binding.
      - string parameter: /Example/Print/1   relative URL <- the action returns: id: 1
                        - /Example/Print/    relative URL <- the action returns: id:
      - int parameter:    /Example/Print/1   relative URL <- the action returns: id: 1 
                        - /Example/Print/a   relative URL <- the action returns: id: 0 
			- /Example/Print     relative URL <- the action returns: id: 0 // int is a value type, cannot store null values
      - nullable parameter: /Example/Print/1 relative URL <- the action returns: id: 1
                          - /Example/Print/a relative URL <- the action returns: id: 
			  - /Example/Print   relative URL <- the action returns: id: 
      - optional parameter: /Example/Print/1 relative URL <- the action returns: id: 
                          - /Example/Print/a relative URL <- the action returns: id: 444 
			  - /Example/Print   relative URL <- the action returns: id: 444 

5. Configuring Routes by using Attributes
   1) ASP.NET Core MVC supports 2 types of routing: Convention-Based Routing and Attribute-Based Routing.
   2) Route Attribute -> specify the route for a specific action.
   3) Route Attribute can pass parameters to an action [Route("My/{param}")] (MyController, SomeMethod(string param))
   4)                 can get several segment variables [Route("My/{param1}/{param2:int}")] (.., SomeMethod(string param1, int param2))
   5)                 can configure a segment variable to be optional by using ? [Route("My/{param}/{param2?}")]
   6) All routes in a controller class should start with the SAME PREFIX.
   7) If a common Prefix is set on entire controller class by [Route] attribute above the class, /My/Method1 good; /Method1 will fail.
   8) Http[Verb] instead of [Route] -> Limit access to the action to a specific HTTP Verb. \* [Route] and [HttpVerb] can be combined.
      - Action to run only when HTTP verb is GET --> [HttpGet] Attribute
      - Action to run only when HTTP verb is POST --> [HttpPost] Attribute

### Writing Action Filters

1. Action Filters Overview
   1) MVC programming model enforces the Seperation of Concerns.
   2) Cross-Cutting Concerns -- where requirements are relavant to many parts of app and cut across logical boundaties.
   3) Cross-Cutting Concerns Examples -- Authorization, Logging, Caching.
   4) Filters are MVC classes used to manage cross-cutting concerns in the web app.
   5) Apply a filter to an action by annotating the action method w/ an appropriate attribute. (ex. [SimpleActionFilter])
   6) Filters run within a filter pipeline, Some Filter Types:
      - Authorization Filters: Run Before any other filters and Before the code in the action method. // Check User's Access Rights.
      - Resource Filters: Run After the Authorization Before any other. // Performance. IResourceFilter/IAsyncResourceFilter interface.
      - Action Filters: Run Before and After the code in the action method. // Manipulate parameters. IActionFilter/IAsyncActionFilter.
      - Exception Filters: Run only if an action or other filter throw an exception. // Handle Errors. I(Async)ExceptionFilter.
      - Result Filters: Run Before and After an action result is run. // IResultFilter or IASyncResultFilter interface implemented.
      -> Authorization -> Resource -> Model Binding -> Action ->Exception -> Result -> Result Execution
   7) Create custom filter classes/ Use existing filter classes.

2. Create and Use Action Filters
```cs
public class SimpleActionFilter: ActionFilterAttribute
{
   public override void OnActionExecuting (ActionExecutingContextfilterContext) { 
      Debug.WriteLine("This Event Fired: OnActionExecuting"); //before the action is run 
   }
   public override void OnActionExecuted(ActionExecutedContextfilterContext) { 
      Debug.WriteLine("This Event Fired: OnActionExecuted"); //after the action is run 
   }
   public override void OnResultExecuted(ResultExecutedContextfilterContext) { 
      Debug.WriteLine("This Event Fired: OnResultExecuted");//after the result is returned 
   }
   // there is also OnResultExecuting…
}
```
*A more common scenario would be to write messages to a log file. Check: Visual Studio Output Window ==============
```cs
namespace MvcApplication1.ActionFilters
{
     public class LogActionFilter : ActionFilterAttribute
     {
          public override void OnActionExecuting(ActionExecutingContext filterContext)
          {
               Log("OnActionExecuting", filterContext.RouteData);       
          }
          public override void OnActionExecuted(ActionExecutedContext filterContext)
          {
               Log("OnActionExecuted", filterContext.RouteData);       
          }
          public override void OnResultExecuting(ResultExecutingContext filterContext)
          {
               Log("OnResultExecuting", filterContext.RouteData);       
          }
          public override void OnResultExecuted(ResultExecutedContext filterContext)
          {
               Log("OnResultExecuted", filterContext.RouteData);       
          }
          private void Log(string methodName, RouteData routeData)
          {
               var controllerName = routeData.Values["controller"];
               var actionName = routeData.Values["action"];
               var message = String.Format("{0} controller:{1} action:{2}", methodName, controllerName, actionName);
               Debug.WriteLine(message, "Action Filter Log");
          }
     }
}
```
```cs
namespace MvcApplication1.Controllers
{
     [LogActionFilter]
     public class HomeController : Controller
     {
          public ActionResult Index()
          {
               return View();
          }
          public ActionResult About()
          {
               return View();
          }
     }
}
```
### Common Issue and Troubleshooting Tip

1. Issue: Navigate to an existing action though get an HTTP 404 Not Found Error. --> A Configuration-Based Route never took effect.
2. Troubleshooting tip: 
   Verify that the routes are configured correctly in the MVC app.
   Ensure to Add Configuration-Based Routes in the correct ORDER.
   Generally speaking, the most specific routes should be added FIRST and the lease specific should be added LAST.
