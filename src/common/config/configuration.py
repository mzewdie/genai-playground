import yaml

class Configuration:
    
    def __init__(self,data):
        self.__data=data
    
    @classmethod
    def load(cls,path="configs/config.yaml"):
        with open(path) as file:
            data = yaml.safe_load(file)
            
        return cls(data)  
    
    def get_providers(self):
        return list(self.__data["providers"].keys())
    
    def get_models(self, provider):
        return self.__data["providers"][provider]
    