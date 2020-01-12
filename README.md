# google-drive-invite [![](https://img.shields.io/github/stars/roharon/google-drive-invite.svg?style=social)](https://github.com/roharon/google-drive-invite/stargazers)

[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy)

Invite memeber to *Google Drive shared folder/file* **easily & automate**!

## Getting started

You can deploy google-drive-invite web with heroku.

### With Heroku

Should enter google api key

1. Create New Project

![image](https://user-images.githubusercontent.com/4939738/72213740-935c6200-3537-11ea-8d84-763a67c13d1a.png)



2. Go to Credentials Tab and **Create credentials**

![image](https://user-images.githubusercontent.com/4939738/72213777-4b8a0a80-3538-11ea-98b8-960f236d67e7.png)


3. If this is your first credentials, then Configure Consent screen.

![image](https://user-images.githubusercontent.com/4939738/72213802-a3c10c80-3538-11ea-910b-e4f168298ffa.png)

4. Select ***External*** and click CREATE

![image](https://user-images.githubusercontent.com/4939738/72213954-732ea200-353b-11ea-910d-7a7a980e4613.png)


5. Enter ***Application name***

![image](https://user-images.githubusercontent.com/4939738/72213994-4d55cd00-353c-11ea-8b32-b686900f1e90.png)

6. Select ***Web application***, Enter the Name to identify.

And, Input the ***URL*** on ***Authorized redirect URIs***
> URL : `https://developers.google.com/oauthplayground`

![image](https://user-images.githubusercontent.com/4939738/72214605-1934d900-3549-11ea-9922-7a53ee26cb4c.png)


7. You can find Credentials created.
Click the Name to get the credentials's more information

![image](https://user-images.githubusercontent.com/4939738/72214096-770ff380-353e-11ea-87f0-536e136414a4.png)

8. Copy ***Client ID*** and ***Client secret***.
It will be used to config deploy enviroment variable

![image](https://user-images.githubusercontent.com/4939738/72214688-85640c80-354a-11ea-81d9-9485ecb53e15.png)


9-1. Go to [https://developers.google.com/oauthplayground/](https://developers.google.com/oauthplayground/)

9-2. Paste ***Client ID, Secret*** on OAuth 2.0 Configuration(check Use Your own Oauth credentials) - On right section.

9-3.Paste 
`https://www.googleapis.com/auth/drive.file` on left input Button.
Or you can select ***`Drive API V3 - ~~/auth/drive.file`***

And, Click **Authorize APIs** Button!

![image](https://user-images.githubusercontent.com/4939738/72214178-737d6c00-3540-11ea-970d-8a3269e86870.png)

9-4. Click **`Exchange authorization code for tokens`**

![image](https://user-images.githubusercontent.com/4939738/72214948-ada23a00-354f-11ea-809f-780fdeab5219.png)


You've got ***Authorization code***, ***Refresh token***

Use all of token to heroku deploy!