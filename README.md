   # FastAPI CRUD Application

   This project implements a **CRUD** based on the official FastAPI documentation, using the models **Hero** and **Team** as examples. 
   However, additional features have been added to make the application more robust and useful in real-world scenarios.

   ## Features

   1. **Pagination**:
      Pagination has been added to the query routes to improve the handling of large datasets. 
      This ensures that results are returned in manageable pages, allowing efficient navigation through the records.

   2. **Soft Delete**:
      Instead of permanently deleting records from the database, a **soft delete** system has been implemented in the **Hero** model. 
      This is achieved via the `is_active` field, which allows marking a record as "deleted" without physically removing it. 
      This way, the record remains in the database for potential future recovery or auditing.

   3. **Organized Routes**:
      The application organizes the routes related to **Hero** and **Team** into separate modules using routers, 
      keeping the code modular and scalable.

   ## Project Objective:

   The aim is to demonstrate how to extend the basic **CRUD** functionality with FastAPI by adding pagination 
   and soft deletes, making the application more suitable for real-world scenarios where permanent data deletion is often not preferable.
 
 # Setup instructions
   ### Step 1: Clone the repository
      Start by cloning the project repository  to your local machine:
      git clone <repository_url>
   ### Step 2: create a virtual environment 
      python -m venv venv
      source venv/bin/activate  # On Windows, use `venv\Scripts\activate`

   ### Step 3: install the requirementx.txt
      pip install -r requirements.txt
   ### Step 4: add to .env
      Set Up Environment Variables
      DATABASE_URL="mysql+pymysql://user:password@localhost/db_name"
   ### Step 5:  Apply Migrations with Alembic
      alembic init
      alembic revision --autogenerate -m "Initial migration"
      alembic upgrade head
   ### Step 6: run fastapi server on dev
      fastapi dev main.py

go to http://127.0.0.1:8000/
or http://127.0.0.1:8000/docs to view the documentation