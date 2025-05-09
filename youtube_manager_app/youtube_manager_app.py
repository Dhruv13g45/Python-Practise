import json  ##for json format data accessing


def load_data():
    try:
        with open("youtube_manager_data.txt","r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []


def save_youtube_video(videos):
    with open("youtube_manager_data.txt",'w') as file:
        json.dump(videos,file)


def display_youtube_video_list(videos):
    for index,video_info in enumerate(videos,start=1):
        print(f"{index}. video name: {video_info['name']} video timeframe: {video_info['time_frame']}")

def add_youtube_video(videos):
    video_name = input("\nEnter your youtube video name: ")
    video_time = input("\nEnter your youtube video time length: ")

    videos.append({'name':video_name, 'time_frame' : video_time})
    save_youtube_video(videos)
    print("\n Your youtube video is added in your list\n")


def update_video_info(videos):
    display_youtube_video_list(videos)
    user_update_choice = int(input("\nEnter the index number of video you want to update or change information of: "))

    for index,video_info in enumerate(videos,start=1):
        if index == user_update_choice:
            updated_video_name = input("\nEnter the udpated name of the video: ")
            updated_video_time_frame = input("\nEnter the updated time frame: ")
            video_info['name'] = updated_video_name
            video_info['time_frame'] = updated_video_time_frame
            save_youtube_video(videos)
            print("the video list has been updated succesfully")

def delete_youtube_video(videos):
    display_youtube_video_list(videos)
    user_delete_choice = int(input("\nEnter the index number of the video you want to delete: "))
    del videos[user_delete_choice - 1]
    save_youtube_video(videos)
    print("\nYoutube video deleted succefully")



def main():
    videos = load_data()
    while True:
        print("Youtube Manager App\n")
        print("1. See your list of youtube videos\n")
        print("2. Add a new youtube video to your list\n")
        print("3. Update a youtube video detail from the list\n")
        print("4. Delete a youtube video from the list\n")
        user_choice = int(input("Enter your choice: "))

        match user_choice:
            case 1 : 
                display_youtube_video_list(videos)
            case 2:
                add_youtube_video(videos)
            case 3:
                update_video_info(videos)
            case 4:
                delete_youtube_video(videos)
            case _:
                print("Invalid selection !!")

if __name__ == "__main__":
    main()