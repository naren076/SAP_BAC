def create_sales_order(order_type_form, sales_order_values):
  #---Order Type:
  order_type_field = order_type_form.FindElement("//input[@id=(//label[.='Order Type']/@for)]")
  order_type_field.SetText(sales_order_values["order_type"])
  
  #---Sales Organization:
  sales_org_field = order_type_form.FindElement("//input[@id=(//label[.='Sales Organization']/@for)]")
  sales_org_field.SetText(sales_order_values["sales_organization"])
  
  #---Distribution Channel:
  distribution_channel_field = order_type_form.FindElement("//input[@id=(//label[.='Distribution Channel']/@for)]")
  distribution_channel_field.SetText(sales_order_values["distribution_channel"])
  distribution_channel_field.Keys("[Enter]")