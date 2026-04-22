import sqlite3
import os

def seed():
    db_path = "glenigan_takehome_FS.db"
    
    # Remove existing db if any
    if os.path.exists(db_path):
        os.remove(db_path)
        print(f"Removed existing {db_path}")

    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    # Create table projects
    cursor.execute("""
        CREATE TABLE projects (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            project_name TEXT NOT NULL,
            project_start TEXT NOT NULL,
            project_end TEXT NOT NULL,
            company TEXT NOT NULL,
            description TEXT NOT NULL,
            project_value INTEGER NOT NULL,
            area TEXT NOT NULL
        )
    """)

    # Seed data
    projects = [
        (
            "Wembley Stadium Renovation", 
            "2026-05-01 09:00:00", 
            "2027-12-31 17:00:00", 
            "BuildCorp UK", 
            "Major structural renovation and expansion of seating capacity.", 
            50000000, 
            "North London"
        ),
        (
            "Manchester Tech Hub", 
            "2026-01-15 08:30:00", 
            "2028-06-20 18:00:00", 
            "Innovation Developers", 
            "State-of-the-art office spaces for technology startups.", 
            12500000, 
            "North West"
        ),
        (
            "Bristol Residential Towers", 
            "2026-03-10 08:00:00", 
            "2027-09-15 17:00:00", 
            "Urban Living Ltd", 
            "High-rise luxury apartments with sustainable design.", 
            22000000, 
            "South West"
        ),
        (
            "Birmingham Logistics Center", 
            "2026-02-01 07:00:00", 
            "2026-11-30 20:00:00", 
            "Swift Logistics Partners", 
            "New distribution center for e-commerce fulfilment.", 
            8000000, 
            "Midlands"
        ),
        (
            "Edinburgh Bridge Maintenance", 
            "2026-07-20 22:00:00", 
            "2026-08-05 05:00:00", 
            "ScotRoads Maintenance", 
            "Routine structural integrity checks and painting.", 
            150000, 
            "Scotland"
        ),
        (
            "Cardiff City Center Library", 
            "2026-04-01 09:00:00", 
            "2027-03-31 17:00:00", 
            "Welsh Heritage Builders", 
            "Construction of a modern public library and community center.", 
            4500000, 
            "Wales"
        ),
    ]

    cursor.executemany("""
        INSERT INTO projects (project_name, project_start, project_end, company, description, project_value, area)
        VALUES (?, ?, ?, ?, ?, ?, ?)
    """, projects)

    conn.commit()
    conn.close()
    print(f"Successfully seeded {db_path} with {len(projects)} records.")

if __name__ == "__main__":
    seed()
