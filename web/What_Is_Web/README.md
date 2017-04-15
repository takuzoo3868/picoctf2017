<!-- This markdown file is writeup template. -->

## What Is Web 20pt

### Problem
> Someone told me that [some guy](https://en.wikipedia.org/wiki/Tim_Berners-Lee) came up with the "World Wide Web", using "HTML" and "stuff". Can you help me figure out what that is? [Website](http://shell2017.picoctf.com:58191/).

### Answer
Look in the source code with the browser developer tool (`F12 > Sources`). We found the split flags in html, css, and Javascript.

```html
<!DOCTYPE html>
<html>
<head>
<title>Hello World!</title>
<link rel="stylesheet" type="text/css" href="hacker.css">
</head>
<body>

HI MOM! LOOK WHAT I MADE!

<h1>I used some tags.</h1>
<p>More tags!</p>
<h3>I typed here.</h3>

This is my cat. He is nice.
<br><br>
<img src="./cat.jpg" alt="Cat" /img>

<button type="button" onclick="sayHI()"> Click me to say hello!</button>

<script src="script.js"></script>

</body>
</html>

<!-- Cool! Look at me! This is an HTML file. It describes what each page contains in a format your browser can understand. -->
<!-- The first part of the flag (there are 3 parts) is 4eabea7c5b1 -->
<!-- What other types of files are there in a webpage? -->
```

```css
/*
This is the css file. It contains information on how to graphically display
the page. It is in a seperate file so that multiple pages can all use the same 
one. This allows them all to be updated by changing just this one.
The second part of the flag is e8e0c84cc61 
*/
```

```javascript
/* This is a javascript file. It contains code that runs locally in your
 * browser, although it has spread to a large number of other uses.
 *
 * The final part of the flag is 2a79d2dc833
 */


function sayHI(){
	alert("Hi there!");
}
```

### Flag
4eabea7c5b1e8e0c84cc612a79d2dc833

