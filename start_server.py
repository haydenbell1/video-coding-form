import http.server
import socketserver
import webbrowser
import os
import sys
import json

# Configuration
PORT = 8000

# Change directory to the location of the script
if getattr(sys, 'frozen', False):
    current_dir = os.path.dirname(sys.executable)
else:
    current_dir = os.path.dirname(os.path.abspath(__file__))

os.chdir(current_dir)

DATA_FILE = os.path.join(current_dir, 'combined_tiktok_data.json')

class CustomHandler(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        # Add CORS headers
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        super().end_headers()

    def do_POST(self):
        if self.path == '/save-data':
            try:
                # Get content length and read the data
                content_length = int(self.headers['Content-Length'])
                post_data = self.rfile.read(content_length).decode('utf-8')
                
                # Debug: Print the received data
                print("\n=== Received Data ===")
                print(post_data[:500])
                
                # Parse the incoming JSON data
                update_data = json.loads(post_data)
                
                # Handle the data based on its type
                if isinstance(update_data, list):
                    if not update_data:
                        raise ValueError("Empty data received")
                    current_video = update_data[0]
                    video_id = current_video.get('id')
                    new_coding = current_video.get('coding', {})
                else:
                    # Assume it's a dictionary
                    video_id = update_data.get('videoId')
                    new_coding = update_data.get('coding', {})

                if not video_id:
                    raise ValueError("No video ID found in update data")
                
                # Read the existing file
                with open(DATA_FILE, 'r', encoding='utf-8') as f:
                    all_videos = json.load(f)
                
                # Find and update the matching video
                found_video = False
                for i, video in enumerate(all_videos):
                    if video['id'] == str(video_id):  # Convert to string for comparison
                        found_video = True
                        print(f"\nFound matching video ID: {video['id']}")
                        
                        # Initialize coding if it doesn't exist
                        if 'coding' not in all_videos[i]:
                            all_videos[i]['coding'] = {}
                        
                        print("\nNew coding data:", json.dumps(new_coding, indent=2))
                        
                        # Update the coding data
                        for user, data in new_coding.items():
                            all_videos[i]['coding'][user] = data
                        
                        print(f"\nUpdated coding data for video {video['id']}")
                        break
                
                if not found_video:
                    raise ValueError(f"Could not find video with ID {video_id}")

                # Write the updated data back to file
                print("\n=== Writing to File ===")
                with open(DATA_FILE, 'w', encoding='utf-8') as f:
                    json.dump(all_videos, f, ensure_ascii=False, indent=4)
                print("Successfully wrote to file")

                # Send success response
                self.send_response(200)
                self.send_header('Content-type', 'application/json')
                self.end_headers()
                self.wfile.write(json.dumps({
                    "status": "success",
                    "message": "Data updated successfully!"
                }).encode())

            except Exception as e:
                print("\n=== Error Details ===")
                print(f"Error Type: {type(e)}")
                print(f"Error Message: {str(e)}")
                import traceback
                print("\nFull traceback:")
                traceback.print_exc()
                
                self.send_response(500)
                self.send_header('Content-type', 'application/json')
                self.end_headers()
                self.wfile.write(json.dumps({
                    "status": "error",
                    "message": f"Error saving data: {str(e)}. Please try again."
                }).encode())
        else:
            super().do_POST()

# Enable port reuse
socketserver.TCPServer.allow_reuse_address = True

# Start the server
try:
    with socketserver.TCPServer(("", PORT), CustomHandler) as httpd:
        print(f"\n=== Server Starting ===")
        print(f"Server running at http://localhost:{PORT}")
        print(f"Data file: {DATA_FILE}")
        print("\nPress Ctrl+C to stop the server")
        
        webbrowser.open(f"http://localhost:{PORT}/form.html")
        httpd.serve_forever()
except KeyboardInterrupt:
    print("\nShutting down server...")
    sys.exit(0)
except Exception as e:
    print(f"\nError starting server: {str(e)}")
    sys.exit(1)