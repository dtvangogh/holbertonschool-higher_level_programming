# 0x0F. Python - Object-relational mapping
## Description
 This project is part of Foundations - Higher-level programming ― Python:
## Project tasks :wrench:
### [0. Get all states ](./0-select_states.py) 
* Write a script that lists all states from the database hbtn_0e_0_usa:
### [1. Filter states ](./0x0F-python-object_relational_mapping) 
* Write a script that lists all states with a name starting with N (upper N) from the database hbtn_0e_0_usa:
### [2. Filter states by user input ](./localhost) 
* Write a script that takes in an argument and displays all values in the states table of hbtn_0e_0_usa where name matches the argument.
### [3. SQL Injection... ](./1-filter_states.py) 
* Wait, do you remember the previous task? Did you test "Arizona'; TRUNCATE TABLE states ; SELECT * FROM states WHERE name = '" as an input?
### [4. Cities by states ](./2-my_filter_states.py) 
* Write a script that lists all cities from the database hbtn_0e_4_usa
### [5. All cities by state ](./3-my_safe_filter_states.py) 
* Write a script that takes in the name of a state as an argument and lists all cities of that state, using the database hbtn_0e_4_usa
### [6. First state model ](./4-cities_by_state.py) 
* 
### [7. All states via SQLAlchemy ](./5-filter_cities.py) 
* Write a script that lists all State objects from the database hbtn_0e_6_usa
### [8. First state ](./model_state.py) 
* Write a script that prints the first State object from the database hbtn_0e_6_usa
### [9. Contains `a` ](./7-model_state_fetch_all.py) 
* Write a script that lists all State objects that contain the letter a from the database hbtn_0e_6_usa
### [10. Get a state ](./8-model_state_fetch_first.py) 
* Write a script that prints the State object with the name passed as argument from the database hbtn_0e_6_usa
### [11. Add a new state ](./9-model_state_filter_a.py) 
* Write a script that adds the State object “Louisiana” to the database hbtn_0e_6_usa
### [12. Update a state ](./10-model_state_my_get.py) 
* Write a script that changes the name of a State object from the database hbtn_0e_6_usa
### [13. Delete states ](./11-model_state_insert.py) 
* Write a script that deletes all State objects with a name containing the letter a from the database hbtn_0e_6_usa
### [14. Cities in state ](./12-model_state_update_id_2.py) 
* Write a Python file similar to model_state.py named model_city.py that contains the class definition of a City.
---
Created by [DT Van](https://github.com/dtvangogh)