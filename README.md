## CS 340 Module Eight Journal Reflection

### How do you write programs that are maintainable, readable, and adaptable?

I write maintainable, readable, and adaptable programs by separating different responsibilities and creating reusable components. In Project One, I created the AnimalShelter CRUD Python module to handle communication with MongoDB. The module contains separate methods for creating, reading, updating, and deleting records. In Project Two, I reused this module to connect my dashboard to the database instead of putting all of the database code directly into the dashboard.

The main advantage of this approach was that the database logic and dashboard logic remained separate. This made the program easier to understand, test, and modify. In the future, I could reuse or adapt the CRUD module for other applications that need to interact with MongoDB, such as inventory systems, administrative dashboards, or other data-driven applications.

### How do you approach a problem as a computer scientist?

I approach a problem by first understanding the requirements and then breaking the problem into smaller parts. For the Grazioso Salvare project, I first considered what information the client needed from the animal shelter database. I then worked on the MongoDB connection and CRUD operations before connecting the database to the dashboard. After that, I implemented the required rescue filters and connected the filtered data to the table, pie chart, and geolocation map.

This project was different from many of my previous programming assignments because I had to build a solution based on specific client requirements and connect several components together. In future database projects, I would use a similar approach by analyzing the client's requirements, designing appropriate database queries, separating database operations from the user interface, testing individual components, and then integrating them into a complete application.

### What do computer scientists do, and why does it matter?

Computer scientists use programming, data, and computational thinking to solve real-world problems. They design systems that can organize information, automate tasks, and help users make better decisions.

For an organization such as Grazioso Salvare, my project provides a more efficient way to work with animal shelter data. Instead of manually searching through a large dataset, users can filter animals based on rescue requirements and view the results through an interactive table, chart, and map. This can save time and make it easier to identify animals that may be suitable for search-and-rescue training.

## Technologies Used

- Python
- MongoDB
- PyMongo
- Dash
- Plotly
- Dash Leaflet
- Jupyter Notebook
