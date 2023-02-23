import AirHandlingConfiguration

def water_management(page, water_management_values):
  frame = page.sectionShellSplitCanvas.frameApplicationSalesdocumentCre.formWebguiform0.frameC102
  textNode = frame.sectionShellSplitCanvas.sectionApplicationVariantconfigu
  textNode2 = textNode.sectionSplitter0Content1
  textNode2.FindElement("//span[.='Water Management']").Click()
  #page.WaitConfirm(15000)
  #textNode2.textnodeWaterManagement.Click()
  material_of_construciton = frame.FindElement("//*[contains(text(),'Material of Construction')]//parent :: span//parent :: label//parent::div//parent::div//span[@class='sapMSltLabel']")
  material_of_construciton.Click()
  page.WaitConfirm(1000)
  frame.FindElement("//li[.='"+water_management_values["material_of_construction"]+"']").Click()
  page.WaitConfirm(1000)
  #--Casing and Louver Material
  textNode2.FindElement("//*[contains(text(),'Casing and Louver Material')]//parent :: span//parent :: label//parent::div//parent::div//span[@class='sapMSltLabel']").Click()
  page.WaitConfirm(1000)
  frame.FindElement("//li[.='"+water_management_values["casing_lovuver_material"]+"']").Click()
  page.WaitConfirm(1000)
  #frame.sectionShellSplitCanvas.sectionApplicationVariantconfigu.sectionSplitter0Content1.panelConfigurationcomponentValua5.Drag(1024, 39, 5, 176)
  
  #--Independent Cell Operation?
  textNode2.FindElement("//*[contains(text(),'Independent Cell Operation?')]//parent :: span//parent :: label//parent::div//parent::div//span[@class='sapMSltLabel']").Click()
  page.WaitConfirm(1000)
  #frame.FindElement("//ul[contains(@id,'list96')]//li[contains(text(),'"+water_management_values["independent_cell_operation"]+"')]").Click()
  frame.FindElement("//bdi[text()='Independent Cell Operation?:']//preceding::div[@class='sapUiSimpleFixFlexFlexContent'][1]//li[text()='"+water_management_values["independent_cell_operation"]+"']").Click()
  page.WaitConfirm(1000)
  
  #Inlet/Outlet connections
  textNode2.FindElement("//*[contains(text(),'Inlet/Outlet Connections')]//parent :: span//parent :: label//parent::div//parent::div//span[@class='sapMSltLabel']").Click()
  page.WaitConfirm(1000)
  frame.FindElement("//li[.='"+water_management_values["inlet_outlet_connections"]+"']").Click()
  page.WaitConfirm(1000)
  
  #Depressed Sum Box
  if water_management_values["depressed_sump_box"] != "None":
    textNode2.FindElement("//*[contains(text(),'Depressed Sump Box')]//parent :: span//parent :: label//parent::div//parent::div//span[@class='sapMSltLabel']").Click()
    page.WaitConfirm(1000)
    frame.FindElement("//li[.='"+water_management_values["depressed_sump_box"]+"']").Click()
    page.WaitConfirm(1000)
  
  #SGL Inlet Piping Drain Valve
  if water_management_values["sgl_inlet_piping_draing_valve"] != "None":
    textNode2.FindElement("//*[contains(text(),'SGL Inlet Piping Drain Valve')]//parent :: span//parent :: label//parent::div//parent::div//span[@class='sapMSltLabel']").Click()
    page.WaitConfirm(1000)
    frame.FindElement("//li[.='"+water_management_values["sgl_inlet_piping_draing_valve"]+"']").Click()
    page.WaitConfirm(1000)
  
  #Basin Water Level Control
  if water_management_values["basin_water_level_control"] != "None":
    textNode2.FindElement("//*[contains(text(),'Basin Water Level Control')]//parent :: span//parent :: label//parent::div//parent::div//span[@class='sapMSltLabel']").Click()
    page.WaitConfirm(1000)
    frame.FindElement("//li[.='"+water_management_values["basin_water_level_control"]+"']").Click()
    page.WaitConfirm(1000)
  
  #Basin Heaters
  if water_management_values["basin_heaters"] != "None":
    textNode2.FindElement("//*[contains(text(),'Basin Heaters')]//parent :: span//parent :: label//parent::div//parent::div//span[@class='sapMSltLabel']").Click() 
    page.WaitConfirm(1000)
    frame.FindElement("//li[.='"+water_management_values["basin_heaters"]+"']").Click()
    page.WaitConfirm(2000)
  
  #Basin Sweeper Piping:
  if water_management_values["basin_sweeper_piping"] != "None":
    textNode2.FindElement("//*[contains(text(),'Basin Sweeper Piping')]//parent :: span//parent :: label//parent::div//parent::div//span[@class='sapMSltLabel']").Click() 
    page.WaitConfirm(2000)
    frame.FindElement("//li[.='"+water_management_values["basin_sweeper_piping"]+"']").Click()
    page.WaitConfirm(1000)
  
  #frame.sectionShellSplitCanvas.sectionApplicationVariantconfigu.sectionSplitter0Content1.panelConfigurationcomponentValua5.Drag(1024, 39, 5, 176)
  
  #Float Switch:
  if water_management_values["float_switch"] != "None":
    textNode2.FindElement("//*[contains(text(),'Float Switch')]//parent :: span//parent :: label//parent::div//parent::div//span[@class='sapMSltLabel']").Click() 
    page.WaitConfirm(1000)
    frame.FindElement("//li[.='"+water_management_values["float_switch"]+"").Click()
    page.WaitConfirm(1000)
  
  #Flume Box Options:
  if water_management_values["flume_box_options"] != "None":
    textNode2.FindElement("//*[contains(text(),'Flume Box Options')]//parent :: span//parent :: label//parent::div//parent::div//span[@class='sapMSltLabel']").Click() 
    page.WaitConfirm(1000)
    frame.FindElement("//li[.='"+water_management_values["flume_box_options"]+"']").Click()
    page.WaitConfirm(1000)
  
  #Bottom Equalizer/Bypass conn:
  if water_management_values["bottom_equalizer"] != "None":
    textNode2.FindElement("//*[contains(text(),'Bottom Equalizer/Bypass conn')]//parent :: span//parent :: label//parent::div//parent::div//span[@class='sapMSltLabel']").Click() 
    page.WaitConfirm(1000)
    frame.FindElement("//li[.='"+water_management_values["bottom_equalizer"]+"']").Click()
    page.WaitConfirm(1000)
  
  #End Equalizer/Bypass conn:
  if water_management_values["end_equalizer"] != "None":
    textNode2.FindElement("(//span[.='End Equalizer/Bypass conn']//parent::label//parent::div//parent::div//child::span)[3]").Click() 
    page.WaitConfirm(1000)
    frame.FindElement("//li[.='"+water_management_values["end_equalizer"]+"']").Click()
    page.WaitConfirm(1000)
  
  #Inlet Connection Size Change:
  if water_management_values["inlet_connection_size_change"] != "None":
    textNode2.FindElement("//*[contains(text(),'Inlet Connection Size Change')]//parent :: span//parent :: label//parent::div//parent::div//span[@class='sapMSltLabel']").Click()
    page.WaitConfirm(1000)
    frame.FindElement("//li[.='"+water_management_values["inlet_connection_size_change"]+"']").Click()
    page.WaitConfirm(1000)
  
  #Outlet Connection Size Change:
  if water_management_values["outlet_connection_size_change"] != "None":
    textNode2.FindElement("//*[contains(text(),'Outlet Connection Size Change')]//parent :: span//parent :: label//parent::div//parent::div//span[@class='sapMSltLabel']").Click() 
    page.WaitConfirm(1000)
    frame.FindElement("//li[.='"+water_management_values["outlet_connection_size_change"]+"']").Click()
    page.WaitConfirm(1000)
  
  textNode2.FindElement("//span[.='Air Handling System']").Click()