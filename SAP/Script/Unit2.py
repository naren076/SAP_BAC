import loginForm
import searchBox
import createSalesPage
import createStandardOrder
import USRegionConfigurationPage
import CNRegionConfigurationPage
import WaterManagementConfiguration
import AirHandlingConfiguration
import AdditionalEnhancement
import ShippingConfigurationPage

RecNo = 0

def sap_test():
  global RecNo
  # Creates the driver
  # If you connect to an Excel 2007 sheet, use the following method call:
  Driver = DDT.ExcelDriver("C:\\Users\\vaishnavi.r\\Downloads\\SAP Test Parameters.xlsx", "Test Cases FINAL (2)")
  Browsers.Item[btChrome].Navigate(Project.Variables.sap_url)
  browser = Aliases.browser
  browser.BrowserWindow.Maximize()
  page = browser.pageFlp
  #--Login form
  loginForm.login_form(page, Project.Variables.v_username)
  #page.Wait()
  #page.WaitConfirm(5000)
  
  while not Driver.EOF():
    # Iterates through records
    #Set Error Count
    ErrCount = Log.ErrCount;
    Fldr = Log.CreateFolder("Record: " + aqConvert.VarToStr(RecNo))
    Log.PushLogFolder(Fldr)
    sap_field_values = ProcessData(browser, page); # Processes data
    searchBox.search_item(page, "va01")
    page.FindElement("//a[contains(., 'Create Sales Orders')]").Click()
    form = page.FindElement("//iframe[@name='application-SalesDocument-create-iframe']")
    
    order_form = form.FindElement("//div[@id='webguiPage0']/form")
    #--Enter order Type--  
    createSalesPage.create_sales_order(order_form, sales_order_values(sap_field_values))
    if Log.ErrCount > ErrCount:
      RecNo = RecNo + 1
      Log.PopLogFolder()
      Driver.Next()
      continue
     #--Enter Order Details---
    panel = page.sectionShellSplitCanvas
    textbox = panel.frameApplicationSalesdocumentCre.formWebguiform0
    createStandardOrder.create_standard_order(browser, textbox, page, standard_order_values(sap_field_values))
    if Log.ErrCount > ErrCount:
         RecNo = RecNo + 1
         Log.PopLogFolder()
         Driver.Next()
         continue
    #--Enter Configuration--
    CNRegionConfigurationPage.set_configuration_details(textbox, page, general_requirement_values(sap_field_values))   
    if Log.ErrCount > ErrCount:
     RecNo = RecNo + 1
     Log.PopLogFolder()
     Driver.Next()
     continue
    #Water Configurations
    WaterManagementConfiguration.water_management(page, water_management_values(sap_field_values))
    if Log.ErrCount > ErrCount:
     RecNo = RecNo + 1
     Log.PopLogFolder()
     Driver.Next()
     continue
          
    frame = page.sectionShellSplitCanvas.frameApplicationSalesdocumentCre.formWebguiform0.frameC102
    textNode = frame.sectionShellSplitCanvas.sectionApplicationVariantconfigu
    textNode2 = textNode.sectionSplitter0Content1
    
    #Air Handling Configuration
    AirHandlingConfiguration.air_handling(page, frame, textNode2, air_handling_values(sap_field_values))
    if Log.ErrCount > ErrCount:
     RecNo = RecNo + 1
     Log.PopLogFolder()
     Driver.Next()
     continue
    #AdditionalEnhancement
    AdditionalEnhancement.additional_configs(page, frame, textNode2, additional_config_vaues(sap_field_values))
    if Log.ErrCount > ErrCount:
      RecNo = RecNo + 1
      Log.PopLogFolder()
      Driver.Next()
      continue
    #Shipping Page
    ShippingConfigurationPage.shipping_configurations(page, frame, textNode2, shipping_values(sap_field_values))
    if Log.ErrCount > ErrCount:
      RecNo = RecNo + 1
      Log.PopLogFolder()
      Driver.Next()
      continue
    #Done button
    frame.FindElement("//button[.='Done']").Click()
    
    #browser = Aliases.browser
    frame = browser.pageFlp.sectionShellSplitCanvas.frameApplicationSalesdocumentCre
    frame2 = frame.formWebguiform0
    if(NameMapping.Sys.browser.pageFlp.frameApplicationSalesdocumentCre.WaitNamedChild("frameC104", 30000).Exists):
      review_frame = frame2.FindElement("//div[@id='C104-r']/iframe")
      review_frame.FindElement("//button[.='Apply']").Click()
          
    textbox.FindElement("//div[@id='msgarea']//span[2]/div").Click()
    if(NameMapping.Sys.browser.pageFlp.frameApplicationSalesdocumentCre.WaitNamedChild("panelContinue", 75000).Exists):
      textbox.FindElement("//div[.='Continue']").Click()
    page.WaitConfirm(3000)
  
    image = page.FindElement("//header[contains(@class, 'sapUshellShellHeader')]")
    image.FindElement("//a[@title='Navigate to Home Page']").Click()
    searchBox.search_item(page, "csk2")
    section = browser.pageFlp.sectionShellSplitCanvas
    section.FindElement("//span/span/span[contains(text(), 'Multi-')]").Click()
    item_field = textbox.FindElement("//input[@id=(//label[.='Item']/@for)]")
    item_field.SetText("100")
    material_field = textbox.FindElement("//input[@id=(//label[.='Material']/@for)]")
    material_field.SetText("S3E")
    textbox2 = textbox.FindElement("//input[@id=(//label[.='BOM Application']/@for)]")
    textbox2.SetText("PP01")
    textbox.FindElement("//div[.='Execute']").Click()
    
    
    frame = panel.frameApplicationBillofmaterialMu
    form = frame.formWebguiform0
    if(NameMapping.Sys.browser.pageFlp.frameApplicationBillofmaterialMu.WaitNamedChild("panelSpreadsheetCtrlShiftF7", 10000).Exists):
      form.FindElement("//div[@title='Spreadsheet... (Ctrl+Shift+F7)']").Click()
    if(NameMapping.Sys.browser.pageFlp.frameApplicationBillofmaterialMu.WaitNamedChild("panelUpdowndialogchoose", 10000).Exists):
     frame.FindElement("//div[.='OK']").Click()
    page.WaitConfirm(10000)
    Log.PopLogFolder()
    RecNo = RecNo + 1
    Driver.Next(); # Goes to the next record
    
 
  # Closes the driver
  DDT.CloseDriver(Driver.Name)
  
# Posts data to the log (helper routine)
def ProcessData(browser, page):
  global RecNo
  Fldr = Log.CreateFolder("Record: " + aqConvert.VarToStr(RecNo))
  sap_field_values = {}
  for i in range(DDT.CurrentDriver.ColumnCount):
    sap_field_values[DDT.CurrentDriver.ColumnName[i]] = aqConvert.VarToStr(DDT.CurrentDriver.Value[i])
 
  #--Search va01 ----
  if RecNo > 0:
    Browsers.Item[btChrome].Navigate(Project.Variables.sap_url)
    browser = Aliases.browser
    browser.BrowserWindow.Maximize()
  return sap_field_values
  
# Sales Order Values
def sales_order_values(sap_field_values):
  sales_order_field_values = {}
  sales_order_field_values["order_type"] = sap_field_values["Order Type"].strip()
  sales_order_field_values["sales_organization"] = sap_field_values["Sales Organization"].strip()
  sales_order_field_values["distribution_channel"] = sap_field_values["Distribution Channel"].strip()
  
  return sales_order_field_values
  
def standard_order_values(sap_field_values):
  standard_order_field_values = {}
  standard_order_field_values["sold_to_party"] = sap_field_values["Sold To Party"].strip()
  standard_order_field_values["customer_reference"] = sap_field_values["Customer Reference (PO #)"].strip()
  standard_order_field_values["delivery_block"] = sap_field_values["Delivery Block"].strip()
  standard_order_field_values["material"] = sap_field_values["Material (BAC Model)"].strip()
  standard_order_field_values["order_quantity"] = sap_field_values["Order Quantity"].strip()
  standard_order_field_values["plant"] = sap_field_values["Plant"].strip()
  
  return standard_order_field_values

#Set values for general requirement configurations  
def general_requirement_values(sap_field_values):
  general_requirement_configurations = {}
  general_requirement_configurations["region_specific"] = sap_field_values["Region Specific"].strip()
  general_requirement_configurations["model_number"] = sap_field_values["Model Number"].strip()
  general_requirement_configurations["unit_of_measure"] = sap_field_values["Unit of Measure"].strip()
  general_requirement_configurations["unit_flow_uom"] = sap_field_values["Unit Flow UOM"].strip()
  general_requirement_configurations["unit_flow"] = sap_field_values["Water Flow Rate"].strip()
  general_requirement_configurations["entering_water_temperature"] = sap_field_values["Entering Water Temperature"].strip()
  general_requirement_configurations["leaving_water_temperature"] = sap_field_values["Leaving Water Temperature"].strip()
  general_requirement_configurations["entering_wet_bulb_temp"] = sap_field_values["Entering Wet-Bulb Temp"].strip()
  general_requirement_configurations["fill_material"] = sap_field_values["Fill Material"].strip()
  general_requirement_configurations["cti_certification"] = sap_field_values["CTI Certification"].strip()
  #general_requirement_configurations["ibc"] = sap_field_values["IBC 2018 or Later?"] --This fields for US Region
  #general_requirement_configurations["california_oshpd_proj"] = sap_field_values["California OSHPD Project"] --This fields for US Region
  general_requirement_configurations["special_seismic"] = sap_field_values["Special Seismic Cert Required"].strip()
  general_requirement_configurations["fm_approval"] = sap_field_values["FM Approval"].strip()
  general_requirement_configurations["cooling_tower_structure"] = sap_field_values["Cooling Tower Structure"].strip()
  general_requirement_configurations["basinless_unit"] = sap_field_values["Basinless Unit"].strip()
  general_requirement_configurations["anchorage"] = sap_field_values["Anchorage"].strip()
  general_requirement_configurations["anchor_bolt_hole_spacing"] = sap_field_values["Anchor Bolt Hole Spacing"].strip()
  general_requirement_configurations["shipping_plant"] = sap_field_values["Shipping/Production Plant"].strip()
  general_requirement_configurations["field_assembly"] = sap_field_values["Knockdown For Field Assembly?"].strip()
  
  return general_requirement_configurations
  
#Set values for Water Management configurations
def water_management_values(sap_field_values):
  water_management_configurations = {}
  water_management_configurations["material_of_construction"] = sap_field_values["Material of Construction"].strip()
  water_management_configurations["casing_lovuver_material"] = sap_field_values["Casing and Louver Material"].strip()
  water_management_configurations["independent_cell_operation"] = sap_field_values["Independent Cell Operation?"].strip()
  water_management_configurations["inlet_outlet_connections"] = sap_field_values["Inlet/Outlet Connectons"].strip()
  water_management_configurations["outlet_strainer_material"] = sap_field_values["Outlet Strainer Material"].strip()
  water_management_configurations["depressed_sump_box"] = sap_field_values["Depressed Sump Box"].strip()
  water_management_configurations["sgl_inlet_piping_draing_valve"] = sap_field_values["SGL Inlet Piping Drain Valve"].strip()
  water_management_configurations["basin_water_level_control"] = sap_field_values["Basin Water Level Control"].strip()
  water_management_configurations["basin_heaters"] = sap_field_values["Basin Heaters"].strip()
  water_management_configurations["basin_sweeper_piping"] = sap_field_values["Basin Sweeper Piping"].strip()
  water_management_configurations["float_switch"] = sap_field_values["Float Switch"].strip()
  water_management_configurations["flume_box_options"] = sap_field_values["Flume Box Options"].strip()
  water_management_configurations["bottom_equalizer"] = sap_field_values["Bottom Equalizer/Bypass conn"].strip()
  water_management_configurations["end_equalizer"] = sap_field_values["End Equalizer/Bypass conn"].strip()
  water_management_configurations["standard_inlet_connection_size"] = sap_field_values["Standard Inlet Connection Size"].strip()
  water_management_configurations["inlet_connection_options"] = sap_field_values["Inlet Connection Options"].strip()
  water_management_configurations["inlet_connection_size_change"] = sap_field_values["Inlet Connection Size Change"].strip()
  water_management_configurations["standard_outlet_connection_size"] = sap_field_values["Standard Outlet Conn Size"].strip()
  water_management_configurations["outlet_connection_options"] = sap_field_values["Outlet Connection Options"].strip()
  water_management_configurations["outlet_connection_size_change"] = sap_field_values["Outlet Connection Size Change"].strip()
  
  return water_management_configurations
  
#--Set Values for Air Handling System---
def air_handling_values(sap_field_values):
  air_handling_configurations = {}
  air_handling_configurations["system_frequency"] = sap_field_values["System Frequency"].strip()
  air_handling_configurations["system_phase"] = sap_field_values["System Phase"].strip()
  air_handling_configurations["system_voltage"] = sap_field_values["System Voltage"].strip()
  air_handling_configurations["fan_type"] = sap_field_values["Fan Type"].strip()
  air_handling_configurations["fan_drive_system"] = sap_field_values["Fan Drive System"].strip()
  air_handling_configurations["enclosure"] = sap_field_values["Enclosure"].strip()
  air_handling_configurations["motor_efficiency_class"] = sap_field_values["Motor Efficiency Class"].strip()
  air_handling_configurations["manufacturer"] = sap_field_values["Manufacturer"].strip()
  air_handling_configurations["horsepower_motor_a"] = sap_field_values["Horsepower Motor A"].strip()
  air_handling_configurations["fan_motor_rpm"] = sap_field_values["Fan Motor RPM A"].strip()
  air_handling_configurations["fan_motor_type"] = sap_field_values["Fan Motor Type"].strip()
  air_handling_configurations["fan_motor_options_a"] = sap_field_values["Fan Motor Options A"].strip()
  #air_handling_configurations["add_shaft_grounding_ring"] = sap_field_values["Add Shaft Grounding Ring?"]
  air_handling_configurations["vibration_cutout_switch"] = sap_field_values["Vibration Cutout Switch (VCOS)"].strip()
  air_handling_configurations["extended_lube_line"] = sap_field_values["Extended Lube Line"].strip()
  air_handling_configurations["fan_motor_removal_system"] = sap_field_values["Fan Motor Removal System"].strip()
  
  return air_handling_configurations
  
def additional_config_vaues(sap_field_values):
  #-- Set additional Config values
  additional_configs = {}
  additional_configs["side_air_taken_option"] = sap_field_values["Side Air Intake Option"].strip()
  additional_configs["air_discharge_configuration"] = sap_field_values["Air Discharge Configuration"].strip()
  ad = additional_configs["air_discharge_configuration"]
  additional_configs["x_path"] = ""
  #check if string contains double quptes
  if aqString.Contains(ad, '"') < 0 :
     additional_configs["air_discharge_configuration"]
  else:
    #split the string by double quotes
    aqString.ListSeparator = '"'
    #get the first element
    first_element = aqString.GetListItem(ad, 0)
    #get the second element
    second_element = aqString.GetListItem(ad, 1)
    x_path = "//li[contains(text(), \"" + first_element + "\") and contains(text(), '"+second_element+"')]"
    additional_configs["x_path"] = x_path
  additional_configs["upgrade_fan_guard_material"] = sap_field_values["Upgrade Fan Guard Material?"].strip()
  additional_configs["fan_deck_safety_rails"] = sap_field_values["Fan Deck Safety Rails"].strip()
  additional_configs["3Side_safetyRail_to_exist_cell"] = sap_field_values["3Side SafetyRail to Exist Cell"].strip()
  additional_configs["ladder_fan_deck"] = sap_field_values["Ladder to Fan Deck"].strip()
  additional_configs["add_safety_cages_to_ladders"] = sap_field_values["Add Safety Cages to Ladders?"].strip()
  additional_configs["safety_gates_to_all_ladder"] = sap_field_values["Safety Gates to All Ladder?"].strip()
  additional_configs["ladder_safety_cage_extensions"] = sap_field_values["Ladder/Safety Cage Extensions"].strip()
  additional_configs["moc_platform_supports"] = sap_field_values["MOC-Platform Supports"].strip()
  additional_configs["fan_deck_ext_with_handrils"] = sap_field_values["Fan Deck Ext with Handrails"].strip()
  additional_configs["louver_face_platform"] = sap_field_values["Louver Face Platform"].strip()
  additional_configs["access_door_platform"] = sap_field_values["Access Door Platform"].strip()
  additional_configs["louver_face_cage_extension"] = sap_field_values["Louver Face Ldr/Cage Extension "].strip()
  additional_configs["access_door_pltf"] = sap_field_values["Access Door Pltf Ladder Ext"].strip()
  additional_configs["internal_walkway_access_door"] = sap_field_values["Internal Walkway @ Access Door"].strip()
  additional_configs["internal_walkway_moc"] = sap_field_values["Internal Walkway MOC"].strip()
  additional_configs["internal_access"] = sap_field_values["Internal Access"]
  return additional_configs

#Set Shipping Configs  
def shipping_values(sap_field_values):
  shipping_configs = {}
  shipping_configs["special_required"] = sap_field_values["Specials Required?"].strip()
  
  return shipping_configs