import pkgutil
import google.generativeai.types

for module in pkgutil.iter_modules(google.generativeai.types.__path__):
    print(module.name)