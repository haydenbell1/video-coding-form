# Video Coding Form

A research tool designed for systematically reviewing and coding scraped TikTok videos about schizophrenia content. This application provides an objective interface for researchers to analyze video content while reviewing associated comments and metadata.

## Overview

This application was developed to support qualitative research on schizophrenia-related content shared across social media platforms. It enables multiple researchers to independently review and code the same video content in a standardized format, with the ability to merge findings for comprehensive analysis.

## Demo

Watch the demo video to see the coding interface in action:

[Click here to watch the demo video](QIMR_coding_interface.mp4)

## Key Features

- **Objective Interface**: View video content and associated metadata in a structured, neutral interface
- **Comment Review**: Analyze comments and user responses alongside video content
- **Multi-Researcher Support**: Multiple researchers can simultaneously open and code the same videos independently
- **Data Aggregation**: Easily merge coding results from multiple researchers for comprehensive analysis
- **Structured Data Export**: Compiled video and coding data available in JSON format

## Getting Started

### Requirements

- Python 3.7+
- Flask (for server)
- Modern web browser (Chrome, Firefox, Safari, Edge)

### Installation

1. Clone this repository
2. Install dependencies:
   ```bash
   python Setup.py
   ```

3. Start the application:
   ```bash
   python start_server.py
   ```

4. Open your browser and navigate to `http://localhost:5000`

### Running the Executable

Alternatively, you can run the pre-built executable:
- Double-click `VideoCodingApp.exe` to launch the application directly

## Usage

1. **Load Data**: The application loads video and comment data from `combined_tiktok_data.json`
2. **Review Content**: View each video and its associated comments in the Form.html interface
3. **Code Videos**: Apply your coding schema to classify and analyze content
4. **Export Results**: Your coding data is saved and can be merged with other researchers' work

## File Structure

- `VideoCodingApp.exe` - Standalone executable (pre-built)
- `Form.html` - Web interface for video coding
- `start_server.py` - Flask server initialization
- `Setup.py` - Installation and dependency configuration
- `build.py` - Build script for creating the executable
- `combined_tiktok_data.json` - Research dataset (videos and comments)
- `VideoCodingApp.spec` - PyInstaller specification for building executable
- `QIMR_coding_interface.mp4` - Demo video of the coding interface

## Data

The `combined_tiktok_data.json` file contains the compiled TikTok video data used in this research, including:
- Video metadata
- Associated comments and engagement metrics
- Coded data from multiple researchers

## Research Purpose

This tool was created to facilitate systematic, objective review of social media content related to mental health topics. By providing a standardized interface and enabling collaborative coding, it ensures consistency and rigor in qualitative research analysis.

## License

[Add your license information here]

## Contact

For questions or collaboration inquiries, please contact the research team.

---

*This tool was developed to support ethical, IRB-approved research on social media content.*
