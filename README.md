# google-drive-invite [![](https://img.shields.io/github/stars/roharon/google-drive-invite.svg?style=social)](https://github.com/roharon/google-drive-invite/stargazers) ![](https://img.shields.io/github/last-commit/roharon/google-drive-invite) ![Heroku](https://heroku-badge.herokuapp.com/?app=heroku-badge&svg=1)

[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy)

Just share this web! You can invite member *without your hands*😎

<img style="display:block margin:auto" src="https://user-images.githubusercontent.com/4939738/72342036-108dff80-370f-11ea-8dca-e100a9b78f0e.png" width="400" height="400">


## Getting started

You can deploy google-drive-invite web with heroku.

### With Heroku

Should enter google api key

#### How to get Google API Token

1. Create New Project

<img style="display:block margin:auto" src="https://user-images.githubusercontent.com/4939738/72342241-61055d00-370f-11ea-9116-0978083e7cc1.png" width="500" height="300">


2. Go to Credentials Tab and **Create credentials**

<img style="display:block margin:auto" src="https://user-images.githubusercontent.com/4939738/72213777-4b8a0a80-3538-11ea-98b8-960f236d67e7.png" width="500" height="300">


3. **If this is your first credentials**, then Configure Consent screen. You should set some information.

> If you have other credentials already, then skip to ***8***

4. Select ***External*** and click CREATE

<img style="display:block margin:auto" src="https://user-images.githubusercontent.com/4939738/72213954-732ea200-353b-11ea-910d-7a7a980e4613.png" width="500" height="300">


5. Enter ***Application name***

<img style="display:block margin:auto" src="https://user-images.githubusercontent.com/4939738/72213994-4d55cd00-353c-11ea-8b32-b686900f1e90.png" width="500" height="300">

6. Select ***Web application***, Enter the Name to identify.

And, Input the ***URL*** on ***Authorized redirect URIs***
> URL : `https://developers.google.com/oauthplayground`

<img style="display:block margin:auto" src="https://user-images.githubusercontent.com/4939738/72214605-1934d900-3549-11ea-9922-7a53ee26cb4c.png" width="500" height="300">


7. You can find Credentials created.
Click the Name to get the credentials's more information

<img style="display:block margin:auto" src="https://user-images.githubusercontent.com/4939738/72214096-770ff380-353e-11ea-87f0-536e136414a4.png" width="500" height="400">

8. Copy ***Client ID*** and ***Client secret***.
It will be used to config deploy enviroment variable

<img style="display:block margin:auto" src="https://user-images.githubusercontent.com/4939738/72214688-85640c80-354a-11ea-81d9-9485ecb53e15.png" width="500" height="400">

9-1. Go to [https://developers.google.com/oauthplayground/](https://developers.google.com/oauthplayground/)

9-2. Paste ***Client ID, Secret*** on OAuth 2.0 Configuration(check Use Your own Oauth credentials) - On right section.

9-3.Select ***Drive API V3's*** *`https://www.googleapis.com/auth/drive`*, *`https://www.googleapis.com/auth/drive.file`*

And, Click **Authorize APIs** Button!


9-4. Click **`Exchange authorization code for tokens`**

<img style="display:block margin:auto" src="https://user-images.githubusercontent.com/4939738/72214948-ada23a00-354f-11ea-809f-780fdeab5219.png" width="500" height="300">

You've got ***Authorization code***, ***Refresh token***

Use all of token to heroku deploy!