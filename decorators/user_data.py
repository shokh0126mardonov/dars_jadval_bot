from telegram import Update
from telegram.ext import CallbackContext
import json


def logger(func):
    def wrapper(update: Update,context: CallbackContext):
        user = update.effective_user
        
        user_data = {
            "id":user.id,
            "first_name":user.first_name,
            "username":user.username,
            "language_code":user.language_code,
            "is_bot":user.is_bot
        }
        
      
        with open("database/users.json",'r') as file:
            try:
                data = json.load(file)
            except json.JSONDecodeError:
                data = []

            
            found = False
            for i in data:
                if i['id'] == user_data['id']:
                    found = True
                    break

            if not found:  
                data.append(user_data)
                        
        with open("database/users.json",'w') as f:
            json.dump(data,f,indent=4)
                
        
        return func(update,context)
    
    return wrapper