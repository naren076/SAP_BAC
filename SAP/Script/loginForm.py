def login_form(login_page, username):
  login_form = login_page.FindElement("//form")
  #---Username:
  username_field = login_form.FindElement("//div[@id='USERNAME_BLOCK']/input")
  username_field.SetText(username)
  username_field.Keys("[Tab]") 
  
  #---Password:
  passwordBox = login_form.FindElement("//div[@id='PASSWORD_BLOCK']/input")
  passwordBox.SetText(Project.Variables.password)
  login_form.FindElement("//button[.='Log On']").Click()