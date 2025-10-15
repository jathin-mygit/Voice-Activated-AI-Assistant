# Voice-Activated AI Assistant 🎙️🤖

A comprehensive Python-based voice assistant that can process voice commands to perform various tasks including web searches, system controls, note-taking, and more.

## 📋 Features

### 🔍 Wikipedia Search
- Say **"wikipedia Albert Einstein"** to get concise summaries (400 characters)
- Quick access to information on any topic

### 🌐 Website Navigation
- Say **"open YouTube"** or **"open Google"** 
- Automatically adds '.com' if missing from the command
- Seamless web browsing through voice commands

### 💻 System Control
- **Shutdown**: Say "shutdown" to turn off your computer
- **Restart**: Say "restart" to reboot your system  
- **Lock**: Say "lock" to lock your computer
- Cross-platform support (Windows/Linux)

### ⏰ Time Queries
- Ask **"what is the time?"** to hear the current time
- Real-time clock functionality

### 📝 Note Management
- **Add Notes**: Say "add note buy groceries" to save important reminders
- **List Notes**: Say "show notes" or "list notes" to hear recent notes
- Notes are stored in `voice_notes.txt` file

### 🗣️ Natural Interaction
- **Greetings**: Responds to "hello", "hi", "how are you"
- **Smart Command Matching**: Suggests closest known commands for unclear inputs
- **Graceful Exit**: Say "exit", "quit", or "bye" to close the assistant

## 🛠️ Installation

### Prerequisites
- Python 3.8 or above
- Working microphone
- Internet connection (for initial setup)

### Setup Steps

1. **Clone/Download** the project files

2. **Create Virtual Environment** (Recommended)
   ```bash
   python -m venv venv
   
   # On Windows
   venv\Scripts\activate
   
   # On macOS/Linux
   source venv/bin/activate
   ```

3. **Install Dependencies**
   ```bash
   pip install speechrecognition pyttsx3 wikipedia-api
   ```

## 🚀 Usage

### Running the Assistant
```bash
python python_project_updated.py
```

The assistant will:
- Greet you upon startup
- Begin listening for voice commands
- Process and respond to your requests

### Example Commands
- `"wikipedia Python programming"`
- `"open GitHub"`
- `"what is the time?"`
- `"add note meeting at 3 PM"`
- `"show notes"`
- `"shutdown"`

## ⚙️ Technical Features

### 🎛️ Audio Processing
- **Ambient Noise Adjustment**: Automatically calibrates for background noise
- **Efficient Listening**: Optimized phrase duration for better performance
- **Error Handling**: Graceful handling of API and network errors

### 🧠 Smart Recognition
- **Fuzzy Command Matching**: Suggests similar commands for unclear inputs
- **Cross-Platform Compatibility**: Works on Windows and Linux systems
- **Robust Error Management**: Handles recognition failures smoothly

### 💾 Data Management
- Notes stored in `voice_notes.txt`
- Persistent storage across sessions
- Easy access to recent notes (displays last 3 by default)

## 🔧 Customization

### Adding New Commands

You can easily extend the assistant's functionality by:

1. **Adding command logic** in the `process_command(cmd)` function
2. **Mapping commands** in the `COMMANDS` dictionary
3. **Creating corresponding functions** for new features

### File Structure
```
voice-assistant/
├── python_project_updated.py    # Main application file
├── voice_notes.txt              # Notes storage (created automatically)
├── README.md                    # This file
└── requirements.txt             # Dependencies list
```

## 📦 Dependencies

- **speechrecognition**: Voice input processing
- **pyttsx3**: Text-to-speech output  
- **wikipedia-api**: Wikipedia search functionality

## 🔧 Troubleshooting

### Common Issues
- **Microphone not detected**: Ensure microphone permissions are enabled
- **Internet connection**: Required for Wikipedia searches and initial setup
- **Voice recognition errors**: Speak clearly and ensure minimal background noise

### Performance Tips
- Use in a quiet environment for better recognition accuracy
- Speak at a moderate pace and volume
- Ensure stable internet connection for web-based features

## 🤝 Contributing

Feel free to contribute to this project by:
- Adding new voice commands
- Improving recognition accuracy
- Enhancing cross-platform compatibility
- Adding new integrations

## 📄 License

This project is open source and available under the MIT License.

---

**Enjoy your voice-activated AI assistant!** 🎉