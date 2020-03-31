# Overview

General Information of listed cities in the world, including their population, MiniMap, and TimeZone.

# Objectives
- Add an MVC view to a web application.
- Use Razor to differentiate server-side code from HTML code.
- Write HTML code and tag helpers in a view.
- Add partial views and view components.

# Views Notes

## Overview -- A View = HTML markup + C# code, runs on the web server.
## Adding Views --

1. Define the UI by Creating views, using various helper classes built into MVC.
2. By convention, all views reside in Views folder.
                  within the Views folder, Each Controller has its own folder.
3. Razor view engine + C# --> .cshtml 

Razor comment will not be rendered by the Razor view Engine.
if you want the comment to go to the user side but not showing to the user, use html comments. Razor comment won't go to the other side at all even when viewing the site in developer mode.

razor view engine is one type of view engines, which translate the HTML + C# into pure HTML for the browser
Razor view engine can be customized.

