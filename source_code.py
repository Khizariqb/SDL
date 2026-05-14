import json
import psycopg2
import getpass

# 1. Read config file
with open('config.json', 'r') as f:
    config = json.load(f)

print("Config loaded:", config)

# 2. Ask user for login/password
print("\nEnter database credentials:")
username = input("Username: ")
password = getpass.getpass("Password: ")

# 3. Connect to database
try:
    # Combine config + user input (user cannot add extra options)
    conn = psycopg2.connect(
        host=config['host'],
        port=config['port'],
        database=config['database'],
        user=username,
        password=password
    )
    
    # 4. Run the required query
    cursor = conn.cursor()
    cursor.execute("SELECT VERSION();")
    result = cursor.fetchone()
    
    print("\n✅ Successfully connected!!")
    print("PostgreSQL version:", result[0])
    
    # Clean upp
    cursor.close()
    conn.close()
    
except Exception as e:
    print("\n❌ Error:", e)