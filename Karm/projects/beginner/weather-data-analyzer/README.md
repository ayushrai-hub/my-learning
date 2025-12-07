# Project: Weather Data Analyzer

**Difficulty:** Beginner
**Time Estimate:** 8 hours
**Skills Tested:** Python fundamentals, API integration, data processing, CLI interface

## Overview
Build a command-line weather data analyzer that fetches weather data from a public API, processes it, and provides useful insights through a text-based interface. This project demonstrates practical Python programming with real-world data handling.

## Learning Objectives
- [ ] Learn API integration and HTTP requests handling
- [ ] Practice data parsing and processing with Python
- [ ] Implement error handling for network operations
- [ ] Create a user-friendly CLI interface
- [ ] Work with JSON data structures

## Requirements

### Functional Requirements
1. Fetch current weather data for any city using OpenWeatherMap API
2. Display weather information in a formatted way
3. Provide weather insights (recommendations based on conditions)
4. Support multiple cities comparison
5. Save weather data to local JSON file for offline access
6. Include temperature unit conversion (Celsius/Fahrenheit)

### Technical Requirements
- **Language:** Python 3.8+
- **Libraries:** requests, json, datetime (standard library), Rich for CLI formatting
- **API:** OpenWeatherMap free tier (signup required)
- **Testing:** Basic unit tests for data processing functions
- **Documentation:** Clear setup instructions and usage examples
- **Error Handling:** Network failures, invalid city names, API errors

## Architecture

### System Design
```
weather_analyzer/
├── weather_api.py      # API client for OpenWeatherMap
├── data_processor.py   # Weather data processing logic
├── cli_interface.py    # Command-line interface
├── storage.py         # Local JSON storage
├── tests/             # Unit tests
├── config.py          # API keys and settings
└── README.md          # Project documentation
```

### Technology Stack
| Layer          | Technology      | Purpose              |
|----------------|-----------------|----------------------|
| HTTP Client    | requests        | API communication    |
| CLI Framework  | Rich            | Terminal formatting  |
| Data Storage   | JSON            | Local data persistence|
| Configuration  | Python dicts    | Settings management  |
| Testing        | unittest        | Code validation      |

## Implementation Guide

### Phase 1: Setup & Foundation (2 hours)
1. **Set up project structure** - Create directories and basic files
2. **Install dependencies** - requests and rich libraries
3. **Create configuration** - API key setup and default settings
4. **Basic API client** - WeatherAPI class with get_weather method

### Phase 2: Core Features (4 hours)
1. **Weather data fetching** - Implement current weather endpoint
2. **Data processing** - Parse API response into structured data
3. **CLI interface** - Create user-friendly command-line menus
4. **Display formatting** - Weather information with emojis and colors

### Phase 3: Enhancement & Polish (2 hours)
1. **City comparison** - Compare weather between multiple cities
2. **Local storage** - Save/fetch weather data offline
3. **Unit conversion** - Celsius to Fahrenheit toggle
4. **Error handling** - Comprehensive error messages

## Testing Strategy

### Unit Tests
- Test weather data parsing functions
- Mock API responses for reliable testing
- Test error conditions (network failures, invalid responses)
- Validate data transformation logic

### Integration Tests
- Test full weather fetching workflow
- Verify CLI interface interactions
- Test file storage and retrieval

### Manual Testing
- Test with various city names
- Verify different weather conditions display correctly
- Test network error scenarios

## Success Criteria
- [x] Fetches real weather data from OpenWeatherMap API
- [x] Displays current temperature, humidity, wind speed, conditions
- [x] Provides weather-based recommendations (bring umbrella, wear jacket, etc.)
- [x] Supports comparing weather between 2-3 cities
- [x] Saves weather history to local JSON files
- [x] Handles API errors gracefully with helpful messages
- [x] Code follows PEP 8 style guidelines
- [x] Includes basic unit tests (>60% coverage)
- [x] Works on both Windows and Unix systems

## Bonus Challenges
- [ ] **Forecast Feature:** Add 5-day weather forecast
- [ ] **Weather Alerts:** Display severe weather warnings
- [ ] **Historical Data:** Show weather trends over time
- [ ] **Geolocation:** Auto-detect user's location

## Example Usage

```bash
# Check current weather
weather_analyzer get "New York"

# Compare cities
weather_analyzer compare "London" "Paris" "Tokyo"

# View saved data
weather_analyzer history

# Get weather advice
weather_analyzer advice "Seattle"
```

### Sample Output
```
🌤️  Weather in New York, US
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Temperature: 22°C (72°F)
Conditions: Partly cloudy
Humidity: 65%
Wind: 8 km/h from WSW
Feels like: 24°C

💡 Recommendation: Great weather! Perfect for outdoor activities.
   Don't forget sunscreen for that afternoon sun.
```

## Portfolio Presentation

### GitHub README Structure
```markdown
# Weather Data Analyzer ☀️

[![Python](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)

A beautiful command-line tool for weather analysis and insights.

## Features
- Real-time weather data from OpenWeatherMap
- Multi-city comparisons
- Weather-based recommendations
- Local data storage
- Beautiful terminal interface

## Installation
1. Clone repository
2. Install dependencies: `pip install -r requirements.txt`
3. Get API key from OpenWeatherMap
4. Configure API key in config.py

## Usage
```bash
python -m weather_analyzer get "Tokyo"
```

## Demo
[Include animated GIF showing CLI usage]
```

### Demo Video Script (90 seconds)
1. **Intro (15s):** "I built a weather analyzer CLI tool to practice API integration and data processing"
2. **Setup (30s):** "Get OpenWeatherMap API key, install dependencies, configure settings"
3. **Demo (45s):** "Show fetching weather for different cities, comparing them, saving data offline"

### Blog Post Outline
- **Title:** "Building a Weather CLI: My First API Integration Project"
- **Challenges:** Handling API rate limits, parsing complex JSON responses
- **Solutions:** Proper error handling, user-friendly interfaces
- **Lessons:** Importance of configuration management, external API contracts

## Related Projects
- **Prerequisite:** Simple HTTP client script
- **Next Level:** Weather web app with React frontend
