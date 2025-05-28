import json

file_name = "Youtube.txt"
def load_data():
    try:
        with open(file_name,'r') as file:
            return json.load(file) # deserialize
    except FileNotFoundError:
        return []
    # finally:
    #     pass

def save_data_helper(videos):
    with open(file_name, 'w') as file:
        json.dump(videos, file) # serialize

def list_all_videos(videos):
    for index, video in enumerate(videos, start=1):
        print(f"{index} : {video}")

def add_video(videos):
    video_name = input("Enter video name : ")
    videos_time = input("Enter video time : ")
    videos.append({'name':video_name, 'time': videos_time})
    save_data_helper(videos)

def update_video(videos):
    pass

def delete_video(videos):
    pass

def main():
    videos = load_data()
    while True:
        print("Choose the following options:")
        print("1. List of all the fav. videos")
        print("2. Add new video to the list")
        print("3. Update the video list")
        print("4. Delete the video")
        print("5. Exit")
        
        # print(videos)
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