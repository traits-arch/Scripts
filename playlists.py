import csv
import sys
import time
from ytmusicapi import YTMusic

def import_single_playlist(yt, csv_path, playlist_name):
    print(f"\n==============================================")
    print(f"--- Starting Import for: {playlist_name} ---")
    print(f"==============================================")
    
    print("Creating playlist on YouTube Music...")
    try:
        playlist_id = yt.create_playlist(playlist_name, "Imported via automated local script")
        time.sleep(3) 
    except Exception as e:
        print(f"❌ Failed to create playlist '{playlist_name}': {e}")
        return

    added_count = 0
    missing_songs = []
    
    try:
        with open(csv_path, mode='r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                track_name = row.get('Track Name')
                artist_name = row.get('Artist Name(s)')
                
                if track_name and artist_name:
                    search_query = f"{track_name} {artist_name}"
                    
                    try:
                        search_results = yt.search(search_query, filter="songs")
                        
                        video_id = None
                        if isinstance(search_results, list) and len(search_results) > 0:
                            video_id = search_results[0]['videoId']
                        elif isinstance(search_results, dict) and 'videoId' in search_results:
                            video_id = search_results['videoId']
                        
                        if video_id:
                            # INSTANT ADD: Push the song to the playlist right now
                            yt.add_playlist_items(playlist_id, [video_id])
                            added_count += 1
                            print(f"✅ [ADDED TO PLAYLIST] -> {search_query}")
                        else:
                            print(f"⚠️ [NOT FOUND]         -> {search_query}")
                            missing_songs.append(search_query)
                        
                        # A solid human-like pause between tracks
                        time.sleep(1.5) 
                        
                    except Exception as e:
                        print(f"⚠️ [SERVER ERROR]      -> {search_query} (Retrying layout drop...)")
                        missing_songs.append(search_query)
                        time.sleep(3.0) # Wait longer if the server pushes back
                        
    except FileNotFoundError:
        print(f"❌ Error: Could not find file at {csv_path}")
        return

    print(f"\n🎉 Finished processing '{playlist_name}'! Successfully populated {added_count} tracks directly.")

    if missing_songs:
        print(f"\n❌ Summary of skipped/unfound tracks:")
        for song in missing_songs:
            print(f"   - {song}")
    
    print(f"\nResting for 10 seconds before starting the next file...\n")
    time.sleep(10)

def main():
    try:
        yt = YTMusic('browser.json')
    except Exception as e:
        print(f"Error loading browser.json: {e}")
        sys.exit(1)

    # Your exact targeted playlists
    playlists_to_import = [
        {"csv": "/home/xal/Downloads/Français.csv", "name": "Français"},
        {"csv": "/home/xal/Downloads/Indo-indie.csv", "name": "Indo"},
        {"csv": "/home/xal/Downloads/Soft-hop.csv", "name": "Hope"}
    ]

    for pl in playlists_to_import:
        import_single_playlist(yt, pl["csv"], pl["name"])

if __name__ == "__main__":
    main()
