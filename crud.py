from Autodesk.Revit.DB import Transaction, FilteredElementCollector, BuiltInCategory

# access the current Revit document
doc = __revit__.ActiveUIDocument.Document

# get a list containing all sheets in the project
sheet_collector = FilteredElementCollector(doc).OfCategory(
    BuiltInCategory.OST_Sheets).WhereElementIsNotElementType().ToElements()


# initiate a transaction to modify the model
t = Transaction(doc, 'Update sheet Parameters')     # instantiate a transaction
t.Start()                                       # start the transaction

for sheet in sheet_collector:
    print(sheet)
    # Access value of CUSTOM_PARAM parameter of current sheet
    custom_param = sheet.LookupParameter('CUSTOM_PARAM')
    # Check if the parameter exists
    if custom_param:
        # Set the value of the CUSTOM_PARAM parameter
        custom_param.Set('NEW_VALUE')


t.Commit()                                      # commit the transaction
