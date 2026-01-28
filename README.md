# Crowdfunding Back End
Shannon Lowe

## Planning:
### Concept/Name
The I Just Need One Thing Fund
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
{{ Fill out the table below to define your endpoints. An example of what this might look like is shown at the bottom of the page. 

It might look messy here in the PDF, but once it's rendered it looks very neat! 

It can be helpful to keep the markdown preview open in VS Code so that you can see what you're typing more easily. }}

| URL | HTTP Method | Purpose | Request Body | Success Response Code | Authentication |
|----|------------|--------|--------------|----------------------|----------------|
| `/users/` | POST | Create a new user account | username, email, password | 201 Created | None |
| `/users/` | GET | Get all users | None | 200 OK | None |
| `/users/<id>/` | GET | Get a specific user | None | 200 OK | None |
| `/fundraisers/` | POST | Create a new fundraiser | title, description, goal, image, is_open | 201 Created | Token |
| `/fundraisers/` | GET | Get all fundraisers | None | 200 OK | None |
| `/fundraisers/<id>/` | GET | Get a specific fundraiser | None | 200 OK | None |
| `/pledges/` | POST | Create a pledge | amount, comment, anonymous, fundraiser | 201 Created | Token |
| `/pledges/` | GET | Get all pledges | None | 200 OK | None |
| `/api-token-auth/` | POST | Obtain authentication token | username, password | 200 OK | None |

### DB Schema
![]( {{ ./relative/path/to/your/schema/image.png }} )

