#Dependencies
import streamlit as st
import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('Agg')
import calendar
from PIL import Image

#Database
conn = sqlite3.connect('inventory.db')
c = conn.cursor()

#Inventory Item Template
from html_template import *

# Configure app Name
st.set_page_config(page_title = 'Inventory Tracking App', page_icon = 'U+1F4E6')
st.markdown(hide_default_footer, unsafe_allow_html=True) 

# Functions

#Creating a table
def create_table():
    c.execute('CREATE TABLE IF NOT EXISTS inventorytable(InventoryName TEXT, InventoryDetails TEXT, CreationDate DATE)')

# Recieve or add table
def add_data(InventoryName, InventoryDetails, CreationDate):
    c.execute('INSERT INTO inventorytable(InventoryName, InventoryDetails, CreationDate) VALUES(?,?,?)',(InventoryName, InventoryDetails, CreationDate))
    conn.commit()

# Function to fetch all items from database
def view_all_inventory():
    c.execute('SELECT * FROM inventorytable')
    data = c.fetchall()
    return data

# Function to fetch all items from database based on name
def view_all_items():
    c.execute('SELECT DISTINCT InventoryName FROM inventorytable')
    data = c.fetchall()
    return data

# Function to get specific requested item from database
def get_item_by_name(InventoryName):
    c.execute(f'SELECT * FROM inventorytable WHERE InventoryName="{InventoryName}"')
    data = c.fetchall()
    return data

# Function to delete database
def delete_data(InventoryName):
    c.execute(f'DELETE FROM inventorytable WHERE InventoryName="{InventoryName}"')
    conn.commit()

# Function to update database
def update_data(InventoryName, InventoryDetails, CreationDate, CurrentInventory):
    c.execute(f'UPDATE inventorytable SET InventoryName ="{InventoryName}", InventoryDetails="{InventoryDetails}", CreationDate ="{CreationDate}" WHERE InventoryName = "{CurrentInventory}"')
    conn.commit()

# Function for creating dataframe
def inventory_db():
    result = view_all_inventory()
    clean_db = pd.DataFrame(result,columns=['Inventory Name', 'Inventory Details', 'Creation Date'])
    return clean_db

# CSV Export Button
@st.cache
def convert_df(df):
    # IMPORTANT: Cache the conversion to prevent computation on every rerun
    return df.to_csv().encode('utf-8')

def main():

    st.title("Inventory Tracking")

    menu = ["Home", "View Metrics", "Add Inventory", "Search", "Manage Inventory"]
    #Creating menu bar at the side of the application
    choice = st.sidebar.selectbox("Menu", menu)

    if choice == "Home":
        #Where all inventory tracking exist
        st.subheader("Homepage")
        result = view_all_inventory()
        #Reformatting list layout
        for i in result:
            Inv_Name = i[0]
            Inv_details = i[1]
            Inv_date = i[2]
            st.markdown(template.format(Inv_Name, Inv_details, Inv_date), unsafe_allow_html=True)

    elif choice == "View Metrics":
        st.subheader("View Metrics on your Inventory")

        #Call on dataframe
        st.dataframe(inventory_db())
        new_df = inventory_db()

        #Push a button export product data to a CSV
        csv = convert_df(new_df)
        st.download_button(label="Download data as CSV", data=csv, file_name='Inventory Data.csv',mime='text/csv',)

        st.subheader("Inventory Levels Over Time")
        # Inventory Data per month
        max_inventory_month = pd.to_datetime(new_df["Creation Date"]).dt.strftime("%b").value_counts()
        month_names = calendar.month_abbr[1:]
        max_inventory_month = max_inventory_month.reindex(month_names, fill_value=0)
        st.bar_chart(max_inventory_month, use_container_width=True) #.plot(kind='bar')


    elif choice == "Add Inventory":
        st.subheader("Add Inventory Items")

        create_table()
        #Selections
        inventory_name = st.text_input("Enter Inventory Name")
        inventory_details = st.text_area("Enter Inventory Details", height=150)
        inventory_date = st.date_input("Date")
        if st.button("Add"):
            #Sending data to add data function
            add_data(inventory_name, inventory_details, inventory_date)
            st.success("{} have been submitted".format(inventory_name))

    elif choice == "Search":
        st.subheader("Search Inventory Items")

        #Create loop to allow multiselect of all items
        search_items = [i[0] for i in view_all_items()]
        search_term = st.multiselect('Which Inventory Item Would Like to Open?', search_items)
        try:
            if st.button("Search"):
                #search_result = get_item_by_name(search_term)
                for i in search_term:
                    search_result = get_item_by_name(i)
                    for i in search_result:
                        Inv_Name = i[0]
                        Inv_details = i[1]
                        Inv_date = i[2]
                        st.markdown(template.format(Inv_Name, Inv_details, Inv_date), unsafe_allow_html=True)
        except:
            st.write('Unable to find item')

    elif choice == "Manage Inventory":
        st.subheader("Manage Inventory Items")

        #Dataframe to be displayed
        st.dataframe(inventory_db())

        #Loop to obtain all unique items in inventory
        unique_items = [i[0] for i in view_all_items()]
        inventory_by_title = st.selectbox('Item Selection',unique_items)
        
        st.write("Update or Delete Inventory Items")
        try:
            #Form to allow updating of data
            Item = get_item_by_name(inventory_by_title)
            Updated_inventory_name = st.text_input("Enter Inventory Name", value=inventory_by_title)
            Updated_inventory_details = st.text_area("Enter Inventory Details", value=Item[0][1], height=150)
            Updated_inventory_date = st.date_input("Date")

            col1, col2 = st.columns([1,5])

            with col1:
                if st.button("Update"):
                    #Sending data to update data function
                    update_data(Updated_inventory_name, Updated_inventory_details, Updated_inventory_date, inventory_by_title)
                    st.success("{} have been updated".format(inventory_by_title))
            with col2:
                    #Sending data to delete data function
                if st.button("Delete"):
                    delete_data(inventory_by_title)
                    st.warning("Deleted: '{}'".format(inventory_by_title))
        except:
            st.write('No Items to Update or Delete')

if __name__ == '__main__':
    main()