# Overview
General Information of listed cities in the world, including their population, MiniMap, and TimeZone.
# Objectives
- Add an MVC view to a web application.
- Use Razor to differentiate server-side code from HTML code.
- Write HTML code and tag helpers in a view.
- Add partial views and view components.
# Views Notes 
## A View = HTML markup + C# code, runs on the web server.
![simple drawing of MVC](https://github.com/Xingyixzhang/Coding-Projects/blob/master/Cities%20Info%20Worldwide/MVC.png "MVC drawing")
## Create Views with Razor Syntax
1. Define the UI by Creating views, using various helper classes built into MVC.
2. By convention, all views reside in Views folder.
                  within the Views folder, Each Controller has its own folder.
3. Razor view engine + C# --> .cshtml 

- A **View Engine** is a MVC Framework component responsible for:
1. **Locate** view files;
2. **Run** server-side code that view files contain;
3. **Render** HTML that the browser can display to the user.

**RazorView(HTML + C#) \-> View Engine \-> Browser(Pure HTML)**

Razor comment will not be rendered by the Razor view Engine.
if you want the comment to go to the user side but not showing to the user, use html comments. Razor comment won't go to the other side at all even when viewing the site in developer mode.

Razor view engine is one type of view engines, which translate the HTML + C# into pure HTML for the browser
**Razor** is the **Default** view engine in MVC, Razor view engine can be customized:
1. Implement **IViewEngine** interface, which contains **FindView** method returning a **ViewEngineResult** object.
2. Custom View Engines are **rarely created** since they require sophisticated string parsing code.

- '@@': render the @ symbol to display in html page.
- '@:': explicitly declare a line of text as **content** not **code**, (\<text>\</text>)
- '@Model.price * 1.2': Implicit code expression \-> "2.00 * 1.2"
- '@(Model.price * 1.2)': Explicitly delimit expression \-> "2.40"
- '@ { ... }': write multiple lines of server-side code:
```cshtml
@ {
    // Razor interpretes all text here as server-side code.
}
@ {
    int i = 5, j = 6;
    @if (i < j){      // A razor if code block.
        ...
        @i
    }
}
@* Razor Froeach Code Block: *@
@foreach (string name in ViewBag.Names){
    <span>@name </span>
}
```
- **Dependency Injection** into Views:
1. Injecting a service directly into a view using "**@inject** \<type> \<instance name>" directive.
2. Compare injecting services into Views and Controllers:

|               |             **Views**             |             **Controllers**             |
|---------------|-----------------------------------|-----------------------------------------|
|               |     Transform ot format text      |              Retrieve Data              |
| Services that |     Impact Visual Appearance      |       Depend on external resources      |
|               | Required for repeated use in view |  Return consistent results for one view |
## Use HTML Helpers and Tag Helpers
- HTML Helpers
**Html.ActionLink** & **Url.Action** helpers render HTML that **calls controller actions**.
1. **Html.ActionLink()** \-> [Does not require Explicit enabling of the feature]
```cshtml
@Html.ActionLink("Click here to view photo 1", "Display", new {id = 1})
@*
  <a href="/photo/display/1">
      Click here to view photo 1
  </a>
*@
```
2. **Url.Action()**: Alternative to HTML helpers. \-> [Require Explicit directive usage]
```cshtml
@* This renders a URL by using the routing engine without rendering the enclosing <a> element. *@
<img alt="This image came from an action" src="@Url.Action("GetImage", new {id = 1})" />
@*
    <img alt="This image came from an action" src="/photo/getimage/1" />
*@
```
- Tag Helpers
## Reuse Code in Views
