from schema import Schema, Optional, Or

class Detect:
    def __call__(self, protolesson):
        # Two variants are possible
        # First:
        try:
            answer = "Human Input"
            Schema({
                "date":str,
                "marks":{
                    str:str
                },
                Optional(str):object
            }).validate(protolesson)
        except:
            # merlidiary based
            try:
                answer = "Merlindiary"
                Schema({
                    "date":str,
                    "marks":{
                        str:{
                            str:Or(str,int)
                        }
                    },
                    Optional(str):object
                }).validate(protolesson)
            
            except:
                answer = ""
        
        return answer
    
    def __or__(self, protolesson):
        return self(protolesson)

detect = Detect()