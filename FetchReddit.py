import praw

# Initialize the Reddit client
reddit = praw.Reddit(
    client_id='KBXj5qzAesIfg3pSgiEcEg',
    client_secret='LtcJnMCMu6Hsmd6vsyDpQDLgu7AyTA',
    user_agent='TestAIApp/0.1 by Dababab_yes'
)

# Function to get top post title and selftext
def get_top_post(subreddit_name):
    subreddit = reddit.subreddit(subreddit_name)
    top_post = next(subreddit.top(time_filter='day', limit=1))  # Get top post
    return top_post.title, top_post.selftext

# List of subreddits to pull data from
subreddits = ['AmItheAsshole', 'relationship_advice']
