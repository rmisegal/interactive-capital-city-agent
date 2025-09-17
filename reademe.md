# Interactive Capital City Agent

## 🎯 Project Description
This project demonstrates an interactive LLM agent built with Google's ADK (Agent Development Kit) and `google-generativeai` library. The agent can chat with users about capital cities, showing the complete sequence of operations including tool usage, memory access, and LLM calls.

### ✨ Features
- **Interactive Chat**: Real-time conversation with the agent
- **Operation Logging**: See every step (USER → MEMORY → LLM → TOOL → AGENT)
- **Demo Mode**: Automated demonstration of agent capabilities
- **Extended Database**: Supports multiple countries (Japan, France, Germany, Australia, etc.)
- **Error Handling**: Graceful fallbacks for unknown countries

---

## 📋 Prerequisites
- Python 3.8+
- Google Gemini API Key
- Git (for version control)
- WSL (Windows Subsystem for Linux) - recommended for development

---

## 🚀 Environment Setup

### Option 1: Windows Setup
```bash
# Create virtual environment
python -m venv .venv

# Activate virtual environment
.venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

### Option 2: WSL Setup (Recommended)
```bash
# Create virtual environment  
python3 -m venv .venv

# Activate virtual environment (fix line endings if needed)
dos2unix .venv/Scripts/activate
source .venv/Scripts/activate

# Install dependencies
.venv/Scripts/pip.exe install -r requirements.txt
```

---

## 🔑 API Key Configuration

### Method 1: Environment File (.env) - Recommended
1. Update the `.env` file in the project root:
```bash
GEMINI_API_KEY=your_actual_api_key_here
```

2. The application will automatically load this key using `python-dotenv`

### Method 2: System Environment Variables

#### For WSL (Permanent):
```bash
# Add to ~/.bashrc and ~/.profile
echo 'export GEMINI_API_KEY="your_api_key_here"' >> ~/.bashrc
echo 'export GEMINI_API_KEY="your_api_key_here"' >> ~/.profile
source ~/.bashrc
```

#### For Windows (Session):
```cmd
set GEMINI_API_KEY=your_api_key_here
```

### 🔗 Getting Your API Key
1. Visit [Google AI Studio](https://makersuite.google.com/app/apikey)
2. Create a new project or select existing one
3. Generate API key
4. Copy and use in your configuration

---

## ▶️ Running the Application

### Quick Start
```bash
# Activate environment and run
source .venv/Scripts/activate && .venv/Scripts/python.exe main.py
```

### Available Modes

#### 1. Demo Mode (Automatic)
Shows the complete operation sequence with 4 sample questions:
- Displays all [USER], [MEMORY], [LLM], [TOOL], [AGENT] operations
- No user input required
- Perfect for learning the agent workflow

#### 2. Interactive Chat Mode
Real-time conversation with the agent:
- Type questions about capital cities
- See operation logging in real-time
- Type 'quit', 'exit', or 'bye' to stop

### Sample Questions to Try
- "What is the capital of Japan?"
- "Tell me about France's capital"
- "What about Germany?"
- "Capital of Australia?"
- "What's the capital of Italy?"

---

## 📊 Understanding the Operation Sequence

When you run the agent, you'll see this flow:

```
[USER] INPUT: 'What is the capital of Japan?'
[MEMORY] Storing user message...
[LLM] Sending to Gemini for processing...
[LLM] Analyzing user question...
[LLM] Country detected: japan
[TOOL] CALLED: get_capital_city('japan')
[TOOL] RESULT: 'Tokyo'
[LLM] Generating final response...
[AGENT] FINAL: Tokyo! That's the capital of Japan...
[MEMORY] Conversation stored
```

### Operation Types Explained:
- **[USER]**: User input capture
- **[MEMORY]**: Conversation history management
- **[LLM]**: Large Language Model processing
- **[TOOL]**: Function/tool execution
- **[AGENT]**: Final response generation

---

## 🌐 GitHub Integration

### 1. Initial Upload to GitHub

#### Create Repository:
1. Go to GitHub and create a new repository
2. Don't initialize with README (we have one)

#### Upload Commands:
```bash
# Initialize git (if not already done)
git init

# Add files
git add .

# Commit
git commit -m "Initial commit: Interactive Capital City Agent"

# Add remote origin
git remote add origin https://github.com/rmisegal/interactive-capital-city-agent.git

# Push to GitHub
git push -u origin main
```

### 2. Clone in WSL
```bash
# Clone repository
git clone https://github.com/rmisegal/interactive-capital-city-agent.git

# Navigate to project
cd interactive-capital-city-agent

# Set up environment (see Environment Setup section above)
```

### 3. Keep Repository Updated

#### Push Changes to GitHub:
```bash
# Add changes
git add .

# Commit with message
git commit -m "Update: describe your changes"

# Push to remote
git push origin main
```

#### Pull Updates from GitHub:
```bash
# Fetch and merge latest changes
git pull origin main

# If you have conflicts, resolve them and commit
git add .
git commit -m "Resolve merge conflicts"
```

#### Update Dependencies After Pull:
```bash
# Activate environment
source .venv/Scripts/activate

# Update packages if requirements.txt changed
.venv/Scripts/pip.exe install -r requirements.txt
```

---

## 📁 Project Structure
```
capital-city-agent/
├── .env                 # API key configuration
├── .venv/              # Virtual environment
├── main.py             # Main application
├── requirements.txt    # Python dependencies
├── README.md          # This file
└── .gitignore         # Git ignore rules
```

---

## 🛠 Troubleshooting

### Common Issues:

#### 1. Unicode/Encoding Errors
- **Solution**: Use Windows Command Prompt or update terminal encoding

#### 2. API Key Not Found
- **Check**: Verify `.env` file exists and contains correct key
- **Verify**: Run `echo $GEMINI_API_KEY` to check environment variable

#### 3. Module Import Errors
- **Solution**: Ensure virtual environment is activated
- **Reinstall**: `pip install -r requirements.txt`

#### 4. WSL Virtual Environment Issues
- **Solution**: Use `dos2unix .venv/Scripts/activate` to fix line endings
- **Alternative**: Use `.venv/Scripts/python.exe` directly

#### 5. Tool Not Called
- **Check**: Ensure your question mentions a supported country
- **Supported**: Japan, France, Germany, Italy, Spain, USA, UK, Canada, Australia

---

## 🔮 Next Steps
- Add more countries to the database
- Implement conversation memory persistence
- Add more tools (weather, population, etc.)
- Create web interface
- Add vector database for semantic search

---

## 📝 Notes
- The agent demonstrates Google ADK patterns but uses direct Gemini API calls for clarity
- All operations are logged for educational purposes
- WSL environment recommended for consistent behavior
