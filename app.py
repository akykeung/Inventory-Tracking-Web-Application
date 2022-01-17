import streamlit as st
import sqlite3

#Database
conn = sqlite3.connect('inventory.db')
c = conn.cursor()

# Functions

#Creating a table
def create_table():
    c.execute('CREATE TABLE IF NOT EXISTS inventorytable(InventoryName TEXT, InventoryDetails TEXT, CreationDate DATE)')

# Recieve or add table
def add_data(InventoryName, InventoryDetails, CreationDate):
    c.execute('INSERT INTO inventorytable(InventoryName, InventoryDetails, CreationDate) VALUES(?,?,?)',(InventoryName, InventoryDetails, CreationDate))
    conn.commit()

def view_all_inventory():
    c.execute('SELECT * FROM inventorytable')
    data = c.fetchall()
    return data

def view_all_items():
    c.execute('SELECT DISTINCT InventoryName from inventorytable')
    data = c.fetchall()
    return data

def get_item_by_name(InventoryName):
    c.execute('SELECT * from inventorytable WHERE InventoryName="{}"'.format(InventoryName))
    data = c.fetchall()
    return data



# Template on Layout
template = """
<div style="background-color:#55aaaa;padding:10px;border-radius:10px;margin:20px;">
<h4 style="color:white; text-align: center;">{}</h4>
<p style = "text-align:center;">{}</p>
<h6 style="color:white; text-align: center;">Creation Date: {}</h4>
</div>

"""

st.title("Inventory Tracking")

menu = ["Home", "View Inventory", "Add Inventory", "Search", "Manage Inventory"]
#Creating menu bar at the side of the application
choice = st.sidebar.selectbox("Menu", menu)

if choice == "Home":
    #Where all inventory tracking exist
    st.subheader("Home")
    result = view_all_inventory()
    #Reformatting list layout
    for i in result:
        Inv_Name = i[0]
        Inv_details = i[1]
        Inv_date = i[2]
        st.markdown(template.format(Inv_Name, Inv_details, Inv_date), unsafe_allow_html=True)

elif choice == "View Inventory":
    st.subheader("View Inventory Items")
    #Calling Function for all items
    all_items = [i[0] for i in view_all_items()]
    inventory_list = st.sidebar.selectbox('View Inventory',all_items)
    inventory_result = get_item_by_name(inventory_list)
    for i in inventory_result:
        Inv_Name = i[0]
        Inv_details = i[1]
        Inv_date = i[2]
        st.markdown(template.format(Inv_Name, Inv_details, Inv_date), unsafe_allow_html=True)
  


elif choice == "Add Inventory":
    st.subheader("Add Inventory Items")
    create_table()
    #Selections
    inventory_name = st.text_input("Enter Inventory Name", max_chars=100)
    inventory_details = st.text_area("Enter Inventory Details", height=150)
    inventory_date = st.date_input("Date")
    if st.button("Add"):
        #Sending data to add data function
        add_data(inventory_name, inventory_details, inventory_date)
        st.success("{} have been submitted".format(inventory_name))

elif choice == "Search":
    st.subheader("Search Inventory Items")

elif choice == "Manage Inventory":
    st.subheader("Manage Inventory Items")