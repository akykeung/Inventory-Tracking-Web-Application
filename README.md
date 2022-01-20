# Inventory Tracking Web Application
Welcome to the Inventory Tracking Web Application! This application is built around providing users the ease in creating, reading, updating and deleting inventory items. Click the link below to access the web application:

[Cool Inventory Tracker](https://coolinventorytracker.herokuapp.com/)

Beyond simply a CRUD application, further enhancements were made to the applications with added features.

# Features
In creating this application, the following requirements were considered to ensure the basics were covered in creating an inventory tracking application:

1. Create inventory items
2. Edit Them
3. Delete Them
4. View a list of them

To better organize and for future flexibility in adding more pages and features, all pages of this applications can be seamlessly accessed using the dropdown feature on the left. ![Page Access](/Images/screenshot_dropdown.png)

## Creating inventory items
Users can create inventory items by navigating to the **Add Inventory Page** where details on the **inventory name**, **inventory details** and **date of creation** can be added. Once details are provided, simply click **Add**. ![Add Inventory](/Images/screenshot_add.png)

## Editing inventory items
Users can edit inventory items by navigating to the **Manage Inventory Page** where the item can be selected and details on the **inventory name**, **inventory details** and **date of creation** can be adjusted. To update simply click **Update**. ![Edit Inventory](/Images/screenshot_edit.png)


## Deleting inventory items
Users can delete inventory items by navigating to the **Manage Inventory Page** where the item can be selected and to delete, simply click **Delete** to remove the item. ![Delete Inventory](/Images/screenshot_delete.png)

## Exporting inventory data as CSV
When users upload inventory details on to the application, the data can be extracted through an export of the data from the database from navigating to the **View Metrics Page** as shown: ![Export to CSV Functionality](/Images/screenshot_export.png)

# Extra Features
Further enhancements to the inventory tracking experience were made including adding a **search feature** and a provided page for which more insights can be derived in the **View Metrics Page**.

## Search Functionality
Navigating to the **Search Page**, users are greeted with the ability to find inventory items either by typing or through a dropdown menu for multi-select. ![Search Inventory](/Images/screenshot_search.png)

## Insight generation
Navigating to the **View Metrics Page**, users are greeted with the ability to download the data as a CSV and also view metrics on the inventory levels over time by month. ![Inventory Insights](/Images/screenshot_insight.png)

# Future Improvements
With the inventory tracking application, more pages and features can be added. Such features can include but not limited to:

1. For the home page, allowing users to not only see the list of inventory items but also allowing users to upload AND store image with generated thumbnails. In addition, customization of how you wish to see your inventory items including list view or a flexible dashboard so that you can organize it according to your needs.

2. Current insights from the view metrics page is limited and in future releases of this application, more insights can be derived with filters and slicers providing insights on the most or least inventory for a given month or inventory based on location.

3. In adding inventory items, the form can be improved with more information requirements such as shipment date, quantity, SKUs or etc.

4. For the search page further improvements can be made to this page in future releases where the user can filter based on fields/inventory count/tags/other metadata.

5. For the managing inventory page, a feature to allow users to undo their deleted inventory items could be added to prevent mistaken deletions. For updating the inventory items, enhancements can be made by providing users to ability to assign/remove inventory items to a named group/collection or create warehouses/locations and assign inventory to specific locations.

# How to run this program
The inventory tracking application can be run using the link: [Cool Inventory Tracker](https://coolinventorytracker.herokuapp.com/)

If you wish to run this application locally, the following instructions will need to be followed in the next section.

## Running Locally
1. To run the application locally, clone the repository on your local machine using the following command: 
`git clone: https://github.com/akykeung/Inventory-Tracking-Web-Application.git` using an IDE of your choice (ex. Visual Studios). If you don't have git on your machine, you can download git using the following link: 
[git Download](https://git-scm.com/)

2. Once cloned, navigate to the folder of where it is cloned and open the file: `app.py`. This application was built using Python. If Python is not installed on your local machine, you can download the latest version of Python in this link: 
[Python Download](https://www.python.org/downloads/)

In addition to Python, the following libraries will need to be installed according to the `requirements.txt` file. This includes matplotlib, pandas, sqlite (backend database) and streamlit. The following commands can be made in the terminal to install the following libraries for windows.

```python
pip install matplotlib streamlit pandas
```

More instructions to download the following libraries for troubleshooting:
1. [Streamlit](https://docs.streamlit.io/library/get-started/installation)
2. [matplotlib](https://matplotlib.org/stable/users/installing/index.html)
3. [pandas](https://pandas.pydata.org/getting_started.html)

3. Once cloned, run the `app.py` python file. To run the application, open the terminal of your IDE and type the following command `streamlit run app.py`. You should be able to access now the inventory tracking application using local host. ![Local Web Application](/Images/screenshot_local.png)

# Authors
Adrian Keung

LinkedIn: https://www.linkedin.com/in/adrian-keung/

# Version History
0.1
- Initial Release of Inventory Tracking Application. Future version to include improvements highlighted in the improvements section of this project.

