![pysql](https://raw.githubusercontent.com/jamesonfajardo/PySQL_Assistant/master/pysql.png)  

# PySQL_EZ_Query
Python MySQL Easy Query is another version of my [PySQL_Assistant](https://github.com/jamesonfajardo/PySQL_Assistant)  
No querying needed~! Its intended purpose is to help beginners familiarize themselves with MySQL

How to use:  
1. Start by importing the module  
    **![#00FA9A](https://placehold.it/15/00FA9A/000000?text=+) import PySQL_EZ_Query**
    
2. Define a function (steps 3-5 will be inside this function)  
    **![#00FA9A](https://placehold.it/15/00FA9A/000000?text=+) def ezQuery():**
   
3. Create 4 variables. Make the value empty if you won't be using it:  
    **![#00FA9A](https://placehold.it/15/00FA9A/000000?text=+) host = ''** `Your database host`  
    **![#00FA9A](https://placehold.it/15/00FA9A/000000?text=+) user = ''** `Your database username`  
    **![#00FA9A](https://placehold.it/15/00FA9A/000000?text=+) passwd = ''** `Your database password`  
    **![#00FA9A](https://placehold.it/15/00FA9A/000000?text=+) db = ''** `Your database name, if applicable`  

4. Bind the object method EZ_Query to a var  
  **![#00FA9A](https://placehold.it/15/00FA9A/000000?text=+) dbo = PySQL_EZ_Query.EZ_Query(host, user, passwd, db)**  

5. Each queries are bound to a function, here's a sample for creating a database. All functions are listed below  
  **![#00FA9A](https://placehold.it/15/00FA9A/000000?text=+) dbo.create_database('pydb')**  
  
6. Call the function (in this case ezQuery)  
  **![#00FA9A](https://placehold.it/15/00FA9A/000000?text=+) ezQuery()**  
  
  
# Function bound queries  
* create_database(`database_name`)  
  * create a database
* create_table(`table_name`, `columns`)  
  * columns should be written as a 'column1::, column2::, column3::, etc'
  * double colon (::) after every column name is important
  * keep your column names simple to prevent errors. camelCase or under_scores only
  * ID is automatically generated, so no need to include one in the columns
* insert_into(`table_name`, `dictionary`)
  * dictionary key must be the name of the column of the created table, dictionary value must be the column value
* select(`table_name`)
  * show all records
* update(`table_name`, `column_to_update`, `new_value`, `record_id`)
  * update record
* delete(`table_name`, `record_id`)
  * delete selected record
* truncate(`table_name`)  
  * delete all data inside the table
* drop_table(`database_name`)  
  * deletes the table  
* drop_database(`database_name`)  
  * deletes the database
  
  
# Sample usage

**![#00FA9A](https://placehold.it/15/00FA9A/000000?text=+) Create database**  
  
    import PySQL_EZ_Query

    def ezQuery():
        host = 'localhost'
        user = 'root'
        passwd = ''
        db = ''

        dbo = PySQL_EZ_Query.EZ_Query(host, user, passwd, db)
        dbo.create_database('pydb')

    ezQuery()
    
    
**![#00FA9A](https://placehold.it/15/00FA9A/000000?text=+) Create table**  

    import PySQL_EZ_Query

    def ezQuery():
        host = 'localhost'
        user = 'root'
        passwd = ''
        db = 'pydb'

        dbo = PySQL_EZ_Query.EZ_Query(host, user, passwd, db)
        table = 'customers'
        columns = 'name::, address::'
        dbo.create_table(table, columns)

    ezQuery()


**![#00FA9A](https://placehold.it/15/00FA9A/000000?text=+) Insert records**  
  
    import PySQL_EZ_Query

    def ezQuery():
        host = 'localhost'
        user = 'root'
        passwd = ''
        db = 'pydb'

        dbo = PySQL_EZ_Query.EZ_Query(host, user, passwd, db)
        table = 'customers'
        data = {'name': 'Johnny', 'address': 'Highway 21'}
        dbo.insert_into(table, data)

    ezQuery()

    

**![#00FA9A](https://placehold.it/15/00FA9A/000000?text=+) Select records**  
  
    import PySQL_EZ_Query

    def ezQuery():
        host = 'localhost'
        user = 'root'
        passwd = ''
        db = 'pydb'

        dbo = PySQL_EZ_Query.EZ_Query(host, user, passwd, db)
        table = 'customers'
        dbo.select(table)

    ezQuery()
    

**![#00FA9A](https://placehold.it/15/00FA9A/000000?text=+) Update record**  
  
    import PySQL_EZ_Query

    def ezQuery():
        host = 'localhost'
        user = 'root'
        passwd = ''
        db = 'pydb'
        dbo = PySQL_EZ_Query.EZ_Query(host, user, passwd, db)

        table = 'customers'
        column = 'name'
        column_value = 'Henry'
        record_id = 1
        dbo.update(table, column, column_value, str(record_id))

    ezQuery()
    

**![#00FA9A](https://placehold.it/15/00FA9A/000000?text=+) Delete record**  

    import PySQL_EZ_Query

    def ezQuery():
        host = 'localhost'
        user = 'root'
        passwd = ''
        db = 'pydb'
        dbo = PySQL_EZ_Query.EZ_Query(host, user, passwd, db)

        table = 'customers'
        id = 1
        dbo.delete(table, str(id))

    ezQuery()
    
    
    
    
**![#00FA9A](https://placehold.it/15/00FA9A/000000?text=+) Delete all table records**  

    import PySQL_EZ_Query

    def ezQuery():
        host = 'localhost'
        user = 'root'
        passwd = ''
        db = 'pydb'

        dbo = PySQL_EZ_Query.EZ_Query(host, user, passwd, db)
        dbo.truncate('customers')

    ezQuery()
    
    
    
**![#00FA9A](https://placehold.it/15/00FA9A/000000?text=+) Delete table**  

    import PySQL_EZ_Query

    def ezQuery():
        host = 'localhost'
        user = 'root'
        passwd = ''
        db = 'pydb'

        dbo = PySQL_EZ_Query.EZ_Query(host, user, passwd, db)
        dbo.drop_table('customers')

    ezQuery()





**![#00FA9A](https://placehold.it/15/00FA9A/000000?text=+) Delete database**  

    import PySQL_EZ_Query

    def ezQuery():
        host = 'localhost'
        user = 'root'
        passwd = ''
        db = 'pydb'

        dbo = PySQL_EZ_Query.EZ_Query(host, user, passwd, db)
        dbo.drop_database('pydb')

    ezQuery()
