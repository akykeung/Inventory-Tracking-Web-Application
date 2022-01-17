import streamlit as st
import sqlite3

#Database
conn = sqlite3.connect('inventory.db')
c = conn.cursor()

# Functions

#Creating a table
def create_table():
    c.execute('CREATE TABLE IF NOT EXISTS inventorytable(Inventory Name TEXT, Inventory Details TEXT, Creation Date DATE)')

# Recieve or add table
def add_data(Inventory Name, Inventory Details, Creation Date):
    c.execute('INSERT INTO inventorytable(Inventory Name, Inventory Details, Creation Date) VALUES(?,?,?)',(Inventory Name, Inventory Details, Creation Date))
    conn.commit()

def view_all_inventory():
    c.execute('SELECT * FROM inventorytable')
    data = c.fetchall()
    return data


st.title("Inventory Tracking")

menu = ["Home", "View Inventory", "Add Inventory", "Search", "Manage Inventory"]
#Creating menu bar at the side of the application
choice = st.sidebar.selectbox("Menu", menu)

if choice == "Home":
    #Where all inventory tracking exist
    st.subheader("Home")

elif choice == "View Inventory":
    st.subheader("View Inventory Items")

elif choice == "Add Inventory":
    st.subheader("Add Inventory Items")

    inventory_name = st.text_input("Enter Inventory Name", max_chars=100)
    inventory_details = st.text_area("Enter Inventory Details", height=150)
    inventory_date = st.date_input("Date")
    if st.button("Add"):
        st.success("Submit:{} saved".format(inventory_name))

elif choice == "Search":
    st.subheader("Search Inventory Items")

elif choice == "Manage Inventory":
    st.subheader("Manage Inventory Items")