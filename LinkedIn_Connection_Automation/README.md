
# 🤖 LinkedIn Connection Automation

A **Python-based automation tool** that streamlines the process of sending **personalized connection requests** on LinkedIn by intelligently **searching for specific job roles, locations, and companies**. This project highlights my **problem-solving skills** in automating complex, repetitive tasks using **Python**, **Selenium**, and explores the potential of integrating the **LinkedIn API** for future development. A **video demonstration** is included to showcase the tool in action.

## 📽️ Demonstration Video
[LinkedIn_Connection_Requests](/LinkedIn_Connection_Automation/linkedIn_Connections.mp4)


## 🧠 Problem Statement

Manually searching for and connecting with professionals on LinkedIn based on specific criteria (job title, location, company) is tedious, repetitive, and prone to errors. The tool solves this by automating:

✅ Targeted search for **specific job roles, locations, and companies**  
✅ Filtering to connect only with **verified accounts** to avoid spam  
✅ Sending **personalized connection requests**  
✅ **Automatic page navigation** and the ability to define the number of pages to iterate through

This project showcases my **problem-solving skills** by combining **web scraping** and **automation** techniques to tackle a real-world networking challenge.

## 🚀 Solution Overview

The automation process includes:

1. **Search Automation**  
   - Inputs: **Job role**, **location**, and **company**  
   - Automatically searches LinkedIn based on the criteria

2. **Profile Filtering**  
   - Connects **only with verified profiles**  
   - Skips spam and incomplete profiles

3. **Personalized Connection Requests**  
   - Sends a custom message with each request

4. **Pagination Handling**  
   - Automatically proceeds to the **next page** once profiles on the current page are processed  
   - User specifies the **number of pages** to process

5. **Logging & Error Handling**  
   - Logs successful and failed connection attempts  
   - Handles rate limits and unexpected page errors

## 🔗 LinkedIn API (Future Enhancements)

While the current project uses **Selenium WebDriver** for browser automation, there is potential to integrate the **LinkedIn API** (via the official or unofficial libraries) for a more robust, efficient, and compliant solution. 

Potential API benefits:
- **Rate limit awareness** to avoid temporary bans
- **Direct data access** (profile info, connections, messages) without browser automation
- **More scalable** and **secure** handling of authentication and user data

Due to API access limitations and strict usage policies, **this project currently does not use the LinkedIn API**, but its inclusion is an exciting future possibility!

## 🛠️ Features

- Custom search by **job title**, **location**, **company**
- Filters for **verified profiles only** (reduces spam)
- **Personalized message sending**
- Define how many **pages** to iterate through
- Human-like delays to avoid detection
- Batch processing of multiple profiles
- Comprehensive logging

## 🧰 Tech Stack

- **Python**
- **Selenium WebDriver** (Browser automation)
- **Text file (names.text)** for search input
- **Jupyter Notebook** (for easy experimentation)
- **(Planned)**: LinkedIn API integration

## 📁 Project Structure

```
LinkedIn_Connection_Automation/
├── main.ipynb               # Jupyter Notebook with automation logic
├── names.txt               # Input file containing search criteria
├── logs/                    # Connection attempt logs
├── README.md                # Project documentation
```

## ⚠️ Limitations & Disclaimer

- **Use responsibly**: Automating LinkedIn interactions may violate their Terms of Service. Use at your own risk.
- **For educational purposes only**: This project is a demonstration of automation concepts, not an endorsement for automated networking.
- LinkedIn API access requires proper authorization and compliance with their usage policies.

## 📄 License

[![MIT License](https://img.shields.io/badge/License-MIT-green.svg)](https://choosealicense.com/licenses/mit/)