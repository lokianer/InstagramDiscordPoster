import instaloader
import discord
from discord.ext import tasks
import os
import json
from dotenv import load_dotenv

load_dotenv()
bot = instaloader.Instaloader()

# use .env file to store your credentials
bot.login(os.getenv('INSTAGRAM_USERNAME'), os.getenv('INSTAGRAM_PASSWORD'))

# The class that will be used to create the Discord Client
class MyClient(discord.Client):
    # The constructor of the class
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    # The function that will be called when the bot is ready
    async def on_ready(self):
        print('Logged on as', self.user)
    
    # A hook that will be called when the bot is ready
    async def setup_hook(self) -> None:
        self.check_for_new_post.start()

    # This function will be called every 5 minutes. You can change the time by changing the seconds parameter
    # This will check if there is a new post for each account and if there is, it will send a message to the channel you want
    @tasks.loop(seconds=300)
    async def check_for_new_post(self):
        # You can add more accounts to the list if you want
        accounts = ['Name1', 'Name2', 'Name3']
        print('checking for new posts')

        for account in accounts:
            profile = instaloader.Profile.from_username(bot.context, account)
            posts = profile.get_posts()
            post = next(posts)

            post_details = {}
            post_details['username'] = post.owner_username
            post_details['caption'] = post.caption
            post_details['hashtags'] = post.caption_hashtags
            post_details['media'] = post.url
            post_details['shortcode'] = post.shortcode

            # You can modify this part if you want to use a database instead of a file, but I think it's easier to use a file
            try:
                with open('old_posts.json', 'r') as f:
                    old_posts = json.load(f)
            except:
                old_posts = {}
            
            if old_posts.get(account, {}).get('media', None) != post_details['media']: 
                old_posts[account]['media'] = post_details['media']
                with open('old_posts.json', 'w') as f:
                    json.dump(old_posts, f)

                the_posts = post_details
                print(f'new post for {account}')
                # You can change the channel id to the channel you want
                channel = client.get_channel()
                # The embed that will be sent
                # You can change the color of the embed by changing the value of the color parameter
                embed = discord.Embed(
                    title="New Post by " + the_posts['username'],
                    url="https://instagram.com/" + the_posts['username'],
                    description=the_posts['caption'],color=0xdb2777)
                embed.set_author(name='Link to Post', url="https://instagram.com/p/"+the_posts['shortcode'])
                embed.set_thumbnail(url="https://allfacebook.de/wp-content/uploads/2020/02/ig-logo-normal.png")
                embed.set_image(url=the_posts['media'])
                await channel.send(embed=embed)
            else:
                print(f'no new post for {account}')
    # This function will be called before the loop starts
    # Just a security measure to make sure the bot is ready before the loop starts
    @check_for_new_post.before_loop
    async def before_check_for_new_post(self):
        await self.wait_until_ready()
        print('finished waiting')

# Creating the client
intents = discord.Intents.default()
intents.message_content = True
client = MyClient(intents=intents)
# add the token of your bot
client.run(os.getenv('DISCORD_TOKEN'))          
