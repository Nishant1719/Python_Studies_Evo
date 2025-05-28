def list_all_videos():
    pass

def add_video():
    pass

def update_video():
    pass

def delete_video():
    pass

videos = []

def main():
    while True:
        print("Choose the following options:")
        print("1. List of all the fav. videos")
        print("2. Add new video to the list")
        print("3. Update the video list")
        print("4. Delete the video")
        print("5. Exit")
        
        choice =  input("Please Enter Your Choice")
        match choice:
            case '1':
                list_all_videos(videos)
            case '2':
                add_video(videos)
            case '3':
                update_video(videos)
            case '4':
                delete_video(videos)
            case '5':
                break
            case _:
                print("Invalid Choice!")

# This is a common Python idiom that allows the script to be run as a standalone program or imported as a module without executing the main function.
if __name__ == "__main__":
    main() 