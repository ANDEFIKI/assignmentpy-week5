# assignmentpy-week5
his Python script is a simple, command-line library management system designed to demonstrate fundamental Object-Oriented Programming (OOP) concepts: Encapsulation, Inheritance, and Polymorphism. The program manages a collection of both physical books and digital e-books.

Features
Book and E-Book Management: The system can handle two different types of library items, each with unique behaviors.

Checkout/Return Logic: Books can be checked out and returned, while e-books are "downloaded."

Library Collection: A Library class holds and manages all items.

Information Retrieval: Users can list all items in the library with their details.

OOP Concepts Demonstrated
1. Encapsulation
The Book and EBook classes use an underscore (_) prefix for attributes like _title, _author, and _pages. This is a Python convention to indicate that these attributes are "protected" and should not be accessed directly from outside the class. Instead, they are accessed through getter methods like get_title() and get_author(), which provides controlled access to the data.

2. Inheritance
The EBook class inherits from the Book class. This means it automatically gets all the attributes and methods of Book (_title, _author, check_out(), etc.) and extends them with its own unique attributes (_file_size_mb) and methods (get_file_size()). This avoids redundant code and promotes a clear hierarchy.

3. Polymorphism
Polymorphism allows objects of different classes to be treated as objects of a common superclass. This is demonstrated in two ways:

check_out() method: The Book and EBook classes both have a method named check_out(), but they have different functionalities. The Book method updates a status, while the EBook method simulates a download. When the Library calls check_out(), the correct method is executed automatically based on the object type.

__str__() method: This method provides a human-readable string representation of an object. Both classes override this method to display their unique information, showing how a single method name can produce different results depending on the object.






for program py

What the Code Does
The script defines three simple classes: Car, Plane, and Boat. Each class represents a vehicle and has a move() method.

The core of the demonstration is a list of these different vehicle objects. By iterating through this list and calling the move() method, the program shows how each object's unique implementation of move() is executed, even though the call itself is identical for every item in the list. This illustrates how Python's built-in polymorphism allows for flexible and reusable code.

Key Concept: Polymorphism
The word "polymorphism" comes from Greek and means "many forms." In programming, it refers to the ability of different classes to respond to the same method call in different ways.

In this example:

The Car's move() method prints "The car is driving."

The Plane's move() method prints "The plane is flying."

The Boat's move() method prints "The boat is sailing."

The transport_showcase() function further highlights this by accepting any of these vehicle objects as an argument and successfully calling its move() method without needing to know the specific type of vehicle.

How to Run the Code
Save the provided code as a Python file named polymorphism.py.

Open a terminal or command prompt.

Navigate to the directory where you saved the file.

Run the script using the following command:
