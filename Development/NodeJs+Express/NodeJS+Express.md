![[nodejs_roadmap.png]]

![[difference_js_nodejs.png]]

---
* NPM = Node Package Manager

* To initiate the directory in which you're going to use nodejs :
```js
npm init
```
* It will ask you some question to answer so that it will create the **package.json**.

* To Install Express :
```js
npm install express
```

Example of our ***index.js***:
```js
const express = require('express') // Import the Express Framework
const app = express() // Create an instance of express

const router = express.Router() // Create a router that will take us to specific url when specified

router.get('/9ahwa', (req,res)=>{ // when accessing localhost:3000/9ahwa
res.send('9ahwa') // it will print the word "9ahwa" by sending the response (res)
})
router.get('/the', (req,res)=>{
res.send('the')
})
router.get('/superet', (req,res)=>{
res.send('superet')
})

app.use('/', router) // It mounts the router so that any routes defined in the router are accessible from the                                           // root path (/).

app.listen(3000, ()=> { // method in Express.js that starts the server and begins listening for incoming 
console.log('server is running on port 3000') // connections on the specified port and host.
})
```

>[!note]
>* There is a package called **nodemon** that will auto restart the node.js server when one of the file has changes to avoid manual starting.
>```js
>npm install nodemon
>```
>and then edit the **package.json** scripts to add the nodemon command:
>```js
>/* existing code*/
>"scripts": {
>"server": "nodemon index.js",
>"test": "nodemon index.js"
>},
>/* existing code*/
>```

* In the index.js:
```js
/* existing code*/
router.get('/:drink', (req,res) => {  // R1
res.send("You have requested "+`${req.params.drink}`)  //R2
})
/*existing code*/
```

* R1: The data after `/` is dynamic, so we capture it with variable named `drink`.
* R2: \`\`  is used as template to inject dynamic data on it and we access the dynamic data from the url after `/` by using `req.params.drink`.

* Example : (calculator from the URL bar)
```js
const express = require('express')
const app = express()
const router = express.Router()

router.get('/:num1/:num2', (req,res) => {
res.send(
"addition" + `${parseInt(req.params.num1) + parseInt(req.params.num2)}` +
"subtraction" + `${parseInt(req.params.num1) - parseInt(req.params.num2)}` +
"multiplication" + `${parseInt(req.params.num1) * parseInt(req.params.num2)}` +
"subdivision" + `${parseInt(req.params.num1) / parseInt(req.params.num2)}`
)
})

app.use('/', router)

app.listen(3000, ()=> {
console.log('server is running on port 3000')
})
```
![[calc_app.png]]

---
#### FS (npm):

* It is a built-in module that allows you to interact with the file system on your computer. 
* With fs, you can:
	- Read files
	- Write files
	- Create, delete, and rename files and directories
	- Work with file streams
	- Check file stats and permissions
- Example :
```js
const express = require('express')
const fs = require('fs')

const app = express()

const router = express.Router()

router.get('/:num1/:num2', (req,res) => {

res.send("addition: " + `${parseInt(req.params.num1) + parseInt(req.params.num2)}`)

fs.writeFile( // In here, if the addition is success,
'test.txt', // it will store the result of the addition in a file called 'test.txt'
`${parseInt(req.params.num1) + parseInt(req.params.num2)}`,
(err) => {
if (err) {
console.log(err)
}
else {
console.log("Operation Success")
}})
})

app.use('/', router)

app.listen(3000, ()=> {
console.log('server is running on port 3000')
})
```

---
##### MongoDB (mongoose):
* Non-relational DB
* mongoose is an npm package that helps with the ODM (Object Document Mapping) so that from our nodejs+express server, we can send our request to db (crud for e.g)
* To install it in our project, we do:
```js
npm install mongoose
```

* Example of our `server.js`:
```js
const express = require('express')
const mongoose = require('mongoose')
const app = express()
const router = express.Router()

router.get('/hi', (req, res) => {
res.send('Hello World')
})
router.get('/bonjour', (req,res) => {
res.send('Bonjour')
})

mongoose.connect('mongodb+srv://mhj:mhj@cluster0.iphuamo.mongodb.net/test')
         .then(() => {
         console.log('Connected to MongoDB')
         })
         .catch((err) => {
         console.log("Failed to connect to MongoDB", err.message)
         })
         
app.use('/', router)
app.listen(3000, () => {
console.log('Server is running on port 3000')
})

// mongodb+srv://mhj:<db_password>@cluster0.iphuamo.mongodb.net/
```
>[!note]
>* mongoose.connect('<url_to_db>'): to connect to the MongoDB database (locally or remotely)
>* .then( ()=>{} ): callback function to what to do if the DB is connected
>* .catch( (err)=>{} ): callback function to what to do if the connection failed

* Schemas and Models : 
* Example of `etudiant.js`:
```js
const mongoose = require('mongoose')

const etudiantSchema = new mongoose.Schema({
cin : {
	type: String,
	required: true,
},
nom : {
	type: String,
	required: true,
},
	prenom : {
	type: String,
	required: true,
},
email : {
	type: String,
	required: false,
}
});

const Etudiant = mongoose.model('etudiant', etudiantSchema)

module.exports = Etudiant
```

* Here, we create an `etudiantSchema` which defines the structure the `etudiant` in the Database
* Now, We create the `Etudiant` Modal with `mongoose.modal()` which can be concedered as the template
* and finally, we export the module that we created with `module.exports = Etudiant`.
