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
    # Use the directory of the executable if frozen (packaged .exe)
    current_dir = os.path.dirname(sys.executable)
else:
    # Use the script directory when running normally
    current_dir = os.path.dirname(os.path.abspath(__file__))

# Change to the directory containing form.html and combined_tiktok_data.json
os.chdir(current_dir)

DATA_FILE = os.path.join(current_dir, 'combined_tiktok_data.json')

# Custom Handler to Handle POST Requests for Saving Data
class CustomHandler(http.server.SimpleHTTPRequestHandler):
    def do_POST(self):
        if self.path == '/save-data':
            content_length = int(self.headers['Content-Length'])  # Get content length
            post_data = self.rfile.read(content_length)  # Read POST data

            try:
                # Parse the received JSON data
                updated_data = json.loads(post_data)

                # Write the updated data to the JSON file
                with open(DATA_FILE, 'w', encoding='utf-8') as json_file:
                    json.dump(updated_data, json_file, ensure_ascii=False, indent=4)

                # Send a success response
                self.send_response(200)
                self.send_header('Content-type', 'application/json')
                self.end_headers()
                self.wfile.write(b'{"status": "success", "message": "Data updated successfully!"}')
            except Exception as e:
                self.send_response(500)
                self.send_header('Content-type', 'application/json')
                self.end_headers()
                self.wfile.write(f'{{"status": "error", "message": "{e}"}}'.encode())
        else:
            super().do_POST()

# Start the server
with socketserver.TCPServer(("", PORT), CustomHandler) as httpd:
    print(f"Serving at http://localhost:{PORT}")

    # Automatically open form.html in the browser
    webbrowser.open(f"http://localhost:{PORT}/form.html")

    # Start serving
    httpd.serve_forever()
