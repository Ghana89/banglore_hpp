import pickle 
import numpy as np
class prediction():

    def __init__ (self , data):
        self.data = data

    def model_call (self):
        with open('linear_model.pkl' , 'rb') as file:

            self.model = pickle.load(file)
    
    def uer_predict (self):
        self.model_call()
        x_features = self.model.feature_names_in_
        user_input = np.zeros(self.model.n_features_in_)
        user_input[0] =self.data['size']
        user_input[1] =self.data['total_sqft']
        user_input[2] =self.data['bath']
        self.location_input = self.data['locations']
        self.areaType = self.data['area_type']
        index = np.where(x_features=='location_'+self.location_input)[0][0]

        user_input[index ] = 1
        index2 = np.where(x_features =='area_type_'+self.areaType)[0][0]
        user_input[index2] =1

        result = self.model.predict([user_input])
        print(user_input)


        return result
