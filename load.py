import pickle, sklearn, numpy
# Load the model
with open(f'random_forest_model.pkl', 'rb') as f:
    model = pickle.load(f)
with open(f'scaler.pkl', 'rb') as scale:
    scaler = pickle.load(scale)
#set up dummy data(user input)
inputs = [[10400.0, 104433.0, 699.0, 3.0, 1, 1, 0]]
inputs_scaled = scaler.transform(inputs)



# run prediction
predictions = model.predict(inputs_scaled)
# print the response
print(predictions)

