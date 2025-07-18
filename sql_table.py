# pip install mysql-connector-python

import mysql.connector
from mysql.connector import errorcode
import create_table
import json

try:
    conn = mysql.connector.connect(
        host="localhost",       # or your Docker host IP
        port=3306,              # default MySQL port
        user="db_user",
        password="6equj5_db_user"
    )

    cursor = conn.cursor()
    print("Connecteion Established...")

    cursor.execute("CREATE DATABASE IF NOT EXISTS home_db;")
    print("Database is created (or already exists)...")

    cursor.execute("use home_db;")

    cursor.execute(create_table.properties)
    print("Table 'properties' created (or already exists).")
    cursor.execute(create_table.valuations)
    print("Table 'valuations' created (or already exists).")
    cursor.execute(create_table.hoa)
    print("Table 'hoa' created (or already exists).")
    cursor.execute(create_table.rehab)
    print("Table 'rehab' created (or already exists).")

    #create target table
    cursor.execute(create_table.final_properties)
    
    # Load JSON
    with open("C:\Projects\data_engineer_assessment\data\/fake_property_data.json") as f:
        data = json.load(f)

    # Helper function
    def safe_get(obj, key, default=None):
        return obj[key] if key in obj else default

    # Insert into tables
    for prop in data:
        # Insert main property
        prop_values = (
            prop['Property_Title'],
            prop['Address'],
            prop['Reviewed_Status'],
            prop['Most_Recent_Status'],
            prop['Source'],
            prop['Market'],
            prop['Occupancy'],
            prop['Flood'],
            prop['Street_Address'],
            prop['City'],
            prop['State'],
            prop['Zip'],
            prop['Property_Type'],
            prop['Highway'],
            prop['Train'],
            prop['Tax_Rate'],
            prop['SQFT_Basement'],
            prop['HTW'],
            prop['Pool'],
            prop['Commercial'],
            prop['Water'],
            prop['Sewage'],
            prop['Year_Built'],
            prop['SQFT_MU'],
            prop['SQFT_Total'],
            prop['Parking'],
            prop['Bed'],
            prop['Bath'],
            prop['BasementYesNo'],
            prop['Layout'],
            prop['Net_Yield'],
            prop['IRR'],
            prop['Rent_Restricted'],
            prop['Neighborhood_Rating'],
            prop['Latitude'],
            prop['Longitude'],
            prop['Subdivision'],
            prop['Taxes'],
            prop['Selling_Reason'],
            prop['Seller_Retained_Broker'],
            prop['Final_Reviewer'],
            prop['School_Average']
        )
        cursor.execute("""
            INSERT INTO properties (
                Property_Title, Address, Reviewed_Status, Most_Recent_Status,
                Source, Market, Occupancy, Flood, Street_Address, City, State, Zip,
                Property_Type, Highway, Train, Tax_Rate, SQFT_Basement, HTW, Pool,
                Commercial, Water, Sewage, Year_Built, SQFT_MU, SQFT_Total, Parking,
                Bed, Bath, BasementYesNo, Layout, Net_Yield, IRR, Rent_Restricted,
                Neighborhood_Rating, Latitude, Longitude, Subdivision, Taxes,
                Selling_Reason, Seller_Retained_Broker, Final_Reviewer, School_Average
            ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,
                    %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,
                    %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """, prop_values)

        # Insert Valuation
        for v in prop.get("Valuation", []):
            cursor.execute("""
                INSERT INTO valuations (
                    Property_Title, List_Price, Previous_Rent, ARV, Rent_Zestimate,
                    Expected_Rent, Low_FMR, High_FMR, Zestimate, Redfin_Value
                ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
            """, (
                prop['Property_Title'],
                safe_get(v, "List_Price"),
                safe_get(v, "Previous_Rent"),
                safe_get(v, "ARV"),
                safe_get(v, "Rent_Zestimate"),
                safe_get(v, "Expected_Rent"),
                safe_get(v, "Low_FMR"),
                safe_get(v, "High_FMR"),
                safe_get(v, "Zestimate"),
                safe_get(v, "Redfin_Value")
            ))

        # Insert HOA
        for h in prop.get("HOA", []):
            cursor.execute("""
                INSERT INTO hoa (Property_Title, HOA, HOA_Flag)
                VALUES (%s, %s, %s)
            """, (prop['Property_Title'], h.get("HOA"), h.get("HOA_Flag")))

        # Insert Rehab
        for r in prop.get("Rehab", []):
            cursor.execute("""
                INSERT INTO rehab (
                    Property_Title, Underwriting_Rehab, Rehab_Calculation, Paint,
                    Flooring_Flag, Foundation_Flag, Roof_Flag, HVAC_Flag,
                    Kitchen_Flag, Bathroom_Flag, Appliances_Flag, Windows_Flag,
                    Landscaping_Flag, Trashout_Flag
                ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
            """, (
                prop['Property_Title'],
                r.get("Underwriting_Rehab"),
                r.get("Rehab_Calculation"),
                r.get("Paint"),
                r.get("Flooring_Flag"),
                r.get("Foundation_Flag"),
                r.get("Roof_Flag"),
                r.get("HVAC_Flag"),
                r.get("Kitchen_Flag"),
                r.get("Bathroom_Flag"),
                r.get("Appliances_Flag"),
                r.get("Windows_Flag"),
                r.get("Landscaping_Flag"),
                r.get("Trashout_Flag")
            ))

    # Commit changes
    conn.commit()
    print("Data inserted successfully.")

    

except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("Authentication error: check user/password")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("Database does not exist.")
    else:
        print(err)
finally:
    cursor.close()
    conn.close()