﻿def air_handling(air_handling_page, air_frame, air_page, air_handling_values):
  #---System Frequency:
  air_page.FindElement("//*[contains(text(),'System Frequency')]//parent :: span//parent :: label//parent::div//parent::div//span[@class='sapMSltLabel']").Click() 
  air_handling_page.WaitConfirm(1000)
  air_frame.FindElement("//li[.='"+air_handling_values["system_frequency"]+"']").Click()
  air_handling_page.WaitConfirm(1000)
  
  #---System Voltage:
  if air_handling_values["system_phase"] != "SAP Defined":
    air_page.FindElement("//*[contains(text(),'System Phase')]//parent :: span//parent :: label//parent::div//parent::div//span[@class='sapMSltLabel']").Click() 
    air_frame.FindElement("//li[.='"+air_handling_values["system_phase"]+"']").Click()
    air_handling_page.WaitConfirm(1000)
  
  #---System Voltage:
  if air_handling_values["system_voltage"] != "SAP Defined":
    air_page.FindElement("//*[contains(text(),'System Voltage')]//parent :: span//parent :: label//parent::div//parent::div//span[@class='sapMSltLabel']").Click() 
    air_frame.FindElement("//li[.='"+air_handling_values["system_voltage"]+"']").Click()
    air_handling_page.WaitConfirm(1000)
  
  #---Fan Type:
  air_page.FindElement("//*[contains(text(),'Fan Type')]//parent :: span//parent :: label//parent::div//parent::div//span[@class='sapMSltLabel']").Click() 
  air_handling_page.WaitConfirm(1000)
  air_frame.FindElement("//li[.='"+air_handling_values["fan_type"]+"']").Click()
  air_handling_page.WaitConfirm(1000)
  
  #---Fan Drive System:
  air_page.FindElement("//*[contains(text(),'Fan Drive System')]//parent :: span//parent :: label//parent::div//parent::div//span[@class='sapMSltLabel']").Click() 
  air_handling_page.WaitConfirm(2000)
  air_frame.FindElement("//li[.='"+air_handling_values["fan_drive_system"]+"']").Click()
  air_handling_page.WaitConfirm(2000)
  
  #---Upgrade Fan Shaft Material?
  air_page.FindElement("//*[contains(text(),'Upgrade Fan Shaft Material?')]//parent :: span//parent :: label//parent::div//parent::div//span[@class='sapMSltLabel']").Click() 
  air_handling_page.WaitConfirm(1000)
  if air_handling_values["upgrade_fan_shaft_material?"] != "No":
    air_frame.FindElement("//li[.='"+air_handling_values["upgrade_fan_shaft_material?"]+"']").Click()
  else:
    air_page.FindElement("//*[contains(text(),'Upgrade Fan Shaft Material?')]//parent :: span//parent :: label//parent::div//parent::div//span[@class='sapMSltLabel']").Keys(air_handling_values["upgrade_fan_shaft_material?"])
    air_page.FindElement("//*[contains(text(),'Upgrade Fan Shaft Material?')]//parent :: span//parent :: label//parent::div//parent::div//span[@class='sapMSltLabel']").Keys("[Enter]")
  air_handling_page.WaitConfirm(1000)
  
  #---Enclosure
  if air_handling_values["enclosure"] != "SAP Defined":
    air_page.FindElement("//*[contains(text(),'Enclosure')]//parent :: span//parent :: label//parent::div//parent::div//span[@class='sapMSltLabel']").Click() 
    air_handling_page.WaitConfirm(1000)
    air_frame.FindElement("//li[.='"+air_handling_values["enclosure"]+"']").Click()
    air_handling_page.WaitConfirm(1000)
  
  #---Motor Efficiency Class:
  air_page.FindElement("//*[contains(text(),'Motor Efficiency Class')]//parent :: span//parent :: label//parent::div//parent::div//span[@class='sapMSltLabel']").Click() 
  air_handling_page.WaitConfirm(1000)
  air_frame.FindElement("//li[.='"+air_handling_values["motor_efficiency_class"]+"']").Click()
  air_handling_page.WaitConfirm(1000)
  
  #---Manufacturer:
  if air_handling_values["manufacturer"] != "BAC Choice":
    air_page.FindElement("//*[contains(text(),'Manufacturer')]//parent :: span//parent :: label//parent::div//parent::div//span[@class='sapMSltLabel']").Click() 
    air_handling_page.WaitConfirm(1000)
    air_frame.FindElement("//li[.='"+air_handling_values["manufacturer"]+"']").Click()
    air_handling_page.WaitConfirm(1000)
  
  #---Horsepower Motor A:
  if air_handling_values["horsepower_motor_a"] != "SAP Defined":
    air_page.FindElement("//*[contains(text(),'Horsepower Motor A')]//parent :: span//parent :: label//parent::div//parent::div//span[@class='sapMSltLabel']").Click() 
    air_handling_page.WaitConfirm(1000)
    air_frame.FindElement("//li[.='"+air_handling_values["horsepower_motor_a"]+"']").Click()
    air_handling_page.WaitConfirm(1000)
  
  #---Fan Motor RPM A:
  if air_handling_values["fan_motor_rpm_a"] != "SAP Defined":
    air_page.FindElement("//*[contains(text(),'Fan Motor RPM A')]//parent :: span//parent :: label//parent::div//parent::div//span[@class='sapMSltLabel']").Click() 
    air_handling_page.WaitConfirm(1000)
    air_frame.FindElement("//li[.='"+air_handling_values["fan_motor_rpm_a"]+"']").Click()
    air_handling_page.WaitConfirm(1000)
  
  #---Fan Motor Type:
  air_page.FindElement("//*[contains(text(),'Fan Motor Type')]//parent :: span//parent :: label//parent::div//parent::div//span[@class='sapMSltLabel']").Click() 
  air_handling_page.WaitConfirm(1000)
  air_frame.FindElement("//li[.='"+air_handling_values["fan_motor_type"]+"']").Click()
  air_handling_page.WaitConfirm(1000)
  
  #---Fan Motor Quantity - Main A:
  if air_handling_values["fan_motor_quantity_main_a"] != "SAP Defined":
    air_page.FindElement("//*[contains(text(),'Fan Motor Quantity - Main A')]//parent :: span//parent :: label//parent::div//parent::div//span[@class='sapMSltLabel']").Click() 
    air_handling_page.WaitConfirm(1000)
    air_frame.FindElement("//li[.='"+air_handling_values["fan_motor_quantity_main_a"]+"']").Click()
    air_handling_page.WaitConfirm(1000)
  
  #---Fan Motor RPM A Pony:
  if air_handling_values["fan_motor_rpm__a_pony"] != "SAP Defined" and air_handling_values["fan_motor_rpm__a_pony"] != "Not Visible":
    air_page.FindElement("//*[contains(text(),'Fan Motor RPM A Pony')]//parent :: span//parent :: label//parent::div//parent::div//span[@class='sapMSltLabel']").Click() 
    air_handling_page.WaitConfirm(1000)
    air_frame.FindElement("//li[.='"+air_handling_values["fan_motor_rpm__a_pony"]+"']").Click()  
    
  #---Fan Motor Type - Pony:
  if air_handling_values["fan_motor_type_pony"] != "SAP Defined" and air_handling_values["fan_motor_type_pony"] != "Not Visible":
    air_page.FindElement("//*[contains(text(),'Fan Motor Type - Pony')]//parent :: span//parent :: label//parent::div//parent::div//span[@class='sapMSltLabel']").Click() 
    air_handling_page.WaitConfirm(1000)
    air_frame.FindElement("//li[.='"+air_handling_values["fan_motor_type_pony"]+"']").Click()
    air_handling_page.WaitConfirm(1000)
    
  #---Fan Motor Quantity - Pony A:
  if air_handling_values["fan_motor_quantity_pony_a"] != "SAP Defined" and air_handling_values["fan_motor_quantity_pony_a"] != "Not Visible":
    air_page.FindElement("//*[contains(text(),'Fan Motor Quantity - Pony A')]//parent :: span//parent :: label//parent::div//parent::div//span[@class='sapMSltLabel']").Click() 
    air_handling_page.WaitConfirm(1000)
    air_frame.FindElement("//li[.='"+air_handling_values["fan_motor_quantity_pony_a"]+"']").Click()
    air_handling_page.WaitConfirm(1000)
    
  #---Fan Motor Options A Pony:
  if air_handling_values["fan_motor_options_a_pony"] != "Not Visible":
    air_page.FindElement("//*[contains(text(),'Fan Motor Options A Pony')]//parent :: span//parent :: label//parent::div//parent::div//span[@class='sapMSltLabel']").Click() 
    air_handling_page.WaitConfirm(1000)
    air_frame.FindElement("//li[.='"+air_handling_values["fan_motor_options_a_pony"]+"']").Click()
    air_handling_page.WaitConfirm(1000)
    
  #---Shaft Grounding Ring - Pony A:
  if air_handling_values["shaft_grounding_ring_pony_a"] != "Not Visible":
    air_page.FindElement("//*[contains(text(),'Shaft Grounding Ring - Pony A')]//parent :: span//parent :: label//parent::div//parent::div//span[@class='sapMSltLabel']").Click() 
    air_handling_page.WaitConfirm(1000)
    air_page.FindElement("//*[contains(text(),'Shaft Grounding Ring - Pony A')]//parent :: span//parent :: label//parent::div//parent::div//span[@class='sapMSltLabel']").Keys(air_handling_values["shaft_grounding_ring_pony_a"])
    air_page.FindElement("//*[contains(text(),'Shaft Grounding Ring - Pony A')]//parent :: span//parent :: label//parent::div//parent::div//span[@class='sapMSltLabel']").Keys("[Enter]")
    air_handling_page.WaitConfirm(1000)
    
  #---Horsepower Motor B
  if air_handling_values["horsepower_motor_b"] != "SAP Defined" and air_handling_values["horsepower_motor_b"] != "Not Visible":
    air_page.FindElement("//*[contains(text(),'Horsepower Motor B')]//parent :: span//parent :: label//parent::div//parent::div//span[@class='sapMSltLabel']").Click() 
    page.WaitConfirm(1000)
    air_frame.FindElement("//li[.='"+air_handling_values["horsepower_motor_b"]+"']").Click()
    page.WaitConfirm(1000)
  
  #---Horsepower Motor B
  if air_handling_values["horsepower_motor_b"] != "SAP Defined" and air_handling_values["horsepower_motor_b"] != "Not Visible":
    air_page.FindElement("//*[contains(text(),'Horsepower Motor B')]//parent :: span//parent :: label//parent::div//parent::div//span[@class='sapMSltLabel']").Click() 
    air_handling_page.WaitConfirm(1000)
    air_frame.FindElement("//li[.='"+air_handling_values["horsepower_motor_b"]+"']").Click()
    air_handling_page.WaitConfirm(1000)
  
  #---Fan Motor RPM B
  if(air_handling_values["fan_motor_rpm_b"] != "SAP Defined" and air_handling_values["fan_motor_rpm_b"] != "Not Visible"):
      air_page.FindElement("//*[contains(text(),'Fan Motor RPM B')]//parent :: span//parent :: label//parent::div//parent::div//span[@class='sapMSltLabel']").Click() 
      air_handling_page.WaitConfirm(1000)
      air_frame.FindElement("//li[.='"+air_handling_values["fan_motor_rpm_b"]+"']").Click()
      air_handling_page.WaitConfirm(1000)
  
  #---Fan Motor Quantity - B:
  if(air_handling_values["fan_motor_quantity_b"] != "SAP Defined" and air_handling_values["fan_motor_quantity_b"] != "Not Visible"): 
    air_page.FindElement("//*[contains(text(),'Fan Motor Quantity - B:')]//parent :: span//parent :: label//parent::div//parent::div//span[@class='sapMSltLabel']").Click() 
    air_handling_page.WaitConfirm(1000)
    air_frame.FindElement("//li[.='"+air_handling_values["fan_motor_quantity_b"]+"']").Click()
    air_handling_page.WaitConfirm(1000)

  #---Fan Motor Options A:
  air_page.FindElement("//*[contains(text(),'Fan Motor Options A')]//parent :: span//parent :: label//parent::div//parent::div//span[@class='sapMSltLabel']").Click() 
  air_handling_page.WaitConfirm(1000)
  air_page.FindElement("//*[contains(text(),'Fan Motor Options A')]//parent :: span//parent :: label//parent::div//parent::div//span[@class='sapMSltLabel']").Keys(air_handling_values["fan_motor_options_a"])
  air_page.FindElement("//*[contains(text(),'Fan Motor Options A')]//parent :: span//parent :: label//parent::div//parent::div//span[@class='sapMSltLabel']").Keys("[Enter]")
  air_handling_page.WaitConfirm(2000)
  
  #---Add Shaft Grounding Ring:
  air_page.FindElement("//*[contains(text(),'Add Shaft Grounding Ring?')]//parent :: span//parent :: label//parent::div//parent::div//span[@class='sapMSltLabel']").Click()
  air_handling_page.WaitConfirm(1000)
  air_page.FindElement("//*[contains(text(),'Add Shaft Grounding Ring?')]//parent :: span//parent :: label//parent::div//parent::div//span[@class='sapMSltLabel']").Keys(air_handling_values["add_shaft_grounding_ring?"])
  air_page.FindElement("//*[contains(text(),'Add Shaft Grounding Ring?')]//parent :: span//parent :: label//parent::div//parent::div//span[@class='sapMSltLabel']").Keys("[Enter]")
  air_handling_page.WaitConfirm(1000)
  
  #---Fan Motor Options B:  
  if air_handling_values["fan_motor_options_b"] != "Not Visible":
    air_page.FindElement("//*[contains(text(),'Fan Motor Options B')]//parent :: span//parent :: label//parent::div//parent::div//span[@class='sapMSltLabel']").Click() 
    air_handling_page.WaitConfirm(3000)
    air_page.FindElement("//*[contains(text(),'Fan Motor Options B')]//parent :: span//parent :: label//parent::div//parent::div//span[@class='sapMSltLabel']").Keys(air_handling_values["fan_motor_options_b"])
    air_page.FindElement("//*[contains(text(),'Fan Motor Options B')]//parent :: span//parent :: label//parent::div//parent::div//span[@class='sapMSltLabel']").Keys("[Enter]")
    air_handling_page.WaitConfirm(2000) 
  
  #---Shaft Grounding Ring - Main B:
  if air_handling_values["shaft_grounding_ring_main_b"] != "Not Visible":
    air_page.FindElement("//*[contains(text(),'Shaft Grounding Ring - Main B')]//parent :: span//parent :: label//parent::div//parent::div//span[@class='sapMSltLabel']").Click()
    air_handling_page.WaitConfirm(1000)
    air_page.FindElement("//*[contains(text(),'Shaft Grounding Ring - Main B')]//parent :: span//parent :: label//parent::div//parent::div//span[@class='sapMSltLabel']").Keys(air_handling_values["shaft_grounding_ring_main_b"])
    air_page.FindElement("//*[contains(text(),'Shaft Grounding Ring - Main B')]//parent :: span//parent :: label//parent::div//parent::div//span[@class='sapMSltLabel']").Keys("[Enter]")
    air_handling_page.WaitConfirm(1000)
  
  #---Vibration Cutout Switch (VCOS):
  air_page.FindElement("//*[contains(text(),'Vibration Cutout Switch (VCOS)')]//parent :: span//parent :: label//parent::div//parent::div//span[@class='sapMSltLabel']").Click() 
  air_handling_page.WaitConfirm(1000)
  if air_handling_values["vibration_cutout_switch"] != 'None':
    air_frame.FindElement("//li[.='"+air_handling_values["vibration_cutout_switch"]+"']").Click()
  else:
    air_page.FindElement("//*[contains(text(),'Vibration Cutout Switch (VCOS)')]//parent :: span//parent :: label//parent::div//parent::div//span[@class='sapMSltLabel']").Keys(air_handling_values["vibration_cutout_switch"])
    air_page.FindElement("//*[contains(text(),'Vibration Cutout Switch (VCOS)')]//parent :: span//parent :: label//parent::div//parent::div//span[@class='sapMSltLabel']").Keys("[Enter]")
  air_handling_page.WaitConfirm(1000)
  
  #---Extended Lube Line:
  air_page.FindElement("//*[contains(text(),'Extended Lube Line')]//parent :: span//parent :: label//parent::div//parent::div//span[@class='sapMSltLabel']").Click() 
  air_handling_page.WaitConfirm(1000)
  air_page.FindElement("//*[contains(text(),'Extended Lube Line')]//parent :: span//parent :: label//parent::div//parent::div//span[@class='sapMSltLabel']").Keys(air_handling_values["extended_lube_line"]) 
  air_page.FindElement("//*[contains(text(),'Extended Lube Line')]//parent :: span//parent :: label//parent::div//parent::div//span[@class='sapMSltLabel']").Keys("[Enter]")
  air_handling_page.WaitConfirm(1000)
  
  #---Fan Motor Removal System:
  air_page.FindElement("//*[contains(text(),'Fan Motor Removal System')]//parent :: span//parent :: label//parent::div//parent::div//span[@class='sapMSltLabel']").Click() 
  air_handling_page.WaitConfirm(1000)
  if air_handling_values["fan_motor_removal_system"] != "None":
    air_frame.FindElement("//li[.='"+air_handling_values["fan_motor_removal_system"]+"']").Click()
  else:
    air_page.FindElement("//*[contains(text(),'Fan Motor Removal System')]//parent :: span//parent :: label//parent::div//parent::div//span[@class='sapMSltLabel']").Keys(air_handling_values["fan_motor_removal_system"])
    air_page.FindElement("//*[contains(text(),'Fan Motor Removal System')]//parent :: span//parent :: label//parent::div//parent::div//span[@class='sapMSltLabel']").Keys("[Enter]")
  air_handling_page.WaitConfirm(1000)
  
  #---Factory Wiring:
  air_page.FindElement("//*[contains(text(),'Factory Wiring')]//parent :: span//parent :: label//parent::div//parent::div//span[@class='sapMSltLabel']").Click() 
  air_handling_page.WaitConfirm(1000)
  if air_handling_values["factory_wiring"] != "None":
    air_frame.FindElement("//li[.='"+air_handling_values["factory_wiring"]+"']").Click()
  else:
    air_page.FindElement("//*[contains(text(),'Factory Wiring')]//parent :: span//parent :: label//parent::div//parent::div//span[@class='sapMSltLabel']").Keys(air_handling_values["factory_wiring"])
    air_page.FindElement("//*[contains(text(),'Factory Wiring')]//parent :: span//parent :: label//parent::div//parent::div//span[@class='sapMSltLabel']").Keys("[Enter]")
  air_handling_page.WaitConfirm(1000)
  
  #---go to Additional Enhancements:
  air_page.FindElement("//span[.='Additional Enhancements']").Click()