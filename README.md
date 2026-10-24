\# 🧠 NLP App



!\[Python](https://img.shields.io/badge/Python-3.8%2B-blue?logo=python\&logoColor=white)

!\[GUI](https://img.shields.io/badge/GUI-Tkinter-informational)

!\[API](https://img.shields.io/badge/API-NLP%20Cloud-green)

!\[License](https://img.shields.io/badge/License-MIT-yellow)



A desktop application built with Python and Tkinter that combines secure user authentication with three NLP tools: \*\*sentiment analysis\*\*, \*\*named entity recognition\*\* and \*\*emotion prediction\*\*, powered by the \[NLP Cloud](https://nlpcloud.com) API.



\## ✨ Features



\- \*\*User accounts:\*\* register and log in, with passwords stored as salted PBKDF2-SHA256 hashes

\- \*\*Sentiment analysis:\*\* returns every label with its confidence score

\- \*\*Named entity recognition:\*\* detects people, places, dates, organizations and more

\- \*\*Emotion prediction:\*\* scores text across multiple emotions

\- \*\*Error handling:\*\* empty input and network or API failures show a message instead of crashing the app



\## 📸 Screenshots



| Login | Sentiment Analysis |

|-------|--------------------|

| !\[Login](screenshots/login.png) | !\[Sentiment](screenshots/sentiment.png) |



| Named Entity Recognition | Emotion Prediction |

|--------------------------|--------------------|

| !\[NER](screenshots/ner.png) | !\[Emotion](screenshots/emotion.png) |



\## 🛠️ Tech Stack



| Area | Technology |

|------|-----------|

| Language | Python |

| GUI | Tkinter |

| NLP | NLP Cloud API (`nlpcloud` client) |

| Storage | JSON file |

| Config | `python-dotenv` |



\## 📁 Project Structure



```

nlp-gui/

├── nlpapp.py          # GUI and application flow

├── myapi.py           # NLP Cloud API wrapper

├── mydb.py            # User storage and password hashing

├── resources/         # App icon and assets

├── requirements.txt   # Python dependencies

├── .env.example       # Template for your API key

└── .gitignore

```



\## 🚀 Getting Started



\### Prerequisites

\- Python 3.8 or newer (Tkinter is included with the standard Windows installer)

\- A free API key from \[NLP Cloud](https://nlpcloud.com)



\### Installation



1\. \*\*Clone the repository\*\*

&#x20;  ```bash

&#x20;  git clone https://github.com/KrrishTiwari/nlp-gui.git

&#x20;  cd nlp-app

&#x20;  ```



2\. \*\*Create and activate a virtual environment\*\* (recommended)

&#x20;  ```bash

&#x20;  python -m venv .venv

&#x20;  .venv\\Scripts\\activate

&#x20;  ```



3\. \*\*Install dependencies\*\*

&#x20;  ```bash

&#x20;  pip install -r requirements.txt

&#x20;  ```



4\. \*\*Add your API key\*\*



&#x20;  Copy `.env.example` to `.env` and replace the placeholder with your key:

&#x20;  ```

&#x20;  NLPCLOUD\_API\_KEY=your\_api\_key\_here

&#x20;  ```



5\. \*\*Run the app\*\*

&#x20;  ```bash

&#x20;  python nlpapp.py

&#x20;  ```



\## 💡 Usage



1\. Register a new account, then log in.

2\. Choose a tool from the home screen.

3\. Enter some text and click the action button to see the results.



\*\*Example:\*\* sentiment analysis of \*"I loved this movie, the acting was brilliant"\*



```

POSITIVE: 0.99

NEGATIVE: 0.01

```



\## 🔒 Security Notes



\- Passwords are never stored in plain text. Each one is salted and hashed with PBKDF2-HMAC-SHA256.

\- The API key is read from a `.env` file, which is excluded from version control.

\- `db.json` is created locally on first run and is also excluded from version control.

\- This is a learning project. A production system would use a proper database and a hardened authentication flow.



\## 🗺️ Roadmap



\- \[ ] Replace JSON storage with SQLite

\- \[ ] Multi-line text input

\- \[ ] Loading indicator during API calls

\- \[ ] Unit tests for the database and API layers

\- \[ ] Package as a standalone `.exe`



\## 🤝 Contributing



Suggestions and pull requests are welcome. For major changes, please open an issue first to discuss what you'd like to change.





\## 👤 Author



\*\*Krrish\*\*

GitHub: 

