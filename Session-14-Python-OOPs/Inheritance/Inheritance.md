# Concepts of Inheritance

- Child can access all the properties of Parent class
- child class name after that you need to mention parent class name to inherit
- if your child class is not having any constructor than automatically when you create object of child class it will directly call parent class constructor

- But, if you have child class constructor as well then you have to call parent class constructor from child class constructor using super keyword.

- we can not override constructor but we can override methods.
- if parent class and child class having same methods them child class will use its own method and override parent class method.
- if you want to purposely use parent class method as well then call it using super() inside the child class method.