This Peter Jang guy is just great: https://peterxjang.com/blog/modern-javascript-explained-for-dinosaurs.html

### Old school JS

```html
<!-- index.html -->  
<!DOCTYPE html>  
<html lang="en">  
<head>  
  <meta charset="UTF-8">  
  <title>JavaScript Example</title>  
  **<script src="index.js"></script>**  
</head>  
<body>  
  <h1>Hello from HTML!</h1>  
</body>  
</html>
```
- super simple js
```javascript
// index.js  
console.log("Hello from JavaScript!");
```

But if you want to use a js libraru like moment.js which formats the date
```javascript
moment().startOf('day').fromNow();        // 20 hours ago
```
you have to install npm, yawn, nuget, spm... which becomes bloated!
and the libraries can update a lot and get broken...

## package manager - npm to the rescue (starting in 2010)
- bower in 2013, taken over by npm in 2015, yawn gained a lot of traction too
- these are CLI a la: `npm install moment --save`
which updates packages on your sister, as well as a json - but you still
have to manually include them in your html

### webpack - js module bundler
since js was designed for the browser, it had no way to import code between .js files
so you would load the files to the html and they would define global variables availible
to each other...

- 2009 commonJS added modules, to import code without global variables!
node.js is an implementation (for the server)
```javascript
// index.js  
var moment = require('moment');
console.log("Hello from JavaScript!");  console.log(moment().startOf('day').fromNow());
```
- js knows the location of the npm modules, so you don't need
`require('./node_modules/moment/min/moment.min.js)`
but the browser can't read require... (just the server...)

##### module builder
creates browser compatabile output in build step (the client doesnt have access
to the file system, but the server building does). This will replace require with
the file contents. 
- browserify 2011 was most popular.
- webpack 2015 replaced it (React uses webpack's features)
`$ npm install webpack webpack-cli --save-dev`
then `./node_modules/.bin/webpack index.js --mode=development` which will
replace require with the right code in an output file. You must run this each
time you change index.js (also your html should refer to thhe output.js and not
index.js which is just how you construct it)

# this seemed tedious. Im sleepy. did not finish, but might later

summary: plain -> package manager -> module bundler -> transpile code (typescript)
-> task runner automating build process
- node won. npm as package manager, node require or import statements, npm scripts
- ember-cli, angular-cli, create-react-app, vue-cli set everything up for you!











