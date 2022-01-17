import streamlit as st



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

elif choice == "Search":
    st.subheader("Search Inventory Items")

elif choice == "Manage Inventory":
    st.subheader("Manage Inventory Items")