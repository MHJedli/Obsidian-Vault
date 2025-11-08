# Day 1 : appointment-app

![[angular_part.png]]

* **component**: what the user can actually see and interact with (the building blocks)
* **service**: used to handle our data (communication with REST APIs to load data via DBs)
* **modules**: used for encapsulation to keep the entire app nice and well structured
![[angular_app.png]]

* To create a new angular project :
```
ng new <project-name>
```

>[!note]
>For angular v17+, the `app.modules.ts` is not present by default.
>To generate it, add `--no-standalone` argument when creating a new project


* To launch angular local server :
```
ng serve <-o>
```

## Angular Structure :

![[angular_structure.png]]
* In `app.component.ts`, we have :
![[component_ts.png]]
### Data Binding :
#### 1. One-way Binding :
* display the content of a property in the template (html)
![[owb.png]]

* To generate a new component :
```
ng g component <component-name>
or 
ng g c <component-name>
```

* To generate a new interface :
```
ng g interface <interface-name>
or 
ng g i <interface-name>
```

* **Example of 1-way data binding:**
![[owb_exp1.png]]
![[owb_exp2.png]]

#### 2. Two-Way binding:
* The data inside template can be extracted and used in the component (ts)
![[twb_exp.png]]
* in the `appointment-list.component.html`:
	- When using the directive `[(ngModel)]=""`, we can extract the value inside the `input` tag and use it in the `appointment-list.component.ts`
>[!important]
> To be able to use the forms directive when using forms in html,
> We need to declare the `FormsModule` inside `app.module.ts` to be able to use its directive
> ![[declare_forms-modules.png]]

* To add an event in the `button` tag :
```
<button (event)="function_to_invoke">value</button>
```
* In our appointment.html, we can do this:
```
<button (click)="addAppointment()">Add</button>
```
* To create a loop that loops into an array of appointments and print its values inside our template :
![[ngfor_directive.png]]
* In our case, we use the directive `*ngFor` to create a loop that iterates and prints the values of `appointments` properties inside our `appointment-list.component.html`.
* The line `{{ appointment.date | date : 'dd/MM/yyyy' }}` :
	* we pipe the `appointment.date` to change its format

> [!note]
> In the loop we created earlier, we can add an `index` to each printed element so that it will be easier to delete one of them or one specific element when needed.
> Just do this :
> `<li *ngFor="let appointment of appointments; index as i">`

#### Browser Local Storage:

* To store a value (in our case, the appointments array) inside the Local Browser Storage :
```
localStorage.setItem("appointments", JSON.stringify(appointments))
```

* To get a value (in our case, the appointments array) from the Local Browser Storage :
```
savedAppointments = localStorage.getItem("appointments")
appointments = savedAppointments ? JSON.parse(savedAppointments) : []
```
* In the second, we used a ternary expression to check if `savedAppointments` is null or not :
	* if it's `NULL`, appointments will get assigned an empty array
	* if it's not, appointments will get assigned the parsed value from `savedAppointments`

#### ngOnInit():
* We use `ngOnInit()` to execute some function or initialize variables earlier when loading a page.
* To be able to use it, we need to 
	1. Declare it in the component ts file
	2. implement it on the working class
	3. create its function

![[ngoninit_steps.png]]

>[!note]
>To install and import bootstrap to our angular app :
>1. Install Bootstrap with `npm install bootstrap@<version-number>`
>2. Inside src/styles.css, type : `@import "bootstrap/dist/css/bootstrap.min.css"`

* More about Angular Components Handouts :
![[Angular-Components-Handouts.pdf]]

---

## Day 2 : hotel-reservation-app

![[main_ops.png]]

* The structure of the project:
![[prj_strc_d2.png]]

* To create a new module :
```
ng generate module <module-name>
```

* To create a new component and attach it to a module :
```
ng g c <component-name> --module=<module-name>
```

>[!note]
>a component can only have 1 module

* To create a new service :
```
ng generate service <service-name>
or
ng g s <service-name>
```

#### Routes:
* With routes, we can navigate from page to page by setting up its path
* In our case, 
	* `localhost:4200` takes us to home page
	* `localhost:4200/list` takes us to the reservation list page
	* `localhost:4200/new` takes us to the reservation form list
* We set the pages path inside the `app-routing.module.ts`:
![[app_routing.png]]

>[!important]
>* `router-outlet` tag must be kept in `app.component.html`
>* Every new module created should be imported to `app.module.ts` (the root module)
>![[importing_modules.png]]
>

* In `home.component.html` :
	* To navigate from page to page using button and the page path :
	```
	<button [routerLink]="['/<path>']">
	```
	![[router_link.png]]

#### Form Validation :

* There are two types of Form Validation :
![[form_validation_types.png]]
* In our case, we wil be using the `Reactive Form Validation`.
* To use the `Reactive Form Validation`, we have to prepare :
```
	1.  the html component (in our case: reservation-form.component.html)
	2. the ts component (in our case: reservation-form.component.ts)
```

1. `reservation-form.component.html`: ![[form_validator_html.png]]
2. `reservation-form.component.ts`:
![[form_validator_ts.png]]

>[!note]
>To make the submit button auto disable/enable when the form is invalid/valid :
>`<button type="submit" [disabled]="reservationForm.invalid">Submit</button>`

* We can show some message when a one of the input values are not valid using `*ngIf` Directive:
![[showing_validation_msgs.png]]
#### Injection a Service in a component :

* In our case, we are going to inject the `reservation.service.ts` in `reservation-form.component.ts` so that we will be able to handle our data (updating, adding, removing, reading/ CRUD).
* The `reservation.service.ts` :
![[reservation_service_ts.png]]
* The `reservation-form.component.ts` :
![[injecting_reservation_service.png]]
#### ngtemplate and local reference :
* In `reservation-list.component.html`, we are going to print all the available reservations from the local browser storage.
* When there are no available reservations, we need to display the message `No reservation Available`.
* In this case, we can use the `ng-template` tag and its `local reference` like this:
![[ng-template_local-reference.png]]
* This is useful for a good User eXperience.

#### Redirecting the user with the route navigate method :

* Let's say that when we submit the reservation form, we want to redirect the user to the reservation list page.
* To do this, head to the `reservation-form.component.ts` and :
![[user_redirection.png]]

#### Adding the edit route with parameter:
* Here, we need to add an `edit` button in the Reservation list page so that we can edit a reservation.
* For that, we have to :
	1. Add a new path in the `app-routing.module.ts`
	2. Add a new button in the `reservation-list.component.html` 
	3. modify that button so that it will redirect us to the edit page with id of the reservation passed in the url
1. `app-routing.module.ts`:
![[app_routing_edit.png]] 
2/3. `reservation-list.component.html`:
![[app_routing_edit_page.png]]
* Now that we prepared the edit page, it's time to add the logic of editing a reservation
* First of all, we are going to use the same reservation form for editing a reservation.
* That means the reservation form page is used for :
	1. Creating a new reservation
	2. Editing/Updating an existing reservation
* Earlier, we set up the edit page in a way that we send the id of the reservation in the url so that we can capture it to get the reservation and update it
* So, we need to update our `reservation-form.component.ts`:
![[update_reservation.png]]
>[!note]
>we changed the updateReservation method in the ReservationService so that it accepts an id and a reservation as arguments
>![[update_reservation_service.png]]

#### Combining components from different modules:
* Here, we want to combine the home, reservation-list and reservation-form components so that the reservation-list and reservation-form components will show inside the home component.
* To do so, we have to:
	1. Integrate the `app-home` selector inside the `reservation-list.component.html` and `reservation-form.component.html`
	2. Import the `HomeModule` in the `reservation.module.ts`
	3. Make the `HomeComponent` external to others Modules in `home.modules.ts`
	
1. In `reservation-list.component.html` and `reservation-form.component.html`,                                          add `<app-home></app-home>`
2. In `reservation.modules.ts`:
![[home_module_import.png]]
3. In `home.modules.ts`:
![[home_module_export.png]]
* More about Angular Modules :
![[Angular-Modules-Handouts.pdf]]

---
## Day 3 : hotel-reservation-app (Extended)

![[mwa1.png]]
![[mwa2.png]]
![[request_type.png]]
![[response_type.png]]

* What we are going to do here is that we are going to change our `hotel-reservation-app` to use fake APIs instead of the local browser storage
* We are going to use `http requests` and `observables` to interact with the fake API that we created (instead of creating a whole backend, we create a `fake` backend environment to test our angular application)
* To apply those new changes, we need to:
	1. Delete the code of the local browser storage in `reservation.service.ts`
	2. Import the `importHttpClient` in `app.module.ts`
	3. Import the `HttpClient` and `Observable` in the `reservation.service.ts`
	4. Change the `getReservations` method so it will pull data from the API
	5. `subscribe` the `reservationService.getReservations()` to receive the date in asynchronous way in `reservation-list.component.ts`

2. in `app.modules.ts`:
![[import_http.png]]
3. in `reservation.service.ts`:
![[prepare_api_return.png]]
4. in `reservation-list.component.ts`:
![[get_data_from_api.png]]
* Now, we are going to complete the rest of the `reservation.service.ts` and `reservation-form.component.ts` methods to make them interact with the fake API that we created so it will mock a real-life development environment.

* In `reservation.service.ts`:
![[crud.png]]

* In `reservation-form.component.ts`:
![[res_form.png]]

---

## Day 4 : E-commerce Web Application

* In this section, we are going to develop a simple E-commerce web app (amazing Animal Paintings) using Mock APIs and Angular Material.

>[!note]
>We can create a development environment to store some global variables like the API URL be executing : `ng g environments` and place your global constants in `environment.development.ts`
>
>By default, Angular uses the Production Environment instead of the Development Environment.
>To start the server with the development environment, execute : 
>`ng serve --configuration=development`

* To Add Angular Material :
```
ng add @angular/material
```

>[!note]
>In angular 19 :
>To import your assets(videos, images, ...), place them in the `Public` directory

* To apply a filter dynamically when typing in an input field :
* In `product-list.component.ts`:
![[dynamic_filter_ts.png]]
* In `product-list.component.html`:
![[dynamic_filter_html.png]]
* To sort the price of products:
* In `product-list.component.ts`:
![[sort_ts.png]]
* In `product-list.component.html`:
![[sort_html.png]]
* To use Angular Material Components, visit the [documentation](https://material.angular.io/components/categories). It's very easy to implement and use. (Not worth mentioning here. ( You can see the project source code for more understanding of its usage )

---
## Day 5 : Reactive Book Management App

![[without_ngrx1.png]]
![[without_ngrx2.png]]
![[ngrx_sol1.png]]
![[ngrx_sol2.png]]

* **NgRx** is a **state management library** for Angular applications, inspired by the **Redux** pattern. It provides a predictable and centralized way to manage the state of your application, making it easier to debug, test, and maintain complex apps.

#### NgRx Flow :
![[ngrx_flow.png]]

![[ngrx_flow_elements.png]]
![[owdf.png]]

* To install NgRx store and effects :
```
npm install @angular/store @angular/effects
```

* An appstate can contain multiple states
* A reducer take care of its related states ONLY (book reducer takes care of book state)
* We cannot change the appstate directly.
* A reducer can change the appstate by :
	1. Copying the current state of the appstate
	2. Make changes
	3. Return the new state

* The project structure is the following :
![[proj_struct.png]]

* In `app.state.ts`:
![[app_state.png]]
* In `book.actions.ts`:
![[book_actions.png]]
* In `book.effect.ts`:
![[book_effects.png]]

>[!note]
>if a variable of type `Observable`, we name it : `<var_name>$`
>Example: `actions$`


* In `book.reducer.ts`:
![[book_reducer.png]]
* In `book.service.ts`:
![[book_service.png]]
* In `book-list.component.ts`: 
![[book_list_component.png]]
* In `app.module.ts`:
![[reducers_effects_app_module.png]]
* In `book-list.component.html`:
![[book_list_template.png]]
>[!note]
>if you got an error when piping to async, add the following line to `config.ts`:
>![[config_ts.png]]

---
### @Input() and @Output:

* `@Input()` and `@Output()` allow Angular to share data between the parent context and child directives or component.
* an `@Input()` property is writable while `@Output()` property is observable.
* Consider this example of parent/child relationship:
```html
<parent-component>
	<child-component></child-component>
</parent-component>
```
* `@Input()` and `@Output()` act as the API of the child component in that they allow the child to communicate with the parent.

##### 1. How to Use `@Input()`:

* The `@Input()` allows data to be input _into_ the child component from the parent component.
* To illustrate the use of `@Input()`, edit these parts of your app:
	- The child component class and template
	- The parent component class and template
###### ___In the child (item-detail)___:
* In the `item-detail.component.ts`:
```ts
import { Component, Input } from '@angular/core'; // First, import Input
export class ItemDetailComponent {
  @Input() item: string; // decorate the property with @Input()
}
```

>[!note]
>In this case, `@Input()` decorates the property `item`, which has a type of `string`, however, `@Input()` properties can have any type, such as `number`, `string`, `boolean`, or `object`. The value for `item` will come from the parent component, which the next section covers.

* In the `item-detail.component.html`:
```html
<p>
  Today's item: {{item}}
</p>
```

###### ___In the Parent (app)___:
* The next step is to bind the property in the parent component's template. In this example, the parent component template is `app.component.html`.
* First, use the child's selector, here `<app-item-detail>`, as a directive within the parent component template. Then, use [property binding](https://docs.angular.lat/guide/property-binding) to bind the property in the child to the property of the parent.
```html
<app-item-detail [item]="currentItem"></app-item-detail>
```

* Next, in the `app.component.ts`:
```ts
export class AppComponent {
  currentItem = 'Television';
}
```

* With `@Input()`, Angular passes the value for `currentItem` to the child so that `item` renders as `Television`.
* The following diagram shows this structure:
![[diag_input.png]]

##### 2. How to use `@Output()` :

* Use the `@Output()` decorator in the child component or directive to allow data to flow from the child _out_ to the parent.
* An `@Output()` property should normally be initialized to an Angular [`EventEmitter`](https://docs.angular.lat/api/core/EventEmitter) with values flowing out of the component as [events](https://docs.angular.lat/guide/event-binding).
* Just like with `@Input()`, you can use `@Output()` on a property of the child component but its type should be `EventEmitter`.
* When you use `@Output()`, edit these parts of your app:
	- The child component class and template
	- The parent component class and template

###### ___In the child (item-output):___
* This example features an `<input>` where a user can enter a value and click a `<button>` that raises an event. The `EventEmitter` then relays the data to the parent component.
* In the `item-output.component.ts`:
```ts
import { Output, EventEmitter } from '@angular/core';
export class ItemOutputComponent {
  @Output() newItemEvent = new EventEmitter<string>();
  addNewItem(value: string) {
    this.newItemEvent.emit(value);
  }
}
```
>[!note]
>* The different parts of the above declaration are as follows:
>	- `@Output()`: a decorator function marking the property as a way for data to go from the child to the parent
>	- `newItemEvent`: the name of the `@Output()`
>	- `EventEmitter<string>`: the `@Output()`'s type
>	- `new EventEmitter<string>()`: tells Angular to create a new event emitter and that the data it emits is of type string. The type could be any type, such as `number`, `boolean`, and so on. For more information on `EventEmitter`, see the [EventEmitter API documentation](https://docs.angular.lat/api/core/EventEmitter).

* The `addNewItem()` function uses the `@Output()`, `newItemEvent`, to raise an event in which it emits the value the user types into the `<input>`. In other words, when the user clicks the add button in the UI, the child lets the parent know about the event and gives that data to the parent.

###### ___In the child's template___:
* The child's template has two controls. The first is an HTML `<input>` with a [template reference variable](https://docs.angular.lat/guide/template-reference-variables) , `#newItem`, where the user types in an item name. Whatever the user types into the `<input>` gets stored in the `#newItem` variable.
```html
<label>Add an item: <input #newItem></label>
<button (click)="addNewItem(newItem.value)">Add to parent's list</button>
```

* The second element is a `<button>` with an [event binding](https://docs.angular.lat/guide/event-binding). You know it's an event binding because the part to the left of the equal sign is in parentheses, `(click)`.
* The `(click)` event is bound to the `addNewItem()` method in the child component class which takes as its argument whatever the value of `#newItem` is.
* Now the child component has an `@Output()` for sending data to the parent and a method for raising an event. The next step is in the parent.

###### ___In the parent (app):___

* In this example, the parent component is `AppComponent`, but you could use any component in which you could nest the child.
* The `AppComponent` in this example features a list of `items` in an array and a method for adding more items to the array.
```ts
export class AppComponent {
  items = ['item1', 'item2', 'item3', 'item4'];

  addItem(newItem: string) {
    this.items.push(newItem);
  }
}
```

* The `addItem()` method takes an argument in the form of a string and then pushes, or adds, that string to the `items` array.

###### In the parent's template:
* Next, in the parent's template, bind the parent's method to the child's event. Put the child selector, here `<app-item-output>`, within the parent component's template, `app.component.html`
```html
<app-item-output (newItemEvent)="addItem($event)"></app-item-output>
<ul>
  <li *ngFor="let item of items">{{item}}</li>
</ul>
```
* The event binding, `(newItemEvent)='addItem($event)'`, tells Angular to connect the event in the child, `newItemEvent`, to the method in the parent, `addItem()`, and that the event that the child is notifying the parent about is to be the argument of `addItem()`. In other words, this is where the actual hand off of data takes place. The `$event` contains the data that the user types into the `<input>` in the child template UI.

* The `*ngFor` iterates over the items in the `items` array. When you enter a value in the child's `<input>` and click the button, the child emits the event and the parent's `addItem()` method pushes the value to the `items` array and it renders in the list.

##### 3. How to use `@Input()` and `@Output()` together :

* You can use `@Input()` and `@Output()` on the same child component as in the following:
```html
<app-input-output [item]="currentItem" (deleteRequest)="crossOffItem($event)"></app-input-output>
```
* The target, `item`, which is an `@Input()` property in the child component class, receives its value from the parent's property, `currentItem`. When you click delete, the child component raises an event, `deleteRequest`, which is the argument for the parent's `crossOffItem()` method.
  
* The following diagram is of an `@Input()` and an `@Output()` on the same child component and shows the different parts of each:
![[diag_input_output.png]]
