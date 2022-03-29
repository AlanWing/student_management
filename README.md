# Assignment

+ Structure

  Use two apps `student` and `student_class` to manage related resources.

+ Model
    + StudentClass
      ```text
      id: primary key.
      updated_at: auto-saved, refer to the point in time the instance be updated.
      created_at: auto-saved, refer to the point in time the instance be created.
      grade: grade of the class.
      sequence_num: class number. 
      ```
    + Student
      ```text
      id: primary key.
      updated_at: auto-saved, refer to the point in time the instance be updated.
      created_at: auto-saved, refer to the point in time the instance be created.
      name: student name.
      gender: student gender (M|F).
      age: student age.
      cls_id: a foreign key point to `Student`.
      ```

+ FIELDS

  specify `ordering_fields`, `search_fields`, `readonly_fields` under `StudentViewSet`

+ REST API

  For app `Student`, I use `ModelViewSet`, which provides several MixIns of REST methods.   
  And `ModelSerializer` at the same time, handling the fields as well as methods `update()` and `create()`.

  However, to meet the requirements of this assignment, I chose the standard way to perform app `StudentClass`.  
  Under this condition, we have to deal with the basic REST api logic in our `ViewSet` class.  
  Meanwhile, override `update()` and `create()` in `Serializer` class.

+ TEST
    1. Database migrations and model test under django admin page(using default database `sqlite`)
    2. REST api logic test, CRUD

+ ACCOUNT
  ```text
  username: alan
  password: 123
  ```