FORMAT: 1A
 
# Group todo
 
## todo task [/todos/{title}]
 
### GET a todo task [GET]
 
#### Description
 
* Get a todo task
 
+ Response 200 (Content-Type: application/json)

 
```
    {
        "todos": [
            {
                "title": "task1",
                "content": "eat the lunch"
            }
        ]
    }
```

#### Description 

* Can't find task

+ Responce 404 (Content-Type: application/json)

        {
            "message": "Todo not found."
        }




### POST new todo task  [POST]
#### Description  
* Create new todo task
+ Request (Content-Type: application/json)

        {
            "content": "eat the lunch"
        }
        
        

+ Response 201 (Content-Type: application/json)

    + Headers

            Location: /todos/{task}

    + Body  

        ```
        {
            "title": "task1",
            "content": "eat the lunch"
        }
        ```

#### Description 
* already task exists
+ Request (Content-Type: application/json)

        {
            "content": "duplicated title"
        }  

+ Responce 400 (Content-Type: application/json)


    + Headers

            Location: /todos/{task}

    + Body

            {
                "message": "the todo {title} already exists"
            }


### DELETE todo task  [DELETE]
#### Description  
* Delete todo task(Content-Type: application/json)
+ Request 

        {
            "content": "eat the lunch"
        }

+ Response 200 (Content-Type: application/json)

    + Headers
            
        
            Location: /todos/{task}

    + Body  

        ```
        {
            "message": "Todo deleted"
        }
        
        ```

### UPDATE todo task  [PUT]
#### Description  
* Update todo task content
+ Request (Content-Type: application/json) 

    ```
    {
        "content": "shopping"
    }
    ```

+ Response 200 (Content-Type: application/json)

    + Headers
    

            Location: /todos/{task}
        

    + Body  

        ```
        {
	        "content": "shopping"
        }
        
        ```

## todo tasks [/todos]

### GET todo tasks[GET]
#### Description
* Get all todo tasks
+ Response 200 (Content-Type: application/json)

        {
            "todos": [
                {
                    "title": "task1",
                    "content": "shopping"
                },
                {
                    "title": "task2",
                    "content": "eat the lunch"
                }
            ]
        }



