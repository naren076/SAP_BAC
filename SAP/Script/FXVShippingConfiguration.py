def shipping_configurations(shipping_configuration_page, shipping_frame, shipping_page, shipping_configuration_values):
  #---3 Piece Rig Construction:
  shipping_page.FindElement("//*[contains(text(),'3 Piece Rig Construction')]//parent :: span//parent :: label//parent::div//parent::div//span[@class='sapMSltLabel']").Click()
  shipping_configuration_page.WaitConfirm(1000)
  shipping_frame.FindElement("//*[contains(text(),'3 Piece Rig Construction')]//parent :: span//parent :: label//parent::div//parent::div//span[@class='sapMSltLabel']").Keys(shipping_configuration_values["three_Piece_rig_construction"])
  shipping_frame.FindElement("//*[contains(text(),'3 Piece Rig Construction')]//parent :: span//parent :: label//parent::div//parent::div//span[@class='sapMSltLabel']").Keys("[Enter]")
  shipping_configuration_page.WaitConfirm(1000)
  
  #---Type of Crating:
  if shipping_configuration_values["type_of_crating"] != 'None':
    shipping_page.FindElement("//*[contains(text(),'Type of Crating')]//parent :: span//parent :: label//parent::div//parent::div//span[@class='sapMSltLabel']").Click() 
    shipping_configuration_page.WaitConfirm(1000)
    shipping_frame.FindElement("//li[.='"+shipping_configuration_values["type_of_crating"]+"']").Click()
     
  #---Specials Required:
  shipping_page.FindElement("//*[contains(text(),'Specials Required?')]//parent :: span//parent :: label//parent::div//parent::div//span[@class='sapMSltLabel']").Click() 
  shipping_configuration_page.WaitConfirm(1000)
  shipping_frame.FindElement("//li[.='"+shipping_configuration_values["special_required"]+"']").Click()
  
  #---Configuration Type:
  if shipping_configuration_values["configuration_type"] != "SAP Defined":
    shipping_page.FindElement("//*[contains(text(),'Configuration Type')]//parent :: span//parent :: label//parent::div//parent::div//span[@class='sapMSltLabel']").Click() 
    shipping_configuration_page.WaitConfirm(1000)
    shipping_frame.FindElement("//li[.='"+shipping_configuration_values["configuration_type"]+"']").Click()
   
  #---ETO Type:
  if shipping_configuration_values["eto_type"] != "SAP Defined":
    shipping_page.FindElement("//*[contains(text(),'ETO Type')]//parent :: span//parent :: label//parent::div//parent::div//span[@class='sapMSltLabel']").Click() 
    shipping_configuration_page.WaitConfirm(1000)
    shipping_frame.FindElement("//li[.='"+shipping_configuration_values["eto_type"]+"']").Click()
  
  #---Model with Suffix:
  if shipping_configuration_values["model_with_suffix"] != "SAP Defined":
    shipping_page.FindElement("//*[contains(text(),'Model with Suffix')]//parent :: span//parent :: label//parent::div//parent::div//span[@class='sapMSltLabel']").Click() 
    shipping_configuration_page.WaitConfirm(1000)
    shipping_frame.FindElement("//li[.='"+shipping_configuration_values["model_with_suffix"]+"']").Click() 
    
  #---Truck Type:
  if shipping_configuration_values["truck_type"] != "SAP Defined":
    shipping_page.FindElement("//*[contains(text(),'Truck Type')]//parent :: span//parent :: label//parent::div//parent::div//span[@class='sapMSltLabel']").Click() 
    shipping_configuration_page.WaitConfirm(1000)
    shipping_frame.FindElement("//li[.='"+shipping_configuration_values["truck_type"]+"']").Click() 

  #---Fan Type Freight:
  if shipping_configuration_values["fan_type_freight"] != "SAP Defined":
    shipping_page.FindElement("//*[contains(text(),'Fan Type Freight')]//parent :: span//parent :: label//parent::div//parent::div//span[@class='sapMSltLabel']").Click() 
    shipping_configuration_page.WaitConfirm(1000)
    shipping_frame.FindElement("//li[.='"+shipping_configuration_values["fan_type_freight"]+"']").Click()
  
  #---Side Air Intake Option Freight:
  if shipping_configuration_values["side_air_intake_option_freight"] != "SAP Defined":
    shipping_page.FindElement("//*[contains(text(),'Side Air Intake Option Freight')]//parent :: span//parent :: label//parent::div//parent::div//span[@class='sapMSltLabel']").Click() 
    shipping_configuration_page.WaitConfirm(1000)
    shipping_frame.FindElement("//li[.='"+shipping_configuration_values["side_air_intake_option_freight"]+"']").Click()
  
  #---Air Discharge Configuration F:
  if shipping_configuration_values["air_discharge_configuration_f"] != "SAP Defined":
    shipping_page.FindElement("//*[contains(text(),'Air Discharge Configuration F')]//parent :: span//parent :: label//parent::div//parent::div//span[@class='sapMSltLabel']").Click() 
    shipping_configuration_page.WaitConfirm(1000)
    shipping_frame.FindElement("//li[.='"+shipping_configuration_values["air_discharge_configuration_f"]+"']").Click() 
    
  #---Louver Face Platform Freight:
  if shipping_configuration_values["louver_face_platform_freight"] != "SAP Defined":
    shipping_page.FindElement("//*[contains(text(),'Louver Face Platform Freight')]//parent :: span//parent :: label//parent::div//parent::div//span[@class='sapMSltLabel']").Click() 
    shipping_configuration_page.WaitConfirm(1000)
    shipping_frame.FindElement("//li[.='"+shipping_configuration_values["louver_face_platform_freight"]+"']").Click() 
    
  #---Access Door Platform Freight:
  if shipping_configuration_values["access_door_platform_freight"] != "SAP Defined":
    shipping_page.FindElement("//*[contains(text(),'Access Door Platform Freight')]//parent :: span//parent :: label//parent::div//parent::div//span[@class='sapMSltLabel']").Click() 
    shipping_configuration_page.WaitConfirm(1000)
    shipping_frame.FindElement("//li[.='"+shipping_configuration_values["access_door_platform_freight"]+"']").Click()