Backend of lets-ride app 
created using python-Django and Django Rest Framework

=====================================================================

APIs

/users/ - creating and getting the users

users/me/ - getting current logged in user and update details

/token/login/ - get token on login

token/logout/ - logout and destroy token

/api/rider/ - get all rider details/ create new rider (get/post)

/api/requester/ - get/create request details (get/post)

api/my-requests/?asset_type=LAPTOP&ordering=-date_time - get current user requests details (get/filter on asset type and sort data on date)

/api/user-requests-matched/ - All rider-requester matched details of current user (get)

/api/user-request-update/pk/ - Update the requests on user applying to matched requests (put/patch)


=====================================================================


Frontend created in Reactjs and material UI which consumes above APIs

=====================================================================

Screenshots:

Login Screen:
![image](https://user-images.githubusercontent.com/51402396/205983024-b3631467-0105-4957-98f6-e24cb469a36c.png)

Dashboard
![image](https://user-images.githubusercontent.com/51402396/205982501-2ee34c46-f53a-4772-a031-2e88fd7c2b7c.png)

Rider Screen
![image](https://user-images.githubusercontent.com/51402396/205982631-e9332bcc-003c-476e-961c-d6639a876069.png)

Requester Screen
![image](https://user-images.githubusercontent.com/51402396/205982907-c6e2d092-8b34-44e0-b0ca-71233e1df7fa.png)


