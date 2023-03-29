def login_form(page, username):
  login_form = page.FindElement("//form")
  username_field = login_form.FindElement("//div[@id='USERNAME_BLOCK']/input")
  username_field.SetText(username)
  username_field.Keys("[Tab]")
  passwordBox = login_form.FindElement("//div[@id='PASSWORD_BLOCK']/input")
  passwordBox.SetText(Project.Variables.password)
  login_form.FindElement("//button[.='Log On']").Click()