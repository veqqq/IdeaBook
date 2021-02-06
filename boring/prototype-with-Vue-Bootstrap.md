## Prototyping with vue.js and bootstrap
notes from: https://peterxjang.com/blog/prototyping-with-vuejs-and-bootstrap.html

# did not finish, seems like hastle

Quick protoypes in a few hours use bootstrap for visuals, vue for interactivity
https://getbootstrap.com/docs/4.0/getting-started/introduction/#starter-template
insert: https://vuejs.org/v2/guide/#Getting-Started

```html
<div class="container">  
  <h1>Items</h1>  
  <div class="list-group">  
    <button type="button" class="list-group-item list-group-item-action">Morbi</button>  
    <button type="button" class="list-group-item list-group-item-action">Fusce</button>  
    <button type="button" class="list-group-item list-group-item-action">Aenean</button>  
    <button type="button" class="list-group-item list-group-item-action">Rhoncus</button>  
    <button type="button" class="list-group-item list-group-item-action">Sed</button>  
  </div>  
</div>
```

then add js to make it dynamic and shorter:

```html
<div id="app" class="container">  
  <h1>Items</h1>    <div class="list-group">        <button   
        type="button"          class="list-group-item list-group-item-action"  
        v-for="item in items" 
      >  
        {{ item.title }}
    </button>    </div>  </div>
```
    
v-for renders a list of items, defined in the Vue instance:

```javascript
var app = new Vue({  
  el: "#app",  
  data: {  
    items: [  
      {title: "Morbi", body: "Morbi nec dictum..."},  
      {title: "Fusce", body: "Fusce molestie..."},  
      {title: "Aenean", body: "Aenean et lectus..."},  
      {title: "Rhoncus", body: "Rhoncus eleifend..."},  
      {title: "Sed", body: "Sed tellus..."}  
    ]  
  }  
})
```

= = = = https://bootstrap-vue.js.org/ = = =
this library helps avoid conflicts in their JS approaches






