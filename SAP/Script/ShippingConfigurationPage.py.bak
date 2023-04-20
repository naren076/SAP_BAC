def shipping_configurations(page, shipping_frame, shipping_page, shipping_configs):
  #Specials Required
  shipping_page.FindElement("//*[contains(text(),'Specials Required?')]//parent :: span//parent :: label//parent::div//parent::div//span[@class='sapMSltLabel']").Click() 
  page.WaitConfirm(1000)
  shipping_frame.FindElement("//li[.='"+shipping_configs["special_required"]+"']").Click()