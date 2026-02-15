# Crowdfunding Back End
Shannon Lowe

## Planning:
### Concept/Name
My Shot Fund
(I am not throwin' away my shot
Ayo, I'm just like my country
I'm young, scrappy and hungry
And I'm not throwin' away my shot)

A fundraising program that you can only use once. What is the one thing you need to get your life together?
A new office chair? A plane ticket to get away? A new Mattress? A gym membership for a year?
Each idea would have to be verified manually before being allowed.

### Intended Audience/User Stories
People who just need a one chance to change their daily lives in a simple way

### Front End Pages/Functionality
- {{ A page on the front end }}
    - {{ A list of dot-points showing functionality is available on this page }}
    - {{ etc }}
    - {{ etc }}
- {{ A second page available on the front end }}
    - {{ Another list of dot-points showing functionality }}
    - {{ etc }}

### API Spec

| URL                  | HTTP Method | Purpose                                  | Request Body                                       | Success Response Code | Authentication |
| -------------------- | ----------- | ---------------------------------------- | -------------------------------------------------- | --------------------- | -------------- |
| `/users/`            | POST        | Create a new user account                | `username`, `email`, `password`                    | 201 Created           | None           |
| `/users/`            | GET         | Get all users                            | None                                               | 200 OK                | None           |
| `/users/<id>/`       | GET         | Get a specific user                      | None                                               | 200 OK                | None           |
| `/api-token-auth/`   | POST        | Obtain auth token + user details         | `username`, `password`                             | 200 OK                | None           |
| `/fundraisers/`      | GET         | Get all fundraisers                      | None                                               | 200 OK                | None           |
| `/fundraisers/`      | POST        | Create a new fundraiser                  | `title`, `description`, `goal`, `image`, `is_open` | 201 Created           | Token          |
| `/fundraisers/<id>/` | GET         | Get fundraiser detail (includes pledges) | None                                               | 200 OK                | None           |
| `/fundraisers/<id>/` | PATCH       | Update fundraiser (owner or admin)       | Any fundraiser fields (partial)                    | 200 OK                | Token          |
| `/fundraisers/<id>/` | DELETE      | Delete fundraiser (owner or admin)       | None                                               | 204 No Content        | Token          |
| `/pledges/`          | GET         | Get all pledges                          | None                                               | 200 OK                | None           |
| `/pledges/`          | POST        | Create a pledge                          | `amount`, `comment`, `anonymous`, `fundraiser`     | 201 Created           | Token          |
| `/pledges/<id>/`     | DELETE      | Delete a pledge (supporter only)         | None                                               | 204 No Content        | Token          |


### DB Schema

![Users Table](./imgs/db-users.PNG)
![Fundraisers Table](./imgs/db-fundraisers.PNG)

## API Testing Evidence

Below is proof that each endpoint works correctly, including authentication, permissions, and business rules.


### Create User – 201 Created

![Create User](./imgs/insomnia-post-users-201.PNG)


### Get All Fundraisers – 200 OK

![Get Fundraisers](./imgs/insomnia-get-fundraisers-200.jpeg)


### Create Fundraiser (Without Token) – 401 Unauthorized

![Create Fundraiser No Token](./imgs/insomnia-post-fundraiser-no-token-401.png)


### Create Fundraiser (Success) – 201 Created

![Create Fundraiser Success](./imgs/insomnia-post-fundraiser-success-201.png)


### Business Rule – Only One Pending/Approved Fundraiser – 400 Bad Request

![Fundraiser One Rule](./imgs/insomnia-post-fundraisers-400-one-rule.PNG)



### Patch Fundraiser (Admin) – 200 OK

![Patch Fundraiser Admin](./imgs/insomnia-patch-fundraiser-admin-200.jpeg)


### Patch Fundraiser (User Forbidden) – 403 Forbidden

![Patch Fundraiser User Forbidden](./imgs/insomnia-patch-fundraiser-user-403.jpeg)



### Create Pledge – 201 Created

![Create Pledge Success](./imgs/insomnia-post-pledges-201-success.jpeg)



### Pledge Rejected – Fundraiser Closed – 400 Bad Request

![Pledge Closed](./imgs/insomnia-post-pledges-400-closed.jpeg)



### Pledge Rejected – Fundraiser Not Approved – 400 Bad Request

![Pledge Not Approved](./imgs/insomnia-post-pledges-400-not-approved.PNG)



### Obtain Authentication Token – 200 OK

![Token Authentication](./imgs/insomnia-post-token-200.jpeg)



### Backend API
https://crowdfunding-ijustneedonething-06a0f674c900.herokuapp.com/


###  How to Register a New User + Create a Fundraiser (Step-by-step)

> Base URL (local): `http://127.0.0.1:8000`

#### 1 Register a new user
**Endpoint:** `POST /users/`  
**Auth:** None  
**Body (JSON):**
```json
{
  "username": "Tester1",
  "email": "testuser@example.com",
  "password": "password123"
}
```

#### 2 Obtain an Authentication Token
**Endpoint:** `POST /api-token-auth/`  
**Auth:** None
**Body (JSON):**
```json
{
  "username": "Tester1",
  "password": "_ENTER_USERPASS"
}
```

#### 3 Create a New Fundraiser
**Endpoint:** `POST /fundraisers/`  
**Auth:** Token (Bearer)
**Body (JSON):**
```json

{
  "title": "Tester1 fundraiser",
  "description": "Tester1 this is just blah blah blah gimme monies",
  "goal": 500,
  "image": "https://h5p.org/sites/default/files/h5p/content/825/images/image-53e9e42b9ba63.jpg",
  "is_open": true
}
```