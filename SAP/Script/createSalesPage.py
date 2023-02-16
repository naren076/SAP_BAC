def create_sales_order(order_type_form, field_values):
  order_type_text_box = order_type_form.FindElement("//input[@id=(//label[.='Order Type']/@for)]")
  order_type_text_box.SetText(field_values["order_type"])
  sales_org_field = order_type_form.FindElement("//input[@id=(//label[.='Sales Organization']/@for)]")
  sales_org_field.SetText(field_values["sales_organization"])
  distribution_channel = order_type_form.FindElement("//input[@id=(//label[.='Distribution Channel']/@for)]")
  distribution_channel.SetText(field_values["distribution_channel"])
  distribution_channel.Keys("[Enter]")