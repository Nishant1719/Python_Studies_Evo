import sqlite3

conn = sqlite3.connect('youtube_videos.db')
cursor = conn.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS videos (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        time TEXT NOT NULL
    )               
""")

def list_all_videos():
    cursor.execute("""SELECT * FROM videos""") # Returns tuple
    for row in cursor.fetchall():
        print("ROW  :",row)

def add_video(name, time):
    cursor.execute("""
    INSERT INTO videos (name,time) VALUES (?, ?)
    """,(name,time,))
    conn.commit()
    
def update_video(video_id, new_name, new_time):
    cursor.execute(""" 
    UPDATE videos SET name = ?, time = ? WHERE id = ?
    """, (new_name, new_time, video_id))
    conn.commit()


def delete_video(id):
    cursor.execute("""
    DELETE FROM videos WHERE id = ?
    """,(id,))
    conn.commit()
    

def main():
    while True:
        print("\n")
        print("Youtube manager with DB")
        print("1. List of all the fav. videos")
        print("2. Add new video to the list")
        print("3. Update the video list")
        print("4. Delete the video")
        print("5. Exit")
        
        choice =  input("Please Enter Your Choice : ")
        if choice == '1':
            list_all_videos()
        elif choice == '2':
            name = input("Enter the video name : ")
            time = input("Enter the video time : ")
            add_video(name,time)
        elif choice == '3':
            video_id = input("Enter the video Id to update : ")
            name = input("Enter the video name : ")
            time = input("Enter the video time : ")
            update_video(video_id,name,time)
        elif choice == '4':
            video_id = input("Enter the video Id to update : ")
            delete_video(video_id)
        elif choice == '5':
            break
        else:
            print("Invalid Choice!")  
                  
    conn.close() # To make sure db dont go corrupts (Good practice).
if __name__ == "__main__":
    main()