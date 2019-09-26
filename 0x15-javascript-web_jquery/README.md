0. No jQuery mandatory
Write a Javascript script that updates the text color of the HTML tag HEADER to red (#FF0000):

You must use document.querySelector to select the HTML tag
You can’t use the jQuery API
Please test with this HTML file in your browser:

guillaume@ubuntu:~/0x15$ cat 0-main.html 
<!DOCTYPE html>
<html lang="en">
  <head>
    <title>Holberton School</title>
  </head>
  <body>
    <header> 
      First HTML page
    </header>
    <footer>
      Holberton School - 2017
    </footer>
    <script type="text/javascript" src="0-script.js"></script>
  </body>
</html>
guillaume@ubuntu:~/0x15$ 
Repo:

GitHub repository: holbertonschool-higher_level_programming
Directory: 0x15-javascript-web_jquery
File: 0-script.js

1. With jQuery mandatory
Write a Javascript script that updates the text color of the HTML tag HEADER to red (#FF0000):

You can’t use document.querySelector to select the HTML tag
You must use the jQuery API
Please test with this HTML file in your browser:

guillaume@ubuntu:~/0x15$ cat 1-main.html 
<!DOCTYPE html>
<html lang="en">
  <head>
    <title>Holberton School</title>
    <script src="https://code.jquery.com/jquery-3.2.1.min.js"></script>
  </head>
  <body>
    <header> 
      First HTML page
    </header>
    <footer>
      Holberton School - 2017
    </footer>
    <script type="text/javascript" src="1-script.js"></script>
  </body>
</html>
guillaume@ubuntu:~/0x15$ 
Repo:

GitHub repository: holbertonschool-higher_level_programming
Directory: 0x15-javascript-web_jquery
File: 1-script.js

2. Click and turn red mandatory
Write a Javascript script that updates the text color of the HTML tag HEADER to red (#FF0000) when the user clicks on the tag DIV#red_header:

You can’t use document.querySelector to select the HTML tag
You must use the jQuery API
Please test with this HTML file in your browser:

guillaume@ubuntu:~/0x15$ cat 2-main.html 
<!DOCTYPE html>
<html lang="en">
  <head>
    <title>Holberton School</title>
    <script src="https://code.jquery.com/jquery-3.2.1.min.js"></script>
  </head>
  <body>
    <header> 
      First HTML page
    </header>
    <div id="red_header">Red header</div>
    <footer>
      Holberton School - 2017
    </footer>
    <script type="text/javascript" src="2-script.js"></script>
  </body>
</html>
guillaume@ubuntu:~/0x15$ 
Repo:

GitHub repository: holbertonschool-higher_level_programming
Directory: 0x15-javascript-web_jquery
File: 2-script.js

3. Add `.red` class mandatory
Write a Javascript script that adds the class red to the HTML tag HEADER to red (#FF0000) when the user clicks on the tag DIV#red_header:

You can’t use document.querySelector to select the HTML tag
You must use the jQuery API
Please test with this HTML file in your browser:

guillaume@ubuntu:~/0x15$ cat 3-main.html 
<!DOCTYPE html>
<html lang="en">
  <head>
    <title>Holberton School</title>
    <script src="https://code.jquery.com/jquery-3.2.1.min.js"></script>
    <style>
      .red {
        color: #FF0000;
      }
    </style>
  </head>
  <body>
    <header> 
      First HTML page
    </header>
    <div id="red_header">Red header</div>
    <footer>
      Holberton School - 2017
    </footer>
    <script type="text/javascript" src="3-script.js"></script>
  </body>
</html>
guillaume@ubuntu:~/0x15$ 
Repo:

GitHub repository: holbertonschool-higher_level_programming
Directory: 0x15-javascript-web_jquery
File: 3-script.js

4. Toggle classes mandatory
Write a Javascript script that toggles the class of the HTML tag HEADER to red (#FF0000) when the user clicks on the tag DIV#toggle_header:

The HEADER tag must always have one class: red or green, never both in the same time, never empty.
If the current class is red, when the user click on DIV#toggle_header, the class must be updated to green ; and the reverse.
You can’t use document.querySelector to select the HTML tag
You must use the jQuery API
Please test with this HTML file in your browser:

guillaume@ubuntu:~/0x15$ cat 4-main.html 
<!DOCTYPE html>
<html lang="en">
  <head>
    <title>Holberton School</title>
    <script src="https://code.jquery.com/jquery-3.2.1.min.js"></script>
    <style>
      .red {
        color: #FF0000;
      }
      .green {
        color: #00FF00;
      }
    </style>
  </head>
  <body>
    <header class="green"> 
      First HTML page
    </header>
    <div id="toggle_header">Toggle header</div>
    <footer>
      Holberton School - 2017
    </footer>
    <script type="text/javascript" src="4-script.js"></script>
  </body>
</html>
guillaume@ubuntu:~/0x15$ 
Repo:

GitHub repository: holbertonschool-higher_level_programming
Directory: 0x15-javascript-web_jquery
File: 4-script.js

5. List of elements mandatory
Write a Javascript script that adds a LI element to a list when the user clicks on the tag DIV#add_item:

The new element must be: <li>Item</li>
The new element must be added to UL.my_list
You can’t use document.querySelector to select the HTML tag
You must use the jQuery API
Please test with this HTML file in your browser:

guillaume@ubuntu:~/0x15$ cat 5-main.html 
<!DOCTYPE html>
<html lang="en">
  <head>
    <title>Holberton School</title>
    <script src="https://code.jquery.com/jquery-3.2.1.min.js"></script>
  </head>
  <body>
    <header> 
      First HTML page
    </header>
    <br />
    <div id="add_item">Add item</div>
    <br />
    <ul class="my_list">
      <li>Item</li>
    </ul>
    <footer>
      Holberton School - 2017
    </footer>
    <script type="text/javascript" src="5-script.js"></script>
  </body>
</html>
guillaume@ubuntu:~/0x15$ 
Repo:

GitHub repository: holbertonschool-higher_level_programming
Directory: 0x15-javascript-web_jquery
File: 5-script.js

6. Change the text mandatory
Write a Javascript script that updates the text of the HTML tag HEADER to “New Header!!!” when the user clicks on DIV#update_header

You can’t use document.querySelector to select the HTML tag
You must use the jQuery API
Please test with this HTML file in your browser:

guillaume@ubuntu:~/0x15$ cat 6-main.html 
<!DOCTYPE html>
<html lang="en">
  <head>
    <title>Holberton School</title>
    <script src="https://code.jquery.com/jquery-3.2.1.min.js"></script>
  </head>
  <body>
    <header> 
      First HTML page
    </header>
    <br />
    <div id="update_header">Update the header</div>
    <br />
    <footer>
      Holberton School - 2017
    </footer>
    <script type="text/javascript" src="6-script.js"></script>
  </body>
</html>
guillaume@ubuntu:~/0x15$ 
Repo:

GitHub repository: holbertonschool-higher_level_programming
Directory: 0x15-javascript-web_jquery
File: 6-script.js

7. Star wars character mandatory
Write a Javascript script that fetches and replaces the name of this URL: https://swapi.co/api/people/5/?format=json

The name must be displayed in the HTML tag DIV#character
You can’t use document.querySelector to select the HTML tag
You must use the jQuery API
Please test with this HTML file in your browser:

guillaume@ubuntu:~/0x15$ cat 7-main.html 
<!DOCTYPE html>
<html lang="en">
  <head>
    <title>Holberton School</title>
    <script src="https://code.jquery.com/jquery-3.2.1.min.js"></script>
  </head>
  <body>
    <header> 
      Star Wars character
    </header>
    <br />
    <div id="character"></div>
    <br />
    <footer>
      Holberton School - 2017
    </footer>
    <script type="text/javascript" src="7-script.js"></script>
  </body>
</html>
guillaume@ubuntu:~/0x15$ 
Repo:

GitHub repository: holbertonschool-higher_level_programming
Directory: 0x15-javascript-web_jquery
File: 7-script.js

8. Star Wars movies mandatory
Write a Javascript script that fetches and lists all movies title by using this URL: https://swapi.co/api/films/?format=json

All movie titles must be list in the HTML tag UL#list_movies
You can’t use document.querySelector to select the HTML tag
You must use the jQuery API
Please test with this HTML file in your browser:

guillaume@ubuntu:~/0x15$ cat 8-main.html 
<!DOCTYPE html>
<html lang="en">
  <head>
    <title>Holberton School</title>
    <script src="https://code.jquery.com/jquery-3.2.1.min.js"></script>
  </head>
  <body>
    <header> 
      Star Wars movies
    </header>
    <br />
    <ul id="list_movies">
    </ul>
    <br />
    <footer>
      Holberton School - 2017
    </footer>
    <script type="text/javascript" src="8-script.js"></script>
  </body>
</html>
guillaume@ubuntu:~/0x15$ 
Repo:

GitHub repository: holbertonschool-higher_level_programming
Directory: 0x15-javascript-web_jquery
File: 8-script.js

9. Say Hello! mandatory
Write a Javascript script that fetches and prints how to say “Hello” depending of the language: (here in French) https://fourtonfish.com/hellosalut/?lang=fr

The translation of “Hello” must be display in the HTML tag DIV#hello
You can’t use document.querySelector to select the HTML tag
You must use the jQuery API You script must be work when it imported from the HEAD tag
Please test with this HTML file in your browser:

guillaume@ubuntu:~/0x15$ cat 9-main.html 
<!DOCTYPE html>
<html lang="en">
  <head>
    <title>Holberton School</title>
    <script src="https://code.jquery.com/jquery-3.2.1.min.js"></script>
    <script type="text/javascript" src="9-script.js"></script>
  </head>
  <body>
    <header> 
      Say Hello!
    </header>
    <br />
    <div id="hello"></div>
    <br />
    <footer>
      Holberton School - 2017
    </footer>
  </body>
</html>
guillaume@ubuntu:~/0x15$ 
Repo:

GitHub repository: holbertonschool-higher_level_programming
Directory: 0x15-javascript-web_jquery
File: 9-script.js

