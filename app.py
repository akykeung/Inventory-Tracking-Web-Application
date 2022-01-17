import streamlit as st
import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('Agg')

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
    c.execute('SELECT DISTINCT InventoryName FROM inventorytable')
    data = c.fetchall()
    return data

def get_item_by_name(InventoryName):
    c.execute(f'SELECT * FROM inventorytable WHERE InventoryName="{InventoryName}"')
    data = c.fetchall()
    return data

def delete_data(InventoryName):
    c.execute(f'DELETE FROM inventorytable WHERE InventoryName="{InventoryName}"')
    conn.commit()

def update_data(InventoryName, InventoryDetails, CreationDate, CurrentInventory):
    c.execute(f'UPDATE inventorytable SET InventoryName ="{InventoryName}", InventoryDetails="{InventoryDetails}", CreationDate ="{CreationDate}" WHERE InventoryName = "{CurrentInventory}"')
    conn.commit()

# Template on Layout
template = """
<div style="background-color:#55aaaa;padding:10px;border-radius:10px;margin:20px;">
<h4 style="color:white; text-align: center;">{}</h4>
<p style = "text-align:center;">{}</p>
<h6 style="color:white; text-align: center;">Creation Date: {}</h4>
</div>

"""
def main():

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
        inventory_name = st.text_input("Enter Inventory Name")
        inventory_details = st.text_area("Enter Inventory Details", height=150)
        inventory_date = st.date_input("Date")
        if st.button("Add"):
            #Sending data to add data function
            add_data(inventory_name, inventory_details, inventory_date)
            st.success("{} have been submitted".format(inventory_name))

    elif choice == "Search":
        st.subheader("Search Inventory Items")
        search_term = st.text_input('Enter Search Term')
        if st.button("Search"):
            search_result = get_item_by_name(search_term)
            for i in search_result:
                Inv_Name = i[0]
                Inv_details = i[1]
                Inv_date = i[2]
                st.markdown(template.format(Inv_Name, Inv_details, Inv_date), unsafe_allow_html=True)


    elif choice == "Manage Inventory":
        st.subheader("Manage Inventory Items")

        result = view_all_inventory()
        clean_db = pd.DataFrame(result,columns=['Inventory Name', 'Inventory Details', 'Creation Date'])
        st.dataframe(clean_db)
        unique_items = [i[0] for i in view_all_items()]

        inventory_by_title = st.selectbox('Item Selection',unique_items)
        
        st.write("Update or Delete Inventory Items")
        try:
            Item = get_item_by_name(inventory_by_title)
            Updated_inventory_name = st.text_input("Enter Inventory Name", value=inventory_by_title)
            Updated_inventory_details = st.text_area("Enter Inventory Details", value=Item[0][1], height=150)
            Updated_inventory_date = st.date_input("Date")

            col1, col2 = st.columns([1,5])

            with col1:
                if st.button("Update"):
                    #Sending data to add data function
                    update_data(Updated_inventory_name, Updated_inventory_details, Updated_inventory_date, inventory_by_title)
                    st.success("{} have been updated".format(inventory_by_title))
            with col2:
                if st.button("Delete"):
                    delete_data(inventory_by_title)
                    st.warning("Deleted: '{}'".format(inventory_by_title))
        except:
            st.write('No Items to Update or Delete')



        if st.checkbox("Metrics"):
            new_df = clean_db
            new_df['Length'] = new_df['Inventory Details'].str.len()
            st.dataframe(new_df)

            st.subheader("Inventory Levels Over Time")
            new_df["Creation Date"].value_counts().plot(kind='bar')
            st.set_option('deprecation.showPyplotGlobalUse', False)
            st.pyplot()

if __name__ == '__main__':
    main()