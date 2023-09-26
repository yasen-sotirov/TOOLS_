<img src="https://webassets.telerikacademy.com/images/default-source/logos/telerik-academy.svg)" alt="logo" width="300px" style="margin-top: 20px;"/>

## Database Design - Create a database model for a car rental system

### **Description of the system**

A car rental company rents cars to customers. The company owns several cars. Each car has a brand, model name, production year, mileage, color. Cars are divided into different categories: small, mid-size, large, limousines.

The company has many locations where you can rent a car. The rental locations are located in different cities throughout the country. There can be more than one company location in a city.
Anyone over 21 who has a valid driver’s license can rent a car.

Customers under 25 or over 75 years pay different (higher) charges then other customers.

Before renting a car, a customer usually makes a reservation for a car. A customer specifies the dates when the car will be rented, the pick-up location, the drop-off location, and the category of car he wants to rent. 

When a customer rents a car, he declares the pick-up and drop-off location, and the drop-off date. The customer can buy various types of insurance. He can also decide that he doesn’t need insurance because the insurance is covered otherwise, for example by his credit card company. The customer can choose additional options such as the possibility of an early drop-off, various refueling options, etc.

The customer pays the charges when he returns the car.

### **Highlight All nouns**

A `car` rental `company` rents `cars` to `customers`. The `company` owns several `cars`. Each `car` has a `brand`, `model name`, `production year` `mileage`, `color`.` Cars` are divided into different `categories`: small, mid-size, large, limousines.

The `company` has many `locations` where you can rent a `car`. The rental `locations` are located in different `cities` throughout the `country`. There can be more than one `company location` in a `city`.
Anyone over 21 who has a valid `driver’s license` can rent a `car`.

`Customers` under 25 or over 75 years pay different (higher) `charges` then other `customers`.

Before renting a `car`, a `customer` usually makes a `reservation` for a car. A `customer` specifies the `dates` when the `car` will be rented, the `pick-up location`, the `drop-off location`, and the `category` of car he wants to rent. 

When a `customer` rents a car, he declares the `pick-up` and `drop-off location`, and the `drop-off date`. The `customer` can buy various types of `insurance`. He can also decide that he doesn’t need `insurance` because the `insurance` is covered otherwise, for example by his `credit card company`. The `customer` can choose additional `options` such as the `possibility` of an early drop-off, various refueling `options`, etc.

The `customer` pays `the charges` when he returns the `car`.

### **Tables, Relationships, Columns**

The next stage is to find tables. We look for the basic entities in the system. For a start, you should at least have these: 
`car, customer, location, city, (car) category, insurance`. 

We put them in the diagram. We add the `id column` in every table because every table should have some sort of id. We can always change the primary key later.

![tables](D:\Telerik\Telerik_course_python\39_DB\in_class_Rent_a_Car\tables.png)

The basic system entities are in the model but we’re missing the core functionality of the system: `renting cars and reservations`. Remember what we talked: tables are not only physical objects but also events and transactions. Let's add reservation and rental as tables as well.

![tables1](D:\Telerik\Telerik_course_python\39_DB\in_class_Rent_a_Car\tables1.png)

**Now we add the references between the tables in the model.**

1. Each car belongs to a category,
2. Each reservation is for a 3. category of cars,
3. Each location is in a city,
4. Each reservation has a pickup and a drop off location,
5. Each reservation is made by a customer,
6. Each rental is made by a customer,
7. Each rental is for a certain car,
8. Each rental has a pickup and a drop off location.
9. Each rental is connected to some insurances - think how many ensurances can one car have? Perhaps we are looking at many-to-many relation?

**Add columns and their datatypes**

![diagram](D:\Telerik\Telerik_course_python\39_DB\in_class_Rent_a_Car\diagram.png)



