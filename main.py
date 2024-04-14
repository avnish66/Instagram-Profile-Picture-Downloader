import instaloader

ig=instaloader.Instaloader()
dp=input("enter insta username: ")

ig.download_profile(dp,profile_pic_only=True)