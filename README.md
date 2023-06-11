# CashManager

A simple app to manage your physical cash.

## Characteristics

- Manage your physical cash (total)
- Manage your day to day expenses
- Delimite a budget for each day
- See your expenses history
- See how much you have saved per day

## Technologies

- Node.js
- Vue.js
- Flask
- PostgreSQL

## How to install

The project have two parts: the backend and the frontend. You need to install both.

### Frontend

- Go to the `frontend` folder

- Run the **following commands**:
  
  ```
  npm install
  ```
  
  You should now have a `node_modules` folder in the `frontend` folder.
  
  ```
  npm run serve
  ```
  
  This will start the frontend server on `localhost:8080`.

### Backend

- Go to the `backend` folder

- Create a virtual environment:
  
  ```
  python -m venv venv
  ```

- Activate the **virtual environment**:
  In case you are using Windows:
  
  ```
  venv\Scripts\activate
  ```
  
  In case you are using Linux or Mac:
  
  ```
  source venv/bin/activate
  ```

- Once you are in the virtual environment, **install the requirements**:
  
  ```
  pip install -r requirements.txt
  ```

- Then **set the app folder** as the main folder:
  In case you are using Windows:
  
  ```
  set FLASK_APP=app/
  ```
  
  or in case you are using Linux or Mac:
  
  ```
  export FLASK_APP=app/
  ```

- Finally, **run the app**:
  
  ```
  flask run
  ```
  
  This will start the backend server on `localhost:5000`.

## Backend API

### Models:

The models will be used to create the database tables. This are some rules that the models must follow:

- An User is identified by an username and have a password. 
- An User can have many Expenses. An expense is identified by a date and a username. It has a category, a value and a description.
- An User can configure a Budget per day. A budget is identified by an id and a username. It has a value and a date. A budget can be repeated weekly, monthly, or not repeated at all.
- An User have a Saving per day. A saving is identified a username and a date and has a value. It will increment every day if the user have a budget configured and if the user have expenses less than the budget.
- An User can create many Categories that are only available for that user. A category is identified by an username and a name.
- An expense can have many categories. A category can be used by one or many expenses.
- A budget is only active between the start date and the end date. If the end date is not set, the budget will be active until the user deletes it.
- A budget cannot conflict with another budget. If the user tries to create a budget that conflicts with another budget, the new budget will not be created. The user will be notified about the conflict and will be able to delete the old budget or change the dates of the new budget.
- If a day does not have a budget configured, the saving will be 0 for that day. Also if the user have expenses greater than the budget, the saving will be negative.

Following this rules, the models have this behavior:

```mermaid
erDiagram
    User ||--o{ Expense : has
    User ||--o{ Budget : has
    User ||--o{ Saving : has
    User ||--o{ Category : has
    Expense }o--|| Category : has
    Budget }o--|| Category : has
    Budget }o--|| Saving : has
```

From the diagram we can set the models:

- User model, with the fields: username and password.

  | User |          |        |
  | ---- | -------- | ------ |
  | PK   | username | string |
  |      | password | string |

- Expense model, with the fields: username, date, value, description and category_name.
  
  | Expense |               |        |
  | ------- | ------------- | ------ |
  | FK      | username      | string |
  | FK      | date          | date   |
  |         | value         | float  |
  |         | description   | string |
  | FK      | category_name | string |

- Budget model, with the fields: id, username, value, start_date, end_date.
  
  | Budget |            |        |
  | ------ | ---------- | ------ |
  | PK     | id         | int    |
  | PK, FK | username   | string |
  |        | value      | float  |
  |        | start_date | date   |
  |        | end_date   | date   |

- Saving model, with the fields: username, date and value.
  
  | Saving |          |        |
  | ------ | -------- | ------ |
  | PK, FK | date     | date   |
  | PK, FK | username | string |
  |        | value    | float  |

- Category model, with the fields: name and username.
  
  | Category |          |        |
  | -------- | -------- | ------ |
  | PK       | name     | string |
  | FK       | username | string |

### Endpoints:

The endpoints will be used to interact with the database. So they have to follow the models rules. 

- `/user`:
  
  - `GET`: Get the current user.
  - `POST`: Create a new user.
  - `PUT`: Update the current user.
  - `DELETE`: Delete the current user.

- `/Expense`:
  
  - `GET`: Get all the expenses of the current user.
  - `POST`: Create a new expense for the current user.
  - `PUT`: Update an expense of the current user.
  - `DELETE`: Delete an expense of the current user.

- `/Budget`:
  
  - `GET`: Get all the budgets of the current user.
  - `POST`: Create a new budget for the current user.
  - `PUT`: Update a budget of the current user.
  - `DELETE`: Delete a budget of the current user.

- `/Saving`:
  
  - `GET`: Get all the savings of the current user.
  - `POST`: Create a new saving for the current user.
  - `PUT`: Update a saving of the current user.
  - `DELETE`: Delete a saving of the current user.

- `/Category`:
  
  - `GET`: Get all the categories of the current user.
  - `POST`: Create a new category for the current user.
  - `PUT`: Update a category of the current user.
  - `DELETE`: Delete a category of the current user.
