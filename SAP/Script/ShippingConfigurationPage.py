def shipping_configurations(shipping_configuration_page, shipping_frame, shipping_page, shipping_configuration_values):
  #---Specials Required:
  shipping_page.FindElement("//*[contains(text(),'Specials Required?')]//parent :: span//parent :: label//parent::div//parent::div//span[@class='sapMSltLabel']").Click() 
  shipping_configuration_page.WaitConfirm(1000)
  shipping_frame.FindElement("//li[.='"+shipping_configuration_values["special_required"]+"']").Click()