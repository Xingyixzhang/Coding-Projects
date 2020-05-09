# This is a tryout project for CSS Animation
**[Useful Reference Link: CSS Animation](https://www.w3schools.com/css/css3_animations.asp)**

## Properties to Discuss:
### @keyframes rule (Animation within will gradually change from current style to the new style at certain times.)
- Bind the animation to an element.
- Set the animation-duration property. **IF NOT SPECIFIED, default: 0s, no animation will happen**.
```css
/* The animation code */
@keyframes example {
  from { background-color: red; }
  to { background-color: yellow; }
}

/* OR The animation code using percentage and position settings */
@keyframes example {
  0%   {background-color:red; left:0px; top:0px;}
  25%  {background-color:yellow; left:200px; top:0px;}
  50%  {background-color:blue; left:200px; top:200px;}
  75%  {background-color:green; left:0px; top:200px;}
  100% {background-color:red; left:0px; top:0px;}
}

/* The element to apply the animation to */
div {
  width: 100px;
  height: 100px;
  background-color: red;
  animation-name: example;
  animation-duration: 4s; /* for 4 seconds */
}
```
### animation-name
### animation-duration
### animation-delay (Specifies a delay for the start of an animation.)
```css
div {
  width: 100px;
  height: 100px;
  position: relative;
  background-color: red;
  animation-name: example;
  animation-duration: 4s;
  animation-delay: -2s;   /* Can be either positive or negative int. */
}
```
### animation-iteration-count
```css
div {
  width: 100px;
  height: 100px;
  position: relative;
  background-color: red;
  animation-name: example;
  animation-duration: 4s;
  animation-iteration-count: 3; /* Specifies the # of times an animation should run. */
  /* Infinite run: animation-iteration-count: 3; */
}
```
### animation-direction
- **normal** : The animation is played as normal (forwards). This is **default**
- **reverse** : The animation is played in reverse direction (backwards)
- **alternate** : The animation is played forwards first, then backwards
- **alternate-reverse** : The animation is played backwards first, then forwards
### animation-timing-function (Specifies the speed curve of the animation)
- **ease** : Specifies an animation with a slow start, then fast, then end slowly (this is default)
- **linear** : Specifies an animation with the same speed from start to end
- **ease-in** : Specifies an animation with a slow start
- **ease-out** : Specifies an animation with a slow end
- **ease-in-out** : Specifies an animation with a slow start and end
- **cubic-bezier(n,n,n,n)** : Lets you define your own values in a cubic-bezier function
### animation-fill-mode (Specifies a style for the target element when the animation isn't playing.)
- **none** : Default value. Animation will not apply any styles to the element before or after it is executing
- **forwards** : The element will retain the style values that is set by the last keyframe (depends on animation-direction and animation-iteration-count)
- **backwards** : The element will get the style values that is set by the first keyframe (depends on animation-direction), and retain this during the animation-delay period
- **both** : The animation will follow the rules for both forwards and backwards, extending the animation properties in both directions
### animation
```css
/* Transform the following animation effects to the shorthand animation property */
div {
  animation-name: example;
  animation-duration: 5s;
  animation-timing-function: linear;
  animation-delay: 2s;
  animation-iteration-count: infinite;
  animation-direction: alternate;
}

/* After using the shorthand animation property: */
div {
  animation: example 5s linear 2s infinite alternate;
}
```
