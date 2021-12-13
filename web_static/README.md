__Learn how to manipulate HTML and CSS languages__

AirBnB clone - Web static
==========================
<p>
![alt text](https://s3.amazonaws.com/intranet-projects-files/concepts/74/hbnb_step1.png)
</p>

## Web static, what???
```
Now having a command interpreter for managing your AirBnB objects, it’s time to make them alive!

Before developing a big and complex web application, we will build the front end step-by-step.

The first step is to “design” / “sketch” / “prototype” each element:

Create simple HTML static pages
* Style guide
* Fake contents
* No Javascript
* No data loaded from anything
```

[What is HTML](#HTML/CSS)

[How to create an HTML page](#HTML_steps)

[What is a markup language](#markup_language)

[What is the DOM](#DOM)

[What is an element / tag](#element/tag)

[What is an attribute](#Atributes)

[How does the browser load a webpage](#load_webpage)

[What is CSS](#CSS)

[How to add style to an element](#Style_element)

[What is a class](#Class)

[What is a selector](#Selectors)

[How to compute CSS Specificity Value](#CSS_specifics)

[What are Box properties in CSS](#Box_properties)


>Learn everything in 15 min?!?!
>>**Skim through all this information beloww and your a MASTER....**
>:alien:


Learn to Code HTML & CSS 🤌🏽 <a name="HTML/CSS"></a>
-------------
> Develop & Style Websites 

* The HTML is ***HyperText Markup Language***, is the standard markup language for documents designed to be displayed in a web browser.
In other words, the text on a web page is “marked up” with these codes to give the web browser instructions about how to display the text.
which means that it is written with codes readable by a person without it needing to be compiled first.

<p>
HTML is the structure of your page, it should be the first thing to write.
CSS is the styling of your page, the design. make sure to fix your HTML part before starting the styling.
Indeed, without any structure, you can’t apply any design.
</p>


How to create an [HTML page](https://www.tutorialrepublic.com/html-tutorial/html-get-started.php)<a name="HTML_steps"></a>
-----------------------------

* An HTML file is simply a text file saved with an .html or .htm extension.
>Getting Started:

To begin coding HTML you need only two stuff: a simple-text editor and a web browser.

![picture alt](https://learn.shayhowe.com/assets/images/courses/html-css/getting-to-know-html/building-structure.png)

[Document Structure example](https://learn.shayhowe.com/html-css/building-your-first-web-page/#html-document-structure):

```
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <title>Hello World</title>
  </head>
  <body>
    <h1>Hello World</h1>
    <p>This is a web page.</p>
  </body>
</html>
```

What is a markup language<a name="markup_language"></a>
--------------------------
<p>
A markup language is a computer language that uses tags to define elements within a document. It is human-readable, meaning markup files contain standard words, rather than typical programming syntax.While several markup languages exist, the two most popular are HTML and XML.. HTML is a markup language used for creating webpages.The contents of each webpage are defined by HTML tags.
</p>

What is the [DOM](http://cf.ppt-online.org/files/slide/l/lG6hjyFR8carDYH7oVAtPW3exEOg0sSpQ1JKfm/slide-4.jpg) <a name="DOM"></a>
------------------

<p>
When a web page is loaded, the browser creates a **Document Object Model** of the page.

The *HTML DOM* model is constructed as a tree of *Objects*:

![alt text](https://www.w3schools.com/js/pic_htmltree.gif)
</p>

What is an [element](https://www.w3schools.com/tags/default.asp) / [tag](https://www.w3schools.com/tags/default.asp)<a name="element/tag"></a>
-------------------------
<p>
Technically, an ***HTML element*** is the collection of start tag, its attributes, an end tag and everything in between.
An ***HTML tag*** (either opening or closing) is used to mark the start or end of an element.
The terms HTML *element* and HTML *tag* are interchangeable
i.e. a tag is an element and element is a tag.
For simplicity's sake, the terms "tag" and "element" ***are*** used to mean ***the same thing*** ***as it will define something on your web page***.

* Element : An HTML element is an individual component of an HTML document.It represents semantics, or meaning.
  * An element is the basic building block of HTML and is typically made up of two tags: an opening tag and a closing tag.
  * It can also contain attributes that defines its additional properties.

|**Block elements**|Types|*Self Closing Elements*|
|-----|:-----:|:-:|
| **X**|`<div>` *(divisions)*|No|
| **X**|`<p>` *(paragraphs)* |No|
|**X**|`<h1>`-`<h6>` *(Multiple Headings)*|No|
| | `<form>`|
| | `<ol>`|
| |`<ul>`|
| | `<li>`|
|**Inline elements**|Types |*Self Clossing*|
|*Inline elements typically may only contain text and other inline elements.*|------|---------------|
||`<img>`|**X**|
|An anchor link|`<a>...</a>`|
|spans|`<span>`|
|strong element|`<strong>`|
||`<b>`|
|emphasized pieces of text|`<em>`|**X**|
||`<i>`|
||`<code>`|
||`<input>`|
||`<button>`|

> *Generally, block-level elements may contain inline elements and other block-level elements.* *For example, paragraph element (`<p>`), headings (`<h1>` to `<h6>`), divisions (`<div>`) etc.*

</p>

What is an [attribute](https://www.tutorialrepublic.com/html-tutorial/html-attributes.php)<a name="Atributes"></a>
-------------------------
<p>
Attributes are properties used to provide additional information about an element.
They define additional characteristics or properties of the element such as width and height of an image.

  * Provide additional information about elements
  * all HTML elements can have attributes
  * are always specified in the start tag (or opening tag)
  * and usually consists of name/value pairs like `name="value"`

Attribute values should always be enclosed in quotation marks.

Some attributes are required for certain elements. For instance, an `<img>` tag must contain a `src` and `alt` attributes.
</p>

|**Atributes**|Types |
|-------------|:------:|
|identifies an element|`id `|
|classifies an element|`class`|
|specifies a source for embeddable content|`src`|
|provides a hyperlink reference to a URL of the page linked resource.|`href`|

Summary: All HTML elements can have attributes:

* The `href` attribute of `<a>` specifies the URL of the page the link goes to
* The `src` attribute of `<img>` specifies the path to the image to be displayed
* The `width` and `height` attributes of `<img>` provide size information for images
* The `alt` attribute of `<img>` provides an alternate text for an image
* The `style` attribute is used to add styles to an element, such as color, font, size, and more
* The `lang` attribute of the `<html>` tag declares the language of the Web page
* The `title` attribute defines some extra information about an element

How does the browser load a webpage<a name="load_webpage"></a>
------------------------------------
<p>
First, we need to understand what **DOM** is.
When a browser sends a request to a server to fetch an HTML document, the server returns an HTML page in binary stream format which is basically a text file with the response header `Content-Type` set to the `value text/html; charset=UTF-8`.
</p>

What is CSS<a name="CSS"></a>
--------------
<p>
Cascading Style Sheets is a style sheet language used for describing the presentation of a document written in a markup language such as HTML. CSS is a cornerstone technology of the World Wide Web, alongside HTML and JavaScript. CSS is designed to enable the separation of **presentation and content, including layout, colors, and fonts**.
</p>


How to add style to an element<a name="Style_element"></a>
-------------------------------
The HTML style attribute is used to add styles to an element, such as color, font, size, and more.
[HTML Style Attribute](https://www.w3schools.com/html/html_styles.asp)

What is a class<a name="Class"></a>
------------------
<p>
The class attribute is often used to point to a class name in a style sheet.
</p>

What is a selector<a name="Selectors"></a>
---------------------
CSS Selectors & Properties:
![picture alt](https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Ftse4.mm.bing.net%2Fth%3Fid%3DOIP.-dGRwLxF4NL1ojR79fVX3wHaER%26pid%3DApi&f=1)


How to compute CSS Specificity Value<a name="CSS_specifics"></a>
-------------------------------------
<p>
If there are two or more conflicting CSS rules that point to the same element, the browser follows some rules to determine which one is most specific and therefore wins out.

Think of specificity as a score/rank that determines which style declarations are ultimately applied to an element.

The universal selector (`*`) has low specificity, while ID selectors are highly specific!
</p>

[Specificity Hiherarchy](https://www.w3schools.com/css/css_specificity.asp)

What are Box properties in CSS<a name="Box_properties"></a>
--------------------------------
<p>
Every element that can be displayed on a web page is comprised of one or more rectangular boxes. CSS box model typically describes how these rectangular boxes are laid out on a web page.

![alt text](https://www.tutorialrepublic.com/lib/images/css-box-model.png)


These boxes can have different properties and can interact with each other in different ways, but every box has a content area and optional surrounding padding, border, and margin areas.
</p>

Resources
============

**Read or watch:**

* [Learn to Code HTML & CSS](https://learn.shayhowe.com/html-css/) (until “Creating Lists” included)
* [Inline Styles in HTML](https://www.codecademy.com/articles/html-inline-styles)
* [Specifics on CSS Specificity](https://css-tricks.com/specifics-on-css-specificity/)
* [CSS SpeciFishity](http://www.standardista.com/wp-content/uploads/2012/01/specificity3.pdf)
* [Introduction to HTML](https://developer.mozilla.org/en-US/docs/Learn/HTML/Introduction_to_HTML)
* [CSS](https://developer.mozilla.org/en-US/docs/Learn/CSS)
  * [Why is CSS so wierd](https://www.youtube.com/watch?v=aHUtMbJw8iA)
  * [CSS Intro](https://www.w3schools.com/Css/css_intro.asp)
* [MDN](https://developer.mozilla.org/en-US/)
* [center boxes](https://css-tricks.com/centering-css-complete-guide/)
  * [CSS Box Model](https://www.tutorialrepublic.com/css-tutorial/css-box-model.php) (*Very Detailed*)

**General Rules**
----------------------
```
Allowed editors: `vi`, `vim`, `emacs`
All your files should end with a new line
A `README.md` file, at the root of the folder of the project, is mandatory
Your code should be W3C compliant and validate with [W3C-Validator](https://github.com/holbertonschool/W3C-Validator)
All your CSS files should be in `styles` folder
All your images should be in `images` folder
You are not allowed to use `!important` and `id` (`#...` in the CSS file)
You are not allowed to use tags `img`, `embed` and `iframe`
You are not allowed to use Javascript
Current screenshots have been done on `Chrome 56` or more.
No cross browsers
You have to follow all requirements but some `margin/padding` are missing - you should try to fit as much as you can to screenshots
```

<p align="center"> AUTHOR </p>

<h3 align="center">Made by Johanne Lopez</h3>

