def create_standard_order(sales_document_textbox, standard_order_page, standard_order_values):
  #---Sold-to Party:
  sold_to_party_field = sales_document_textbox.FindElement("//input[@title='Sold-to Party']")
  sold_to_party_field.SetText(standard_order_values["sold_to_party"])
  
  #---Customer Reference:
  customer_reference_field = sales_document_textbox.FindElement("//input[@title='Customer Reference']")
  customer_reference_field.SetText(standard_order_values["customer_reference"])
  
  #---Delivery Block:
  delivery_block_field = sales_document_textbox.FindElement("//input[@id=(//label[.='Delivery Block']/@for)]")
  delivery_block_field.Click()
  
  delivery_block = sales_document_textbox.FindElement("//div[.='"+standard_order_values["delivery_block"]+"']")
  delivery_block.Click()
  delivery_block_field.Keys("[Enter]")
  standard_order_page.WaitConfirm(5000)
  
  #---Material:
  sales_document_textbox.FindElement("//span/input[@name='InputField']").SetText(standard_order_values["material"])
  sales_document_textbox.Keys("[Tab]")
  
  #---Order Quantity:
  order_quantity_field = sales_document_textbox.FindElement("//td[2]//tr/td//input")
  order_quantity_field.Click()
  order_quantity_field.SetText(standard_order_values["order_quantity"])
  order_quantity_field.Keys("[Tab][Tab][Tab][Tab][Tab][Tab][Tab][Tab][Tab]")
  
  #---Plant:
  plnt_field = sales_document_textbox.FindElement("//tr/td[11]/div")
  plnt_field.Click()
  plnt_field.Keys(standard_order_values["plant"])
  plnt_field.Keys("[Enter]")