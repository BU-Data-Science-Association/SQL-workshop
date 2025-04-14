# A Python (Flask) web app with PostgreSQL ~~in Azure~~
### Workshop for the BU Data Science Association, Spring 2025, Adapted from Pamela Fox

This is a Python web app using the Flask framework and a Postgres database  
  
- It can be used as a playground for testing SQL queries  
  
## How to Use  
- Launch in Codespaces (Create Codespace on Main)  
- Wait for SQLTools extension to load on the left navbar of VS Code  
- Connect to the postgres database in the SQLTools menu (the cylinder) - if this does not work by default, the connection info is in the .env file  
- run `python3 data_utils.py` to populate the postgres tables with BU dining hall information  
- There should be a container database tab from SQLTools, you can type in a query and press `Run on Active Connection` to see the result  
- Note that Github Copilot is automatically installed and offers terrible suggestions, if this is a problem you can disable it in extensions  
