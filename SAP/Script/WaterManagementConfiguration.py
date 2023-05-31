import AirHandlingConfiguration

def water_management(water_management_page, water_management_values):
  variant_config_frame = water_management_page.sectionShellSplitCanvas.frameApplicationSalesdocumentCre.formWebguiform0.frameC102
  variant_config_textNode = variant_config_frame.sectionShellSplitCanvas.sectionApplicationVariantconfigu
  variant_config_textNode2 = variant_config_textNode.sectionSplitter0Content1
  variant_config_textNode2.FindElement("//span[.='Water Management']").Click()
  #---Material of Construction:
  material_of_construciton_field = variant_config_frame.FindElement("//*[contains(text(),'Material of Construction')]//parent :: span//parent :: label//parent::div//parent::div//span[@class='sapMSltLabel']")
  material_of_construciton_field.Click()
  water_management_page.WaitConfirm(1000)
  variant_config_frame.FindElement("//li[.='"+water_management_values["material_of_construction"]+"']").Click()
  water_management_page.WaitConfirm(1000)
  
  #---Casing and Louver Material:
  variant_config_textNode2.FindElement("//*[contains(text(),'Casing and Louver Material')]//parent :: span//parent :: label//parent::div//parent::div//span[@class='sapMSltLabel']").Click()
  water_management_page.WaitConfirm(1000)
  variant_config_frame.FindElement("//li[.='"+water_management_values["casing_lovuver_material"]+"']").Click()
  water_management_page.WaitConfirm(1000)
  
  #---Independent Cell Operation:
  variant_config_textNode2.FindElement("//*[contains(text(),'Independent Cell Operation?')]//parent :: span//parent :: label//parent::div//parent::div//span[@class='sapMSltLabel']").Click()
  water_management_page.WaitConfirm(1000)
  variant_config_textNode2.FindElement("//*[contains(text(),'Independent Cell Operation?')]//parent :: span//parent :: label//parent::div//parent::div//span[@class='sapMSltLabel']").Keys(water_management_values["independent_cell_operation"])
  variant_config_textNode2.FindElement("//*[contains(text(),'Independent Cell Operation?')]//parent :: span//parent :: label//parent::div//parent::div//span[@class='sapMSltLabel']").Keys("[Enter]")
  water_management_page.WaitConfirm(3000)
  
  #---Inlet/Outlet connections:
  variant_config_textNode2.FindElement("//*[contains(text(),'Inlet/Outlet Connections')]//parent :: span//parent :: label//parent::div//parent::div//span[@class='sapMSltLabel']").Click()
  water_management_page.WaitConfirm(1000)
  variant_config_frame.FindElement("//li[.='"+water_management_values["inlet_outlet_connections"]+"']").Click()
  water_management_page.WaitConfirm(2000)
  
  #---Depressed Sum Box: 
  if water_management_values["depressed_sump_box"] != "SAP Defined": 
      variant_config_textNode2.FindElement("//*[contains(text(),'Depressed Sump Box')]//parent :: span//parent :: label//parent::div//parent::div//span[@class='sapMSltLabel']").Click()
      water_management_page.WaitConfirm(1000)
      if water_management_values["depressed_sump_box"] != "None":
        variant_config_frame.FindElement("//li[.='"+water_management_values["depressed_sump_box"]+"']").Click()
      else:
        variant_config_textNode2.FindElement("//*[contains(text(),'Depressed Sump Box')]//parent :: span//parent :: label//parent::div//parent::div//span[@class='sapMSltLabel']").Keys(water_management_values["depressed_sump_box"])
        variant_config_textNode2.FindElement("//*[contains(text(),'Depressed Sump Box')]//parent :: span//parent :: label//parent::div//parent::div//span[@class='sapMSltLabel']").Keys("[Enter]")
      water_management_page.WaitConfirm(1000)
  
  #---SGL Inlet Piping Drain Valve:
  variant_config_textNode2.FindElement("//*[contains(text(),'SGL Inlet Piping Drain Valve')]//parent :: span//parent :: label//parent::div//parent::div//span[@class='sapMSltLabel']").Click()
  water_management_page.WaitConfirm(1000)
  if water_management_values["sgl_inlet_piping_draing_valve"] != "None":
    variant_config_frame.FindElement("//li[.='"+water_management_values["sgl_inlet_piping_draing_valve"]+"']").Click()
  else:
    variant_config_textNode2.FindElement("//*[contains(text(),'SGL Inlet Piping Drain Valve')]//parent :: span//parent :: label//parent::div//parent::div//span[@class='sapMSltLabel']").Keys(water_management_values["sgl_inlet_piping_draing_valve"])
    variant_config_textNode2.FindElement("//*[contains(text(),'SGL Inlet Piping Drain Valve')]//parent :: span//parent :: label//parent::div//parent::div//span[@class='sapMSltLabel']").Keys("[Enter]")
  water_management_page.WaitConfirm(1000)
  
  #---Basin Water Level Control:
  if water_management_values["basin_water_level_control"] != "SAP Defined":
    variant_config_textNode2.FindElement("//*[contains(text(),'Basin Water Level Control')]//parent :: span//parent :: label//parent::div//parent::div//span[@class='sapMSltLabel']").Click()
    water_management_page.WaitConfirm(1000)
    if water_management_values["basin_water_level_control"] != "None":
      variant_config_frame.FindElement("//li[.='"+water_management_values["basin_water_level_control"]+"']").Click()
    else:
      variant_config_textNode2.FindElement("//*[contains(text(),'Basin Water Level Control')]//parent :: span//parent :: label//parent::div//parent::div//span[@class='sapMSltLabel']").Keys(water_management_values["basin_water_level_control"])
      variant_config_textNode2.FindElement("//*[contains(text(),'Basin Water Level Control')]//parent :: span//parent :: label//parent::div//parent::div//span[@class='sapMSltLabel']").Keys("[Enter]")
    water_management_page.WaitConfirm(1000)
  
  #---Basin Heaters:
  if water_management_values["basin_heaters"] != "SAP Defined":
    variant_config_textNode2.FindElement("//*[contains(text(),'Basin Heaters')]//parent :: span//parent :: label//parent::div//parent::div//span[@class='sapMSltLabel']").Click() 
    water_management_page.WaitConfirm(1000)
    if water_management_values["basin_heaters"] != "None":
      variant_config_frame.FindElement("//li[.='"+water_management_values["basin_heaters"]+"']").Click()
    else:
      variant_config_textNode2.FindElement("//*[contains(text(),'Basin Heaters')]//parent :: span//parent :: label//parent::div//parent::div//span[@class='sapMSltLabel']").Keys(water_management_values["basin_heaters"])
      variant_config_textNode2.FindElement("//*[contains(text(),'Basin Heaters')]//parent :: span//parent :: label//parent::div//parent::div//span[@class='sapMSltLabel']").Keys("[Enter]")
    water_management_page.WaitConfirm(2000)
  
  #---Basin Sweeper Piping:
  variant_config_textNode2.FindElement("//*[contains(text(),'Basin Sweeper Piping')]//parent :: span//parent :: label//parent::div//parent::div//span[@class='sapMSltLabel']").Click() 
  water_management_page.WaitConfirm(2000)
  if water_management_values["basin_sweeper_piping"] != "None":
    variant_config_frame.FindElement("//li[.='"+water_management_values["basin_sweeper_piping"]+"']").Click()
  else:
    variant_config_textNode2.FindElement("//*[contains(text(),'Basin Sweeper Piping')]//parent :: span//parent :: label//parent::div//parent::div//span[@class='sapMSltLabel']").Keys(water_management_values["basin_sweeper_piping"])
    variant_config_textNode2.FindElement("//*[contains(text(),'Basin Sweeper Piping')]//parent :: span//parent :: label//parent::div//parent::div//span[@class='sapMSltLabel']").Keys("[Enter]")
  water_management_page.WaitConfirm(1000)
  
  #---Float Switch:
  variant_config_textNode2.FindElement("//*[contains(text(),'Float Switch')]//parent :: span//parent :: label//parent::div//parent::div//span[@class='sapMSltLabel']").Click() 
  water_management_page.WaitConfirm(1000)
  if water_management_values["float_switch"] != "None": 
    variant_config_frame.FindElement("//li[.='"+water_management_values["float_switch"]+"']").Click()
  else:
    variant_config_textNode2.FindElement("//*[contains(text(),'Float Switch')]//parent :: span//parent :: label//parent::div//parent::div//span[@class='sapMSltLabel']").Keys(water_management_values["float_switch"])
    variant_config_textNode2.FindElement("//*[contains(text(),'Float Switch')]//parent :: span//parent :: label//parent::div//parent::div//span[@class='sapMSltLabel']").Keys("[Enter]")
  water_management_page.WaitConfirm(1000)
  
  #---Flume Box Options:
  if water_management_values["flume_box_options"] != "No Flume Box(es)":
    variant_config_textNode2.FindElement("//*[contains(text(),'Flume Box Options')]//parent :: span//parent :: label//parent::div//parent::div//span[@class='sapMSltLabel']").Click() 
    water_management_page.WaitConfirm(1000)
    if water_management_values["flume_box_options"] != "None":
      variant_config_frame.FindElement("//li[.='"+water_management_values["flume_box_options"]+"']").Click()
    else:
      variant_config_textNode2.FindElement("//*[contains(text(),'Flume Box Options')]//parent :: span//parent :: label//parent::div//parent::div//span[@class='sapMSltLabel']").Keys(water_management_values["flume_box_options"])
      variant_config_textNode2.FindElement("//*[contains(text(),'Flume Box Options')]//parent :: span//parent :: label//parent::div//parent::div//span[@class='sapMSltLabel']").Click("[Enter]")
    water_management_page.WaitConfirm(1000)
  
  #---Bottom Equalizer/Bypass conn:
  variant_config_textNode2.FindElement("//*[contains(text(),'Bottom Equalizer/Bypass conn')]//parent :: span//parent :: label//parent::div//parent::div//span[@class='sapMSltLabel']").Click() 
  water_management_page.WaitConfirm(1000)
  if water_management_values["bottom_equalizer"] != "None":
    variant_config_frame.FindElement("//li[.='"+water_management_values["bottom_equalizer"]+"']").Click()
  else:
    variant_config_textNode2.FindElement("//*[contains(text(),'Bottom Equalizer/Bypass conn')]//parent :: span//parent :: label//parent::div//parent::div//span[@class='sapMSltLabel']").Keys(water_management_values["bottom_equalizer"])
    variant_config_textNode2.FindElement("//*[contains(text(),'Bottom Equalizer/Bypass conn')]//parent :: span//parent :: label//parent::div//parent::div//span[@class='sapMSltLabel']").Keys("[Enter]")
  water_management_page.WaitConfirm(2000)
  
  #---End Equalizer/Bypass conn:
  variant_config_textNode2.FindElement("//*[contains(text(),'End Equalizer/Bypass conn')]//parent :: span//parent :: label//parent::div//parent::div//span[@class='sapMSltLabel']").Click()
  water_management_page.WaitConfirm(1000)
  if water_management_values["end_equalizer"] != "None":
    variant_config_frame.FindElement("//li[.='"+water_management_values["end_equalizer"]+"']").Click()
  else:
    variant_config_textNode2.FindElement("//*[contains(text(),'End Equalizer/Bypass conn')]//parent :: span//parent :: label//parent::div//parent::div//span[@class='sapMSltLabel']").Keys(water_management_values["end_equalizer"])
    variant_config_textNode2.FindElement("//*[contains(text(),'End Equalizer/Bypass conn')]//parent :: span//parent :: label//parent::div//parent::div//span[@class='sapMSltLabel']").Keys("[Enter]")
  water_management_page.WaitConfirm(1000)
  
  #---Inlet Connection Size Change:
  variant_config_textNode2.FindElement("//*[contains(text(),'Inlet Connection Size Change')]//parent :: span//parent :: label//parent::div//parent::div//span[@class='sapMSltLabel']").Click()
  water_management_page.WaitConfirm(1000)
  if water_management_values["inlet_connection_size_change"] != "None":
    variant_config_frame.FindElement("//li[.='"+water_management_values["inlet_connection_size_change"]+"']").Click()
  else:
    variant_config_textNode2.FindElement("//*[contains(text(),'Inlet Connection Size Change')]//parent :: span//parent :: label//parent::div//parent::div//span[@class='sapMSltLabel']").Keys(water_management_values["inlet_connection_size_change"])
    variant_config_textNode2.FindElement("//*[contains(text(),'Inlet Connection Size Change')]//parent :: span//parent :: label//parent::div//parent::div//span[@class='sapMSltLabel']").Keys("[Enter]")
  water_management_page.WaitConfirm(1000)
  
  #---Outlet Connection Size Change:
  variant_config_textNode2.FindElement("//*[contains(text(),'Outlet Connection Size Change')]//parent :: span//parent :: label//parent::div//parent::div//span[@class='sapMSltLabel']").Click() 
  water_management_page.WaitConfirm(1000)
  if water_management_values["outlet_connection_size_change"] != "None":
    variant_config_frame.FindElement("//li[.='"+water_management_values["outlet_connection_size_change"]+"']").Click()
  else:
    variant_config_textNode2.FindElement("//*[contains(text(),'Outlet Connection Size Change')]//parent :: span//parent :: label//parent::div//parent::div//span[@class='sapMSltLabel']").Keys(water_management_values["outlet_connection_size_change"])
    variant_config_textNode2.FindElement("//*[contains(text(),'Outlet Connection Size Change')]//parent :: span//parent :: label//parent::div//parent::div//span[@class='sapMSltLabel']").Keys("[Enter]")
  water_management_page.WaitConfirm(1000)
  
  #---go to Air Handling System:
  variant_config_textNode2.FindElement("//span[.='Air Handling System']").Click()