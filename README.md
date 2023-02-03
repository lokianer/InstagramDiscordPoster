# InstagramDiscordPoster
A Python script, that searches the new post of a specific Instagram Account and post it on a specific Discord Channel.

## Requirements
- Python 3.10 or higher
- (instaloader)[https://instaloader.github.io/]
- (discord.py)[https://discordpy.readthedocs.io/en/stable/]
- python-dotenv
- A Discord Bot Token
- An Instagram Account
- The old_post.json file is needed for the script to work. It has to be in the same directory as the script. Modify the file to your needs.

## Installation
1. Install Python 3.10 or higher
2. Install instaloader, discord.py and python-dotenv via pip
3. Create a (Discord Bot)[https://discord.com/developers/applications] and copy the Token
4. Create a (Instagram Account)[https://www.instagram.com/accounts/emailsignup/] and copy the Username and Password
5. Create a .env file and add the following lines:
  * INSTAGRAM_USERNAME='THE_USERNAME_OF_YOUR_INSTAGRAM_ACCOUNT'
  * INSTAGRAM_PASSWORD='THE_PASSWORD_OF_YOUR_INSTAGRAM_ACCOUNT'
  * DISCORD_TOKEN='THE DISCORD BOT TOKEN'
1. Add the Channel ID of the Discord Channel you want to post the Instagram Posts to the script. Line 63. (channel = client.get_channel(CHANNEL_ID)) (How to get the Channel ID)[https://support.discord.com/hc/en-us/articles/206346498-Where-can-I-find-my-User-Server-Message-ID-] (For some reason, the Channel ID does not work in the .env file)
2. Run the script

Feel free to report any bugs or issues.
