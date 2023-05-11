def water_management(page, water_management_values):
  frame = page.sectionShellSplitCanvas.frameApplicationSalesdocumentCre.formWebguiform0.frameC102
  textNode = frame.sectionShellSplitCanvas.sectionApplicationVariantconfigu
  textNode2 = textNode.sectionSplitter0Content1
  textNode2.FindElement("//span[.='Water Management']").Click()
  #--Material of Construction
  material_of_construciton = frame.FindElement("//*[contains(text(),'Material of Construction')]//parent :: span//parent :: label//parent::div//parent::div//span[@class='sapMSltLabel']")
  material_of_construciton.Click()
  page.WaitConfirm(1000)
  frame.FindElement("//li[.='"+water_management_values["material_of_construction"]+"']").Click()
  page.WaitConfirm(1000)
  #--Unit Orientation
  textNode2.FindElement("//*[contains(text(),'Unit Orientation')]//parent :: span//parent :: label//parent::div//parent::div//span[@class='sapMSltLabel']").Click()
  page.WaitConfirm(1000)
  frame.FindElement("//li[.='"+water_management_values["unit_orientation"]+"']").Click()
  page.WaitConfirm(1000)
  
  #--Spray Water Outlet
  textNode2.FindElement("//*[contains(text(),'Spray Water Outlet')]//parent :: span//parent :: label//parent::div//parent::div//span[@class='sapMSltLabel']").Click()
  page.WaitConfirm(1000)
  frame.FindElement("//li[.='"+water_management_values["spray_water_outlet"]+"']").Click()
  page.WaitConfirm(1000)
  
  #Spray Distribution Piping
  isEnabled = textNode2.FindElement("//*[contains(text(),'Spray Distribution Piping')]//parent :: span//parent :: label//parent::div//parent::div//span[@class='sapMSltLabel']//preceding-sibling::input[@class='sapUiPseudoInvisibleText sapMSltHiddenSelect']").getAttribute("aria-readonly")
  if isEnabled == "false":
    section2.FindElement("//*[contains(text(),'Spray Distribution Piping')]//parent :: span//parent :: label//parent::div//parent::div//span[@class='sapMSltLabel']").Click()
    page.WaitConfirm(1000)
    frame.FindElement("//li[.='"+water_management_values["spray_distribution_piping"]+"']").Click()
    page.WaitConfirm(1000)
  
  #Spray Pump Motor Type
  if water_management_values["spray_pump_motor_type"] != "SAP Defined":
    section2.FindElement("//*[contains(text(),'Spray Pump Motor Type')]//parent :: span//parent :: label//parent::div//parent::div//span[@class='sapMSltLabel']").Click()
    page.WaitConfirm(1000)
    frame.FindElement("//li[.='"+water_management_values["spray_pump_motor_type"]+"']").Click()
    page.WaitConfirm(1000)
  
  #Pump Motor Efficiency Class
  if water_management_values["pump_motor_efficiency_class"] != "SAP Defined":
    section2.FindElement("//*[contains(text(),'Pump Motor Efficiency Class')]//parent :: span//parent :: label//parent::div//parent::div//span[@class='sapMSltLabel']").Click()
    page.WaitConfirm(1000)
    frame.FindElement("//li[.='"+water_management_values["pump_motor_efficiency_class"]+"']").Click()
    page.WaitConfirm(2000)
  
  #Basin Water Level Control
  if water_management_values["basin_water_level_control"] != "SAP Defined":
    textNode2.FindElement("//*[contains(text(),'Basin Water Level Control')]//parent :: span//parent :: label//parent::div//parent::div//span[@class='sapMSltLabel']").Click()
    page.WaitConfirm(1000)
    if water_management_values["basin_water_level_control"] != "None":
      frame.FindElement("//li[.='"+water_management_values["basin_water_level_control"]+"']").Click()
    else:
      textNode2.FindElement("//*[contains(text(),'Basin Water Level Control')]//parent :: span//parent :: label//parent::div//parent::div//span[@class='sapMSltLabel']").Keys(water_management_values["basin_water_level_control"])
      textNode2.FindElement("//*[contains(text(),'Basin Water Level Control')]//parent :: span//parent :: label//parent::div//parent::div//span[@class='sapMSltLabel']").Keys("[Enter]")
    page.WaitConfirm(1000)
  
  #Basin Heaters
  if water_management_values["basin_heaters"] != "SAP Defined":
    textNode2.FindElement("//*[contains(text(),'Basin Heaters')]//parent :: span//parent :: label//parent::div//parent::div//span[@class='sapMSltLabel']").Click() 
    page.WaitConfirm(1000)
    if water_management_values["basin_heaters"] != "None":
      frame.FindElement("//li[.='"+water_management_values["basin_heaters"]+"']").Click()
    else:
      textNode2.FindElement("//*[contains(text(),'Basin Heaters')]//parent :: span//parent :: label//parent::div//parent::div//span[@class='sapMSltLabel']").Keys(water_management_values["basin_heaters"])
      textNode2.FindElement("//*[contains(text(),'Basin Heaters')]//parent :: span//parent :: label//parent::div//parent::div//span[@class='sapMSltLabel']").Keys("[Enter]")
    page.WaitConfirm(2000)
    
  #heater_element_material
  if water_management_values["heater_element_material"] != "Not Visible":
    textNode2.FindElement("//*[contains(text(),'Heater Element Material')]//parent :: span//parent :: label//parent::div//parent::div//span[@class='sapMSltLabel']").Click()
    page.WaitConfirm(1000)
    frame.FindElement("//li[.='"+water_management_values["heater_element_material"]+"']").Click()
    page.WaitConfirm(1000)
    
   #Basin Heater Controls
  if water_management_values["basin_heater_controls"] != "Not Visible":
    textNode2.FindElement("//*[contains(text(),'Basin Heater Controls')]//parent :: span//parent :: label//parent::div//parent::div//span[@class='sapMSltLabel']").Click()
    page.WaitConfirm(1000)
    frame.FindElement("//li[.='"+water_management_values["basin_heater_controls"]+"']").Click()
    page.WaitConfirm(1000)
  
  #Basin Sweeper Piping:
  textNode2.FindElement("//*[contains(text(),'Basin Sweeper Piping')]//parent :: span//parent :: label//parent::div//parent::div//span[@class='sapMSltLabel']").Click() 
  page.WaitConfirm(2000)
  if water_management_values["basin_sweeper_piping"] != "None":
    frame.FindElement("//li[.='"+water_management_values["basin_sweeper_piping"]+"']").Click()
  else:
    textNode2.FindElement("//*[contains(text(),'Basin Sweeper Piping')]//parent :: span//parent :: label//parent::div//parent::div//span[@class='sapMSltLabel']").Keys(water_management_values["basin_sweeper_piping"])
    textNode2.FindElement("//*[contains(text(),'Basin Sweeper Piping')]//parent :: span//parent :: label//parent::div//parent::div//span[@class='sapMSltLabel']").Keys("[Enter]")
  page.WaitConfirm(1000)
  
  #Float Switch:
  textNode2.FindElement("//*[contains(text(),'Float Switch')]//parent :: span//parent :: label//parent::div//parent::div//span[@class='sapMSltLabel']").Click() 
  page.WaitConfirm(1000)
  if water_management_values["float_switch"] != "None": 
    frame.FindElement("//li[.='"+water_management_values["float_switch"]+"']").Click()
  else:
    textNode2.FindElement("//*[contains(text(),'Float Switch')]//parent :: span//parent :: label//parent::div//parent::div//span[@class='sapMSltLabel']").Keys(water_management_values["float_switch"])
    textNode2.FindElement("//*[contains(text(),'Float Switch')]//parent :: span//parent :: label//parent::div//parent::div//span[@class='sapMSltLabel']").Keys("[Enter]")
  page.WaitConfirm(1000)