import AdditionalEnhancement

def air_handling(page, air_frame, air_page, air_handling_values):
  #System Frequency
  air_page.FindElement("//*[contains(text(),'System Frequency')]//parent :: span//parent :: label//parent::div//parent::div//span[@class='sapMSltLabel']").Click() 
  page.WaitConfirm(1000)
  air_frame.FindElement("//li[.='"+air_handling_values["system_frequency"]+"']").Click()
  page.WaitConfirm(1000)
  
  #System Voltage:
  if air_handling_values["system_voltage"] != "SAP Defined":
    air_page.FindElement("//*[contains(text(),'System Voltage')]//parent :: span//parent :: label//parent::div//parent::div//span[@class='sapMSltLabel']").Click() 
    air_frame.FindElement("//li[.='"+air_handling_values["system_voltage"]+"']").Click()
    page.WaitConfirm(1000)
  
  #Fan Type:
  air_page.FindElement("//*[contains(text(),'Fan Type')]//parent :: span//parent :: label//parent::div//parent::div//span[@class='sapMSltLabel']").Click() 
  page.WaitConfirm(1000)
  air_frame.FindElement("//li[.='"+air_handling_values["fan_type"]+"']").Click()
  page.WaitConfirm(1000)
  
  #Fan Drive System:
  air_page.FindElement("//*[contains(text(),'Fan Drive System')]//parent :: span//parent :: label//parent::div//parent::div//span[@class='sapMSltLabel']").Click() 
  page.WaitConfirm(1000)
  air_frame.FindElement("//li[.='"+air_handling_values["fan_drive_system"]+"']").Click()
  page.WaitConfirm(1000)
  
  #Motor Efficiency Class:
  air_page.FindElement("//*[contains(text(),'Motor Efficiency Class')]//parent :: span//parent :: label//parent::div//parent::div//span[@class='sapMSltLabel']").Click() 
  page.WaitConfirm(1000)
  air_frame.FindElement("//li[.='"+air_handling_values["motor_efficiency_class"]+"']").Click()
  page.WaitConfirm(1000)
  
  #Fan Motor Type:
  air_page.FindElement("//*[contains(text(),'Fan Motor Type')]//parent :: span//parent :: label//parent::div//parent::div//span[@class='sapMSltLabel']").Click() 
  page.WaitConfirm(1000)
  air_frame.FindElement("//li[.='"+air_handling_values["fan_motor_type"]+"']").Click()
  page.WaitConfirm(1000)
  
  #Fan Motor Options A:
  air_page.FindElement("//*[contains(text(),'Fan Motor Options A')]//parent :: span//parent :: label//parent::div//parent::div//span[@class='sapMSltLabel']").Click() 
  page.WaitConfirm(1000)
  air_frame.FindElement("//li[.='"+air_handling_values["fan_motor_options_a"]+"']").Click()
  page.WaitConfirm(1000)
  
  #Vibration Cutout Switch (VCOS):
  air_page.FindElement("//*[contains(text(),'Vibration Cutout Switch (VCOS)')]//parent :: span//parent :: label//parent::div//parent::div//span[@class='sapMSltLabel']").Click() 
  page.WaitConfirm(1000)
  if air_handling_values["vibration_cutout_switch"] != 'None':
    air_frame.FindElement("//li[.='"+air_handling_values["vibration_cutout_switch"]+"']").Click()
  else:
    air_page.FindElement("//*[contains(text(),'Vibration Cutout Switch (VCOS)')]//parent :: span//parent :: label//parent::div//parent::div//span[@class='sapMSltLabel']").Keys(air_handling_values["vibration_cutout_switch"])
    air_page.FindElement("//*[contains(text(),'Vibration Cutout Switch (VCOS)')]//parent :: span//parent :: label//parent::div//parent::div//span[@class='sapMSltLabel']").Keys("[Enter]")
  page.WaitConfirm(1000)
  
  #Extended Lube Line:
  air_page.FindElement("//*[contains(text(),'Extended Lube Line')]//parent :: span//parent :: label//parent::div//parent::div//span[@class='sapMSltLabel']").Click() 
  page.WaitConfirm(1000)
  air_page.FindElement("//*[contains(text(),'Extended Lube Line')]//parent :: span//parent :: label//parent::div//parent::div//span[@class='sapMSltLabel']").Keys(air_handling_values["extended_lube_line"]) 
  air_page.FindElement("//*[contains(text(),'Extended Lube Line')]//parent :: span//parent :: label//parent::div//parent::div//span[@class='sapMSltLabel']").Keys("[Enter]")
  page.WaitConfirm(1000)
  
  #Fan Motor Removal System:
  air_page.FindElement("//*[contains(text(),'Fan Motor Removal System')]//parent :: span//parent :: label//parent::div//parent::div//span[@class='sapMSltLabel']").Click() 
  page.WaitConfirm(1000)
  if air_handling_values["fan_motor_removal_system"] != "None":
    air_frame.FindElement("//li[.='"+air_handling_values["fan_motor_removal_system"]+"']").Click()
  else:
    air_page.FindElement("//*[contains(text(),'Fan Motor Removal System')]//parent :: span//parent :: label//parent::div//parent::div//span[@class='sapMSltLabel']").Keys(air_handling_values["fan_motor_removal_system"])
    air_page.FindElement("//*[contains(text(),'Fan Motor Removal System')]//parent :: span//parent :: label//parent::div//parent::div//span[@class='sapMSltLabel']").Keys("[Enter]")
  page.WaitConfirm(1000)
  
  air_page.FindElement("//span[.='Additional Enhancements']").Click()