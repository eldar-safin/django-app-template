# Шаблон приложения на Django

```bash
clear
echo -n "App name: django-" && read APP_NAME && APP_NAME="django-"$APP_NAME && 
git clone https://github.com/eldar-safin/django-app-template.git $APP_NAME && cd $_ && 
python3 -m venv .venv --upgrade-deps && source .venv/bin/activate && 
pip install -r requirements.txt && echo && pip list && echo; unset APP_NAME
```