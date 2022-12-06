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
